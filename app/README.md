# Application Source

There is **no application source in this repository yet**.

ShiftSense Hockey is currently in beta. Source code will be added here **after beta stabilization**, a publication review, and removal of private test data or machine-specific configuration.

Publishing the technical portfolio first keeps an unstable snapshot from being mistaken for a supported release. It also allows the architecture, evidence boundaries, and AI-skills workflow to be reviewed independently of implementation churn.

## Intended future layout

When the source is ready, this directory is expected to contain:

```text
app/
|-- manifest.xml
|-- monkey.jungle
|-- source/
|-- resources/
|-- tests/
`-- README.md
```

The final layout may change if beta findings require different component boundaries. Any published source will include build prerequisites, supported-device evidence, test instructions, and known limitations.

For current implementation and validation claims, see [Beta status](../docs/BETA_STATUS.md).
