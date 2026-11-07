---
lokf_version: "0.2"
okf_version: "0.2"
base_iri: https://w3id.org/lmodel/nist-ai-rmf/knowledge/
context: https://w3id.org/lokf/context.jsonld
title: nist-ai-rmf Knowledge Bundle
description: "NIST AI RMF family: NIST AI 100-1 and NIST AI 600-1 as one schema (LinkML)"
license: https://creativecommons.org/licenses/by/4.0/
publisher:
  type: Person
  id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/person/noel-mcloughlin
  name: Noel McLoughlin
---

# nist-ai-rmf Knowledge Bundle

A [LOKF](https://lokf.nolan-nichols.com) knowledge base for nist-ai-rmf. Every Markdown file under `knowledge/` is one concept; together they form a queryable knowledge graph, derived from this repository's code and docs.

# Services

* [Documentation site](services/documentation-site.md) - The knowledge website in `website/`, an Astro Starlight site that the Knowledge website workflow publishes to GitHub Pages at `https://lmodel.github.io/nist-ai-rmf`, built from the README, `docs/`, the schema's pages and the bundle. It replaces the mkdocs site.

# Datasets

* [The family schema](datasets/nist-ai-rmf-linkml-schema.md) - `nist_ai_rmf.yaml`, the LinkML umbrella that imports lmodel/nist-ai-100-1's and lmodel/nist-ai-600-1's modules and adds `NistAiRmfFamily`, the one class that holds both publications.
* [Vendored modules](datasets/vendored-modules.md) - The schema modules of lmodel/nist-ai-100-1 at v0.1.0 and lmodel/nist-ai-600-1 at v0.1.1, each copied unchanged from its tag and held to its hash, so the schema needs no network and cannot move under a release.
* [The two catalogues](datasets/upstream-catalogues.md) - `tests/upstream/` holds each repository's whole catalogue at the release its modules come from: `ai-rmf-1.0.yaml` and `ai-600-1.yaml`. Tests validate both under one schema and check that the Profile names only subcategories the framework holds.
* [The schema's adapt copy](datasets/adapt-copy.md) - `.lokf/nist-ai-rmf.yaml`, the copy `just lokf-adapt` writes from the umbrella so that it sits beside LOKF's `lokf.yaml`, with the classes both repositories root on `Concept`. A host imports it in place of their two copies.
* [Generated artefacts](datasets/generated-artefacts.md) - What `just gen-project` and `just gen-doc` generate from the schema: the projections in `project/`, the Python models in `src/nist_ai_rmf/datamodel/`, and the merged schema in `docs/schema/`. None is edited by hand.
* [Example data](datasets/example-data.md) - The examples `tests/test_data.py` checks: both repositories' valid examples and counter-examples, copied unchanged from their tags, and this repository's own for `NistAiRmfFamily`. A counter-example's first line names where it must fail.
* [Neighbours' adapt copies](datasets/neighbour-copies.md) - The adapt copies in `tests/neighbours/`, each pinned by its SHA-256: 20 released lmodel repositories this schema's copy must stay apart from, and the two repositories' copies it stands in for.
* [GOVERN 1.1](datasets/example-subcategory.md) - The subcategory GOVERN 1.1, written as a concept of type `AiRmfSubcategory` in the adapt copy's keys. It shows that the domain schema admits a class of lmodel/nist-ai-100-1 as a concept, beside one of lmodel/nist-ai-600-1.
* [Confabulation](datasets/example-risk.md) - The risk of confabulation, written as a concept of type `GaiRisk` in the adapt copy's keys. It shows that the domain schema admits a class of lmodel/nist-ai-600-1 as a concept, beside one of lmodel/nist-ai-100-1.

# Explanations

* [Why one schema for two publications](explanations/why-one-schema.md) - Why this repository exists when lmodel/nist-ai-100-1 and lmodel/nist-ai-600-1 each model their publication: their adapt copies share elements, validate side by side and stop `lokf convert` with `Conflicting URIs`, so a host carrying both needs this copy.
* [The ISO/IEC 42001 crosswalk](explanations/the-crosswalk.md) - Why the AI RMF to ISO/IEC 42001 crosswalk is built on demand and never committed, what each SSSOM row claims, and how the builder reads the PDF: `skos:relatedMatch` rows, Annex B numbers read as Annex A controls, and three rows flagged.
* [What the repository leaves out](explanations/scope.md) - What this repository does not hold: a model of its own, the earlier fixtures derived from the Microsoft Agent Governance Toolkit, the earlier SSSOM set a matching tool wrote, and crosswalks whose targets have no lmodel schema.

# References

* [NIST AI 100-1](references/nist-ai-100-1.md) - NIST AI 100-1, the Artificial Intelligence Risk Management Framework (AI RMF 1.0) of January 2023. lmodel/nist-ai-100-1 models it, and this schema holds that model.
* [NIST AI 600-1](references/nist-ai-600-1.md) - NIST AI 600-1, the Generative Artificial Intelligence Profile of the AI Risk Management Framework, of July 2024. lmodel/nist-ai-600-1 models it, and this schema holds that model.
* [lmodel/nist-ai-100-1](references/lmodel-nist-ai-100-1.md) - The lmodel repository that models the AI RMF as modules and records. This schema vendors all its modules and its catalogue at v0.1.0, and the weekly watch reports a later release.
* [lmodel/nist-ai-600-1](references/lmodel-nist-ai-600-1.md) - The lmodel repository that models the Generative AI Profile as modules and records. This schema vendors all its modules and its catalogue at v0.1.1, whose schema files are unchanged from v0.1.0, and the weekly watch reports a later release.
* [AI RMF to ISO/IEC 42001 crosswalk](references/iso42001-crosswalk.md) - The PDF that pairs each AI RMF subcategory with clauses and Annex B items of ISO/IEC FDIS 42001. Microsoft provided it, NIST's AI Resource Center lists it, and two scripts pin it by hash. It states no licence.

# Glossary

* [Adapt copy](glossary/adapt-copy.md) - An adapt copy: the copy of a published LinkML schema that `lokf adapt` writes so that it can sit beside LOKF's `lokf.yaml` in a domain schema, with its chosen roots on `Concept`.
* [Crosswalk](glossary/crosswalk.md) - A crosswalk: a table that pairs the elements of one framework with elements of another. Here it means the document that pairs AI RMF subcategories with ISO/IEC 42001 clauses and controls, written out as an SSSOM set.

# Playbooks

* [Regenerate and test](playbooks/regenerate-and-test.md) - How to change the umbrella: edit `nist_ai_rmf.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated and vendored files are never edited by hand.
* [Re-vendor the modules](playbooks/re-vendor-the-modules.md) - What to do when lmodel/nist-ai-100-1 or lmodel/nist-ai-600-1 releases: copy its modules, catalogue and schema asset from the tag, move the pins in the watch and the tests, regenerate and test.
* [Build the crosswalk](playbooks/build-the-crosswalk.md) - How to write the AI RMF to ISO/IEC 42001 crosswalk as SSSOM: run `just build-crosswalk`, which downloads the pinned PDF and writes `tmp/mappings/nist-ai-rmf-to-iso42001.sssom.tsv`. Never commit the result.
* [Release](playbooks/release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Knowledge sources map](playbooks/knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.

# Policies

* [AI covenant](policies/ai-covenant.md) - The rules for AI-assisted work here: whoever submits owns the contribution, a vendored file is never edited, the umbrella adds only what it says, a crosswalk's pair comes from its provider, and no commit carries an AI co-authorship trailer.
* [Licence and attribution](policies/license-and-attribution.md) - Whose work each part is: the code and the schema under Apache-2.0, the bundle under CC BY 4.0, NIST's publications under its statement, and the crosswalk, which states no licence and stays out of the repository. No endorsement by NIST is implied.
* [Security policy](policies/security-policy.md) - How to report a vulnerability in this repository, by GitHub's private reporting, what executes here and what holds each surface. A problem in a model belongs with its repository, and one in NIST's text with NIST.

# Workflows

* [Build and test (main.yaml)](workflows/main.md) - The Build and test workflow: on every pull request and push to `main`, it runs `just test` on Python 3.10 to 3.14, lints the schema and checks the adapt copy on 3.13, and in a job of its own builds the crosswalk from its PDF.
* [Lint and docs (lint-and-docs.yaml)](workflows/lint-and-docs.md) - The static checks on pull requests, on `main` and every Monday: ShellCheck, actionlint, the word budgets of CONTRIBUTING.md and SECURITY.md, markdownlint, lychee and codespell.
* [Upstream watch (upstream-watch.yaml)](workflows/upstream-watch.md) - The weekly check that `scripts/check_upstream_release.py` runs: a new release of either vendored repository, lmodel/iso42001's first release, or other bytes at the crosswalk's address, fail the run and open or update an issue.
* [Semantic release (semantic-release.yml)](workflows/semantic-release.md) - The workflow that computes the next version from Conventional Commits on `main`, promotes the changelog, tags and publishes a GitHub Release, and dispatches the knowledge release once `KNOWLEDGE_RELEASE_ENABLED` is `true`.
* [Knowledge librarian (knowledge-librarian.yaml)](workflows/knowledge-librarian.md) - The sidecar's scheduled agent run that keeps the bundle in step with the repository and opens a pull request for a person to review. It is inert until `KNOWLEDGE_LIBRARIAN_ENABLED` is `true`.
* [Knowledge registrar (knowledge-registrar.yaml)](workflows/knowledge-registrar.md) - The gate on the bundle: it validates the bundle on each pull request that touches it and weekly, and checks that each new `human:` event in a pull request is backed by an approval or a signature. It never judges whether content is true.
* [Knowledge release (knowledge-release.yaml)](workflows/knowledge-release.md) - The workflow that attaches the bundle, a Copilot skill and the schema's adapt copy to a GitHub release, each with a checksum. It starts by hand or, once `KNOWLEDGE_RELEASE_ENABLED` is `true`, on each published release.
* [Knowledge sync (knowledge-sync.yaml)](workflows/knowledge-sync.md) - The weekly workflow that keeps the sidecar's copies and the skills pin at the newest release of Knowledge Trust Ladder, by one pull request that a person merges.
* [Knowledge website (knowledge-website.yaml)](workflows/knowledge-website.md) - The workflow that builds `website/` on each pull request that touches its inputs, and deploys the default branch's build to GitHub Pages once `KNOWLEDGE_WEBSITE_ENABLED` is `true`.
