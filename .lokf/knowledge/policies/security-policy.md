---
type: Policy
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/policies/security-policy
genre: reference
title: Security policy
description: How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in a model belongs with its repository, and one in NIST's text with NIST.
resource: SECURITY.md
references:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/workflows/upstream-watch
sources:
  - id: security.md
    resource: SECURITY.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Security policy

Report a vulnerability through GitHub's private vulnerability reporting. Only the latest release receives fixes.[^security.md]

The release carries the adapt copy, the bundle as a zip and a Copilot skill zip, each with a checksum and a build-provenance attestation.[^security.md]

The vendored catalogues are NIST's text, and this repository treats them as data. Tests validate them, and nothing executes or renders them.[^security.md]

`scripts/check_upstream_release.py` runs only in the weekly watch, and `scripts/build_crosswalk.py` in one job of the build. Neither holds a token, and each reads at most 20 MB.[^security.md]

[^security.md]: SECURITY.md
