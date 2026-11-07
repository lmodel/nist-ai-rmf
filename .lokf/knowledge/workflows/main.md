---
type: Service
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/workflows/main
genre: reference
title: Build and test (main.yaml)
description: "The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, lints the schema and checks the adapt copy on 3.13, and in a job of its own builds the crosswalk from its PDF."
resource: .github/workflows/main.yaml
references:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/playbooks/regenerate-and-test
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/playbooks/build-the-crosswalk
sources:
  - id: main.yaml
    resource: .github/workflows/main.yaml
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Build and test (main.yaml)

The `test` job runs on Python 3.10 to 3.14. It installs with `uv sync --locked`, and runs `just test`. On Python 3.13 it also runs `just lint` and `just lokf-adapt-check`.[^main.yaml]

The `crosswalk` job reads NIST's address, so an outage there fails that job and no other.[^main.yaml]

[^main.yaml]: .github/workflows/main.yaml
