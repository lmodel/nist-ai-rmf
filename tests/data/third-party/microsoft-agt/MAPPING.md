# AGT Examples -> NIST AI RMF Fixture Mapping

This document maps source files in
`upstream-releases/agent-governance-toolkit/examples/`
(snapshot version **3.7.0** — see `upstream-releases/agent-governance-toolkit/VERSION`) to the RMF class fixtures generated under `tests/data/third-party/microsoft-agt/{valid,invalid}/`.

> Third-party data is partitioned per upstream source so that fixtures
> derived from different vendors live side-by-side without colliding.
> Each `SuggestedAction` fixture is joined to a real NIST AI 600-1
> reference action listed in
> [`tests/fixtures/nist_ai_600_1_actions.yaml`](../fixtures/nist_ai_600_1_actions.yaml).

Fixtures are produced by `tests/fixtures/agt_to_rmf.py` and validated by `tests/test_fixtures.py`. Run the generator manually with:

```bash
just gen-fixtures
# or
python -m tests.fixtures.agt_to_rmf
```

## Emitters

| Emitter | Source | RMF target class | Fixture stem prefix | Count |
|---|---|---|---|---|
| `emit_aegis_profiles` | `aegis-governance-profile/profile-*.yaml` | `AiRmfProfile` (USE_CASE) | `AiRmfProfile-aegis-` | 2 |
| `emit_policy_templates` | `policy-templates/*.yaml` | `AiRmfProfile` (CROSS_SECTORAL) | `AiRmfProfile-template-` | 4 |
| `emit_production_policies` | `policies/production/*.yaml` | `AiRmfProfile` + `RiskTolerance` | `AiRmfProfile-production-`, `RiskTolerance-production-` | 10 |
| `emit_maf_scenarios` | `maf-integration/<n>/python/policies/*.yaml` | `AiSystem` + `AiRmfProfile` | `AiSystem-maf-`, `AiRmfProfile-maf-` | 12 |
| `emit_atr_suggested_actions` | `atr-community-rules/atr_security_policy.yaml` (first 20 unique rule families) | `SuggestedAction` | `SuggestedAction-atr-` | 20 |
| `emit_asi_gai_risks` | `tests/fixtures/owasp_asi_catalog.yaml` (canonical OWASP ASI-01..ASI-10, 2026) | `GaiRisk` | `GaiRisk-asi-` | 10 |
| `emit_attestation_suggested_actions` | `{crypto,physical,reasoning}-attestation-governed/README.md` | `SuggestedAction` (+ provenance technique in description) | `SuggestedAction-attestation-` | 3 |
| `emit_github_actors` | `github-actions-governance/agents.yaml` | `AiActor` | `AiActor-github-` | 2 |
| `emit_decision_bom_feedback` | `decision-bom/README.md` | `StructuredPublicFeedback` | `StructuredPublicFeedback-` | 1 |
| `emit_invalid_fixtures` | (synthetic) | various — must fail validation | `tests/data/third-party/microsoft-agt/invalid/` | 5 |

**Total:** 64 valid + 5 invalid fixtures.

## ASI ↔ GAI risk-category mapping (informational)

ASI titles and risk-category bindings come from the **canonical** OWASP
Agentic Security Initiative Top-10 (2026) catalog vendored at
[`tests/fixtures/owasp_asi_catalog.yaml`](../../../fixtures/owasp_asi_catalog.yaml),
which in turn cites the AGT compliance doc
[`owasp-asi-policy-mapping.md`](../../../../upstream-releases/agent-governance-toolkit/docs/compliance/owasp-asi-policy-mapping.md)
and <https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/>.
Each generated `GaiRisk` fixture sets `gai_risk_kind` directly from
this catalog (see-also lists both the upstream policy template and the
AGT mapping doc).

| ASI id | OWASP title (canonical) | `GaiRiskCategoryEnum` |
|---|---|---|
| ASI-01 | Agent Goal Hijack | `INFORMATION_INTEGRITY` |
| ASI-02 | Tool Misuse & Exploitation | `INFORMATION_SECURITY` |
| ASI-03 | Identity & Privilege Abuse | `INFORMATION_SECURITY` |
| ASI-04 | Agentic Supply Chain | `VALUE_CHAIN_AND_COMPONENT_INTEGRATION` |
| ASI-05 | Unexpected Code Execution | `INFORMATION_SECURITY` |
| ASI-06 | Memory & Context Poisoning | `INFORMATION_INTEGRITY` |
| ASI-07 | Insecure Inter-Agent Communication | `INFORMATION_SECURITY` |
| ASI-08 | Cascading Agent Failures | `HUMAN_AI_CONFIGURATION` |
| ASI-09 | Human-Agent Trust Exploitation | `HUMAN_AI_CONFIGURATION` |
| ASI-10 | Rogue Agents | `HUMAN_AI_CONFIGURATION` |

> Earlier revisions of this table used paraphrased titles harvested
> from comment blocks in `policy-templates/healthcare.yaml`; the
> canonical values above supersede them.

## Filename convention

Every fixture filename uses the stem pattern
`<TargetClassName>-<slug>.yaml`. The test
[`tests/test_fixtures.py`](../test_fixtures.py) recovers the target class from the leading token (before the first `-`) and feeds it as `--target-class` to the LinkML JSON-Schema validator.

## Traceability

Every generated fixture sets a `see_also: [<upstream relative path>]` slot pointing back to the AGT source file that seeded it.
