from __future__ import annotations

import argparse
from pathlib import Path
import re
from urllib.parse import unquote


IGNORED_PARTS = {".git", ".pytest_cache", "__pycache__", ".venv", "venv"}


def public_files(root: Path):
    for path in root.rglob("*"):
        if not path.is_file() or IGNORED_PARTS.intersection(path.parts):
            continue
        yield path


def markdown_files(root: Path):
    for path in public_files(root):
        if path.suffix.lower() == ".md" and "tests" not in path.parts:
            yield path


def required_paths(root: Path) -> tuple[Path, ...]:
    relative_paths = (
        "README.md",
        "LICENSE",
        "CONTRIBUTING.md",
        "SECURITY.md",
        "docs/AI_SKILLS.md",
        "docs/DEVELOPMENT_WORKFLOW.md",
        "docs/ARCHITECTURE.md",
        "docs/VALIDATION.md",
        "docs/LESSONS_LEARNED.md",
        "docs/BETA_STATUS.md",
        "assets/diagrams",
        "assets/screenshots",
        "app/README.md",
    )
    return tuple(root / path for path in relative_paths)


def verify_structure(root: Path) -> list[str]:
    errors = [
        f"missing required path: {path.relative_to(root).as_posix()}"
        for path in required_paths(root)
        if not path.exists()
    ]
    forbidden_suffixes = {".fit", ".iq", ".mc", ".mss"}
    for path in public_files(root):
        if path.suffix.lower() in forbidden_suffixes:
            errors.append(f"forbidden initial-publication file: {path.relative_to(root).as_posix()}")
    return errors


def scan_relative_links(root: Path) -> list[str]:
    findings: list[str] = []
    link_pattern = re.compile(r"\[[^]]*\]\(([^)]+)\)")
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        for raw_target in link_pattern.findall(text):
            target = raw_target.strip().strip("<>").split("#", 1)[0]
            if not target or re.match(r"^[a-z][a-z0-9+.-]*:", target, re.IGNORECASE):
                continue
            target = unquote(target)
            resolved = (path.parent / target).resolve()
            if not resolved.exists():
                findings.append(f"{path.relative_to(root).as_posix()}: broken-relative-link")
    return sorted(set(findings))


def scan_sensitive_content(root: Path) -> list[str]:
    findings: list[str] = []
    secret_patterns = (
        re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}\b"),
        re.compile(r"\b(?:api[_-]?key|token|secret)\s*[:=]\s*[^\s<]{12,}", re.IGNORECASE),
    )
    local_path_patterns = (
        re.compile(r"[A-Za-z]:\\Users\\[^\\\s]+", re.IGNORECASE),
        re.compile(r"/(?:Users|home)/[^/\s]+"),
    )

    for path in public_files(root):
        relative = path.relative_to(root).as_posix()
        if "tests" in path.parts:
            continue
        if path.suffix.lower() in {".fit", ".iq"}:
            findings.append(f"{relative}: forbidden-private-artifact")
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            continue
        if any(pattern.search(text) for pattern in secret_patterns):
            findings.append(f"{relative}: secret-like-value")
        if any(pattern.search(text) for pattern in local_path_patterns):
            findings.append(f"{relative}: local-user-path")
    return sorted(set(findings))


def scan_claim_language(root: Path) -> list[str]:
    findings: list[str] = []
    accuracy_pattern = re.compile(
        r"\b(?:achieves?|reaches?|delivers?|has)\s+\d+(?:\.\d+)?\s*%\s+accuracy\b",
        re.IGNORECASE,
    )
    completion_pattern = re.compile(
        r"\b(?:the\s+)?app\s+is\s+(?:fully\s+)?(?:production[- ]ready|complete|released)\b",
        re.IGNORECASE,
    )
    for path in markdown_files(root):
        text = path.read_text(encoding="utf-8")
        relative = path.relative_to(root).as_posix()
        if accuracy_pattern.search(text):
            findings.append(f"{relative}: unsupported-accuracy-claim")
        if completion_pattern.search(text):
            findings.append(f"{relative}: unsupported-completion-claim")
    return sorted(findings)


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the public showcase repository.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    errors = (
        verify_structure(root)
        + scan_relative_links(root)
        + scan_sensitive_content(root)
        + scan_claim_language(root)
    )
    if errors:
        for error in errors:
            print(error)
        return 1
    print("showcase verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
