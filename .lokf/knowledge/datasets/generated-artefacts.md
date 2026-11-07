---
type: Dataset
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/generated-artefacts
genre: reference
title: Generated artefacts
description: "What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/nist_ai_rmf/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand."
resource: project
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/nist-ai-rmf-linkml-schema
sources:
  - id: justfile
    resource: justfile
    title: the gen-project and gen-doc recipes
  - id: generators.yaml
    resource: .linkml/generators.yaml
    title: the jsonschema settings
  - resource: project
  - resource: src/nist_ai_rmf/datamodel
  - resource: docs/schema
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Generated artefacts

`just gen-project` writes the projections in `project/` and the Python models in `src/nist_ai_rmf/datamodel/`. `just gen-doc` writes the merged schema to `docs/schema/nist_ai_rmf.yaml` and the element pages to `docs/elements/`, which git ignores.[^justfile]

`.linkml/generators.yaml` names `NistAiRmfFamily` as the JSON Schema's top level, because two imported classes are tree roots as well.[^generators.yaml]

[^justfile]: justfile, the gen-project and gen-doc recipes
[^generators.yaml]: .linkml/generators.yaml, the jsonschema settings
