"""Generate NIST AI RMF test fixtures from upstream AGT example sources.

This module is a *deterministic transformer*. It reads YAML / Markdown
snapshots under ``upstream-releases/agent-governance-toolkit/examples/``
and emits NIST AI RMF-shaped YAML fixtures into
``tests/data/third-party/microsoft-agt/valid/`` (and a small
``tests/data/third-party/microsoft-agt/invalid/`` companion
set for negative tests).

Design rules:

* No network IO. Only the stdlib + ``PyYAML``.
* Pure / idempotent: re-running yields a zero diff.
* Every fixture sets exactly the slots required by its target class
  (per ``project/jsonschema/nist_ai_rmf.schema.json``), plus a
  ``see_also`` traceability link to the upstream source path.
* Each fixture filename stem is ``<TargetClassName>-<slug>.yaml`` so a
  pytest parametrization can recover the ``--target-class`` from the
  stem.

Run as a CLI for manual inspection::

    python -m tests.fixtures.agt_to_rmf

Or let ``tests/conftest.py`` invoke ``generate_all()`` once per session.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any, Iterable

import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]
UPSTREAM = (
    REPO_ROOT
    / "upstream-releases"
    / "agent-governance-toolkit"
    / "examples"
)
UPSTREAM_VERSION_FILE = (
    REPO_ROOT / "upstream-releases" / "agent-governance-toolkit" / "VERSION"
)
THIRD_PARTY_DIR = (
    REPO_ROOT
    / "tests"
    / "data"
    / "third-party"
    / "microsoft-agt"
)
VALID_DIR = THIRD_PARTY_DIR / "valid"
INVALID_DIR = THIRD_PARTY_DIR / "invalid"

NIST_600_1_REFERENCE = Path(__file__).with_name("nist_ai_600_1_actions.yaml")
OWASP_ASI_CATALOG = Path(__file__).with_name("owasp_asi_catalog.yaml")

# Vendored AGT compliance reference docs (under upstream-releases/).
# Added to profile / risk fixture `see_also` lists for cross-framework
# traceability. Resolved relative to REPO_ROOT lazily by
# `_compliance_see_also` so missing files do not break generation.
_AGT_COMPLIANCE_DIR = (
    "upstream-releases/agent-governance-toolkit/docs/compliance"
)
AGT_RMF_ALIGNMENT_DOC = f"{_AGT_COMPLIANCE_DIR}/nist-ai-rmf-alignment.md"
AGT_ASI_POLICY_MAPPING_DOC = f"{_AGT_COMPLIANCE_DIR}/owasp-asi-policy-mapping.md"

NS = "nist_ai_rmf_test"


# --------------------------------------------------------------------------- #
# Helpers
# --------------------------------------------------------------------------- #


def _slug(text: str) -> str:
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text).strip("-")
    return text or "x"


def _see_also(path: Path) -> list[str]:
    return [path.relative_to(REPO_ROOT).as_posix()]


def _compliance_see_also(rel_path: str) -> list[str]:
    """Return ``[rel_path]`` if the file exists under REPO_ROOT, else ``[]``.

    Keeps generation working even when the vendored AGT docs are absent
    (e.g. a future trimmed snapshot).
    """
    if (REPO_ROOT / rel_path).exists():
        return [rel_path]
    return []


_AGT_ALIGNMENT_NOTE = (
    "Per the AGT NIST AI RMF self-assessment, AGT fully addresses 12/19 "
    "RMF subcategories and partially addresses the remaining 7 "
    "(see `nist-ai-rmf-alignment.md`)."
)


def _agt_profile_enrich(doc: dict[str, Any]) -> dict[str, Any]:
    """Attach the AGT NIST RMF alignment doc to an AGT-derived profile.

    Appends ``AGT_RMF_ALIGNMENT_DOC`` to ``see_also`` and appends a
    one-line attribution to ``description``. Idempotent.
    """
    extra = _compliance_see_also(AGT_RMF_ALIGNMENT_DOC)
    if extra:
        seen = list(doc.get("see_also") or [])
        for ref in extra:
            if ref not in seen:
                seen.append(ref)
        doc["see_also"] = seen
        desc = (doc.get("description") or "").rstrip()
        if _AGT_ALIGNMENT_NOTE not in desc:
            doc["description"] = (
                f"{desc} {_AGT_ALIGNMENT_NOTE}".strip()
            )
    return doc


def _dump(target: Path, doc: dict[str, Any]) -> None:
    target.parent.mkdir(parents=True, exist_ok=True)
    text = yaml.dump(
        doc,
        Dumper=_FixtureDumper,
        sort_keys=True,
        default_flow_style=False,
        width=64,
        allow_unicode=True,
        indent=2,
    )
    target.write_text(text)


# yamllint-friendly string rendering.
#
# Goals:
#   * Block-style collections only (no inline `[a, b]` / `{k: v}` lists or maps).
#   * Folded block scalars (``>-``) for long, breakable strings so PyYAML wraps
#     on word boundaries within the ``line-length`` budget configured in
#     ``.yamllint.yaml`` (max 80).
#   * Literal block scalars (``|``) for any string that already contains
#     newlines.
#   * Plain scalars for short strings and for long single-token strings
#     (e.g. URLs) which cannot be wrapped; ``.yamllint.yaml`` allows the
#     latter via ``allow-non-breakable-words: true``.

_WRAP_THRESHOLD = 70


def _str_presenter(dumper: yaml.SafeDumper, data: str) -> Any:
    if "\n" in data:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style="|"
        )
    if len(data) > _WRAP_THRESHOLD and " " in data:
        return dumper.represent_scalar(
            "tag:yaml.org,2002:str", data, style=">"
        )
    return dumper.represent_scalar("tag:yaml.org,2002:str", data)


class _FixtureDumper(yaml.SafeDumper):
    """SafeDumper that forces block-style collections + folded long strings."""

    def increase_indent(self, flow=False, indentless=False):  # type: ignore[override]
        # Indent sequence items under their parent key so yamllint's
        # default `indentation: indent-sequences: true` rule is satisfied.
        return super().increase_indent(flow=flow, indentless=False)


_FixtureDumper.add_representer(str, _str_presenter)
# Ensure nested sequences/mappings never collapse to flow style even if a
# parent representer requested it implicitly.
_FixtureDumper.default_flow_style = False


def _load_yaml(path: Path) -> Any:
    with path.open() as fh:
        return yaml.safe_load(fh)


def _iter_yaml(root: Path) -> Iterable[Path]:
    return sorted(root.rglob("*.yaml"))


# --------------------------------------------------------------------------- #
# NIST AI 600-1 reference data (vendored)
# --------------------------------------------------------------------------- #


def _load_nist_600_1_reference() -> dict[str, Any]:
    """Load the vendored real-action reference table.

    See ``nist_ai_600_1_actions.yaml`` for provenance. Cached at module
    scope by simple memoisation on first use.
    """
    return _load_yaml(NIST_600_1_REFERENCE) or {}


_NIST_REF = _load_nist_600_1_reference()
_NIST_ACTIONS: dict[str, dict[str, Any]] = _NIST_REF.get("actions") or {}
_ATR_ROUTING: dict[str, Any] = _NIST_REF.get("atr_routing") or {}
_ATTESTATION_ROUTING: dict[str, str] = _NIST_REF.get("attestation_routing") or {}


def _load_owasp_asi_catalog() -> dict[str, dict[str, Any]]:
    """Load the vendored canonical OWASP ASI Top 10 (2026) catalog.

    See ``owasp_asi_catalog.yaml`` for provenance. Returns a mapping
    of two-digit ASI id (``"01"``..``"10"``) to entry dict.
    """
    data = _load_yaml(OWASP_ASI_CATALOG) or {}
    return data.get("risks") or {}


_ASI_CATALOG: dict[str, dict[str, Any]] = _load_owasp_asi_catalog()


def _route_atr_action_id(text: str) -> str:
    """Pick a real NIST AI 600-1 action_id for an ATR rule by keyword.

    Walks ``atr_routing.rules`` in order; first matching substring wins.
    Falls back to ``atr_routing.default_action_id``.
    """
    haystack = (text or "").lower()
    for rule in _ATR_ROUTING.get("rules") or []:
        for needle in rule.get("match") or []:
            if needle.lower() in haystack:
                return rule["action_id"]
    return _ATR_ROUTING.get("default_action_id", "GV-1.1-001")


def _enrich_with_reference(doc: dict[str, Any], action_id: str) -> dict[str, Any]:
    """Copy reference slots (function_prefix/subcategory/risks/tasks) into ``doc``.

    Caller-supplied keys win; reference fills in anything left unset.
    """
    ref = _NIST_ACTIONS.get(action_id) or {}
    for key in ("function_prefix", "applies_to_subcategory", "gai_risks", "actor_task"):
        if key in ref and doc.get(key) is None:
            doc[key] = ref[key]
    doc["action_id"] = action_id
    return doc


# --------------------------------------------------------------------------- #
# Emitters - one per AGT source family
# --------------------------------------------------------------------------- #


def emit_aegis_profiles() -> list[Path]:
    """``aegis-governance-profile/profile-*.yaml`` -> ``AiRmfProfile``."""
    written: list[Path] = []
    src_dir = UPSTREAM / "aegis-governance-profile"
    for src in sorted(src_dir.glob("profile-*.yaml")):
        data = _load_yaml(src) or {}
        prof = data.get("profile", {}) or {}
        pid = prof.get("id") or src.stem
        slug = _slug(pid)
        doc = {
            "id": f"{NS}:profile/aegis/{slug}",
            "profile_type": "USE_CASE",
            "name": pid,
            "title": f"AEGIS profile: {pid}",
            "description": (prof.get("description") or "").strip() or None,
            "sector": _infer_sector(pid),
            "see_also": _see_also(src),
        }
        # Drop None
        doc = {k: v for k, v in doc.items() if v is not None}
        _agt_profile_enrich(doc)
        target = VALID_DIR / f"AiRmfProfile-aegis-{slug}.yaml"
        _dump(target, doc)
        written.append(target)
    return written


def _infer_sector(name: str) -> str | None:
    low = name.lower()
    if "research" in low:
        return "research"
    if "support" in low or "customer" in low:
        return "customer-support"
    return None


def emit_policy_templates() -> list[Path]:
    """``policy-templates/*.yaml`` -> ``AiRmfProfile`` per sector."""
    written: list[Path] = []
    src_dir = UPSTREAM / "policy-templates"
    for src in sorted(src_dir.glob("*.yaml")):
        data = _load_yaml(src) or {}
        sector = src.stem  # healthcare, financial-services, ...
        slug = _slug(sector)
        doc = {
            "id": f"{NS}:profile/template/{slug}",
            "profile_type": "CROSS_SECTORAL",
            "name": data.get("name") or slug,
            "title": f"Policy template profile: {sector}",
            "description": (data.get("description") or "").strip() or None,
            "sector": sector,
            "see_also": _see_also(src),
        }
        doc = {k: v for k, v in doc.items() if v is not None}
        _agt_profile_enrich(doc)
        target = VALID_DIR / f"AiRmfProfile-template-{slug}.yaml"
        _dump(target, doc)
        written.append(target)
    return written


def emit_production_policies() -> list[Path]:
    """``policies/production/*.yaml`` -> ``AiRmfProfile`` + ``RiskTolerance``."""
    written: list[Path] = []
    src_dir = UPSTREAM / "policies" / "production"
    for src in sorted(src_dir.glob("*.yaml")):
        data = _load_yaml(src) or {}
        tier = src.stem  # enterprise, healthcare, ...
        slug = _slug(tier)

        prof = {
            "id": f"{NS}:profile/production/{slug}",
            "profile_type": "USE_CASE",
            "name": data.get("name") or slug,
            "title": f"Production policy profile: {tier}",
            "description": (data.get("description") or "").strip() or None,
            "sector": tier if tier in {"healthcare", "financial"} else None,
            "see_also": _see_also(src),
        }
        prof = {k: v for k, v in prof.items() if v is not None}
        _agt_profile_enrich(prof)
        prof_target = VALID_DIR / f"AiRmfProfile-production-{slug}.yaml"
        _dump(prof_target, prof)
        written.append(prof_target)

        tol = {
            "id": f"{NS}:risk-tolerance/production/{slug}",
            "name": f"{tier}-tolerance",
            "title": f"Risk tolerance derived from {tier} production policy",
            "tolerance_statement": (
                f"Risk tolerance tier '{tier}' synthesised from upstream rule "
                f"pack default action "
                f"'{(data.get('defaults') or {}).get('action', 'unknown')}'."
            ),
            "see_also": _see_also(src),
        }
        tol_target = VALID_DIR / f"RiskTolerance-production-{slug}.yaml"
        _dump(tol_target, tol)
        written.append(tol_target)
    return written


_MAF_SCENARIOS = [
    "01-loan-processing",
    "02-customer-service",
    "03-healthcare",
    "04-it-helpdesk",
    "05-devops-deploy",
    "06-dotnet-extension-validation",
]


def emit_maf_scenarios() -> list[Path]:
    """``maf-integration/<scenario>/*/policies/*.yaml`` -> ``AiSystem`` + ``AiRmfProfile``."""
    written: list[Path] = []
    base = UPSTREAM / "maf-integration"
    for scenario in _MAF_SCENARIOS:
        # Prefer python variant; fall back to dotnet.
        candidates = list((base / scenario).glob("*/policies/*.yaml"))
        if not candidates:
            continue
        src = sorted(candidates)[0]
        data = _load_yaml(src) or {}
        slug = _slug(scenario)
        name = data.get("name") or scenario
        desc = (data.get("description") or "").strip() or None

        sys_doc = {
            "id": f"{NS}:ai-system/maf/{slug}",
            "name": f"maf-{scenario}",
            "title": f"MAF scenario AI system: {scenario}",
            "description": desc,
            "see_also": _see_also(src),
        }
        sys_doc = {k: v for k, v in sys_doc.items() if v is not None}
        sys_target = VALID_DIR / f"AiSystem-maf-{slug}.yaml"
        _dump(sys_target, sys_doc)
        written.append(sys_target)

        prof_doc = {
            "id": f"{NS}:profile/maf/{slug}",
            "profile_type": "USE_CASE",
            "name": name,
            "title": f"MAF governance profile: {scenario}",
            "description": desc,
            "see_also": _see_also(src),
        }
        prof_doc = {k: v for k, v in prof_doc.items() if v is not None}
        _agt_profile_enrich(prof_doc)
        prof_target = VALID_DIR / f"AiRmfProfile-maf-{slug}.yaml"
        _dump(prof_target, prof_doc)
        written.append(prof_target)
    return written


_ASI_FUNCTION_PREFIX = {
    # Retained for documentation only — no longer used by
    # emit_asi_gai_risks (which now reads `owasp_asi_catalog.yaml`).
    "01": "GV",
    "02": "MG",
    "03": "GV",
    "04": "MS",
    "05": "MP",
    "06": "MS",
    "07": "MG",
    "08": "MP",
    "09": "GV",
    "10": "MG",
}


def emit_atr_suggested_actions(limit: int = 20) -> list[Path]:
    """First ``limit`` unique ATR rules -> ``SuggestedAction``.

    Each fixture's ``action_id`` is joined to a real NIST AI 600-1
    reference action via keyword routing
    (see ``nist_ai_600_1_actions.yaml``); ``function_prefix``,
    ``applies_to_subcategory``, ``gai_risks`` and ``actor_task`` are
    populated from the reference entry.
    """
    src = UPSTREAM / "atr-community-rules" / "atr_security_policy.yaml"
    if not src.exists():
        return []
    data = _load_yaml(src) or {}
    written: list[Path] = []
    seen: set[str] = set()
    for rule in (data.get("rules") or []):
        name = rule.get("name") or ""
        # Collapse '-N' suffixes so we get one fixture per base rule id.
        base = re.sub(r"-\d+$", "", name)
        if base in seen:
            continue
        seen.add(base)
        slug = _slug(base)
        message = rule.get("message") or base
        action_id = _route_atr_action_id(f"{base} {message}")
        doc: dict[str, Any] = {
            "id": f"{NS}:suggested-action/atr/{slug}",
            "name": base,
            "title": message,
            "description": (
                f"Suggested mitigation derived from ATR community rule "
                f"`{base}`. Upstream action: {rule.get('action')!r}. "
                f"Joined to NIST AI 600-1 reference action {action_id}."
            ),
            "see_also": _see_also(src),
        }
        _enrich_with_reference(doc, action_id)
        target = VALID_DIR / f"SuggestedAction-atr-{slug}.yaml"
        _dump(target, doc)
        written.append(target)
        if len(written) >= limit:
            break
    return written


def emit_asi_gai_risks() -> list[Path]:
    """OWASP ASI-01..ASI-10 -> ``GaiRisk`` fixtures.

    Titles and ``gai_risk_kind`` are pulled from the *canonical* OWASP
    Agentic Security Initiative Top-10 catalog vendored at
    ``tests/fixtures/owasp_asi_catalog.yaml`` (sourced from the AGT
    compliance docs). The healthcare policy template is still listed in
    ``see_also`` as the upstream artefact whose comment blocks first
    inspired this emitter; the AGT ASI-policy mapping doc is added as
    additional traceability.
    """
    template_src = UPSTREAM / "policy-templates" / "healthcare.yaml"
    written: list[Path] = []
    for num in sorted(_ASI_CATALOG):
        entry = _ASI_CATALOG[num]
        title = entry.get("title") or f"ASI-{num}"
        slug = f"asi-{num}"
        see_also: list[str] = []
        if template_src.exists():
            see_also.extend(_see_also(template_src))
        see_also.extend(_compliance_see_also(AGT_ASI_POLICY_MAPPING_DOC))
        doc: dict[str, Any] = {
            "id": f"{NS}:gai-risk/{slug}",
            "name": f"ASI-{num}",
            "title": title,
            "description": (
                f"GAI-risk fixture derived from OWASP Agentic Security "
                f"Initiative item ASI-{num}: {title}. "
                f"Mapped to GaiRiskCategoryEnum.{entry.get('gai_risk_kind')} "
                f"per the vendored ASI catalog."
            ),
            "see_also": see_also,
        }
        if entry.get("gai_risk_kind"):
            doc["gai_risk_kind"] = entry["gai_risk_kind"]
        target = VALID_DIR / f"GaiRisk-{slug}.yaml"
        _dump(target, doc)
        written.append(target)
    return written


_ATTESTATION_TECHNIQUES = {
    "crypto-attestation-governed": "DIGITAL_FINGERPRINTING",
    "physical-attestation-governed": "HUMAN_AUTHENTICATION",
    "reasoning-attestation-governed": "METADATA_RECORDING",
}


def emit_attestation_suggested_actions() -> list[Path]:
    """Attestation example dirs -> ``SuggestedAction`` w/ real action_id.

    Each AGT attestation flavour is mapped to a real NIST AI 600-1
    reference action via ``attestation_routing`` in
    ``nist_ai_600_1_actions.yaml``.
    """
    written: list[Path] = []
    for sub, technique in _ATTESTATION_TECHNIQUES.items():
        src_dir = UPSTREAM / sub
        readme = src_dir / "README.md"
        if not readme.exists():
            continue
        slug = _slug(sub.replace("-governed", ""))
        action_id = _ATTESTATION_ROUTING.get(sub, "MS-2.7-005")
        doc: dict[str, Any] = {
            "id": f"{NS}:suggested-action/attestation/{slug}",
            "name": f"attestation-{slug}",
            "title": f"Provenance attestation suggested action: {slug}",
            "description": (
                f"Suggested action derived from the AGT '{sub}' example. "
                f"Maps to provenance technique '{technique}'. "
                f"Joined to NIST AI 600-1 reference action {action_id}."
            ),
            "see_also": _see_also(readme),
        }
        _enrich_with_reference(doc, action_id)
        target = VALID_DIR / f"SuggestedAction-attestation-{slug}.yaml"
        _dump(target, doc)
        written.append(target)
    return written


def emit_github_actors() -> list[Path]:
    """``github-actions-governance/agents.yaml`` -> ``AiActor`` per agent."""
    src = UPSTREAM / "github-actions-governance" / "agents.yaml"
    if not src.exists():
        return []
    data = _load_yaml(src) or {}
    written: list[Path] = []
    for agent in (data.get("agents") or []):
        name = agent.get("name") or "agent"
        slug = _slug(name)
        doc = {
            "id": f"{NS}:ai-actor/github/{slug}",
            "name": name,
            "title": f"CI/CD AI actor: {name}",
            "description": agent.get("description"),
            "is_tevv": False,
            "see_also": _see_also(src),
        }
        doc = {k: v for k, v in doc.items() if v is not None}
        target = VALID_DIR / f"AiActor-github-{slug}.yaml"
        _dump(target, doc)
        written.append(target)
    return written


def emit_decision_bom_feedback() -> list[Path]:
    """``decision-bom/README.md`` -> ``StructuredPublicFeedback`` fixture."""
    src = UPSTREAM / "decision-bom" / "README.md"
    if not src.exists():
        return []
    doc = {
        "id": f"{NS}:structured-feedback/decision-bom",
        "feedback_method_kind": "PARTICIPATORY_ENGAGEMENT_METHODS",
        "name": "decision-bom-audit",
        "title": "Structured feedback derived from Decision BOM example",
        "description": (
            "Structured feedback fixture derived from the AGT decision-bom "
            "example, which reconstructs a complete Bill of Materials for "
            "any governance decision from observability signals."
        ),
        "see_also": _see_also(src),
    }
    target = VALID_DIR / "StructuredPublicFeedback-decision-bom.yaml"
    _dump(target, doc)
    return [target]


# --------------------------------------------------------------------------- #
# Invalid fixtures (negative tests)
# --------------------------------------------------------------------------- #


def emit_invalid_fixtures() -> list[Path]:
    cases: list[tuple[str, dict[str, Any]]] = [
        # AiRmfProfile missing required profile_type
        (
            "AiRmfProfile-missing-profile_type.yaml",
            {"id": f"{NS}:invalid/profile-missing-type", "name": "bad"},
        ),
        # ProfileTypeEnum invalid value
        (
            "AiRmfProfile-bad-enum.yaml",
            {
                "id": f"{NS}:invalid/profile-bad-enum",
                "profile_type": "NOT_A_REAL_TYPE",
            },
        ),
        # SuggestedAction missing required action_id
        (
            "SuggestedAction-missing-action_id.yaml",
            {
                "id": f"{NS}:invalid/sa-missing-action-id",
                "function_prefix": "GV",
            },
        ),
        # SuggestedAction with invalid function_prefix
        (
            "SuggestedAction-bad-function_prefix.yaml",
            {
                "id": f"{NS}:invalid/sa-bad-prefix",
                "action_id": "ZZ-9.9-999",
                "function_prefix": "ZZ",
            },
        ),
        # StructuredPublicFeedback missing required feedback_method_kind
        (
            "StructuredPublicFeedback-missing-kind.yaml",
            {"id": f"{NS}:invalid/spf-missing-kind"},
        ),
    ]
    written: list[Path] = []
    for filename, body in cases:
        target = INVALID_DIR / filename
        _dump(target, body)
        written.append(target)
    return written


# --------------------------------------------------------------------------- #
# Entry points
# --------------------------------------------------------------------------- #


_EMITTERS = (
    emit_aegis_profiles,
    emit_policy_templates,
    emit_production_policies,
    emit_maf_scenarios,
    emit_atr_suggested_actions,
    emit_asi_gai_risks,
    emit_attestation_suggested_actions,
    emit_github_actors,
    emit_decision_bom_feedback,
)


def _clean_generated() -> None:
    """Remove previously generated fixtures to keep the output set deterministic."""
    for d in (VALID_DIR, INVALID_DIR):
        if not d.exists():
            continue
        for p in d.glob("*.yaml"):
            p.unlink()


def generate_all() -> dict[str, list[Path]]:
    """Regenerate every fixture; returns ``{emitter_name: [paths]}``."""
    _clean_generated()
    VALID_DIR.mkdir(parents=True, exist_ok=True)
    INVALID_DIR.mkdir(parents=True, exist_ok=True)
    results: dict[str, list[Path]] = {}
    for fn in _EMITTERS:
        results[fn.__name__] = fn()
    results["emit_invalid_fixtures"] = emit_invalid_fixtures()
    return results


def upstream_version() -> str:
    if UPSTREAM_VERSION_FILE.exists():
        return UPSTREAM_VERSION_FILE.read_text().strip()
    return "unknown"


def main() -> None:
    results = generate_all()
    total = sum(len(v) for v in results.values())
    print(f"Upstream AGT version: {upstream_version()}")
    print(f"Generated {total} fixtures across {len(results)} emitters:")
    for name, paths in results.items():
        print(f"  - {name}: {len(paths)} file(s)")


if __name__ == "__main__":
    main()
