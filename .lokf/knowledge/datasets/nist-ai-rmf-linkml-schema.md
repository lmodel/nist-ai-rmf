---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/nist-ai-rmf-linkml-schema
genre: reference
title: The family schema
description: "`nist_ai_rmf.yaml`, the LinkML umbrella that imports lmodel/nist-ai-100-1's and lmodel/nist-ai-600-1's modules and adds `NistAiRmfFamily`, the one class that holds both publications."
resource: src/nist_ai_rmf/schema/nist_ai_rmf.yaml
dependsOn:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/vendored-modules
sources:
  - id: schema
    resource: src/nist_ai_rmf/schema/nist_ai_rmf.yaml
    title: the comments
  - id: test_catalogue.py
    resource: tests/test_catalogue.py
  - resource: src/nist_ai_rmf/schema/README.md
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:06:19Z"
status: draft
---

# The family schema

The umbrella imports both publications' root schemas and declares one class, `NistAiRmfFamily`.[^schema] Each element keeps the IRI its publication gives it.[^schema]

`tests/test_catalogue.py` holds the umbrella to that one class and every element to its publication's IRI.[^test_catalogue.py]

Each publication's root stays a root, so a file holding one publication validates against `AiRmfFramework` or `GaiProfile`. The JSON Schema's top level is `NistAiRmfFamily`, and it refuses a document that holds neither publication.[^schema]

[^schema]: src/nist_ai_rmf/schema/nist_ai_rmf.yaml, the comments
[^test_catalogue.py]: tests/test_catalogue.py
