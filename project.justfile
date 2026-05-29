## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============================================================================
# nist-ai-rmf is an *umbrella* schema.
#
# The only file shipped under ``src/nist_ai_rmf/schema/`` is
# ``nist_ai_rmf.yaml``. It imports the ``nist_ai_100_1`` (AI RMF 1.0)
# and ``nist_ai_600_1`` (GAI Profile) schemas remotely from their
# own ``lmodel`` repositories - they are NOT bundled here. Anything
# specific to those sub-schemas (per-element examples, SSSOM mapping
# tables, Playbook validation, dedicated Pydantic generation, ...)
# lives in the upstream repository and is tested there.
#
# Consequently this project.justfile is intentionally minimal: the
# root justfile already covers generation, linting, and testing of
# the single umbrella schema. The stub recipes below exist only so
# the post-dependency hooks declared in the root justfile resolve
# cleanly.
# ============================================================================

# Root justfile declares ``gen-project: && gen-extra-schemas`` - we have
# no extra schemas to generate, so this is a no-op for nist-ai-rmf.
[group('model development')]
gen-extra-schemas:

# Root justfile declares ``_test-examples: ... && _test-examples-extra`` -
# nist-ai-rmf has no extra example sets to run.
_test-examples-extra:
