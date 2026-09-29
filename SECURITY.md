# Security Policy

## Reporting a vulnerability

Please use [GitHub private vulnerability reporting](https://github.com/coachrichie/AI-Built-Garmin-Hockey-App/security/advisories/new) for vulnerabilities involving published source, build tooling, or repository automation.

Do not include credentials, personal activity data, private beta material, or exploit details in a public issue. If private reporting is unavailable, open a public issue containing only a request for a private contact channel.

## In scope

- vulnerabilities in source published by this repository;
- unsafe build or installation instructions;
- accidental exposure of secrets or private test data;
- documentation that creates a concrete security or privacy risk.

## Out of scope

- Garmin services, devices, firmware, and infrastructure not owned by this project;
- the separately maintained Codex Skills repository;
- general product ideas without a reproducible security impact;
- medical or training-performance claims, which should be handled as evidence corrections.

## Current beta boundary

This repository does not yet publish the application source and contains no intentional personal activity data. The publication verifier checks for common secrets, local user paths, private activity artifacts, broken links, and unsupported completion claims before release.

No system can guarantee perfect detection. Please report anything that appears private or unsafe so it can be removed and the publication checks improved.
