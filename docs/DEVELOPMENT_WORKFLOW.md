# Development Workflow

ShiftSense Hockey used AI as a sequence of bounded engineering roles rather than one long generation request.

## 1. Turn intent into constraints

The project began with the desired experience: a hockey-focused activity on a Garmin watch, useful on ice and inline, functional without a phone, and honest about uncertainty.

Structured design converted that intent into boundaries:

- GPS cannot be required for indoor hockey.
- A chest strap can improve heart-rate quality but cannot be mandatory.
- Manual shift markers take priority over automation.
- The original FIT activity remains the durable record.
- Medical diagnosis and unsupported precision stay out of scope.

## 2. Research before choosing metrics

The Hockey Evidence skill examined what hockey physiology and wearable validation research could support. The output was not a list of impressive metrics; it was a set of limits.

Metrics were separated into measured, device-provided, derived, estimated, and experimental groups. That classification became an architectural input and a user-interface requirement.

## 3. Check the actual platform

The Garmin Connect IQ skill mapped product requirements to Toybox APIs, API levels, permissions, and device capabilities. This prevented a common failure mode in AI coding: producing plausible-looking calls that do not exist or are not available on the target watch.

Platform research also drove capability-based design. A device that lacks a required sensor or resource should expose a reduced, honest feature set rather than pretend to deliver the full analysis.

## 4. Design before implementation

The architecture assigns one responsibility to each unit: session lifecycle, sensor access, capability detection, classification, movement analysis, heart-rate analysis, calibration, load calculation, FIT writing, and user interaction.

Small boundaries make each part easier to understand, test, and revise as beta evidence arrives.

## 5. Build through observable behavior

Implementation work follows short test cycles wherever the platform permits:

1. define the behavior and failure case;
2. observe the test fail for the expected reason;
3. implement the smallest complete behavior;
4. rerun focused and broader checks;
5. record the change in version control.

Simulator checks do not replace real-device testing. Real-device success does not by itself validate a scientific metric.

## 6. Promote claims only with evidence

The workflow ends with a release gate, not with generated code. Documentation, tests, source state, privacy, and claim wording are checked together.

During beta, feedback can change thresholds, interfaces, and priorities. The [beta status register](BETA_STATUS.md) is updated before public language becomes stronger.

## What is intentionally not published here

This repository is a curated technical portfolio, not a message archive. It explains decisions and boundaries without exposing private working conversations, personal training data, unpublished beta artifacts, or unstable source snapshots.
