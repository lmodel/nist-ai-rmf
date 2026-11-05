---
type: Reference
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/references/iso42001-crosswalk
genre: reference
title: AI RMF to ISO/IEC 42001 crosswalk
description: The PDF that pairs each AI RMF subcategory with clauses and Annex B items of ISO/IEC FDIS 42001. Microsoft provided it, NIST's AI Resource Center lists it, and two scripts pin it by hash. It states no licence.
source:
  - https://airc.nist.gov/docs/NIST_AI_RMF_to_ISO_IEC_42001_Crosswalk.pdf
sources:
  - id: notice
    resource: NOTICE
    title: The AI RMF to ISO/IEC 42001 crosswalk
  - id: test_upstream.py
    resource: tests/test_upstream.py
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# AI RMF to ISO/IEC 42001 crosswalk

NIST's listing says inclusion implies no endorsement.[^notice] `scripts/build_crosswalk.py` and `scripts/check_upstream_release.py` hold one address and one SHA-256, and a test keeps them equal.[^test_upstream.py]

[^notice]: NOTICE, The AI RMF to ISO/IEC 42001 crosswalk
[^test_upstream.py]: tests/test_upstream.py
