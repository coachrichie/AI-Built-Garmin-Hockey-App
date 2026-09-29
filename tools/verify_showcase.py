from __future__ import annotations

import argparse
from pathlib import Path


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
    for path in root.rglob("*"):
        if ".git" in path.parts or not path.is_file():
            continue
        if path.suffix.lower() in forbidden_suffixes:
            errors.append(f"forbidden initial-publication file: {path.relative_to(root).as_posix()}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Verify the public showcase repository.")
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args()
    root = args.root.resolve()
    errors = verify_structure(root)
    if errors:
        for error in errors:
            print(error)
        return 1
    print("showcase verification passed")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
