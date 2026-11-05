---
type: Explanation
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/explanations/the-crosswalk
genre: explanation
title: The ISO/IEC 42001 crosswalk
description: "Why the AI RMF to ISO/IEC 42001 crosswalk is built on demand and never committed, what each SSSOM row claims, and how the builder reads the PDF: `skos:relatedMatch` rows, Annex B numbers read as Annex A controls, and three rows flagged."
resource: scripts/build_crosswalk.py
about:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/iso42001-crosswalk
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/glossary/crosswalk
sources:
  - id: notice
    resource: NOTICE
    title: The AI RMF to ISO/IEC 42001 crosswalk
  - id: builder
    resource: scripts/build_crosswalk.py
    title: the docstring
  - id: about.md
    resource: docs/about.md
    title: The crosswalk
  - resource: tests/test_crosswalk.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# The ISO/IEC 42001 crosswalk

Microsoft provided the crosswalk and NIST's AI Resource Center lists it. The document states no licence and quotes ISO's headings, so the repository carries neither it nor its pairs.[^notice] `just build-crosswalk` writes the set under `tmp/`.[^builder]

The document names no relation between its columns, so each row is a `skos:relatedMatch`. It cites Annex B's guidance, so a row names the Annex A control of the same number.[^about.md]

It was written against ISO/IEC FDIS 42001, and nothing here compares it with the published text. Three rows print a number with a heading the document gives that number nowhere else, and each row keeps the number and says so in its comment.[^about.md]

[^notice]: NOTICE, The AI RMF to ISO/IEC 42001 crosswalk
[^builder]: scripts/build_crosswalk.py, the docstring
[^about.md]: docs/about.md, The crosswalk
