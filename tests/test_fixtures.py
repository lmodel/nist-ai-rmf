"""Validate every generated fixture against the umbrella schema.

The fixture filename stem encodes the target class:
``<TargetClassName>-<slug>.yaml``.  We recover ``TargetClassName`` from
the prefix and feed it as ``--target-class`` to the LinkML JSON-Schema
validator.

* Files under ``tests/data/third-party/microsoft-agt/valid/``  -> must validate without errors.
* Files under ``tests/data/third-party/microsoft-agt/invalid/`` -> must produce at least one error.
"""
from __future__ import annotations

from pathlib import Path

import pytest
import yaml
from linkml.validator import Validator
from linkml.validator.plugins import JsonschemaValidationPlugin

REPO_ROOT = Path(__file__).resolve().parent.parent
SCHEMA = REPO_ROOT / "src" / "nist_ai_rmf" / "schema" / "nist_ai_rmf.yaml"
THIRD_PARTY_DIR = REPO_ROOT / "tests" / "data" / "third-party" / "microsoft-agt"
VALID_DIR = THIRD_PARTY_DIR / "valid"
INVALID_DIR = THIRD_PARTY_DIR / "invalid"


def _target_class(path: Path) -> str:
    """``AiRmfProfile-aegis-foo.yaml`` -> ``AiRmfProfile``."""
    return path.stem.split("-", 1)[0]


@pytest.fixture(scope="module")
def validator() -> Validator:
    return Validator(
        schema=str(SCHEMA),
        validation_plugins=[JsonschemaValidationPlugin(closed=True)],
    )


def _valid_files() -> list[Path]:
    return sorted(VALID_DIR.glob("*.yaml"))


def _invalid_files() -> list[Path]:
    return sorted(INVALID_DIR.glob("*.yaml"))


@pytest.mark.parametrize(
    "path",
    _valid_files() or [pytest.param(None, marks=pytest.mark.skip(reason="no fixtures yet"))],
    ids=lambda p: p.name if p else "none",
)
def test_valid_fixture(validator: Validator, path: Path) -> None:
    """Every fixture under ``valid/`` validates against its target class."""
    target = _target_class(path)
    with path.open() as fh:
        instance = yaml.safe_load(fh)
    report = validator.validate(instance, target_class=target)
    assert not report.results, (
        f"{path.name} ({target}) produced unexpected validation errors:\n"
        + "\n".join(f"  - {r.message}" for r in report.results)
    )


@pytest.mark.parametrize(
    "path",
    _invalid_files() or [pytest.param(None, marks=pytest.mark.skip(reason="no fixtures yet"))],
    ids=lambda p: p.name if p else "none",
)
def test_invalid_fixture(validator: Validator, path: Path) -> None:
    """Every fixture under ``invalid/`` produces at least one error."""
    target = _target_class(path)
    with path.open() as fh:
        instance = yaml.safe_load(fh)
    report = validator.validate(instance, target_class=target)
    assert report.results, (
        f"{path.name} ({target}) was expected to fail validation but did not."
    )
