# Schema Directory

Merged LinkML schema for the NIST AI Risk Management Framework family.

## Files

| File | Role |
|---|---|
| [nist_ai_rmf.yaml](nist_ai_rmf.yaml) | Merged schema. Defines no elements of its own - imports `nist_ai_100_1` (AI RMF 1.0) and `nist_ai_600_1` (GAI Profile) from their own `lmodel` repositories and re-exports them under the `nist_ai_rmf` default prefix. |

The sub-schemas are resolved over the network via the
`schema_100_1:` and `schema_600_1:` prefixes declared at the top
of `nist_ai_rmf.yaml`; they are **not** vendored here. See
[../mappings/README.md](../mappings/README.md) for where SSSOM
mappings live, and [../../../docs/about.md](../../../docs/about.md)
for the overall design.

## Tree roots

Both tree-root classes are contributed by the imports - the umbrella
itself defines none. Pass `--target-class` when validating:

| Tree root | Origin schema | Use |
|---|---|---|
| `AiRmfFramework` | `nist_ai_100_1` | Default - bundles Functions, trustworthiness characteristics, lifecycle, profiles |
| `PlaybookCollection` | `nist_ai_100_1` | Loads NIST AI RMF Playbook JSON |
| `GaiProfile` | `nist_ai_600_1` | NIST AI 600-1 GAI Profile |

## Running

```bash
just lint           # linkml-lint on the umbrella (imports resolved remotely)
just gen-project    # regenerate merged Python, JSON Schema, OWL, SHACL, ...
just test           # pytest - umbrella-only unit tests
```

Per-element examples, the SSSOM verifier, and the Playbook
validator are owned by the upstream repositories and run in
their CI.
