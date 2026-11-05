<a href="https://github.com/linkml/linkml-project-copier"><img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/copier-org/copier/master/img/badge/badge-grayscale-inverted-border-teal.json" alt="Copier Badge" style="max-width:100%;"/></a>

# nist-ai-rmf

NIST AI RMF family: NIST AI 100-1 and NIST AI 600-1 as one schema (LinkML)

> **Only want to ask?** Install `ktl-docent` into any agent you use, by a route from [the install page](https://w3id.org/ktl/docs/install/), and ask it about this project. It answers from the bundle and says how far each answer has been checked.
>
> **Agents:** if `.lokf/knowledge/index.md` exists, read it first. `llms.txt` says how to weigh it.

## Documentation Website

[https://lmodel.github.io/nist-ai-rmf](https://lmodel.github.io/nist-ai-rmf)

## What it models

Nothing of its own. The schema holds [NIST AI 100-1](https://doi.org/10.6028/NIST.AI.100-1), the AI Risk Management Framework 1.0, and [NIST AI 600-1](https://doi.org/10.6028/NIST.AI.600-1), its Generative AI Profile, as [lmodel/nist-ai-100-1](https://github.com/lmodel/nist-ai-100-1) and [lmodel/nist-ai-600-1](https://github.com/lmodel/nist-ai-600-1) model them. It adds `NistAiRmfFamily`, which holds both in one document.

Use it when a knowledge bundle needs both. The two repositories' adapt copies validate side by side, but `lokf convert` stops on the elements they share, so this repository's copy is the one way to carry both.

## Crosswalk to ISO/IEC 42001

`just build-crosswalk` writes `tmp/mappings/nist-ai-rmf-to-iso42001.sssom.tsv`, 280 pairs of an AI RMF subcategory and an ISO/IEC 42001 clause or Annex A control. The script reads them from the crosswalk [NIST's AI Resource Center lists](https://airc.nist.gov/airmf-resources/crosswalks/), which Microsoft provided. That document states no licence, so the repository carries neither it nor its pairs. A record of the AI RMF has no IRI of its own, so a row names a subcategory as `nist_ai_100_1:Subcategory#GOVERN_1.1`.

## Mappings

The schema holds the two repositories' mappings unchanged, and `tests/test_schema_rules.py` checks each one against a released copy. This repository's own SSSOM set, whose rows came from a matching tool, is gone.

## Repository Structure

* [docs/](docs/): the website's own pages
* [project/](project/): generated project files (do not edit them)
* [scripts/](scripts/): the crosswalk's builder and the upstream watch
* [src/nist_ai_rmf/schema/](src/nist_ai_rmf/schema): the umbrella `nist_ai_rmf.yaml` (edit this) and the vendored modules (do not edit them)
* [src/nist_ai_rmf/datamodel/](src/nist_ai_rmf/datamodel): the generated Python datamodel
* [tests/](tests/): Python tests, with example data in [data/](tests/data), the two catalogues in [upstream/](tests/upstream) and the neighbours' adapt copies in [neighbours/](tests/neighbours)
* [website/](website/): the Astro Starlight site built from the README, `docs/`, the schema's pages and the knowledge bundle

## Developer Tools

Run `just` to list the project's [just](https://github.com/casey/just/) recipes.

## Knowledge Trust Ladder (KTL)

`.lokf/` holds this project's [KTL](https://w3id.org/ktl/) knowledge bundle. Its domain schema, `.lokf/nist-ai-rmf.yaml`, is the copy `just lokf-adapt` writes from `src/nist_ai_rmf/schema/nist_ai_rmf.yaml`, and `just lokf-adapt-check` says when it is stale. Edit the source, never the copy. A release carries the copy as `schema-<tag>-nist-ai-rmf.yaml`, on the terms [CONTRIBUTING.md](CONTRIBUTING.md#releasing-maintainers) gives.

The copy roots on `Concept` what the two repositories root. In Obsidian, add these to the *Known LOKF types* setting of the KTL Registrar and KTL Curator plugins:

```text
AiRmfFunction, AiRmfCategory, AiRmfSubcategory, AiRmfTrustworthinessCharacteristic, AiRmfDimension, AiRmfLifecycleStage, AiRmfActorTask, AiRmfManagementChallenge, AiRmfMeasurementChallenge, AiRmfSpecificRisk, AiRmfHumanAiIssue, AiRmfAttribute, AiRmfSystem, AiRmfActor, AiRmfRisk, AiRmfResidualRisk, AiRmfImpact, AiRmfHarm, AiRmfRiskTolerance, AiRmfBias, AiRmfProfile, GaiRisk, GaiSubcategory, GaiGovernanceConsideration, GaiPreDeploymentTestingConsideration, GaiContentProvenanceConsideration, GaiIncidentDisclosureConsideration, GaiParticipatoryEngagement, GaiFieldTesting, GaiAiRedTeaming, GaiProfile
```

Import this copy in place of the two repositories' copies, never beside them. In this copy a class attribute projects under `nist_ai_rmf:` rather than its publication's prefix, which [lokf issue 168](https://github.com/nicholsn/lokf/issues/168) reports; a top-level slot and the committed JSON-LD context keep each publication's IRI. `tests/test_schema_rules.py` holds all this.

## License

The schema and the code are under the Apache License 2.0 ([LICENSE](LICENSE)), and the knowledge bundle in [.lokf/knowledge/](.lokf/knowledge) is under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/).

NIST's works are free to reprint under its statement: see [NOTICE](NOTICE), which gives the citations and the crosswalk's position. This is not a NIST project, and its use implies no endorsement by NIST.

## Contributing and security

[CONTRIBUTING.md](CONTRIBUTING.md) is the checklist for pull requests and
releases, [AI_COVENANT.md](AI_COVENANT.md) sets the rules for AI-assisted work,
[SECURITY.md](SECURITY.md) says how to report a vulnerability, and
[CHANGELOG.md](CHANGELOG.md) records the changes.

## Credits

Built from the [linkml-project-copier](https://github.com/linkml/linkml-project-copier) template ([doi:10.5281/zenodo.15163584](https://doi.org/10.5281/zenodo.15163584)).
