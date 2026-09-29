# The AI Skill System

The central experiment behind ShiftSense Hockey was not whether a general AI could emit Monkey C. It was whether specialized, reusable instructions could make AI work more like an engineering team: one capability grounded in hockey evidence, another grounded in Garmin's platform, and a process layer that keeps decisions inspectable.

## Domain skill: Hockey Evidence

The **Hockey Evidence** skill supports sports-science research, evidence appraisal, product audits, and traceable algorithm design for wearable hockey data.

Its job is to connect a product idea to what the evidence can reasonably support:

- find and compare relevant research;
- record population, measurement method, and transfer limits;
- distinguish direct measurements from inference;
- turn findings into algorithm constraints and validation targets;
- flag claims that a wrist-worn device cannot yet justify.

This matters because hockey combines short intense efforts, recovery, collisions, equipment, cold conditions, and wrist movement. A number can be technically computable without being scientifically defensible.

## Platform skill: Garmin Connect IQ

The **Garmin Connect IQ** skill grounds development in the locally mirrored Toybox API reference instead of memory.

It helps resolve:

- which APIs and types own a capability;
- API-level and device availability;
- manifest permissions;
- sensor, activity-recording, and FIT interfaces;
- device-family and display constraints;
- deprecations and platform-specific behavior.

For a first-time Monkey C developer, this changes the question from “What syntax should I write?” to “What does this platform support, on which devices, and under what constraints?”

## Process skills

**Process skills** make the two domain capabilities operate as a repeatable workflow:

1. Brainstorming turns an idea into explicit intent, boundaries, and acceptance criteria.
2. Design captures components, data flow, failure behavior, and validation strategy.
3. Implementation planning breaks the design into reviewable test cycles.
4. Test-driven development defines observable behavior before implementation.
5. Systematic debugging searches for causes instead of patching symptoms.
6. Review and verification require current evidence before completion claims.

These controls are especially important in AI-assisted development because fast output can otherwise hide weak assumptions.

## Human responsibility

AI accelerated research, platform learning, design exploration, documentation, and implementation work. It did not remove the creator's responsibility.

Human decisions remain decisive for:

- the product goal and intended users;
- acceptable tradeoffs and risk;
- access to real hockey sessions and Garmin hardware;
- interpretation of beta feedback;
- privacy choices and publication approval;
- deciding when evidence is strong enough for a claim.

The working principle is simple: **AI can propose and execute; evidence and human judgment authorize confidence.**

## Reusable skills, separate repository

The reusable Hockey Evidence and Garmin Connect IQ skills live in [coachrichie/Codex-Skills](https://github.com/coachrichie/Codex-Skills). Keeping them separate avoids coupling the general tools to one application and allows other projects to use or improve them independently.

This portfolio documents their combined application, not their full installation or internal reference sets.
