"""Checks that the adapt copy can sit beside LOKF and the neighbours' copies."""

import hashlib
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).parent.parent

# What a host may import beside this schema's adapt copy: LOKF's schema, pinned
# by the sidecar, and the adapt copies other lmodel repositories release. Each
# neighbour is the schema asset of a release, downloaded and checked against
# the release's .sha256 and its build-provenance attestation, and pinned here
# by that checksum.
COPY = ROOT / ".lokf" / "nist-ai-rmf.yaml"
LOKF = ROOT / ".lokf" / "lokf.yaml"
# The copies this one stands in for: each repository's schema asset of its v0.1.0, checked
# like the neighbours. They are not imported beside it, since they share elements with it.
FAMILY = {
    "nist-ai-100-1.yaml": "a9498259b8ff781fa3c24e668f5258146fe1fc4cd6e08c2aac394cb63b76a3c9",
    "nist-ai-600-1.yaml": "4fffc03c0db437256b45ffa6814c54053ffeae06a933b4d4550f94c9ff0494f4",
}
NEIGHBOURS = {
    # lmodel/d3fend v0.1.0, schema-v0.1.0-d3fend.yaml
    "d3fend.yaml": "517a5c8a35b916c1efe4e288151d241d2f350fef38aaec218c4ba7ebea986d08",
    # lmodel/slsa v0.10.0, schema-v0.10.0-slsa.yaml
    "slsa.yaml": "9eeb68decc918565886794fe4eb6e32e1fee0620688cc699961c227242a2f4c2",
    # lmodel/github-actions v0.5.0, schema-v0.5.0-github-actions.yaml
    "github-actions.yaml": "375794f7343936ae8c555e8c060c2790346661e7d81fa84d15a761fd5a329969",
    # lmodel/in-toto v0.3.0, schema-v0.3.0-in-toto.yaml
    "in-toto.yaml": "b1d15be557adfbcd538ab75ec9d43f558027d4bcbd150d72d370e83c9602f25b",
    # lmodel/oscal v0.1.2, schema-v0.1.2-oscal.yaml
    "oscal.yaml": "4eb56d7d1106463ed0a2255a29af14b8d619741acc29863d1e86eb3f8923c710",
    # lmodel/spdx v0.1.1, schema-v0.1.1-spdx.yaml
    "spdx.yaml": "3411cf5d19b1955f0362988c542984e4c817417c7b7b7892647aba1adf1ddd4a",
    # lmodel/nist-sp-800-218 v0.1.1, schema-v0.1.1-nist-sp-800-218.yaml
    "nist-sp-800-218.yaml": "479824cdd95e52226a35ff3a471b7ce93239635ccd5db7ac72a8143cdd1d8495",
    # lmodel/nist-sp-800-53 v0.1.0, schema-v0.1.0-nist-sp-800-53.yaml
    "nist-sp-800-53.yaml": "d32a989b5b855281cb45d707bf59cf52b125f05a09c54930e2b4d45c174c0d99",
    # lmodel/nist-sp-800-171 v0.1.0, schema-v0.1.0-nist-sp-800-171.yaml
    "nist-sp-800-171.yaml": "d204efa6653692da665f8604a8fb8bf445f04b37f41460a5ce2853a014b2982f",
    # lmodel/nist-csf-v2 v0.2.0, schema-v0.2.0-nist-csf-v2.yaml
    "nist-csf-v2.yaml": "f5819af21a3dbd4bd758987f166831df35aab9942a650156f6873d10d01a0dcc",
    # lmodel/iso27001 v0.1.0, schema-v0.1.0-iso27001.yaml
    "iso27001.yaml": "f5ca519043cd994c41f286f84ebc2ea510121bd2129d83c017f73a3d24ee2fe1",
    # lmodel/stix v0.1.0, schema-v0.1.0-stix.yaml
    "stix.yaml": "3837d097c0cd48e0d2a98d118003c099d1290333f5b973aee85a7017bae344c9",
    # lmodel/attack v0.1.1, schema-v0.1.1-attack.yaml
    "attack.yaml": "c2e436b0d8ab0e60a8d6557b3ba32894e0b0d23b866f1e0c0d608a97e9f5f08e",
    # lmodel/uco v0.3.0, schema-v0.3.0-uco.yaml
    "uco.yaml": "78bc3a266fa463ba380da7290adcbdfb1b8e1b7cef1ceb992bf8b1bed9b7b758",
    # lmodel/cve v0.1.0, schema-v0.1.0-cve.yaml
    "cve.yaml": "33e6086a81ac8e4cdc1e6143598cfcc961cbc1864ad9268773da9e863c652a73",
    # lmodel/kev-catalog v0.1.0, schema-v0.1.0-kev-catalog.yaml
    "kev-catalog.yaml": "76bdff7d02cc34ac6a14314692e316b005649a34f442eaf54c2846b1dac5396c",
    # lmodel/nist-nvd v0.1.0, schema-v0.1.0-nist-nvd.yaml
    "nist-nvd.yaml": "69dc8a9b34cc6646cf44515c121c8924c4e07232a9699e31065fb8930ed8be40",
    # lmodel/cwe v0.1.0, schema-v0.1.0-cwe.yaml
    "cwe.yaml": "1b2bb4c1beb089f031adc8861572b98ddf0b42f0ed3c6e5c3bfbc0f767b032cd",
    # lmodel/capec v0.1.0, schema-v0.1.0-capec.yaml
    "capec.yaml": "613164c0520384919de7d353ff87debb4e82938cec861158d151b41edd506d46",
    # lmodel/gist v0.7.1, schema-v0.7.1-gist.yaml
    "gist.yaml": "f7283f1c1df4aa6b6e2803e0645c2b1cb2eab37815642a6616d8034feb26d94d",
}
NEIGHBOUR_DIR = ROOT / "tests" / "neighbours"
ELEMENT_KINDS = ("classes", "enums", "types", "subsets")

# Keys the copy shares with a neighbour. LinkML keeps one namespace, and the
# JSON-LD context gives each key one IRI across a composite, whether it is a
# slot or an attribute on either side, so a shared key projects under one
# vocabulary's IRI. The copy shares none, so a new overlap fails the test.
SHARED_WITH_NEIGHBOURS = {name: set() for name in NEIGHBOURS}

# The classes `just lokf-adapt` re-roots on Concept, which the README lists
# for the plugins' Known LOKF types setting.
ROOTS = {
    "AiRmfFunction",
    "AiRmfCategory",
    "AiRmfSubcategory",
    "AiRmfTrustworthinessCharacteristic",
    "AiRmfDimension",
    "AiRmfLifecycleStage",
    "AiRmfActorTask",
    "AiRmfManagementChallenge",
    "AiRmfMeasurementChallenge",
    "AiRmfSpecificRisk",
    "AiRmfHumanAiIssue",
    "AiRmfAttribute",
    "AiRmfRecord",
    "GaiRisk",
    "GaiSubcategory",
    "GaiPrimaryConsideration",
    "GaiStructuredFeedback",
}

MAPPING_KEYS = (
    "mappings",
    "exact_mappings",
    "close_mappings",
    "related_mappings",
    "narrow_mappings",
    "broad_mappings",
)


def _names(path):
    """Each kind of element a schema file declares, and every slot and
    attribute name with the IRI it expands to."""
    doc = yaml.safe_load(path.read_text())
    prefixes = doc.get("prefixes") or {}

    def expand(curie):
        prefix, _, local = curie.partition(":")
        return prefixes[prefix] + local if prefix in prefixes else curie

    default = doc.get("default_prefix")
    elements = {kind: set(doc.get(kind) or {}) for kind in ELEMENT_KINDS}
    slots = {}
    owners = [doc.get("slots") or {}]
    owners += [
        (cls or {}).get("attributes") or {}
        for cls in (doc.get("classes") or {}).values()
    ]
    for owner in owners:
        for name, slot in owner.items():
            uri = (slot or {}).get("slot_uri") or f"{default}:{name}"
            slots.setdefault(name, set()).add(expand(uri))
    return elements, slots


def _mappings(node):
    """Every mapping value anywhere in a parsed schema file."""
    if isinstance(node, dict):
        for key, value in node.items():
            if key in MAPPING_KEYS:
                yield from value if isinstance(value, list) else [value]
            else:
                yield from _mappings(value)
    elif isinstance(node, list):
        for item in node:
            yield from _mappings(item)


def test_neighbours_are_the_released_assets():
    """Each neighbour copy is byte for byte the asset its release published."""
    assert {p.name for p in NEIGHBOUR_DIR.iterdir()} == {*NEIGHBOURS, *FAMILY}
    for name, sha256 in {**NEIGHBOURS, **FAMILY}.items():
        digest = hashlib.sha256((NEIGHBOUR_DIR / name).read_bytes()).hexdigest()
        assert digest == sha256, name


def test_names_apart_from_lokf():
    """No class, enum, type or subset name of the copy is LOKF's, and a slot
    name the two share carries LOKF's IRI."""
    elements, slots = _names(COPY)
    their_elements, their_slots = _names(LOKF)
    for kind in ELEMENT_KINDS:
        assert not elements[kind] & their_elements[kind], kind
    for name in slots.keys() & their_slots.keys():
        assert slots[name] == their_slots[name], name


def test_names_apart_from_the_released_neighbours():
    """A class, enum, type or subset name is the copy's alone, and the only
    keys it shares with a neighbour are the listed ones."""
    elements, slots = _names(COPY)
    for name in NEIGHBOURS:
        their_elements, their_slots = _names(NEIGHBOUR_DIR / name)
        for kind in ELEMENT_KINDS:
            assert not elements[kind] & their_elements[kind], (name, kind)
        assert slots.keys() & their_slots.keys() == SHARED_WITH_NEIGHBOURS[name], name


def test_copy_roots_the_concept_classes():
    """The copy re-roots exactly the listed classes on Concept and imports nothing
    but the LinkML types and LOKF."""
    doc = yaml.safe_load(COPY.read_text())
    rooted = {
        name for name, cls in doc["classes"].items() if cls.get("is_a") == "Concept"
    }
    assert rooted == ROOTS
    assert doc["imports"] == ["linkml:types", "lokf"]


def test_mappings_use_a_bound_prefix():
    """Every mapping in the copy is a CURIE whose prefix the copy binds. A full
    address that no prefix covers makes every `lokf convert --schema` over the
    copy warn that it has no namespace."""
    doc = yaml.safe_load(COPY.read_text())
    prefixes = doc.get("prefixes") or {}
    mappings = list(_mappings(doc))
    assert mappings
    for mapping in mappings:
        prefix, sep, _ = mapping.partition(":")
        assert sep and prefix in prefixes, mapping


NEIGHBOUR_OF_PREFIX = {
    "oscal": "oscal",
    "stix": "stix",
    "spdx_software": "spdx",
    "nist_csf_v2": "nist-csf-v2",
    "iso27001": "iso27001",
    "nist_ai_100_1": "nist-ai-100-1",
}


@pytest.mark.parametrize("prefix", NEIGHBOUR_OF_PREFIX)
def test_mappings_name_a_class_of_the_neighbour(prefix):
    """Every mapping to a neighbour names a class of its copy: its class_uri, or
    `<prefix>:<Name>` for a class that declares none."""
    doc = yaml.safe_load(COPY.read_text())
    file = NEIGHBOUR_OF_PREFIX[prefix]
    neighbour = yaml.safe_load((NEIGHBOUR_DIR / f"{file}.yaml").read_text())
    iris = {
        (cls or {}).get("class_uri") or f"{neighbour['default_prefix']}:{name}"
        for name, cls in neighbour["classes"].items()
    } | {
        (cls or {}).get("class_uri") or f"{prefix}:{name}"
        for name, cls in neighbour["classes"].items()
    }
    mappings = [m for m in _mappings(doc) if m.startswith(f"{prefix}:")]
    assert mappings
    for mapping in mappings:
        assert mapping in iris, mapping


def test_every_mapping_prefix_is_checked_or_a_public_vocabulary():
    """A mapping names a neighbour the test above reads, or PROV, read at its source."""
    doc = yaml.safe_load(COPY.read_text())
    prefixes = {m.partition(":")[0] for m in _mappings(doc)}
    assert prefixes <= {*NEIGHBOUR_OF_PREFIX, "prov"}


def _without_written_iri(entry):
    """An element without the IRI a merged copy writes out, which the next test compares."""
    entry = dict(entry)
    entry.pop("enum_uri", None)
    entry.pop("slot_uri", None)
    return entry


@pytest.mark.parametrize("name", FAMILY)
def test_this_copy_holds_each_family_copy(name):
    """Each element of a family copy is here, with the same body, so a host that imports
    this copy loses nothing. A host cannot import the two side by side: they validate
    together, but `lokf convert` stops with `Conflicting URIs` on their shared elements."""
    mine = yaml.safe_load(COPY.read_text())
    theirs = yaml.safe_load((NEIGHBOUR_DIR / name).read_text())
    for kind in ("classes", "enums", "types", "slots"):
        for element, body in (theirs.get(kind) or {}).items():
            assert element in mine[kind], (kind, element)
            assert _without_written_iri(mine[kind][element]) == _without_written_iri(body), (
                kind,
                element,
            )


@pytest.mark.parametrize(
    ("name", "prefix"),
    [("nist-ai-100-1.yaml", "nist_ai_100_1"), ("nist-ai-600-1.yaml", "nist_ai_600_1")],
)
def test_a_top_level_slot_keeps_its_publications_iri(name, prefix):
    """Each top-level slot of a family copy keeps its IRI here. A class attribute takes this
    schema's prefix in this copy alone: lokf issue 168, which the committed JSON-LD context
    does not share, and tests/test_catalogue.py holds that context to each publication."""
    mine = yaml.safe_load(COPY.read_text())["slots"]
    theirs = yaml.safe_load((NEIGHBOUR_DIR / name).read_text())["slots"]
    for slot, body in theirs.items():
        written = body.get("slot_uri") or f"{prefix}:{slot}"
        assert (mine[slot].get("slot_uri") or f"{prefix}:{slot}") == written, slot


def test_the_family_class_is_no_concept_type():
    """The class that holds both documents is not a type a concept may name."""
    doc = yaml.safe_load(COPY.read_text())
    assert doc["classes"]["NistAiRmfFamily"].get("is_a") != "Concept"
