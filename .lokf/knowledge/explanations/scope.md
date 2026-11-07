---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/explanations/scope
genre: explanation
title: What the repository leaves out
description: "What this repository does not hold: a model of its own, the earlier fixtures derived from the Microsoft Agent Governance Toolkit, the earlier SSSOM set a matching tool wrote, and crosswalks whose targets have no lmodel schema."
resource: docs/about.md
about:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/nist-ai-rmf-linkml-schema
sources:
  - id: about.md
    resource: docs/about.md
    title: What it leaves out
  - resource: CHANGELOG.md
  - resource: docs/index.md
generated:
  by: process:ktl-librarian
  at: "2026-11-05T10:08:28Z"
status: draft
---

# What the repository leaves out

A change to a class belongs in its own repository, and a release carries it here.[^about.md]

The earlier fixtures came from a script that turned a toolkit's snapshot into this schema's shape, so they tested the script. The earlier SSSOM set came from a matching tool, and many of its targets exist in no schema.[^about.md]

Other crosswalks on NIST's page have targets with no lmodel schema to hold their objects.[^about.md]

[^about.md]: docs/about.md, What it leaves out
