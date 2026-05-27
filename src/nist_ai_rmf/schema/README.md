# Schema Directory

LinkML schemas for the NIST AI Risk Management Framework family.

## Files

| File | Models | Source |
|---|---|---|
| [nist_ai_rmf.yaml](nist_ai_rmf.yaml) | AI RMF 1.0 - foundational concepts, Core Functions/Categories/Subcategories, Profiles, Playbook companion data | [NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1) (January 2023) |
| [nist_ai_600_1.yaml](nist_ai_600_1.yaml) | GAI Profile - 12 GAI risks, suggested actions, primary considerations | [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1) (July 2024) |
| [NIST.AI.100-1.pdf](NIST.AI.100-1.pdf), [NIST.AI.600-1.pdf](NIST.AI.600-1.pdf) | Source documents | NIST |
| [ecosystem/](ecosystem/) | Snapshot of related lmodel schemas (NIST CSF v2, OSCAL, ISO 27001/29100, STIX, GIST, ...) used for cross-vocabulary mappings | lmodel ecosystem |

## Status

| Area | State |
|---|---|
| Coverage | 100% of NIST AI 100-1 and NIST AI 600-1 modelled |
| `linkml-lint` | clean on both schemas (only stylistic `standard_naming` warnings for uppercase enum values, per project convention) |
| `gen-project` | produces JSON Schema, OWL, SHACL, ShEx, Pydantic, TypeScript, Java, Protobuf, GraphQL without errors |
| Pytest suite | 20/20 passing - valid + invalid fixtures plus the full 72-entry NIST AI RMF Playbook |
| SSSOM mappings | 33 base + 12 GAI cross-vocabulary mappings, verifier guards against drift (`just verify-mappings`) |
| Playbook validation | `just validate-playbook` runs the third-party NIST Playbook JSON through `scripts/validate_playbook.py` |

## Element counts

### `nist_ai_rmf` (base, AI RMF 1.0)

- **42** classes (e.g. `AiRmfFramework`, `Function`, `Category`, `Subcategory`, `Risk`, `Impact`, `Harm`, `AiSystem`, `AiActor`, `TrustworthinessCharacteristic`, `PlaybookEntry`)
- **13** enums (e.g. `FunctionEnum`, `AiLifecycleStageEnum`, `AiActorTaskEnum`, `TrustworthinessCharacteristicEnum`, `HarmCategoryEnum`, `BiasCategoryEnum`, `RiskResponseEnum`)
- **42** schema-level slots
- **3** custom types with regex patterns: `FunctionCode`, `CategoryCode`, `SubcategoryCode`
- **8** subsets: `core`, `framework_core`, `trustworthiness`, `lifecycle`, `risk_and_harm`, `profiles`, `attributes`, `appendices`, `playbook`
- Tree-root: `AiRmfFramework` (auxiliary: `PlaybookCollection`)

### `nist_ai_600_1` (GAI Profile, AI 600-1)

- **17** classes including `GaiProfile` (tree-root), `GaiRisk`, `SuggestedAction`, `PrimaryGaiConsideration`, `StructuredPublicFeedback`, `AiRedTeaming`
- **9** enums including the 12-value `GaiRiskCategoryEnum`, `GaiRiskCategorizationEnum`, `GaiRiskScopeEnum`, `GaiRiskSourceEnum`, `GaiRiskTimeScaleEnum`, `PrimaryConsiderationEnum`, `RedTeamingTypeEnum`
- **12** schema-level slots
- **1** custom type: `GaiActionId` (regex `^(GV|MP|MS|MG)-N.M-NNN$`)
- **4** subsets: `gai_core`, `gai_actions`, `gai_considerations`, `gai_feedback`
- Imports `./nist_ai_rmf`

## Cross-vocabulary mappings

SSSOM TSV files in [../mappings/](../mappings/) carry exact/close/broad/narrow/related mappings to:

- NIST CSF v2 (`nist_csf:CSFFunction`, `CSFCategory`, `CSFSubcategory`, `CSFDocument`, `CSFMetadata`)
- OSCAL (`oscal_catalog:Catalog`, `oscal_catalog:Control`, `oscal_profile:Profile`)
- NIST SP 800-53 (`nist_sp_800_53:Catalog`, `Control`, `ProfileDocument`)
- ISO 27001 (`Risk`, `ImpactRating`, `LikelihoodRating`, `RiskLevel`, `RiskTreatmentOption`, `InterestedParty`)
- ISO 29100 (`PrivacyRisk`, `PrivacyPrinciple`)
- STIX (`CourseOfAction`, `AttackPattern`, `Identity`)
- GIST (`Function`, `Task`)
- W3C / Schema.org (`schema:Thing`, `schema:CreativeWork`, `schema:SoftwareApplication`, `prov:Agent`, `foaf:Agent`)

These propagate to `skos:exactMatch` / `closeMatch` / `broadMatch` / `narrowMatch` / `relatedMatch` triples in the generated OWL.

## Validation, generation, and tests

```bash
just lint                 # linkml-lint
just gen-project          # regenerate Python, JSON Schema, OWL, SHACL, ...
just test                 # pytest + linkml-run-examples
just validate-playbook    # validate tests/data/third_party/nist/nist_ai_rmf_playbook.json
just verify-mappings      # confirm *_mappings: in YAML match the SSSOM TSV
just refresh-playbook     # re-fetch the playbook from NIST then validate
```

## Tree roots and how to load data

| Tree root | Schema | Use |
|---|---|---|
| `AiRmfFramework` | `nist_ai_rmf` | Default - bundles Functions, trustworthiness chars, lifecycle, profiles |
| `PlaybookCollection` | `nist_ai_rmf` | Loads NIST AI RMF Playbook JSON (`--target-class PlaybookCollection`) |
| `GaiProfile` | `nist_ai_600_1` | NIST AI 600-1 GAI Profile (`--target-class GaiProfile`) |
