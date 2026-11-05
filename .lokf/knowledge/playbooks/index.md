# Playbooks

* [Regenerate and test](regenerate-and-test.md) - How to change the umbrella: edit `nist_ai_rmf.yaml`, run `just lint`, `just gen-project`, `just gen-doc`, `just lokf-adapt` and `just test`, and commit what they write. Generated and vendored files are never edited by hand.
* [Re-vendor the modules](re-vendor-the-modules.md) - What to do when lmodel/nist-ai-100-1 or lmodel/nist-ai-600-1 releases: copy its modules, catalogue and schema asset from the tag, move the pins in the watch and the tests, regenerate and test.
* [Build the crosswalk](build-the-crosswalk.md) - How to write the AI RMF to ISO/IEC 42001 crosswalk as SSSOM: run `just build-crosswalk`, which downloads the pinned PDF and writes `tmp/mappings/nist-ai-rmf-to-iso42001.sssom.tsv`. Never commit the result.
* [Release](release.md) - How a release happens: `semantic-release.yml` reads Conventional Commits on `main`, promotes the `## [Unreleased]` section, tags and publishes. The first release needs the `v0.0.0` baseline tag on `main`, and PyPI publishing stays off.
* [Knowledge sources map](knowledge-sources.md) - The librarian's scrape map: every repository location and external source this bundle derives concepts from, how to re-check each, and the tracked paths left out with their reasons.
