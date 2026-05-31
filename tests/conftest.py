"""Pytest configuration.

Regenerates AGT-derived fixtures once per session so the
parametrized validation tests always run against fresh artifacts.
"""
from __future__ import annotations

import pytest

from tests.fixtures import agt_to_rmf


@pytest.fixture(scope="session", autouse=True)
def _generate_agt_fixtures() -> None:
    """Regenerate ``tests/data/{valid,invalid}/`` from upstream snapshots."""
    agt_to_rmf.generate_all()
