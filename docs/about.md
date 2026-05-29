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

## References

- [NIST AI 100-1](https://nvlpubs.nist.gov/nistpubs/ai/nist.ai.100-1.pdf)
- [NIST AI 600-1](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf)
- [NIST AIRC Playbooks](https://airc.nist.gov/airmf-resources/playbook/)
- [NIST AI RMF Website](https://www.nist.gov/itl/ai-risk-management-framework)
