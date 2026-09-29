from pathlib import Path
import subprocess
import sys


ROOT = Path(__file__).resolve().parents[1]


def test_required_showcase_paths_exist():
    result = subprocess.run(
        [sys.executable, "tools/verify_showcase.py", "--root", "."],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0, result.stdout + result.stderr


def test_unexpected_source_is_not_published():
    forbidden_suffixes = {".fit", ".mc", ".mss", ".iq"}
    published = [path for path in ROOT.rglob("*") if ".git" not in path.parts]

    assert not [path for path in published if path.suffix.lower() in forbidden_suffixes]
