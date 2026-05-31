# About nist-ai-rmf

`nist-ai-rmf` is an **umbrella LinkML schema** for the NIST AI Risk
Management Framework family. It does not redefine any classes,
slots, enums, or types of its own - it simply pulls together two
sibling schemas that are maintained in their own repositories:

| Import | Source repository | Models |
|---|---|---|
| `nist_ai_100_1` | [`lmodel/nist-ai-100-1`](https://w3id.org/lmodel/nist-ai-100-1) | AI RMF 1.0 (NIST AI 100-1): foundational concepts, Core Functions / Categories / Subcategories, Profiles, design attributes, AI RMF Playbook companion data |
| `nist_ai_600_1` | [`lmodel/nist-ai-600-1`](https://w3id.org/lmodel/nist-ai-600-1) | GAI Profile (NIST AI 600-1): 12 GAI risks, Suggested Actions, Primary GAI Considerations, Structured Public Feedback methods |

The sub-schemas are resolved over the network via the `schema_100_1:` and `schema_600_1:` prefixes declared in `src/nist_ai_rmf/schema/nist_ai_rmf.yaml`; they are **not** vendored into this repository.

## Design

```
                     nist_ai_rmf  (umbrella, this repo)
                     /          \
            nist_ai_100_1 ----- nist_ai_600_1
                    \            /
                  nist_ai_rmf_common  (hosted in nist-ai-100-1)
```

* Both sub-schemas import a shared **`nist_ai_rmf_common`** module (hosted in `nist-ai-100-1`) that defines the one canonical base — the `NamedThing` root, identifier/title/description slots, `SubcategoryCode`, and `TrustworthinessCharacteristicEnum`. This is what lets the two be merged into one namespace without colliding.
* Elements re-export under the `nist_ai_rmf:` default prefix, so downstream consumers import only this umbrella to access everything.
* Where the two NIST documents genuinely diverge — the AI lifecycle stages and actor-task vocabularies differ between 100-1 and 600-1 — the GAI Profile keeps its own `GaiLifecycleStageEnum` / `GaiActorTaskEnum` as **class-local attributes** on `GaiRisk` / `SuggestedAction`, so both taxonomies survive the merge intact.
* Two tree-root classes are exposed by the imports:
  * `AiRmfFramework` - from `nist_ai_100_1`
  * `GaiProfile` - from `nist_ai_600_1`
  Callers must pass `--target-class` when running `linkml-validate`.
* SSSOM cross-vocabulary mappings, per-element example fixtures, and the NIST AI RMF Playbook validator all live in the upstream repositories and are exercised by their own CI.

## What this repository ships

* The single umbrella schema (`src/nist_ai_rmf/schema/nist_ai_rmf.yaml`).
* Merged-schema generation targets under `project/` (JSON Schema, OWL, SHACL, ShEx, GraphQL, Pydantic, etc.) produced from the umbrella with all imports inlined.
* Merged-only unit tests under `tests/` that verify both imports resolve and that classes/enums from each sub-schema are reachable through the merged `nist_ai_rmf` namespace.
* A **third-party fixture pipeline** that round-trips real-world governance artefacts through the umbrella schema (see *Solution design state* below).
* **Cross-framework SSSOM mappings** under [`src/nist_ai_rmf/mappings/`](../src/nist_ai_rmf/mappings/) that link RMF subcategories and GAI risks to OWASP ASI, OWASP LLM, EU AI Act, SOC 2, and the AGT ATF.

## Solution design state

The umbrella schema is *consumed* by a deterministic transformer that
converts a pinned snapshot of the **Microsoft Agent Governance Toolkit
(AGT) v3.7.0** into validatable `nist-ai-rmf` instances. This proves
the schema can express a real, externally-maintained governance
corpus end-to-end and gives us regression coverage every time the
umbrella or either sub-schema changes.

### Pipeline

```
upstream-releases/agent-governance-toolkit/   (vendored AGT v3.7.0 snapshot)
   examples/policies/*.yaml                          \
   examples/policy-templates/*.yaml                   \
   examples/atr-community-rules/*.yaml                 \   tests/fixtures/agt_to_rmf.py
   examples/maf-scenarios/*.yaml                       --> (deterministic, network-free,
   examples/aegis/*.yaml                               /    md5-stable, PyYAML + stdlib only)
   docs/compliance/*.md           (RMF / OWASP / ...) /                       |
                                                                              v
                                                       tests/data/third-party/microsoft-agt/
                                                          valid/   AiRmfProfile-*.yaml
                                                                    GaiRisk-asi-*.yaml
                                                                    SuggestedAction-*.yaml
                                                                    Actor-*.yaml
                                                                    StructuredPublicFeedback-*.yaml
                                                          invalid/ (5 negative fixtures)
                                                                              |
                                                                              v
                                                       linkml-validate (closed=True)
                                                          --target-class inferred from filename stem
```

### Reference data vendored under `tests/fixtures/`

| File | Purpose |
|---|---|
| [`nist_ai_600_1_actions.yaml`](../tests/fixtures/nist_ai_600_1_actions.yaml) | Real NIST AI 600-1 `SuggestedAction` reference data (action_id, function_prefix, applies_to_subcategory, gai_risks, actor_task) used to enrich AGT-derived ATR rules and attestation suggested-actions. |
| [`owasp_asi_catalog.yaml`](../tests/fixtures/owasp_asi_catalog.yaml) | Canonical OWASP Agentic Security Initiative Top-10 (2026) catalog: ASI-01..ASI-10 titles + closest `GaiRiskCategoryEnum` value + mapping rationale, sourced from the AGT `owasp-asi-policy-mapping.md` compliance doc. |

### Generator emitters

`tests/fixtures/agt_to_rmf.py` registers ten emitters (currently
producing 69 fixtures):

| Emitter | Upstream source | Target class | Count |
|---|---|---|---|
| `emit_aegis_profiles` | `examples/aegis/*.yaml` | `AiRmfProfile` | 2 |
| `emit_policy_templates` | `examples/policy-templates/*.yaml` | `AiRmfProfile` | 4 |
| `emit_production_policies` | `examples/policies/production/*.yaml` | `AiRmfProfile` (+ derived `Actor` / `StructuredPublicFeedback`) | 10 |
| `emit_maf_scenarios` | `examples/maf-scenarios/*.yaml` | `AiRmfProfile` (+ derived) | 12 |
| `emit_atr_suggested_actions` | `examples/atr-community-rules/atr_security_policy.yaml` | `SuggestedAction` | 20 |
| `emit_asi_gai_risks` | [`owasp_asi_catalog.yaml`](../tests/fixtures/owasp_asi_catalog.yaml) | `GaiRisk` | 10 |
| `emit_attestation_suggested_actions` | `examples/attestation/*` | `SuggestedAction` | 3 |
| `emit_github_actors` | `examples/github-actors/*.yaml` | `Actor` | 2 |
| `emit_decision_bom_feedback` | `examples/decision-bom/*.yaml` | `StructuredPublicFeedback` | 1 |
| `emit_invalid_fixtures` | hand-authored | mixed | 5 |

All AGT-derived `AiRmfProfile` fixtures are enriched with a `see_also`
pointer to
[`docs/compliance/nist-ai-rmf-alignment.md`](../upstream-releases/agent-governance-toolkit/docs/compliance/nist-ai-rmf-alignment.md)
and a one-line coverage attribution sourced from AGT's published
self-assessment (12/19 RMF subcategories fully addressed, 7/19
partially).

### Cross-framework SSSOM

[`src/nist_ai_rmf/mappings/nist_ai_rmf.sssom.tsv`](../src/nist_ai_rmf/mappings/nist_ai_rmf.sssom.tsv)
seeds 60+ cross-framework rows from two AGT compliance docs:

* **Section 9** of `nist-ai-rmf-alignment.md` — RMF category ↔ EU AI
  Act Article ↔ SOC 2 TSC ↔ AGT ATF reference ↔ OWASP LLM Top 10.
* The regulatory-alignment + cross-reference tables of
  `owasp-asi-policy-mapping.md` — `GaiRisk` ↔ OWASP ASI-01..10.

Predicates are `skos:closeMatch` / `skos:relatedMatch`; justification
is `semapv:ManualMappingCuration`. The curie_map covers
`nist_ai_100_1`, `nist_ai_600_1`, `nist_csf`, `oscal_catalog`,
`iso42001`, `eu_ai_act`, `soc2`, `cis_v8`, `owasp_asi`, `owasp_llm`,
and `agt_atf`.

### Invariants enforced by CI

* **Determinism** — `python -m tests.fixtures.agt_to_rmf` is
  idempotent; running it twice produces byte-identical fixture trees
  (md5-stable). No network, no clocks, PyYAML + stdlib only.
* **Pinned upstream** — `upstream-releases/agent-governance-toolkit/`
  is a pinned v3.7.0 snapshot. Its `docs/` subtree is gitignored
  except for `docs/compliance/`, which the fixture pipeline reads
  from directly.
* **Closed-world validation** — every fixture round-trips through
  `linkml-validate` with `JsonschemaValidationPlugin(closed=True)`
  against the merged umbrella schema; `--target-class` is inferred
  from each filename stem.
* **77/77 pytest cases green** at the current head.

### Out of scope (intentionally)

* Element-level `*_mappings:` curation — these continue to live in
  the upstream `nist-ai-100-1` and `nist-ai-600-1` repositories.
* Hosting the AGT snapshot as a git submodule — kept as a vendored
  pinned copy to guarantee reproducible test runs.
* Subcategory-level back-fill of `AiRmfProfile.addresses` — the AGT
  alignment evidence is currently at RMF *category* granularity only.

## References

- [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [NIST AIRC Playbooks](https://airc.nist.gov/airmf-resources/playbook/)
- [NIST AI RMF Website](https://www.nist.gov/itl/ai-risk-management-framework)
- [OWASP Top 10 for Agentic Applications (2026)](https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/)
- [Microsoft Agent Governance Toolkit](https://github.com/microsoft/agent-governance-toolkit) (v3.7.0 vendored under `upstream-releases/`)
