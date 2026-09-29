# I Built a Garmin Hockey App Without Knowing Monkey C—AI Skills Made the Difference

## The real breakthrough was not AI-generated code. It was turning AI into a system of specialized skills, evidence, and verification.

When I started building ShiftSense Hockey, I had an idea—but no experience with Monkey C, Garmin’s programming language for Connect IQ devices.

The obvious approach would have been to ask an AI assistant to “build a Garmin hockey app.” That might have produced code quickly. It would not have answered the questions that actually determine whether a wearable application deserves to exist:

- What can a wrist-worn device measure reliably during hockey?
- Which metrics are direct measurements, and which are estimates?
- Which Garmin APIs are available on the target devices?
- How should the app behave when a sensor disappears or data quality drops?
- What evidence is required before a beta feature becomes a public claim?

The project became possible when I stopped treating AI as a single coding assistant and started treating it as a system of specialized skills.

## From general intelligence to specialized capability

The first major skill focused on hockey evidence.

Its job was not to generate impressive metric names. It was to examine sports-science research, capture the population and measurement method behind each finding, identify transfer limits, and translate that evidence into product constraints.

That distinction matters. A value can be technically computable without being scientifically defensible—especially when intense skating, stick handling, impacts, protective equipment, and wrist movement all affect the data.

The second skill focused on Garmin Connect IQ.

Instead of relying on an AI model’s memory, it used the Garmin Toybox API reference as its source of truth. It helped map requirements to actual APIs, permissions, device capabilities, FIT recording, display constraints, and platform limitations.

For someone new to Monkey C, this changed the problem completely. I no longer needed to begin by memorizing an unfamiliar platform. I could begin with a product question and use the skill to discover what the platform genuinely supported.

## The development process became a skill too

Domain knowledge alone was not enough. The project also needed a disciplined way to move from idea to implementation.

The workflow became:

1. Clarify the product intent and boundaries.
2. Research what the evidence can support.
3. Verify what the platform can implement.
4. Design components and failure behavior before coding.
5. Break the design into testable implementation steps.
6. Debug causes rather than patching symptoms.
7. Review and verify before making completion claims.

This is where AI-assisted development became much more interesting than code generation.

Each skill had a narrow responsibility. The hockey evidence skill could challenge an attractive but weak metric. The Garmin skill could reject a plausible API that did not exist on the target device. The verification workflow could prevent a passing demo from becoming an unsupported accuracy claim.

AI did not become infallible. It became easier to audit.

## What ShiftSense Hockey is designed to do

ShiftSense Hockey is an offline-first Garmin Connect IQ application for ice and inline hockey.

The approved design separates the time-critical watch experience from deeper local analysis. It calls for standard FIT activity recording, work-and-recovery segmentation, hockey-specific load and recovery metrics, optional chest-strap support, and a local browser-based analysis layer.

Just as important, the design separates five kinds of information:

- measured values;
- values provided by the device;
- derived metrics;
- estimated metrics;
- experimental signals.

That classification is part of the product, not a footnote. Users should be able to tell the difference between a recorded duration and an inferred movement event.

The application is currently in beta testing. The public showcase deliberately avoids feature-level accuracy claims, broad compatibility promises, or production-readiness language until the supporting evidence can be published.

## What AI did—and what it could not do

AI accelerated research, platform learning, architecture, documentation, implementation work, testing, debugging, and review.

But it could not wear the watch during a shift. It could not decide whether a vibration was distracting under real game conditions. It could not validate sensor behavior beneath hockey equipment. And it could not take responsibility for publishing a claim.

Human judgment remained essential for the product goal, acceptable tradeoffs, hardware testing, interpretation of beta feedback, privacy decisions, and release approval.

The working principle became:

> AI can propose and execute. Evidence and human judgment authorize confidence.

## The lesson for developers and AI builders

The most useful question is no longer simply, “Can AI write this code?”

A better set of questions is:

- Does the AI have a maintained source of truth for the domain?
- Does it understand the real constraints of the platform?
- Are requirements explicit before implementation begins?
- Can every important claim be traced to evidence?
- Are tests and reviews part of the workflow rather than an afterthought?

Specialized skills do not eliminate engineering discipline. They make that discipline reusable.

That is the part of this project I wanted to publish first. The application source will follow after beta stabilization, but the development system is already useful to anyone exploring an unfamiliar technical platform with AI.

The complete technical portfolio—including the skill architecture, system design, validation model, beta status, and lessons learned—is available here:

https://github.com/coachrichie/AI-Built-Garmin-Hockey-App

I would be interested to hear how other developers structure AI for unfamiliar domains: as one general assistant, or as a set of specialized, verifiable skills?

---

**Suggested LinkedIn SEO title:** How AI Skills Helped Me Build a Garmin Hockey App Without Monkey C Experience

**Suggested SEO description:** A developer-focused case study showing how specialized AI skills, evidence, Garmin platform knowledge, and verification enabled a beta hockey app without prior Monkey C experience.

**Suggested share commentary:** I started with a Garmin hockey-app idea and no Monkey C experience. The breakthrough was not asking AI to write everything—it was building a system of specialized skills for hockey evidence, Garmin APIs, engineering, and verification. Here is the technical story behind the beta.

**Suggested hashtags:** #AISkills #AIAssistedDevelopment #Garmin #ConnectIQ #MonkeyC #Wearables #SportsTech #IceHockey
