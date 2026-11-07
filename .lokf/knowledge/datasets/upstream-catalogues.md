---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/upstream-catalogues
genre: reference
title: The two catalogues
description: "`tests/upstream/` holds each repository's whole catalogue at the release its modules come from: `ai-rmf-1.0.yaml` and `ai-600-1.yaml`. Tests validate both under one schema and check that the Profile names only subcategories the framework holds."
resource: tests/upstream
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/lmodel-nist-ai-100-1
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/lmodel-nist-ai-600-1
sources:
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
  - id: test_upstream.py
    resource: tests/test_upstream.py
    title: VENDORED_PINS
  - resource: tests/upstream
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:06:19Z"
status: draft
---

# The two catalogues

`tests/test_catalogue.py` validates both catalogues in one document against the committed JSON Schema, validates each alone against its own root, and loads the two into the generated models.[^test_catalogue.py]

It also checks that every subcategory the Profile's tables name is one of the framework's 72.[^test_catalogue.py] `tests/test_upstream.py` holds each file to its hash.[^test_upstream.py]

[^test_catalogue.py]: tests/test_catalogue.py
[^test_upstream.py]: tests/test_upstream.py, VENDORED_PINS
