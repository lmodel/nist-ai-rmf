"""Checks that the two publications hold together under one schema.

tests/upstream/ holds each repository's whole catalogue as of its release.
"""

import json
from functools import lru_cache
from pathlib import Path

import jsonschema
import pytest
import yaml
from linkml.generators.jsonschemagen import JsonSchemaGenerator
from linkml.validator import validate
from linkml_runtime.loaders import yaml_loader
from linkml_runtime.utils.schemaview import SchemaView

from nist_ai_rmf.datamodel import nist_ai_rmf as dataclasses
from nist_ai_rmf.datamodel import nist_ai_rmf_pydantic as pydantic_models

ROOT = Path(__file__).parent.parent
UPSTREAM = ROOT / "tests" / "upstream"
SCHEMA_DIR = ROOT / "src" / "nist_ai_rmf" / "schema"
SCHEMA = SCHEMA_DIR / "nist_ai_rmf.yaml"
JSON_SCHEMA = ROOT / "project" / "jsonschema" / "nist_ai_rmf.schema.json"
CONTEXT = ROOT / "project" / "jsonld" / "nist_ai_rmf.context.jsonld"

# Each publication's root schema, and the keys its repository holds it under.
PUBLICATIONS = {
    "nist_ai_rmf_framework": (
        "AiRmfFramework",
        UPSTREAM / "ai-rmf-1.0.yaml",
        SCHEMA_DIR / "nist_ai_100_1" / "nist_ai_100_1.yaml",
    ),
    "nist_ai_rmf_generative_ai_profile": (
        "GaiProfile",
        UPSTREAM / "ai-600-1.yaml",
        SCHEMA_DIR / "nist_ai_600_1.yaml",
    ),
}


@lru_cache(maxsize=1)
def _family():
    return {
        key: yaml.safe_load(path.read_text(encoding="utf-8"))
        for key, (_root, path, _schema) in PUBLICATIONS.items()
    }


def test_the_family_passes_the_committed_json_schema():
    """Both catalogues, in one document, pass the JSON Schema a reader without LinkML uses."""
    schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
    jsonschema.Draft201909Validator(schema).validate(_family())


def test_the_committed_json_schema_refuses_another_key():
    """The top level is the family class, closed, so a stray key fails."""
    schema = json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))
    with pytest.raises(jsonschema.ValidationError):
        jsonschema.Draft201909Validator(schema).validate({"ai_rmf_version": "1.0"})


def test_the_committed_json_schema_is_current():
    """The committed JSON Schema is what the schema generates today, under the settings
    .linkml/generators.yaml names, so an edit to one cannot leave the other behind."""
    generated = JsonSchemaGenerator(
        str(SCHEMA),
        mergeimports=True,
        top_class="NistAiRmfFamily",
        include_range_class_descendants=True,
    ).serialize()
    assert json.loads(generated) == json.loads(JSON_SCHEMA.read_text(encoding="utf-8"))


@pytest.mark.parametrize("key", PUBLICATIONS)
def test_each_catalogue_alone_validates(key):
    """A file that holds one publication validates against that publication's root."""
    root, path, _schema = PUBLICATIONS[key]
    report = validate(
        yaml.safe_load(path.read_text(encoding="utf-8")), str(SCHEMA), root
    )
    assert not report.results, [r.message for r in report.results][:5]


def test_the_family_loads_into_the_generated_models():
    """The dataclasses and the Pydantic models take the family whole."""
    family = yaml_loader.loads(
        yaml.safe_dump(_family()), target_class=dataclasses.NistAiRmfFamily
    )
    assert family.nist_ai_rmf_framework.ai_rmf_version == "1.0"
    assert pydantic_models.NistAiRmfFamily(**_family()).nist_ai_rmf_framework


def test_a_profile_names_only_subcategories_of_the_framework():
    """Every subcategory the Profile's tables name is one the framework holds."""
    family = _family()
    framework = {
        subcategory["ai_rmf_subcategory_id"]
        for function in family["nist_ai_rmf_framework"]["ai_rmf_functions"]
        for category in function["ai_rmf_function_categories"]
        for subcategory in category["ai_rmf_category_subcategories"]
    }
    tables = {
        table["ai_rmf_subcategory_id"]
        for table in family["nist_ai_rmf_generative_ai_profile"]["gai_subcategories"]
    }
    assert len(framework) == 72
    assert tables and tables <= framework, sorted(tables - framework)


@pytest.mark.parametrize("key", PUBLICATIONS)
def test_each_element_keeps_its_publications_iri(key):
    """Merging moves no IRI: each class and slot of a publication has the IRI its own schema
    gives it, in the schema and in the committed JSON-LD context."""
    _root, _path, schema = PUBLICATIONS[key]
    own = SchemaView(str(schema))
    merged = SchemaView(str(SCHEMA))
    context = json.loads(CONTEXT.read_text(encoding="utf-8"))["@context"]

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return (
            context[prefix] + local if isinstance(context.get(prefix), str) else curie
        )

    for name in own.all_classes():
        assert merged.get_uri(name, expand=True) == own.get_uri(name, expand=True), name
    for name, slot in own.all_slots().items():
        iri = own.get_uri(slot, expand=True)
        assert merged.get_uri(merged.get_slot(name), expand=True) == iri, name
        entry = context.get(name)
        if entry is not None:
            term = entry["@id"] if isinstance(entry, dict) else entry
            # An identifier is the record's @id, so it has no IRI of its own to compare.
            assert term == "@id" or expand(term) == iri, name


def test_the_family_class_is_the_only_element_this_schema_adds():
    """The umbrella declares one class and nothing else."""
    own = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    assert list(own["classes"]) == ["NistAiRmfFamily"]
    assert not {"slots", "enums", "types", "subsets"} & own.keys()
