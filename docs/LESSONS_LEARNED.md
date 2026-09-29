# Lessons Learned

## Specialized context beats confident improvisation

The most valuable AI improvement was not a larger prompt. It was giving each difficult domain a maintained source of truth. Garmin platform guidance came from the API reference; hockey measurement decisions came from evidence records and explicit transfer limits.

## Requirements are part of the implementation

Decisions such as “GPS is optional,” “manual markers win,” and “uncertainty stays visible” affect architecture, storage, user experience, tests, and release language. Treating them as first-class requirements prevented later code from quietly redefining the product.

## Measurement and inference must look different

Wearable products easily blur a sensor value, a platform calculation, and a model estimate. Explicit metric classes make that distinction visible to developers and, eventually, users.

## Platform fluency is more than syntax

Learning Monkey C syntax was only one small part of the work. API availability, permissions, FIT conventions, device resources, input methods, and display families shaped the design more strongly than syntax did.

## AI speed increases the need for gates

Fast drafting is useful only when paired with slow confidence. Design review, failing tests, simulator checks, real-device sessions, beta feedback, and publication scans each catch a different class of error.

## Human access remains irreplaceable

AI cannot wear the watch during a shift, judge whether a vibration is distracting, confirm chest-strap behavior under equipment, or decide whether a beta result feels useful to a player. The human creator supplies real-world access and owns the final judgment.

## A transferable pattern

For developers entering an unfamiliar platform, the reusable pattern is:

1. create or adopt a domain-evidence skill;
2. create or adopt a platform-reference skill;
3. establish product boundaries before coding;
4. keep generated work inside test and review gates;
5. publish claims at the strength of the evidence, not the polish of the output.

That pattern is the real showcase. ShiftSense Hockey is its concrete beta case study.
