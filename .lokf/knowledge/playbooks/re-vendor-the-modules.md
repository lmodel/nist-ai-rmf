---
type: Playbook
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/playbooks/re-vendor-the-modules
genre: how-to
title: Re-vendor the modules
description: "What to do when lmodel/nist-ai-100-1 or lmodel/nist-ai-600-1 releases: copy its modules, catalogue and schema asset from the tag, move the pins in the watch and the tests, regenerate and test."
references:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/vendored-modules
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/playbooks/regenerate-and-test
sources:
  - id: contributing.md
    resource: CONTRIBUTING.md
    title: Before opening a pull request
  - id: schema-readme
    resource: src/nist_ai_rmf/schema/README.md
  - id: test_schema_rules.py
    resource: tests/test_schema_rules.py
    title: the comment above the neighbours
  - id: watch
    resource: scripts/check_upstream_release.py
    title: VENDORED_FROM
generated:
  by: process:ktl-librarian
  at: "2026-11-07T01:11:59Z"
status: draft
---

# Re-vendor the modules

1. Copy the modules and the catalogue from the release's tag, unchanged. A vendored file changes at its source.[^contributing.md] When the release changes the base or profiles module, vendor it together with a matching release of the other repository.[^schema-readme]
2. Copy the release's schema asset to `tests/neighbours/`, after checking its `.sha256` and its attestation.[^test_schema_rules.py]
3. Move `VENDORED_PINS` and the release named in `VENDORED_FROM`.[^watch] Move that asset's checksum in `FAMILY` too.[^test_schema_rules.py]
4. Run the steps in the regenerate-and-test playbook.[^contributing.md]

[^contributing.md]: CONTRIBUTING.md, Before opening a pull request
[^schema-readme]: src/nist_ai_rmf/schema/README.md
[^test_schema_rules.py]: tests/test_schema_rules.py, the comment above the neighbours
[^watch]: scripts/check_upstream_release.py, VENDORED_FROM
