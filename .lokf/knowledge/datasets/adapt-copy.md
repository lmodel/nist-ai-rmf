---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/adapt-copy
genre: reference
title: The schema's adapt copy
description: "`.lokf/nist-ai-rmf.yaml`, the copy `just lokf-adapt` writes from the umbrella so that it sits beside LOKF's `lokf.yaml`, with the classes both repositories root on `Concept`. A host imports it in place of their two copies."
resource: .lokf/nist-ai-rmf.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/nist-ai-rmf-linkml-schema
about:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/glossary/adapt-copy
sources:
  - id: project.justfile
    resource: project.justfile
    title: the comment above the recipes
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
  - resource: .lokf/nist-ai-rmf.yaml
  - resource: .lokf/justfile
    title: the schema line
  - resource: .lokf/pyproject.toml
    title: the schema setting
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# The schema's adapt copy

`just lokf-adapt` writes `.lokf/nist-ai-rmf.yaml` from the umbrella, and `just lokf-adapt-check` fails when it is stale. CI runs the check.[^project.justfile]

The README lists the concept types for the *Known LOKF types* setting. A release attaches the copy as `schema-<tag>-nist-ai-rmf.yaml`. In this copy a class attribute projects under `nist_ai_rmf:`, and a top-level slot keeps its publication's IRI.[^readme.md]

Tests hold that the copy has every element of the two repositories' copies, with the same body.[^test_schema_rules.py]

[^project.justfile]: project.justfile, the comment above the recipes
[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^test_schema_rules.py]: tests/test_schema_rules.py
