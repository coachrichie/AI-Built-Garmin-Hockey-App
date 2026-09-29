from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]


def read(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


def test_readme_presents_the_ai_first_beta_portfolio():
    readme = read("README.md")
    opening = readme[:800].lower()

    assert "ai skills" in opening
    assert "without prior monkey c experience" in opening
    assert re.search(r"badge.*beta|beta.*badge|img\.shields\.io.*beta", readme, re.IGNORECASE)
    assert "Hockey Evidence" in readme
    assert "Garmin Connect IQ" in readme


def test_readme_links_every_detailed_document():
    readme = read("README.md")
    expected = {
        "docs/AI_SKILLS.md",
        "docs/DEVELOPMENT_WORKFLOW.md",
        "docs/ARCHITECTURE.md",
        "docs/VALIDATION.md",
        "docs/LESSONS_LEARNED.md",
        "docs/BETA_STATUS.md",
        "app/README.md",
    }
    linked = set(re.findall(r"\[[^]]+\]\(([^)#]+)", readme))

    assert expected <= linked


def test_ai_skills_explains_domain_process_and_human_responsibility():
    content = read("docs/AI_SKILLS.md")

    assert "Hockey Evidence" in content
    assert "Garmin Connect IQ" in content
    assert "Process skills" in content
    assert "Human responsibility" in content


def test_public_story_is_not_a_raw_transcript_dump():
    public_markdown = "\n".join(
        path.read_text(encoding="utf-8")
        for path in ROOT.rglob("*.md")
        if ".git" not in path.parts
    )

    assert "raw chat transcript" not in public_markdown.lower()
    assert "assistant:" not in public_markdown.lower()
    assert "user:" not in public_markdown.lower()
