# Mappings

SSSOM TSV mapping sets for the `nist_ai_rmf` and `nist_ai_rmf_gai`
schemas. The Simple Standard for Sharing Ontological Mappings
([SSSOM](https://mapping-commons.github.io/sssom/)) is the canonical format; the `*_mappings:` fields inside the LinkML schemas are kept in sync from the SSSOM TSV via `scripts/apply_mappings.py`.

## Files

| File | Subject schema | Mapping targets |
|---|---|---|
| `nist_ai_rmf.sssom.tsv` | `nist_ai_rmf` (AI RMF 1.0) | NIST CSF v2, NIST SP 800-53, OSCAL catalog/profile, ISO 27001/29100, GIST, schema.org, PROV, FOAF, DCTERMS |
| `nist_ai_rmf_gai.sssom.tsv` | `nist_ai_rmf_gai` (GAI Profile) | OSCAL profile, NIST CSF v2, ISO 27001/29100, STIX, SLSA, SPDX, GIST |

## Predicates

Each SSSOM row uses a SKOS predicate, which the apply script converts to a LinkML `*_mappings:` key on the corresponding element:

| `predicate_id` (SSSOM) | LinkML field |
|---|---|
| `skos:exactMatch` | `exact_mappings` |
| `skos:closeMatch` | `close_mappings` |
| `skos:broadMatch` | `broad_mappings` |
| `skos:narrowMatch` | `narrow_mappings` |
| `skos:relatedMatch` | `related_mappings` |

`subject_id` is the schema element CURIE (`nist_ai_rmf:Risk`); `object_id` is the external term being mapped to.

## Refreshing

Edit the TSV file (or generate / curate new rows), then run:

```bash
just apply-mappings    # rewrites *_mappings: fields in the YAML schemas
just verify-mappings   # round-trip check that the schema reflects the TSV
just lint              # confirm the schemas still lint clean
```
