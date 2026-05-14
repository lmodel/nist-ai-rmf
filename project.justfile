## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============================================================================
# Third-party data fixtures
#
# NIST refreshes the AI RMF Playbook ~twice a year. The JSON is held under
# `tests/data/third_party/nist/` and validated via the recipes below.
#
# - `just validate-playbook`  - validate the current local copy
# - `just refresh-playbook`   - re-fetch from upstream and re-validate
# - `just dump-playbook`      - write the transformed payload to disk
# ============================================================================

# Local path to the third-party NIST AI RMF Playbook JSON
playbook_path := "tests/data/third_party/nist/nist_ai_rmf_playbook.json"

# Upstream URL for the playbook (kept here so refreshes are reproducible)
playbook_url := "https://airc.nist.gov/AI_RMF_Knowledge_Base/Playbook/data.json"

# Validate the NIST AI RMF Playbook JSON against the schema
[group('model development')]
validate-playbook:
  uv run python scripts/validate_playbook.py {{playbook_path}}

# Re-fetch the Playbook JSON from NIST and validate it
[group('third-party data')]
refresh-playbook:
  @mkdir -p $(dirname {{playbook_path}})
  curl -fsSL {{playbook_url}} -o {{playbook_path}}
  @echo "Fetched playbook to {{playbook_path}}"
  @just validate-playbook

# Dump the transformed (renamed + wrapped) payload for inspection
[group('third-party data')]
dump-playbook output="tmp/playbook-transformed.json":
  @mkdir -p $(dirname {{output}})
  uv run python scripts/validate_playbook.py \
      --keep-transformed {{output}} {{playbook_path}}
  @echo "Wrote transformed playbook to {{output}}"

# ============================================================================
# Cross-vocabulary mappings (SSSOM)
#
# Mappings between schema elements and external vocabularies live in
# `src/nist_ai_rmf/mappings/*.sssom.tsv`. The verifier confirms each
# schema's `*_mappings:` fields are in sync with the TSV.
# ============================================================================

# Verify that *_mappings: fields in the schemas match the SSSOM TSV
[group('model development')]
verify-mappings:
  uv run python scripts/apply_mappings.py

# Strict variant - also fail if the schema has mappings that the TSV omits
[group('model development')]
verify-mappings-strict:
  uv run python scripts/apply_mappings.py --strict

# ============================================================================
# Extra schemas (GAI Profile)
#
# The root `gen-project` recipe targets the base schema via
# `{{source_schema_path}}`. The GAI Profile is a sibling schema that
# imports the base, so its artifacts need a dedicated generation step.
# `gen-project` declares `gen-extra-schemas` as a post-dependency so
# any `just setup` / `just gen-project` run produces *both* datamodels.
# ============================================================================

gai_schema_path := "src/nist_ai_rmf/schema/nist_ai_rmf_gai.yaml"
gai_module_path := "src/nist_ai_rmf/datamodel/nist_ai_rmf_gai.py"
core_schema_path := "src/nist_ai_rmf/schema/nist_ai_rmf_core.yaml"
core_module_path := "src/nist_ai_rmf/datamodel/nist_ai_rmf_core.py"

# Generate every additional schema's artifacts (GAI Profile)
[group('model development')]
gen-extra-schemas: gen-core-python gen-gai-python gen-gai-jsonschema gen-gai-owl

# Regenerate the core schema Python dataclasses (required by nist_ai_rmf_gai.py)
[group('model development')]
gen-core-python:
  @mkdir -p $(dirname {{core_module_path}})
  uv run gen-python --no-mergeimports {{core_schema_path}} > {{core_module_path}}

# Regenerate the GAI Profile Python dataclasses
[group('model development')]
gen-gai-python: gen-core-python
  @mkdir -p $(dirname {{gai_module_path}})
  uv run gen-python --no-mergeimports {{gai_schema_path}} > {{gai_module_path}}

# Regenerate the GAI Profile JSON Schema
[group('model development')]
gen-gai-jsonschema:
  @mkdir -p project/jsonschema
  uv run gen-json-schema {{gai_schema_path}} > project/jsonschema/nist_ai_rmf_gai.schema.json

# Regenerate the GAI Profile OWL turtle
[group('model development')]
gen-gai-owl:
  @mkdir -p project/owl
  uv run gen-owl {{gai_schema_path}} > project/owl/nist_ai_rmf_gai.owl.ttl

# Regenerate Python dataclasses for both schemas (base + GAI)
[group('model development')]
gen-python-all: gen-python gen-core-python gen-gai-python

# Run linkml-run-examples for GAI fixtures (live under tests/data/{valid,invalid}/gai)
# Wired in as a post-dep of `_test-examples` so `just test` covers both schemas.
# Also validates the third-party NIST Playbook JSON.
_test-examples-extra: validate-playbook
  @mkdir -p examples/output/gai
  uv run linkml-run-examples \
      --input-formats json \
      --input-formats yaml \
      --output-formats json \
      --output-formats yaml \
      --counter-example-input-directory tests/data/invalid/gai \
      --input-directory tests/data/valid/gai \
      --output-directory examples/output/gai \
      --schema {{gai_schema_path}} > examples/output/gai/README.md
