# Test data for nist_ai_rmf

`nist-ai-rmf` is an umbrella schema. Per-element example fixtures
for `nist_ai_100_1` (AI RMF 1.0) and `nist_ai_600_1` (GAI Profile)
live in their own repositories and are exercised by their own
CI - they are deliberately **not** mirrored here.

This directory is reserved for unit-test fixtures that:

1. do not exist in
   [`lmodel/nist-ai-100-1` &rarr; `tests/data/`](https://github.com/lmodel/nist-ai-100-1/tree/main/tests/data),
2. do not exist in
   [`lmodel/nist-ai-600-1` &rarr; `tests/data/`](https://github.com/lmodel/nist-ai-600-1/tree/main/tests/data), and
3. can **only** be exercised against the merged umbrella schema
   (e.g. data that crosses the `nist_ai_100_1` / `nist_ai_600_1`
   namespace boundary, or that relies on the umbrella's re-exports
   under the `nist_ai_rmf:` default prefix).

There are no such fixtures today; the umbrella's structural
properties are covered by `tests/test_data.py` using
`linkml-runtime`'s `SchemaView` against `nist_ai_rmf.yaml`.

Sub-folders follow the standard layout if/when fixtures are added:

- `valid/` - data conforming to the merged schema.
- `invalid/` - data that the merged schema must reject.
- `problem/` - merged-schema scenarios not yet handled (`valid/`
  and `invalid/` sub-folders inside).

Filenames must follow the `ClassName-###.yaml` scheme so the test
runner can pick the right `--target-class`.
