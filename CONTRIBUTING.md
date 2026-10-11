# Contributing

Thank you for helping make this technical portfolio more useful and accurate.

## Contribution types

- **Documentation:** improve clarity, accessibility, links, or diagrams without strengthening unsupported claims.
- **Evidence corrections:** identify a source, measurement limit, or interpretation that should be revised; explain the affected claim and provide a primary source where possible.
- **Beta feedback:** report reproducible behavior without attaching personal activity files or another person's data.
- **Application source:** propose code changes in [coachrichie/RinkLogic](https://github.com/coachrichie/RinkLogic); this repository accepts portfolio and evidence-documentation changes.

## Status changes

`docs/BETA_STATUS.md` is the public source of truth. A pull request that strengthens a feature status must state:

- build or model version;
- tested device class and conditions;
- reference method;
- sample scope;
- known limitations.

Implementation alone is not evidence of accuracy. Simulator success alone is not evidence of real-device compatibility.

## Pull requests

Keep each change focused. Explain what changed, why it is correct, and how it was checked. Update linked documents together when a change affects architecture, validation, or beta status.

Before opening a pull request, run:

```powershell
python -m pytest -q
python tools/verify_showcase.py --root .
git diff --check
```

Do not commit credentials, FIT activities, private tester information, machine-specific paths, downloaded research papers, or proprietary documentation.

## Conduct

Discuss evidence and engineering decisions directly and respectfully. Good-faith disagreement is welcome; personal attacks and disclosure of private tester information are not.
