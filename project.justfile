## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ The crosswalk ============

# Write the AI RMF to ISO/IEC 42001 crosswalk under tmp/mappings/ from its provider's PDF
[group('model development')]
build-crosswalk:
  uv run python scripts/build_crosswalk.py

# ============ Knowledge bundle: the adapted domain schema ============

# `.lokf/nist-ai-rmf.yaml` is the copy `lokf adapt` writes from the schema so that it
# can sit beside `.lokf/lokf.yaml` (`lokf adapt --help` lists the moves). The roots are
# the classes a knowledge concept may use as its `type`: those lmodel/nist-ai-100-1 and
# lmodel/nist-ai-600-1 each root. The recipes run the `lokf` the sidecar's floor pins
# (0.9.0 or later); LOKF_CMD runs another, such as a checkout:
# LOKF_CMD="uv run --project ../lokf lokf" just lokf-adapt
lokf_cmd := env_var_or_default("LOKF_CMD", "uv run --project .lokf lokf")
lokf_adapt_roots := "--root AiRmfFunction --root AiRmfCategory --root AiRmfSubcategory --root AiRmfTrustworthinessCharacteristic --root AiRmfDimension --root AiRmfLifecycleStage --root AiRmfActorTask --root AiRmfManagementChallenge --root AiRmfMeasurementChallenge --root AiRmfSpecificRisk --root AiRmfHumanAiIssue --root AiRmfAttribute --root AiRmfRecord --root GaiRisk --root GaiSubcategory --root GaiPrimaryConsideration --root GaiStructuredFeedback"

# Rewrite .lokf/nist-ai-rmf.yaml from the schema (run after every schema change)
[group('knowledge bundle')]
lokf-adapt:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/nist-ai-rmf.yaml

# Fail when .lokf/nist-ai-rmf.yaml is stale against the schema or .lokf/lokf.yaml
[group('knowledge bundle')]
lokf-adapt-check:
  {{lokf_cmd}} adapt {{source_schema_path}} {{lokf_adapt_roots}} --lokf .lokf/lokf.yaml -o .lokf/nist-ai-rmf.yaml --check
