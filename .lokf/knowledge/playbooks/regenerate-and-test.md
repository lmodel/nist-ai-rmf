---
type: Playbook
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/playbooks/regenerate-and-test
genre: how-to
title: Regenerate and test
description: "How to change the umbrella: edit `nist_ai_rmf.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated and vendored files are never edited by hand."
references:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/nist-ai-rmf-linkml-schema
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/generated-artefacts
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: main.yaml
    resource: .github/workflows/main.yaml
    title: the lint step
  - id: justfile
    resource: justfile
    title: the test recipe
generated:
  by: process:ktl-librarian
  at: "2026-11-06T21:26:44Z"
status: draft
---

# Regenerate and test

1. Edit `src/nist_ai_rmf/schema/nist_ai_rmf.yaml`.[^contributing.md]
2. Run `just lint`. A warning fails it.[^main.yaml]
3. Run `just gen-project` and `just gen-doc`, then `just lokf-adapt`.[^contributing.md]
4. Run `just test`, which generates into `tmp/`, runs `pytest` and runs the example runner.[^justfile]
5. Commit the output. `project/`, `src/nist_ai_rmf/datamodel/`, `docs/schema/` and `.lokf/schema/nist-ai-rmf.yaml` are generated.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^main.yaml]: .github/workflows/main.yaml, the lint step
[^justfile]: justfile, the test recipe
