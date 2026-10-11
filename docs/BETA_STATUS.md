# Beta Status

Last reviewed: 11 October 2026

This is the source of truth for public implementation and validation language. It is intentionally more conservative than the product design. A capability moves to a stronger status only when supporting evidence can be published or independently inspected.

## Status definitions

- **Beta tested** — implemented and currently exercised in beta; this does not mean production-ready or scientifically validated.
- **Implemented, validation pending** — present in the beta build, but public evidence is not yet sufficient for a validated claim.
- **Planned** — approved in the design but not claimed as implemented here.
- **Out of scope for version 1** — intentionally excluded from the first release.

## Current register

| Area | Status | Public interpretation |
|---|---|---|
| Garmin watch application | **Beta tested** | A working build is undergoing beta use; release readiness is not claimed. |
| Core activity recording | **Beta tested** | Start, manual shifts, live heart rate, save, and three post-training pages were exercised on a Venu 2 Plus. |
| Hockey-specific analytics | **Implemented, validation pending** | Shift summaries, HR metrics, zones, recovery, experimental pushes, and estimated distance are public; scientific accuracy claims remain withheld. |
| Automatic shift classification | **Implemented, validation pending** | It remains a non-authoritative shadow proposal system and does not change the manual shift record. |
| Verified screenshots | **Planned** | Screenshots will be reviewed for accuracy and privacy before publication. |
| Public application source | **Beta tested** | The reviewed source is published separately at [coachrichie/RinkLogic](https://github.com/coachrichie/RinkLogic). |
| Local FIT analysis | **Implemented, validation pending** | Public tools decode the versioned developer fields locally; personal FIT files remain private. |
| Broad device compatibility matrix | **Planned** | Candidate families require simulator and hardware evidence before support is advertised. |
| Torhüter-specific model | **Out of scope for version 1** | Field-player and goalkeeper workloads are not treated as interchangeable. |
| Medical or concussion detection | **Out of scope for version 1** | The project does not provide diagnosis or medical alerts. |
| Team and coach portal | **Out of scope for version 1** | Version one remains focused on an individual, offline-first workflow. |

## What evidence will change this page?

Status changes should include the tested build or model version, device class, session conditions, reference method, sample scope, and known limitations. A successful demo is useful evidence of operation, not enough evidence for a general performance claim.

## Publication checklist for beta updates

Before strengthening a status:

1. confirm the feature exists in the build being described;
2. identify the test or beta evidence supporting the change;
3. check that the evidence matches the claimed hardware and use case;
4. update the relevant architecture or validation page;
5. remove personal activity data and private tester information;
6. review the wording for scientific and platform overreach.
