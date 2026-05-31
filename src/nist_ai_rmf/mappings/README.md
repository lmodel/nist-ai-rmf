# Mappings

This directory holds **umbrella-level SSSOM mappings** that are
specific to the `nist-ai-rmf` schema (i.e. mappings whose subject is
the merged AI 100-1 + 600-1 namespace, or RMF function/category/
subcategory identifiers cross-referenced against frameworks the
sub-schemas do not curate themselves).

| File | Purpose |
|---|---|
| [`nist_ai_rmf.sssom.tsv`](nist_ai_rmf.sssom.tsv) | Cross-framework mappings (RMF subcategory &harr; EU AI Act / SOC 2 / OWASP ASI / OWASP LLM / AGT ATF), seeded from the Microsoft AGT compliance docs vendored under `upstream-releases/agent-governance-toolkit/docs/compliance/`. |

The element-level `*_mappings:` slot bindings on each schema class /
slot / enum continue to live in the upstream sub-schemas:

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

Because the umbrella merely imports those schemas, the per-element
mappings flow through automatically into the merged artefacts
generated under `project/`. The only mapping curation in *this*
repository is the cross-framework SSSOM TSV listed above.
