# Mappings

This directory is intentionally **empty of mapping files**.

`nist-ai-rmf` is an umbrella schema that imports `nist_ai_100_1`
(AI RMF 1.0) and `nist_ai_600_1` (GAI Profile) from their own
repositories. The SSSOM TSV mapping sets and the `*_mappings:`
fields on each schema element are maintained alongside those
sub-schemas, **not here**:

| Sub-schema | Mappings location |
|---|---|
| `nist_ai_100_1` | [`lmodel/nist-ai-100-1` &rarr; `src/nist_ai_100_1/mappings/`](https://github.com/lmodel/nist-ai-100-1/tree/main/src/nist_ai_100_1/mappings) |
| `nist_ai_600_1` | [`lmodel/nist-ai-600-1` &rarr; `src/nist_ai_600_1/mappings/`](https://github.com/lmodel/nist-ai-600-1/tree/main/src/nist_ai_600_1/mappings) |

Each upstream repository:

* ships the canonical `*.sssom.tsv` files for its schema,
* keeps the `exact_mappings` / `close_mappings` / `broad_mappings`
  / `narrow_mappings` / `related_mappings` fields on each element
  in sync with those TSV rows, and
* enforces that sync in CI via its own `just verify-mappings`
  recipe.

Because the umbrella merely imports those schemas, the mappings
flow through automatically into the merged artefacts generated
under `project/` - there is nothing to curate or verify in this
repository.
