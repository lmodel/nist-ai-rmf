"""Fixtures the test modules share."""

from pathlib import Path

import pytest
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

SCHEMA = (
    Path(__file__).parent.parent / "src" / "nist_ai_rmf" / "schema" / "nist_ai_rmf.yaml"
)


@pytest.fixture(scope="session")
def validator():
    """The validator linkml.validator.validate() builds, closed to undeclared keys, built
    once. LinkML caches the JSON Schema it generates for each loaded schema, and validate()
    loads the schema again on every call, so each call generated the JSON Schema again."""
    return Validator(
        str(SCHEMA), validation_plugins=[JsonschemaValidationPlugin(closed=True)]
    )
