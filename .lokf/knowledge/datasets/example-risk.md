---
type: GaiRisk
id: https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/example-risk
genre: reference
title: Confabulation
description: The risk of confabulation, written as a concept of type `GaiRisk` in the adapt copy's keys. It shows that the domain schema admits a class of lmodel/nist-ai-600-1 as a concept, beside one of lmodel/nist-ai-100-1.
resource: tests/data/valid/GaiProfile-minimal.yaml
derivedFrom:
  - https://w3id.org/lmodel/nist-ai-rmf/knowledge/datasets/upstream-catalogues
sources:
  - id: readme.md
    resource: README.md
    title: the Knowledge Trust Ladder (KTL) section
  - id: example-profile
    resource: tests/data/valid/GaiProfile-minimal.yaml
gai_risk_name: confabulation
gai_risk_section: "2.2"
generated:
  by: process:ktl-librarian
  at: "2026-11-05T09:59:50Z"
status: draft
---

# Confabulation

A concept may name a class the README lists as its `type`, with the copy's keys beside LOKF's.[^readme.md] This one comes from a valid example.[^example-profile]

[^readme.md]: README.md, the Knowledge Trust Ladder (KTL) section
[^example-profile]: tests/data/valid/GaiProfile-minimal.yaml
