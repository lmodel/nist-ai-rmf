---
type: Service
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/workflows/upstream-watch
genre: reference
title: Upstream watch (upstream-watch.yaml)
description: "The weekly check that `scripts/check_upstream_release.py` runs: a new release of either vendored repository, or other bytes at the crosswalk's address, fail the run and open or update an issue."
resource: .github/workflows/upstream-watch.yaml
about:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/lmodel-nist-ai-100-1
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/lmodel-nist-ai-600-1
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/iso42001-crosswalk
sources:
  - id: upstream-watch.yaml
    resource: .github/workflows/upstream-watch.yaml
  - id: watch
    resource: scripts/check_upstream_release.py
    title: the docstring
  - id: test_watch.py
    resource: tests/test_watch.py
    title: the docstring
  - resource: .github/scripts/report-issue.sh
    title: how the issue is opened
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Upstream watch (upstream-watch.yaml)

The workflow runs every Monday, and a failing check opens an issue or comments on the one already open.[^upstream-watch.yaml]

The script asks GitHub for each repository's latest release and compares the crosswalk's SHA-256 with its pin. It sends no token, and follows a redirect only over https to those hosts.[^watch]

`tests/test_watch.py` runs it against stubbed answers.[^test_watch.py]

[^upstream-watch.yaml]: .github/workflows/upstream-watch.yaml
[^watch]: scripts/check_upstream_release.py, the docstring
[^test_watch.py]: tests/test_watch.py, the docstring
