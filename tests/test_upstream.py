"""Checks that the vendored modules and catalogues are the released files."""

import hashlib
import importlib.util
import subprocess
from functools import cache
from pathlib import Path

import yaml

ROOT = Path(__file__).parent.parent
SCHEMA_DIR = ROOT / "src" / "nist_ai_rmf" / "schema"
SCHEMA = SCHEMA_DIR / "nist_ai_rmf.yaml"
UPSTREAM = ROOT / "tests" / "upstream"
WATCH = ROOT / "scripts" / "check_upstream_release.py"
BUILDER = ROOT / "scripts" / "build_crosswalk.py"

# Each file vendored from lmodel/nist-ai-100-1 v0.1.0 and lmodel/nist-ai-600-1 v0.1.1, as
# each repository's tag holds it. The second's v0.1.1 changed no schema file and no
# catalogue. Vendor from a later release, then move these with the release in the watch's
# VENDORED_FROM.
VENDORED_PINS = {
    "nist_ai_100_1/nist_ai_100_1.yaml": "5fabf17f35b1f8641d281bd01bae79dac6f13726de3439f122c32a3ec2fcd5ea",
    "nist_ai_100_1/nist_ai_100_1_base.yaml": "6334c56f4481dfa531aa16d2b166410fc5e23103504c3c56dea36e8ac992f86b",
    "nist_ai_100_1/nist_ai_100_1_foundations.yaml": "c3b641b427d07a2c1e49fe4e0d500e3bb0c083a238672f8cce33e5c617450b68",
    "nist_ai_100_1/nist_ai_100_1_profiles.yaml": "7a9844bcbe191ee309296bb2c2936b9831152bb7d36b90a367708ba93d3b3e65",
    "nist_ai_100_1/nist_ai_100_1_rmf_core.yaml": "b24e13cff15810c53bee95b4cd97cadf2ba5cee3073fe51ea33c2f85b5ca6048",
    "nist_ai_600_1.yaml": "212dee83417891daa8839335d4844db544741e1d4c7595a20053ff6f5bd6569c",
    "nist_ai_600_1_actions.yaml": "fd35994db48c261e20dae1b3cd4fbd122618bef9529651d3f3f72aed4972ad14",
    "nist_ai_600_1_considerations.yaml": "28467067024043bb4d4a55232d5db4c81ca94c6b499d27f62212574023007d1e",
    "nist_ai_600_1_risks.yaml": "c289bcd086f3c911f22d083497b7d1f185e4a603ac4edce63f21be4715f697e8",
    "tests/upstream/ai-600-1.yaml": "30d50ed839772c9f5e96a85197f42acee2289302a01e546f58247170a1a1c01e",
    "tests/upstream/ai-rmf-1.0.yaml": "cb7bf462a7794b5534c3559e61bb6403d9cf9e25e265f0ad1c779aaa04c00462",
}


@cache
def _load(path):
    spec = importlib.util.spec_from_file_location(path.stem, path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def _digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def test_vendored_files_are_the_pinned_ones():
    """Each vendored module and catalogue is byte for byte the pinned file, and no other file
    sits among them."""
    held = {
        str(p.relative_to(SCHEMA_DIR))
        for p in SCHEMA_DIR.rglob("*.yaml")
        if p != SCHEMA
    } | {str(p.relative_to(ROOT)) for p in UPSTREAM.iterdir()}
    assert held == set(VENDORED_PINS)
    for name, sha256 in VENDORED_PINS.items():
        path = ROOT / name if name.startswith("tests/") else SCHEMA_DIR / name
        assert _digest(path) == sha256, name


def test_watch_names_both_repositories_at_their_vendored_release():
    """The watch names each repository this one vendors from, with its tag."""
    assert _load(WATCH).VENDORED_FROM == {
        "lmodel/nist-ai-100-1": "v0.1.0",
        "lmodel/nist-ai-600-1": "v0.1.1",
    }


def test_watch_and_builder_share_the_crosswalks_pin():
    """The watch and the builder compare the same address with the same hash."""
    watch, builder = _load(WATCH), _load(BUILDER)
    assert watch.CROSSWALK_URL == builder.PDF_URL
    assert watch.CROSSWALK_SHA256 == builder.PDF_SHA256


def test_header_holds_what_the_standard_asks():
    """The header carries the version both publications carry, the source and the licence."""
    header = yaml.safe_load(SCHEMA.read_text(encoding="utf-8"))
    assert header["version"] == "1.0.0"
    assert header["license"] == "Apache-2.0"
    assert header["source"] == "https://www.nist.gov/itl/ai-risk-management-framework"
    for name in ("nist_ai_100_1/nist_ai_100_1.yaml", "nist_ai_600_1.yaml"):
        module = yaml.safe_load((SCHEMA_DIR / name).read_text(encoding="utf-8"))
        assert module["version"] == header["version"], name


def test_the_repository_carries_no_crosswalk():
    """The crosswalk states no licence, so neither its PDF nor its pairs are committed: no
    file git tracks, or would add, is a PDF or a TSV. A copy under tmp/, which git ignores,
    is the builder's to write."""
    listed = subprocess.run(
        ["git", "ls-files", "-z", "--cached", "--others", "--exclude-standard"],
        cwd=ROOT,
        capture_output=True,
        check=True,
    ).stdout.decode()
    carried = [
        name for name in listed.split("\0") if Path(name).suffix in {".tsv", ".pdf"}
    ]
    assert not carried, carried
