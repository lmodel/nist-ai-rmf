# Changelog

All notable changes to this project are documented here. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

The `v0.0.0` tag is a baseline, not a release: it marks where versioning starts so the first real release is `0.1.0` rather than `1.0.0`. The schema stays below 1.0.0 until its shape settles, so a breaking change is a minor release.

## [Unreleased]

### Changed

- **The bundle's schema files sit in `.lokf/schema/`**: `lokf.yaml` and the `lokf adapt` copy `nist-ai-rmf.yaml`, as KTL v0.62.0 lays them out.
- **`tests/neighbours/` holds lmodel/iso42001's v0.1.0 asset**, so `just build-crosswalk` checks every crosswalk object against it, and the weekly watch no longer waits for that release.

## [0.1.0] - 2026-11-07

### Added

- **The two repositories' modules, vendored from lmodel/nist-ai-100-1 v0.1.0 and lmodel/nist-ai-600-1 v0.1.1**, in place of an import by address, so the schema needs no network and cannot move under a release. A test holds each file to its hash.
- **`NistAiRmfFamily`**, which holds both publications, is the JSON Schema's top level and refuses a document that holds neither. Each publication's root stays a root.
- **`scripts/build_crosswalk.py`**, which reads the ISO/IEC 42001 crosswalk only from its pinned https address and writes it under `tmp/` as SSSOM. The document states no licence and NIST's listing says its crosswalks come from the user community, so the repository carries neither it nor its pairs.
- **A weekly watch** that reports a release of either repository, lmodel/iso42001's first release and a change to the crosswalk's bytes. It reads only https addresses on its two hosts and quotes what a server answers as code.
- **Tests** that validate both catalogues under one schema, hold every element to its publication's IRI, and run both repositories' examples and counter-examples through one validator.
- **`.lokf/nist-ai-rmf.yaml`, the schema's `lokf adapt` copy.** The knowledge release attaches it as `schema-<tag>-nist-ai-rmf.yaml`.
- **The repository's Knowledge Trust Ladder (KTL) knowledge bundle and its sidecar automation**, from the KTL v0.61.0 templates with the lokf floor at 0.9.0, and a knowledge website that replaces the mkdocs site.
- **The governance files**: SECURITY.md, AI_COVENANT.md, NOTICE and the CONTRIBUTING checklist.

### Changed

- **The template moves to v0.5.0**, with PyPI publishing and the docs preview off, linkml and linkml-runtime locked at 1.12.1, the Python project named `nist-ai-rmf-linkml` and the generators' settings in `.linkml/generators.yaml`.

### Removed

- **The Microsoft Agent Governance Toolkit snapshot and the fixtures a script derived from it**, which tested that script and not the schema.
- **The SSSOM set**, whose rows came from a matching tool, and many of whose targets no schema holds.
- **The mkdocs site**, with redirects from its addresses to the new site.
