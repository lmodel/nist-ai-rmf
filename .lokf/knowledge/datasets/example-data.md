---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/example-data
genre: reference
title: Example data
description: "The examples `tests/test_data.py` checks: both repositories' valid examples and counter-examples, copied unchanged from their tags, and this repository's own for `NistAiRmfFamily`. A counter-example's first line names where it must fail."
resource: tests/data
references:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/nist-ai-rmf-linkml-schema
sources:
  - id: test_data.py
    resource: tests/test_data.py
  - resource: tests/data
  - resource: tests/__init__.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Example data

Each file under `tests/data/valid/` or `tests/data/invalid/` is named after the class it is checked against.[^test_data.py]

Each counter-example's first line, `# Fails at: <pointer>`, names where the validator must fail, so a file that starts failing for another reason fails the test.[^test_data.py]

[^test_data.py]: tests/test_data.py
