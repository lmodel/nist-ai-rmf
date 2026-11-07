---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/explanations/why-one-schema
genre: explanation
title: Why one schema for two publications
description: "Why this repository exists when lmodel/nist-ai-100-1 and lmodel/nist-ai-600-1 each model their publication: their adapt copies share elements, validate side by side and stop `lokf convert` with `Conflicting URIs`, so a host carrying both needs this copy."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/nist-ai-rmf-linkml-schema
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/adapt-copy
sources:
  - id: about.md
    resource: docs/about.md
    title: Why it exists
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Why one schema for two publications

A bundle that names both publications' classes needs one domain schema. The second repository vendors two modules of the first, so the two copies share elements, and `lokf convert` stops on them.[^about.md]

This repository's copy holds each shared element once.[^about.md]

[^about.md]: docs/about.md, Why it exists
