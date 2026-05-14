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
