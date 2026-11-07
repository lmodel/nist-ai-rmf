---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/vendored-modules
genre: reference
title: Vendored modules
description: The schema modules of lmodel/nist-ai-100-1 at v0.1.0 and lmodel/nist-ai-600-1 at v0.1.1, each copied unchanged from its tag and held to its hash, so the schema needs no network and cannot move under a release.
resource: src/nist_ai_rmf/schema/nist_ai_100_1
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/lmodel-nist-ai-100-1
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/lmodel-nist-ai-600-1
sources:
  - id: schema-readme
    resource: src/nist_ai_rmf/schema/README.md
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: VENDORED_PINS
  - resource: src/nist_ai_rmf/schema/nist_ai_100_1
  - resource: src/nist_ai_rmf/schema/nist_ai_600_1.yaml
  - resource: src/nist_ai_rmf/schema/nist_ai_600_1_risks.yaml
  - resource: src/nist_ai_rmf/schema/nist_ai_600_1_actions.yaml
  - resource: src/nist_ai_rmf/schema/nist_ai_600_1_considerations.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:06:19Z"
status: draft
---

# Vendored modules

`nist_ai_100_1/` holds lmodel/nist-ai-100-1's five modules. lmodel/nist-ai-600-1's four modules sit beside the umbrella, so their imports of `./nist_ai_100_1/` find the one copy. That copy serves both only while lmodel/nist-ai-600-1's own copies of the base and profiles modules are the same files.[^schema-readme]

`VENDORED_PINS` holds each file to its SHA-256, and a test fails on any other file among them.[^test_upstream.py]

[^schema-readme]: src/nist_ai_rmf/schema/README.md
[^test_upstream.py]: tests/test_upstream.py, VENDORED_PINS
