from pathlib import Path
import importlib.util


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "verify_showcase", ROOT / "tools" / "verify_showcase.py"
)
verifier = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(verifier)


def write(root: Path, relative: str, content: str) -> None:
    path = root / relative
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding="utf-8")


def test_scan_relative_links_reports_a_missing_local_target(tmp_path):
    write(tmp_path, "README.md", "[Missing](docs/missing.md)\n")

    findings = verifier.scan_relative_links(tmp_path)

    assert findings == ["README.md: broken-relative-link"]


def test_scan_relative_links_accepts_existing_targets_and_web_links(tmp_path):
    write(tmp_path, "README.md", "[Local](docs/ok.md) [Web](https://example.com)\n")
    write(tmp_path, "docs/ok.md", "# Present\n")

    assert verifier.scan_relative_links(tmp_path) == []


def test_sensitive_scan_detects_secrets_paths_and_fit_without_echoing_values(tmp_path):
    fake_token = "ghp_" + "abcdefghijklmnopqrstuvwxyz" + "1234567890"
    assignment = "to" + "ken=" + fake_token
    windows_path = "C:" + "\\Users\\" + "person\\private"
    mac_path = "/" + "Users/" + "person/private"
    linux_path = "/" + "home/" + "person/private"
    write(tmp_path, "notes.md", f"{assignment}\n{windows_path}\n")
    write(tmp_path, "more.md", f"{mac_path}\n{linux_path}\n")
    write(tmp_path, "session.fit", "private activity")

    findings = verifier.scan_sensitive_content(tmp_path)
    joined = "\n".join(findings)

    assert "secret-like-value" in joined
    assert joined.count("local-user-path") == 2
    assert "forbidden-private-artifact" in joined
    assert fake_token not in joined
    assert "person" not in joined


def test_sensitive_scan_checks_nonfixture_files_under_tests(tmp_path):
    fake_token = "ghp_" + "z" * 36
    write(tmp_path, "tests/private_notes.txt", fake_token)

    findings = verifier.scan_sensitive_content(tmp_path)

    assert findings == ["tests/private_notes.txt: secret-like-value"]


def test_sensitive_scan_detects_current_github_tokens_and_quoted_assignments(tmp_path):
    fine_grained = "github" + "_pat_" + "a" * 30
    generic_value = "b" * 40
    key = "to" + "ken"
    write(tmp_path, "config.json", f'{{"{key}": "{generic_value}"}}\n{fine_grained}\n')

    findings = verifier.scan_sensitive_content(tmp_path)
    joined = "\n".join(findings)

    assert findings == ["config.json: secret-like-value"]
    assert fine_grained not in joined
    assert generic_value not in joined


def test_sensitive_scan_accepts_clean_public_content(tmp_path):
    write(tmp_path, "README.md", "# Public beta\nNo private activity data is included.\n")

    assert verifier.scan_sensitive_content(tmp_path) == []


def test_claim_scan_rejects_unsupported_accuracy_and_completion_language(tmp_path):
    write(
        tmp_path,
        "README.md",
        "The classifier achieves 97% accuracy and the app is production-ready.\n",
    )

    findings = verifier.scan_claim_language(tmp_path)

    assert findings == [
        "README.md: unsupported-accuracy-claim",
        "README.md: unsupported-completion-claim",
    ]


def test_claim_scan_accepts_conservative_beta_language(tmp_path):
    write(
        tmp_path,
        "README.md",
        "The app is not production-ready. No numerical accuracy claim is published.\n",
    )

    assert verifier.scan_claim_language(tmp_path) == []


def test_relative_link_scan_rejects_targets_outside_repository(tmp_path):
    outside = tmp_path.parent / "private.md"
    outside.write_text("private", encoding="utf-8")
    write(tmp_path, "README.md", "[Private](../private.md)\n")

    assert verifier.scan_relative_links(tmp_path) == [
        "README.md: link-outside-repository"
    ]


def test_relative_link_scan_is_case_sensitive_like_github(tmp_path):
    write(tmp_path, "README.md", "[Status](docs/beta_status.md)\n")
    write(tmp_path, "docs/BETA_STATUS.md", "# Status\n")

    assert verifier.scan_relative_links(tmp_path) == [
        "README.md: broken-relative-link"
    ]


def test_relative_link_scan_checks_reference_style_targets(tmp_path):
    write(tmp_path, "README.md", "See [status][beta].\n\n[beta]: docs/missing.md\n")

    assert verifier.scan_relative_links(tmp_path) == [
        "README.md: broken-relative-link"
    ]
