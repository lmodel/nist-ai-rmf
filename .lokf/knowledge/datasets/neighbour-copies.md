---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/neighbour-copies
genre: reference
title: Neighbours' adapt copies
description: "The adapt copies in `tests/neighbours/`, each pinned by its SHA-256: 21 released lmodel repositories this schema's copy must stay apart from, and the two repositories' copies it stands in for."
resource: tests/neighbours
references:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/adapt-copy
sources:
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
  - resource: tests/neighbours
  - id: builder
    resource: scripts/build_crosswalk.py
generated:
  by: process:ktl-librarian
  at: "2026-11-07T18:48:21Z"
status: draft
---

# Neighbours' adapt copies

Each file is the schema asset of an lmodel release, pinned in `tests/test_schema_rules.py` by its checksum.[^test_schema_rules.py]

The test fails on a shared class, enum, type or subset, and on a shared key it does not list. `nist-ai-100-1.yaml` and `nist-ai-600-1.yaml` are the copies this one replaces, so they are held the other way: each of their elements must be in this copy.[^test_schema_rules.py]

`iso42001.yaml` is lmodel/iso42001's v0.1.0 asset. The crosswalk builder also holds each object of the crosswalk to its `AimsClause` and `AimsAnnexAControl` values.[^builder]

[^test_schema_rules.py]: tests/test_schema_rules.py
[^builder]: scripts/build_crosswalk.py
