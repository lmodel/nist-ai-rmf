# Change Log

## 2026-11-07

* **Changed**: the neighbour copies cite the crosswalk builder.
* **Changed**: `tests/neighbours/` holds lmodel/iso42001's v0.1.0 asset, so the crosswalk's objects are checked.
* **Changed**: the watch no longer waits for lmodel/iso42001's first release, since its copy is in `tests/neighbours/`.
* **Changed**: the lmodel/nist-ai-600-1 reference and the re-vendor playbook say plainly which files and which asset they mean.
* **Prose**: reworded 2 concept bodies in plain English. No fact, link, number or frontmatter changed.
* **Changed**: the audit of 2026-11-07: lmodel/nist-ai-600-1 is vendored at v0.1.1 (no schema change), `NistAiRmfFamily` refuses a document with neither publication, and the watch reports lmodel/iso42001's first release.

## 2026-11-06

* **Changed**: `lokf.yaml` and `nist-ai-rmf.yaml` moved into `.lokf/schema/`, where KTL v0.62.0 keeps a sidecar's schema files, and the concepts that name them follow.

## 2026-11-05

* **Prose**: reworded one concept body in plain English. No fact, link, number or frontmatter changed.
* **Changed**: What the repository leaves out, a dead word out of its description.
* **Added**: The family schema.
* **Added**: Vendored modules.
* **Added**: The two catalogues.
* **Added**: The schema's adapt copy.
* **Added**: Generated artefacts.
* **Added**: Example data.
* **Added**: Neighbours' adapt copies.
* **Added**: GOVERN 1.1.
* **Added**: Confabulation.
* **Added**: Why one schema for two publications.
* **Added**: The ISO/IEC 42001 crosswalk.
* **Added**: What the repository leaves out.
* **Added**: NIST AI 100-1.
* **Added**: NIST AI 600-1.
* **Added**: lmodel/nist-ai-100-1.
* **Added**: lmodel/nist-ai-600-1.
* **Added**: AI RMF to ISO/IEC 42001 crosswalk.
* **Added**: Adapt copy.
* **Added**: Crosswalk.
* **Added**: Regenerate and test.
* **Added**: Re-vendor the modules.
* **Added**: Build the crosswalk.
* **Added**: Release.
* **Added**: AI covenant.
* **Added**: Licence and attribution.
* **Added**: Security policy.
* **Added**: Documentation site.
* **Added**: Build and test (main.yaml).
* **Added**: Lint and docs (lint-and-docs.yaml).
* **Added**: Upstream watch (upstream-watch.yaml).
* **Added**: Semantic release (semantic-release.yml).
* **Added**: Knowledge librarian (knowledge-librarian.yaml).
* **Added**: Knowledge registrar (knowledge-registrar.yaml).
* **Added**: Knowledge release (knowledge-release.yaml).
* **Added**: Knowledge sync (knowledge-sync.yaml).
* **Added**: Knowledge website (knowledge-website.yaml).
* **Added**: Knowledge sources map.
* **Initialization**: Scaffolded the LOKF bundle for nist-ai-rmf with placeholder
  services. Real concepts to follow.
