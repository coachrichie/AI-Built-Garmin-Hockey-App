# Building a Garmin Hockey App with AI Skills

[![Status: Beta](https://img.shields.io/badge/status-beta-f59e0b)](docs/BETA_STATUS.md)
[![Platform: Garmin Connect IQ](https://img.shields.io/badge/platform-Garmin%20Connect%20IQ-007cc3)](docs/ARCHITECTURE.md)
[![License: MIT](https://img.shields.io/badge/license-MIT-2ea44f)](LICENSE)

> A technical portfolio about using AI skills to build **ShiftSense Hockey** without prior Monkey C experience.

This repository is not a victory lap for generated code. It is a case study in turning AI from a general-purpose assistant into a disciplined engineering system: domain research, platform guidance, explicit architecture, conservative claims, and validation gates.

ShiftSense Hockey is currently in **beta testing**. This repository documents the method and the technical design now; verified screenshots, beta results, and application source will follow only when they are ready to publish.

## The skill stack

Two reusable domain skills made the unfamiliar parts of the project tractable:

| AI skill | What it contributed |
|---|---|
| **Hockey Evidence** | Translated sports-science evidence into metric boundaries, algorithm constraints, and validation targets. |
| **Garmin Connect IQ** | Grounded Monkey C and Toybox decisions in platform APIs, permissions, compatibility, and device constraints. |

Structured development skills added the engineering loop: clarify the idea, write the design, plan the work, test behavior, debug systematically, review changes, and verify before claiming completion.

The skills themselves are published separately in [coachrichie/Codex-Skills](https://github.com/coachrichie/Codex-Skills). This repository focuses on what their combined use made possible.

[Explore the AI skill system →](docs/AI_SKILLS.md)

## From idea to beta

```text
Product intent
    → structured requirements
    → hockey evidence and measurement limits
    → Garmin platform constraints
    → architecture and implementation
    → simulator and real-device validation
    → beta feedback
```

The important shift was not asking AI to “make an app.” Each stage had a narrower job and a stronger source of truth. Research informed what the watch should claim. Garmin documentation constrained what it could do. Tests and beta evidence decide what may be called validated.

[See the development workflow →](docs/DEVELOPMENT_WORKFLOW.md)

## The beta result: ShiftSense Hockey

ShiftSense Hockey is designed as an offline-first Garmin Connect IQ app for ice and inline hockey. It records a standard FIT activity, separates work and recovery periods, and organizes hockey-specific load and recovery metrics without requiring a phone, cloud account, or server for its core operation.

The technical design separates:

- watch-side recording, sensing, classification, and feedback;
- versioned FIT data as the durable activity record;
- local browser analysis for deeper review and trends;
- measured values from derived, estimated, and experimental metrics.

[Read the architecture →](docs/ARCHITECTURE.md)

## Evidence before confidence

A wearable can produce precise-looking numbers long before those numbers deserve trust. This project therefore classifies every metric and uses an evidence ladder from research and deterministic tests through simulator, real-device, and beta evaluation.

No accuracy percentage, supported-device list, or production-readiness claim appears here without the evidence needed to support it.

[Review the validation approach →](docs/VALIDATION.md)

## Current status

| Area | Public status |
|---|---|
| Product and system design | Documented |
| Domain and platform skill workflow | Documented |
| Garmin application | Beta testing |
| Verified beta results | Publication pending |
| Screenshots | Publication pending |
| Application source | Planned after beta stabilization |

The detailed status register is deliberately conservative: [Beta status →](docs/BETA_STATUS.md)

## Repository guide

- [AI skills](docs/AI_SKILLS.md) — the specialized capabilities and their boundaries
- [Development workflow](docs/DEVELOPMENT_WORKFLOW.md) — how the skills work as an engineering system
- [Architecture](docs/ARCHITECTURE.md) — watch, FIT, browser analysis, and data flow
- [Validation](docs/VALIDATION.md) — evidence levels and claim promotion
- [Lessons learned](docs/LESSONS_LEARNED.md) — practical lessons for AI builders
- [Beta status](docs/BETA_STATUS.md) — the source of truth for current claims
- [Application source status](app/README.md) — why source is not published yet

## Why publish this before the source?

The workflow is already useful to developers, while the app is still changing under beta feedback. Publishing the technical portfolio first lets the reasoning, boundaries, and validation discipline stand on their own. It also prevents an unstable code snapshot from being mistaken for a release.

## License and scope

Original repository content is available under the [MIT License](LICENSE). Garmin, Connect IQ, Toybox, and related names belong to their respective owners. Research publications and third-party materials retain their original rights.

This project is a training and analysis tool, not a medical device. It does not diagnose injury, concussion, or any medical condition.

Contributions are welcome within the documented [contribution boundaries](CONTRIBUTING.md). Security and privacy concerns can be reported using the [security policy](SECURITY.md).
