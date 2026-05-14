"""Data tests for the NIST AI RMF schemas.

The fixtures follow the lmodel convention `tests/data/<valid|invalid>/<ClassName>-<desc>.yaml`.
The class-name prefix is used both to look up the Python dataclass for
in-process loading *and* to choose which schema (`nist_ai_rmf` or
`nist_ai_rmf_gai`) to use as the `--target-class` for `linkml-validate`.

Additionally, the NIST AI RMF Playbook JSON (third-party data) is
exercised end-to-end via ``scripts/validate_playbook.py``.
"""
from __future__ import annotations

import glob
import importlib
import os
import shutil
import subprocess
import sys
from pathlib import Path

import pytest

REPO_ROOT = Path(__file__).resolve().parent.parent

DATA_DIR_VALID = REPO_ROOT / "tests" / "data" / "valid"
DATA_DIR_INVALID = REPO_ROOT / "tests" / "data" / "invalid"
DATA_DIR_THIRD_PARTY = REPO_ROOT / "tests" / "data" / "third_party"

SCHEMA_BASE = REPO_ROOT / "src" / "nist_ai_rmf" / "schema" / "nist_ai_rmf.yaml"
SCHEMA_GAI = REPO_ROOT / "src" / "nist_ai_rmf" / "schema" / "nist_ai_rmf_gai.yaml"

VALID_EXAMPLE_FILES = sorted(
    f for f in glob.glob(str(DATA_DIR_VALID / "*")) if f.endswith((".yaml", ".yml", ".json"))
)
INVALID_EXAMPLE_FILES = sorted(
    f for f in glob.glob(str(DATA_DIR_INVALID / "*")) if f.endswith((".yaml", ".yml", ".json"))
)

PLAYBOOK_JSON = DATA_DIR_THIRD_PARTY / "nist" / "nist_ai_rmf_playbook.json"
PLAYBOOK_SCRIPT = REPO_ROOT / "scripts" / "validate_playbook.py"


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #
def _target_class_from_path(filepath: str) -> str:
    """Filename ``ClassName-foo.yaml`` -> ``"ClassName"``."""
    return Path(filepath).stem.split("-")[0]


def _resolve_schema_and_module(class_name: str) -> tuple[Path, str]:
    """Pick the schema + Python module for a fixture's target class.

    Returns ``(schema_yaml_path, python_module_name)``.

    GAI-Profile classes live in the ``nist_ai_rmf_gai`` module/schema;
    everything else lives in the base ``nist_ai_rmf`` schema. Reads the
    generated dataclass module to make the decision so the test doesn't
    drift if new classes are added.
    """
    base_mod = importlib.import_module("nist_ai_rmf.datamodel.nist_ai_rmf")
    gai_mod = importlib.import_module("nist_ai_rmf.datamodel.nist_ai_rmf_gai")
    if hasattr(gai_mod, class_name) and not hasattr(base_mod, class_name):
        return SCHEMA_GAI, "nist_ai_rmf.datamodel.nist_ai_rmf_gai"
    if hasattr(gai_mod, class_name) and hasattr(base_mod, class_name):
        # Class exists in both modules - prefer the GAI schema since it
        # imports the base and is therefore a superset.
        return SCHEMA_GAI, "nist_ai_rmf.datamodel.nist_ai_rmf_gai"
    return SCHEMA_BASE, "nist_ai_rmf.datamodel.nist_ai_rmf"


def _linkml_validate(schema: Path, target_class: str, data_file: Path) -> subprocess.CompletedProcess:
    cmd = [
        "linkml-validate",
        "--schema",
        str(schema),
        "--target-class",
        target_class,
        str(data_file),
    ]
    return subprocess.run(cmd, capture_output=True, text=True, check=False)


def _have_linkml_validate() -> bool:
    return shutil.which("linkml-validate") is not None


# --------------------------------------------------------------------------- #
# Valid fixtures - load with the runtime Python dataclasses
# --------------------------------------------------------------------------- #
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_loads_via_python(filepath: str) -> None:
    """Each valid YAML / JSON fixture loads as its target dataclass."""
    from linkml_runtime.loaders import json_loader, yaml_loader

    class_name = _target_class_from_path(filepath)
    _, module_name = _resolve_schema_and_module(class_name)
    module = importlib.import_module(module_name)
    target_class = getattr(module, class_name)

    loader = json_loader if filepath.endswith(".json") else yaml_loader
    obj = loader.load(filepath, target_class=target_class)
    assert obj is not None


# --------------------------------------------------------------------------- #
# Valid fixtures - cross-check with linkml-validate
# --------------------------------------------------------------------------- #
@pytest.mark.skipif(not _have_linkml_validate(), reason="linkml-validate not installed")
@pytest.mark.parametrize("filepath", VALID_EXAMPLE_FILES)
def test_valid_data_linkml_validate(filepath: str) -> None:
    """linkml-validate accepts each valid fixture."""
    class_name = _target_class_from_path(filepath)
    schema, _ = _resolve_schema_and_module(class_name)
    result = _linkml_validate(schema, class_name, Path(filepath))
    assert result.returncode == 0, (
        f"Expected validation to succeed.\nstdout: {result.stdout}\nstderr: {result.stderr}"
    )
    assert "No issues found" in result.stdout


# --------------------------------------------------------------------------- #
# Invalid fixtures - linkml-validate must reject them
# --------------------------------------------------------------------------- #
@pytest.mark.skipif(not _have_linkml_validate(), reason="linkml-validate not installed")
@pytest.mark.parametrize("filepath", INVALID_EXAMPLE_FILES)
def test_invalid_data_is_rejected(filepath: str) -> None:
    """Each invalid fixture is rejected by linkml-validate."""
    class_name = _target_class_from_path(filepath)
    schema, _ = _resolve_schema_and_module(class_name)
    result = _linkml_validate(schema, class_name, Path(filepath))
    combined = (result.stdout or "") + (result.stderr or "")
    assert "ERROR" in combined or result.returncode != 0, (
        f"Expected validation failure for {filepath} but got:\n"
        f"stdout: {result.stdout}\nstderr: {result.stderr}"
    )


# --------------------------------------------------------------------------- #
# Third-party data: NIST AI RMF Playbook
# --------------------------------------------------------------------------- #
@pytest.mark.skipif(
    not PLAYBOOK_JSON.exists(),
    reason=f"Playbook JSON not present at {PLAYBOOK_JSON}",
)
@pytest.mark.skipif(not _have_linkml_validate(), reason="linkml-validate not installed")
def test_third_party_nist_ai_rmf_playbook() -> None:
    """The full NIST AI RMF Playbook JSON validates against the schema.

    Runs ``scripts/validate_playbook.py`` so the same code path used by
    the ``just validate-playbook`` recipe is exercised here.
    """
    result = subprocess.run(
        [sys.executable, str(PLAYBOOK_SCRIPT), str(PLAYBOOK_JSON)],
        capture_output=True,
        text=True,
        check=False,
        cwd=REPO_ROOT,
    )
    combined = result.stdout + result.stderr
    assert result.returncode == 0, f"Playbook validation failed:\n{combined}"
    assert "No issues found" in combined
    assert "Playbook entries validated" in combined
