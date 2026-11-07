---
type: Playbook
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/playbooks/knowledge-sources
genre: reference
title: Knowledge sources map
description: "The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons."
resource: .
references:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/nist-ai-rmf-linkml-schema
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/lmodel-nist-ai-100-1
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/lmodel-nist-ai-600-1
sources:
  - resource: src/nist_ai_rmf/schema
  - resource: src/nist_ai_rmf/datamodel
  - resource: scripts
  - resource: tests
  - resource: docs
  - resource: website
  - resource: .github/workflows
  - resource: .github/scripts
  - resource: .github/release
  - resource: .linkml
  - resource: .lokf/justfile
  - resource: .lokf/pyproject.toml
  - resource: .lokf/nist-ai-rmf.yaml
  - resource: project
  - resource: project.justfile
  - resource: justfile
  - resource: README.md
  - resource: CHANGELOG.md
  - resource: CONTRIBUTING.md
  - resource: SECURITY.md
  - resource: AI_COVENANT.md
  - resource: NOTICE
  - resource: LICENSE
  - resource: .releaserc.json
exclusions:
  - resource: .github/dependabot.yml
    reason: "Tooling: when Dependabot opens version bumps."
  - resource: .github/ISSUE_TEMPLATE
    reason: Issue forms, which are governance text and state nothing about the schema.
  - resource: .github/pull_request_template.md
    reason: The pull request checklist, which repeats CONTRIBUTING.md.
  - resource: CODE_OF_CONDUCT.md
    reason: The Contributor Covenant, governance text with nothing about the schema.
  - resource: uv.lock
    reason: The package's lock file, tooling that pins versions.
  - resource: pyproject.toml
    reason: Package metadata and the spell checkers' settings; the changelog states the Python project's name.
  - resource: .gitignore
    reason: "Tooling: the files git ignores."
  - resource: .editorconfig
    reason: "Tooling: editor settings."
  - resource: .yamllint.yaml
    reason: "Tooling: the YAML linter's settings."
  - resource: .pre-commit-config.yaml
    reason: "Tooling: the hooks and the files they leave alone."
  - resource: .markdownlint-cli2.jsonc
    reason: "Tooling: the Markdown linter's settings."
  - resource: .linkmllint.yaml
    reason: "Tooling: the schema linter's settings, which relax nothing."
  - resource: lychee.toml
    reason: "Tooling: the link checker's settings."
  - resource: config.public.mk
    reason: "Tooling: the variables the justfile loads."
  - resource: .copier-answers.yml
    reason: The copier template's answers, which `just update` reads.
  - resource: src/README.md
    reason: Text from the project template.
  - resource: docs/templates-linkml
    reason: The template's placeholders for gen-doc, not pages.
  - resource: docs/elements
    reason: Generated pages that git ignores, apart from a placeholder.
  - resource: examples/README.md
    reason: Text from the project template about generated example output.
  - resource: src/nist_ai_rmf/__init__.py
    reason: Package plumbing.
  - resource: src/nist_ai_rmf/_version.py
    reason: Package plumbing.
  - resource: llms.txt
    reason: The pointer that sends agents to this bundle.
  - resource: knowledge_bundle
    reason: The sidecar's link to the bundle.
  - resource: .github/PULL_REQUEST_TEMPLATE
    reason: The sidecar sync's pull request template.
  - resource: .lokf/lokf.yaml
    reason: LOKF's schema, pinned by the sidecar.
  - resource: .lokf/scripts
    reason: The sidecar's scripts, which the weekly sync replaces.
  - resource: .lokf/m365
    reason: The sidecar's Copilot skill files.
  - resource: .lokf/.gitattributes
    reason: The sidecar's line-ending setting.
  - resource: .lokf/.gitignore
    reason: The sidecar's ignore list.
  - resource: .lokf/ingest.yaml.sample
    reason: The sidecar's example manifest, unused here.
  - resource: .lokf/queries.http
    reason: The sidecar's example SPARQL queries.
  - resource: .lokf/README.md
    reason: The sidecar's own description.
  - resource: .lokf/uv.lock
    reason: The sidecar's lock file.
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Knowledge sources map

| Source | Yields | Re-check by |
| --- | --- | --- |
| `src/nist_ai_rmf/schema/` | The schema's datasets | `just lint` and `just test` |
| `tests/upstream/` | The two catalogues | `tests/test_upstream.py` and the weekly watch |
| `scripts/` | The crosswalk and the watch | `just build-crosswalk` and `tests/test_watch.py` |
| `tests/` | The example data and what the tests hold | `just test` |
| `docs/about.md` | The explanations | Reading it |
| `.github/workflows/` | One concept per workflow | Reading each header comment |
| `SECURITY.md`, `AI_COVENANT.md`, `NOTICE`, `CONTRIBUTING.md` | The policies and playbooks | Reading each |
| `website/` | The documentation site | `npm run build` |
