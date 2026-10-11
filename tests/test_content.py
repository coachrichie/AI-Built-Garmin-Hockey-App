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


def test_three_balanced_mermaid_diagrams_cover_the_required_flows():
    technical_docs = "\n".join(
        read(path)
        for path in (
            "docs/ARCHITECTURE.md",
            "docs/VALIDATION.md",
        )
    )

    assert technical_docs.count("```mermaid") == 3
    assert technical_docs.count("```") == 6
    for label in (
        "Hockey Evidence",
        "Human decisions",
        "Garmin watch",
        "Local browser analysis",
        "Evidence",
        "Metric classification",
    ):
        assert label in technical_docs


def test_beta_status_uses_the_approved_conservative_vocabulary():
    status = read("docs/BETA_STATUS.md")

    for label in (
        "Beta tested",
        "Implemented, validation pending",
        "Planned",
        "Out of scope for version 1",
    ):
        assert label in status
    assert not re.search(r"\b\d+(?:\.\d+)?\s*%", status)


def test_app_source_boundary_is_explicit():
    app_readme = read("app/README.md").lower()

    assert "not duplicated in this portfolio" in app_readme
    assert "https://github.com/coachrichie/rinklogic" in app_readme
    assert "single source of truth" in app_readme


def test_feature_level_beta_status_tracks_published_evidence_without_accuracy_claims():
    status = read("docs/BETA_STATUS.md")
    readme = read("README.md")

    assert "| Core activity recording | **Beta tested** |" in status
    assert "| Hockey-specific analytics | **Implemented, validation pending** |" in status
    assert "| Automatic shift classification | **Implemented, validation pending** |" in status
    assert "they do not establish automatic-shift, push-count, or distance accuracy" in read("docs/VALIDATION.md").lower()
    assert "https://github.com/coachrichie/RinkLogic" in readme
