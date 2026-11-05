## Add your own just recipes here. This is imported by the main justfile.

# Overriding recipes from the root justfile by adding a recipe with the same
# name in this file is not possible until a known issue in just is fixed,
# https://github.com/casey/just/issues/2540

# ============ The crosswalk ============

# Write the AI RMF to ISO/IEC 42001 crosswalk under tmp/mappings/ from its provider's PDF
[group('model development')]
build-crosswalk:
  uv run python scripts/build_crosswalk.py
