# nist-ai-rmf

This project holds NIST AI 100-1, the AI Risk Management Framework 1.0, and NIST AI 600-1, its Generative AI Profile, under one LinkML schema. lmodel/nist-ai-100-1 and lmodel/nist-ai-600-1 model the two publications.

- [Schema documentation](elements/index.md), generated from the schema
- [About](about.md): why it exists, what it adds and what it leaves out
- [`nist_ai_rmf.yaml`](schema/nist_ai_rmf.yaml): the schema, with its modules merged

## Validating a document

A file holding one publication names that publication's root:

```bash
uv run linkml-validate -s src/nist_ai_rmf/schema/nist_ai_rmf.yaml -C AiRmfFramework tests/upstream/ai-rmf-1.0.yaml
uv run linkml-validate -s src/nist_ai_rmf/schema/nist_ai_rmf.yaml -C GaiProfile tests/upstream/ai-600-1.yaml
```

`project/jsonschema/nist_ai_rmf.schema.json` is the same schema for anyone without LinkML. Its top level is `NistAiRmfFamily`, which holds the two under `nist_ai_rmf_framework` and `nist_ai_rmf_generative_ai_profile`.
