---
type: Playbook
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/playbooks/build-the-crosswalk
genre: how-to
title: Build the crosswalk
description: "How to write the AI RMF to ISO/IEC 42001 crosswalk as SSSOM: run `just build-crosswalk`, which downloads the pinned PDF and writes `tmp/mappings/nist-ai-rmf-to-iso42001.sssom.tsv`. Never commit the result."
references:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/iso42001-crosswalk
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/explanations/the-crosswalk
sources:
  - id: project.justfile
    resource: project.justfile
    title: the crosswalk recipe
  - id: builder
    resource: scripts/build_crosswalk.py
    title: the docstring
  - resource: scripts/build_crosswalk.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Build the crosswalk

1. Run `just build-crosswalk`.[^project.justfile]
2. Read the set in `tmp/mappings/`. The script stops on other bytes, on a subject that is no subcategory, on a subcategory with no row, and on an object that lmodel/iso42001's copy lacks when `tests/neighbours/` holds one.[^builder]
3. Do not commit it: the source states no licence.[^builder]

[^project.justfile]: project.justfile, the crosswalk recipe
[^builder]: scripts/build_crosswalk.py, the docstring
