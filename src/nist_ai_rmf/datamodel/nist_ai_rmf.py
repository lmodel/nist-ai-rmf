# Auto generated from nist_ai_rmf.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-31T16:38:59
# Schema: nist-ai-rmf
#
# id: https://w3id.org/lmodel/nist-ai-rmf
# description: Merged LinkML schema for the NIST AI Risk Management Framework family.
#
#   Imports:
#     * `nist_ai_100_1` - AI RMF 1.0 (NIST AI 100-1) foundational
#       concepts, Core Functions / Categories / Subcategories,
#       Profiles, design attributes, and the AI RMF Playbook
#       companion data shape.
#     * `nist_ai_600_1` - GAI Profile (NIST AI 600-1): 12 GAI
#       risks, Suggested Actions, Primary GAI Considerations, and
#       Structured Public Feedback methods.
#
#   Most consumers should import this umbrella to get the entire
#   framework via a single namespace (`nist_ai_rmf:`). Two tree-root
#   classes are exposed by the imports - `AiRmfFramework` from the
#   core module and `GaiProfile` from the GAI module - so callers
#   must pass `--target-class` when validating.
# license: Apache-2.0

import dataclasses
import re
from dataclasses import dataclass
from datetime import (
    date,
    datetime,
    time
)
from typing import (
    Any,
    ClassVar,
    Dict,
    List,
    Optional,
    Union
)

from jsonasobj2 import (
    JsonObj,
    as_dict
)
from linkml_runtime.linkml_model.meta import (
    EnumDefinition,
    PermissibleValue,
    PvFormulaOptions
)
from linkml_runtime.utils.curienamespace import CurieNamespace
from linkml_runtime.utils.enumerations import EnumDefinitionImpl
from linkml_runtime.utils.formatutils import (
    camelcase,
    sfx,
    underscore
)
from linkml_runtime.utils.metamodelcore import (
    bnode,
    empty_dict,
    empty_list
)
from linkml_runtime.utils.slot import Slot
from linkml_runtime.utils.yamlutils import (
    YAMLRoot,
    extended_float,
    extended_int,
    extended_str
)
from rdflib import (
    Namespace,
    URIRef
)

from linkml_runtime.linkml_model.types import Boolean, Date, Float, String, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URIorCURIE, XSDDate

metamodel_version = "1.11.0"
version = "1.0.0"

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
FOAF = CurieNamespace('foaf', 'http://xmlns.com/foaf/0.1/')
GIST_LINKML = CurieNamespace('gist_linkml', 'https://w3id.org/lmodel/gist/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO29100 = CurieNamespace('iso29100', 'https://w3id.org/lmodel/iso29100/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_AI_100_1 = CurieNamespace('nist_ai_100_1', 'https://w3id.org/lmodel/nist-ai-100-1/')
NIST_AI_600_1 = CurieNamespace('nist_ai_600_1', 'https://w3id.org/lmodel/nist-ai-600-1/')
NIST_AI_RMF = CurieNamespace('nist_ai_rmf', 'https://w3id.org/lmodel/nist-ai-rmf/')
NIST_CSF = CurieNamespace('nist_csf', 'https://w3id.org/lmodel/nist-csf-v2/')
NIST_SP_800_53 = CurieNamespace('nist_sp_800_53', 'https://w3id.org/lmodel/nist-sp-800-53/')
OSCAL_CATALOG = CurieNamespace('oscal_catalog', 'https://w3id.org/lmodel/oscal_catalog/')
OSCAL_PROFILE = CurieNamespace('oscal_profile', 'https://w3id.org/lmodel/oscal_profile/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_AI_RMF


# Types
class FunctionCode(String):
    """ Identifier of one of the four AI RMF Core functions. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "FunctionCode"
    type_model_uri = NIST_AI_RMF.FunctionCode


class CategoryCode(String):
    """ Identifier for a Core category (e.g., "GOVERN 1", "MAP 3"). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "CategoryCode"
    type_model_uri = NIST_AI_RMF.CategoryCode


class GaiActionId(String):
    """ Action identifier used in NIST AI 600-1 Section 3, of the form
"<prefix>-<category>.<subcategory>-<seq>" - e.g., "GV-1.1-001".
Prefixes: GV (Govern), MP (Map), MS (Measure), MG (Manage). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "GaiActionId"
    type_model_uri = NIST_AI_RMF.GaiActionId


class SubcategoryCode(String):
    """ Identifier for a Core subcategory (e.g., "GOVERN 1.1"). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "SubcategoryCode"
    type_model_uri = NIST_AI_RMF.SubcategoryCode


# Class references
class NamedThingId(URIorCURIE):
    pass


class AiSystemId(NamedThingId):
    pass


class AiSystemDimensionId(NamedThingId):
    pass


class AiLifecycleStageId(NamedThingId):
    pass


class AiActorId(NamedThingId):
    pass


class AiActorTaskId(NamedThingId):
    pass


class RiskId(NamedThingId):
    pass


class ImpactId(NamedThingId):
    pass


class HarmId(NamedThingId):
    pass


class ResidualRiskId(RiskId):
    pass


class RiskToleranceId(NamedThingId):
    pass


class RiskMeasurementChallengeId(NamedThingId):
    pass


class TrustworthinessCharacteristicId(NamedThingId):
    pass


class BiasId(NamedThingId):
    pass


class FunctionId(NamedThingId):
    pass


class CategoryId(NamedThingId):
    pass


class SubcategoryId(NamedThingId):
    pass


class AiRmfProfileId(NamedThingId):
    pass


class RmfAttributeId(NamedThingId):
    pass


class AiSpecificRiskId(NamedThingId):
    pass


class HumanAiInteractionIssueId(NamedThingId):
    pass


class AiRmfDocumentId(NamedThingId):
    pass


class AiRmfFrameworkId(NamedThingId):
    pass


class GaiRiskId(NamedThingId):
    pass


class SuggestedActionId(NamedThingId):
    pass


class PrimaryGaiConsiderationId(NamedThingId):
    pass


class StructuredPublicFeedbackId(NamedThingId):
    pass


class AiRedTeamingId(StructuredPublicFeedbackId):
    pass


class GaiProfileId(NamedThingId):
    pass


@dataclass(repr=False)
class PlaybookEntry(YAMLRoot):
    """
    A single AI RMF Playbook entry - an enrichment of a Core
    subcategory with prose discussion, suggested actions,
    documentation questions, references, and topic tags.

    Attribute names use the same identifiers found in the published
    NIST AI RMF Playbook JSON (e.g., `section_about`,
    `section_actions`) so that the data can be loaded directly.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["PlaybookEntry"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:PlaybookEntry"
    class_name: ClassVar[str] = "PlaybookEntry"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.PlaybookEntry

    type: Optional[str] = None
    title: Optional[str] = None
    category: Optional[str] = None
    description: Optional[str] = None
    section_about: Optional[str] = None
    section_actions: Optional[str] = None
    section_doc: Optional[str] = None
    section_ref: Optional[str] = None
    ai_actors: Optional[Union[str, list[str]]] = empty_list()
    topic: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.type is not None and not isinstance(self.type, str):
            self.type = str(self.type)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.category is not None and not isinstance(self.category, str):
            self.category = str(self.category)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.section_about is not None and not isinstance(self.section_about, str):
            self.section_about = str(self.section_about)

        if self.section_actions is not None and not isinstance(self.section_actions, str):
            self.section_actions = str(self.section_actions)

        if self.section_doc is not None and not isinstance(self.section_doc, str):
            self.section_doc = str(self.section_doc)

        if self.section_ref is not None and not isinstance(self.section_ref, str):
            self.section_ref = str(self.section_ref)

        if not isinstance(self.ai_actors, list):
            self.ai_actors = [self.ai_actors] if self.ai_actors is not None else []
        self.ai_actors = [v if isinstance(v, str) else str(v) for v in self.ai_actors]

        if not isinstance(self.topic, list):
            self.topic = [self.topic] if self.topic is not None else []
        self.topic = [v if isinstance(v, str) else str(v) for v in self.topic]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PlaybookCollection(YAMLRoot):
    """
    A container for a set of PlaybookEntry instances - the
    serialisation root for an AI RMF Playbook companion document.
    Validate with ``linkml-validate --target-class PlaybookCollection``;
    the canonical tree-root for the schema is ``AiRmfFramework``.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["PlaybookCollection"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:PlaybookCollection"
    class_name: ClassVar[str] = "PlaybookCollection"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.PlaybookCollection

    entries: Optional[Union[Union[dict, PlaybookEntry], list[Union[dict, PlaybookEntry]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.entries, list):
            self.entries = [self.entries] if self.entries is not None else []
        self.entries = [v if isinstance(v, PlaybookEntry) else PlaybookEntry(**as_dict(v)) for v in self.entries]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class NamedThing(YAMLRoot):
    """
    A generic grouping for any identifiable AI RMF element.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = SCHEMA["Thing"]
    class_class_curie: ClassVar[str] = "schema:Thing"
    class_name: ClassVar[str] = "NamedThing"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.NamedThing

    id: Union[str, NamedThingId] = None
    name: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    see_also: Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, NamedThingId):
            self.id = NamedThingId(self.id)

        if self.name is not None and not isinstance(self.name, str):
            self.name = str(self.name)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.see_also, list):
            self.see_also = [self.see_also] if self.see_also is not None else []
        self.see_also = [v if isinstance(v, URIorCURIE) else URIorCURIE(v) for v in self.see_also]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiSystem(NamedThing):
    """
    An engineered or machine-based system that can, for a given set
    of objectives, generate outputs such as predictions,
    recommendations, or decisions influencing real or virtual
    environments. AI systems are designed to operate with varying
    levels of autonomy (Adapted from OECD Recommendation on AI:2019;
    ISO/IEC 22989:2022).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiSystem"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiSystem"
    class_name: ClassVar[str] = "AiSystem"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiSystem

    id: Union[str, AiSystemId] = None
    lifecycle_stage: Optional[Union[Union[str, "AiLifecycleStageEnum"], list[Union[str, "AiLifecycleStageEnum"]]]] = empty_list()
    ai_dimension: Optional[Union[Union[str, "AiSystemDimensionEnum"], list[Union[str, "AiSystemDimensionEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiSystemId):
            self.id = AiSystemId(self.id)

        if not isinstance(self.lifecycle_stage, list):
            self.lifecycle_stage = [self.lifecycle_stage] if self.lifecycle_stage is not None else []
        self.lifecycle_stage = [v if isinstance(v, AiLifecycleStageEnum) else AiLifecycleStageEnum(v) for v in self.lifecycle_stage]

        if not isinstance(self.ai_dimension, list):
            self.ai_dimension = [self.ai_dimension] if self.ai_dimension is not None else []
        self.ai_dimension = [v if isinstance(v, AiSystemDimensionEnum) else AiSystemDimensionEnum(v) for v in self.ai_dimension]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiSystemDimension(NamedThing):
    """
    A socio-technical dimension of an AI system (Figure 2):
    Application Context, Data and Input, AI Model, Task and Output,
    or People and Planet.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiSystemDimension"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiSystemDimension"
    class_name: ClassVar[str] = "AiSystemDimension"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiSystemDimension

    id: Union[str, AiSystemDimensionId] = None
    dimension_kind: Union[str, "AiSystemDimensionEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiSystemDimensionId):
            self.id = AiSystemDimensionId(self.id)

        if self._is_empty(self.dimension_kind):
            self.MissingRequiredField("dimension_kind")
        if not isinstance(self.dimension_kind, AiSystemDimensionEnum):
            self.dimension_kind = AiSystemDimensionEnum(self.dimension_kind)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiLifecycleStage(NamedThing):
    """
    A stage of the AI lifecycle (Figure 2): Plan and Design,
    Collect and Process Data, Build and Use Model, Verify and
    Validate, Deploy and Use, or Operate and Monitor.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiLifecycleStage"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiLifecycleStage"
    class_name: ClassVar[str] = "AiLifecycleStage"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiLifecycleStage

    id: Union[str, AiLifecycleStageId] = None
    stage_kind: Union[str, "AiLifecycleStageEnum"] = None
    includes_tevv: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiLifecycleStageId):
            self.id = AiLifecycleStageId(self.id)

        if self._is_empty(self.stage_kind):
            self.MissingRequiredField("stage_kind")
        if not isinstance(self.stage_kind, AiLifecycleStageEnum):
            self.stage_kind = AiLifecycleStageEnum(self.stage_kind)

        if self.includes_tevv is not None and not isinstance(self.includes_tevv, Bool):
            self.includes_tevv = Bool(self.includes_tevv)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiActor(NamedThing):
    """
    An organization or individual that plays an active role in the AI
    system lifecycle. AI actors include those who deploy or operate
    AI as well as those who inform via formal or quasi-formal norms
    and guidance (OECD 2019).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiActor"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiActor"
    class_name: ClassVar[str] = "AiActor"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiActor

    id: Union[str, AiActorId] = None
    actor_task: Optional[Union[Union[str, "AiActorTaskEnum"], list[Union[str, "AiActorTaskEnum"]]]] = empty_list()
    lifecycle_stage: Optional[Union[Union[str, "AiLifecycleStageEnum"], list[Union[str, "AiLifecycleStageEnum"]]]] = empty_list()
    is_tevv: Optional[Union[bool, Bool]] = None
    audience: Optional[Union[str, "AudienceEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiActorId):
            self.id = AiActorId(self.id)

        if not isinstance(self.actor_task, list):
            self.actor_task = [self.actor_task] if self.actor_task is not None else []
        self.actor_task = [v if isinstance(v, AiActorTaskEnum) else AiActorTaskEnum(v) for v in self.actor_task]

        if not isinstance(self.lifecycle_stage, list):
            self.lifecycle_stage = [self.lifecycle_stage] if self.lifecycle_stage is not None else []
        self.lifecycle_stage = [v if isinstance(v, AiLifecycleStageEnum) else AiLifecycleStageEnum(v) for v in self.lifecycle_stage]

        if self.is_tevv is not None and not isinstance(self.is_tevv, Bool):
            self.is_tevv = Bool(self.is_tevv)

        if self.audience is not None and not isinstance(self.audience, AudienceEnum):
            self.audience = AudienceEnum(self.audience)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiActorTask(NamedThing):
    """
    A category of task performed by AI actors (Appendix A). Each
    task is associated with one or more lifecycle stages and a
    typical set of actor roles.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiActorTask"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiActorTask"
    class_name: ClassVar[str] = "AiActorTask"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiActorTask

    id: Union[str, AiActorTaskId] = None
    task_kind: Union[str, "AiActorTaskEnum"] = None
    typical_actors: Optional[Union[str, list[str]]] = empty_list()
    lifecycle_stage: Optional[Union[Union[str, "AiLifecycleStageEnum"], list[Union[str, "AiLifecycleStageEnum"]]]] = empty_list()
    ai_dimension: Optional[Union[Union[str, "AiSystemDimensionEnum"], list[Union[str, "AiSystemDimensionEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiActorTaskId):
            self.id = AiActorTaskId(self.id)

        if self._is_empty(self.task_kind):
            self.MissingRequiredField("task_kind")
        if not isinstance(self.task_kind, AiActorTaskEnum):
            self.task_kind = AiActorTaskEnum(self.task_kind)

        if not isinstance(self.typical_actors, list):
            self.typical_actors = [self.typical_actors] if self.typical_actors is not None else []
        self.typical_actors = [v if isinstance(v, str) else str(v) for v in self.typical_actors]

        if not isinstance(self.lifecycle_stage, list):
            self.lifecycle_stage = [self.lifecycle_stage] if self.lifecycle_stage is not None else []
        self.lifecycle_stage = [v if isinstance(v, AiLifecycleStageEnum) else AiLifecycleStageEnum(v) for v in self.lifecycle_stage]

        if not isinstance(self.ai_dimension, list):
            self.ai_dimension = [self.ai_dimension] if self.ai_dimension is not None else []
        self.ai_dimension = [v if isinstance(v, AiSystemDimensionEnum) else AiSystemDimensionEnum(v) for v in self.ai_dimension]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Risk(NamedThing):
    """
    The composite measure of an event's probability of occurring and
    the magnitude or degree of the consequences of that event. When
    considering negative impact, risk is a function of (1) the
    negative impact or magnitude of harm and (2) the likelihood of
    occurrence (Adapted from ISO 31000:2018; OMB Circular A-130:2016).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Risk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Risk"
    class_name: ClassVar[str] = "Risk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.Risk

    id: Union[str, RiskId] = None
    likelihood: Optional[float] = None
    magnitude: Optional[str] = None
    impact_sign: Optional[Union[str, "ImpactSignEnum"]] = None
    is_residual: Optional[Union[bool, Bool]] = None
    risk_response: Optional[Union[str, "RiskResponseEnum"]] = None
    lifecycle_stage: Optional[Union[Union[str, "AiLifecycleStageEnum"], list[Union[str, "AiLifecycleStageEnum"]]]] = empty_list()
    trustworthiness_characteristic: Optional[Union[Union[str, "TrustworthinessCharacteristicEnum"], list[Union[str, "TrustworthinessCharacteristicEnum"]]]] = empty_list()
    related_impacts: Optional[Union[dict[Union[str, ImpactId], Union[dict, "Impact"]], list[Union[dict, "Impact"]]]] = empty_dict()
    affects_system: Optional[Union[str, AiSystemId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskId):
            self.id = RiskId(self.id)

        if self.likelihood is not None and not isinstance(self.likelihood, float):
            self.likelihood = float(self.likelihood)

        if self.magnitude is not None and not isinstance(self.magnitude, str):
            self.magnitude = str(self.magnitude)

        if self.impact_sign is not None and not isinstance(self.impact_sign, ImpactSignEnum):
            self.impact_sign = ImpactSignEnum(self.impact_sign)

        if self.is_residual is not None and not isinstance(self.is_residual, Bool):
            self.is_residual = Bool(self.is_residual)

        if self.risk_response is not None and not isinstance(self.risk_response, RiskResponseEnum):
            self.risk_response = RiskResponseEnum(self.risk_response)

        if not isinstance(self.lifecycle_stage, list):
            self.lifecycle_stage = [self.lifecycle_stage] if self.lifecycle_stage is not None else []
        self.lifecycle_stage = [v if isinstance(v, AiLifecycleStageEnum) else AiLifecycleStageEnum(v) for v in self.lifecycle_stage]

        if not isinstance(self.trustworthiness_characteristic, list):
            self.trustworthiness_characteristic = [self.trustworthiness_characteristic] if self.trustworthiness_characteristic is not None else []
        self.trustworthiness_characteristic = [v if isinstance(v, TrustworthinessCharacteristicEnum) else TrustworthinessCharacteristicEnum(v) for v in self.trustworthiness_characteristic]

        self._normalize_inlined_as_list(slot_name="related_impacts", slot_type=Impact, key_name="id", keyed=True)

        if self.affects_system is not None and not isinstance(self.affects_system, AiSystemId):
            self.affects_system = AiSystemId(self.affects_system)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Impact(NamedThing):
    """
    A positive, negative, or both consequence of an AI system. Impacts
    can manifest as opportunities (positive) or threats (negative).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Impact"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Impact"
    class_name: ClassVar[str] = "Impact"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.Impact

    id: Union[str, ImpactId] = None
    impact_sign: Optional[Union[str, "ImpactSignEnum"]] = None
    magnitude: Optional[str] = None
    likelihood: Optional[float] = None
    affects: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ImpactId):
            self.id = ImpactId(self.id)

        if self.impact_sign is not None and not isinstance(self.impact_sign, ImpactSignEnum):
            self.impact_sign = ImpactSignEnum(self.impact_sign)

        if self.magnitude is not None and not isinstance(self.magnitude, str):
            self.magnitude = str(self.magnitude)

        if self.likelihood is not None and not isinstance(self.likelihood, float):
            self.likelihood = float(self.likelihood)

        if not isinstance(self.affects, list):
            self.affects = [self.affects] if self.affects is not None else []
        self.affects = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.affects]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Harm(NamedThing):
    """
    A negative impact that may be experienced by individuals,
    groups, communities, organizations, society, the environment, or
    the planet (Figure 1).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Harm"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Harm"
    class_name: ClassVar[str] = "Harm"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.Harm

    id: Union[str, HarmId] = None
    harm_category: Optional[Union[str, "HarmCategoryEnum"]] = None
    harm_to_people_subcategory: Optional[Union[str, "HarmToPeopleSubcategoryEnum"]] = None
    magnitude: Optional[str] = None
    affects: Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HarmId):
            self.id = HarmId(self.id)

        if self.harm_category is not None and not isinstance(self.harm_category, HarmCategoryEnum):
            self.harm_category = HarmCategoryEnum(self.harm_category)

        if self.harm_to_people_subcategory is not None and not isinstance(self.harm_to_people_subcategory, HarmToPeopleSubcategoryEnum):
            self.harm_to_people_subcategory = HarmToPeopleSubcategoryEnum(self.harm_to_people_subcategory)

        if self.magnitude is not None and not isinstance(self.magnitude, str):
            self.magnitude = str(self.magnitude)

        if not isinstance(self.affects, list):
            self.affects = [self.affects] if self.affects is not None else []
        self.affects = [v if isinstance(v, NamedThingId) else NamedThingId(v) for v in self.affects]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class ResidualRisk(Risk):
    """
    Risk remaining after risk treatment (ISO Guide 73). Documenting
    residual risks helps system providers consider risks of deploying
    the AI product and informs end users about potential negative
    impacts.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["ResidualRisk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:ResidualRisk"
    class_name: ClassVar[str] = "ResidualRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.ResidualRisk

    id: Union[str, ResidualRiskId] = None
    is_residual: Optional[Union[bool, Bool]] = True

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, ResidualRiskId):
            self.id = ResidualRiskId(self.id)

        if self.is_residual is not None and not isinstance(self.is_residual, Bool):
            self.is_residual = Bool(self.is_residual)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskTolerance(NamedThing):
    """
    The organization's or AI actor's readiness to bear risk in order
    to achieve its objectives (Adapted from ISO Guide 73). Risk
    tolerance is highly contextual and application- and use-case
    specific.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["RiskTolerance"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:RiskTolerance"
    class_name: ClassVar[str] = "RiskTolerance"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.RiskTolerance

    id: Union[str, RiskToleranceId] = None
    tolerance_statement: Optional[str] = None
    legal_basis: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskToleranceId):
            self.id = RiskToleranceId(self.id)

        if self.tolerance_statement is not None and not isinstance(self.tolerance_statement, str):
            self.tolerance_statement = str(self.tolerance_statement)

        if self.legal_basis is not None and not isinstance(self.legal_basis, str):
            self.legal_basis = str(self.legal_basis)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RiskMeasurementChallenge(NamedThing):
    """
    A challenge that complicates measurement of AI risks
    (Part 1 §1.2.1).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["RiskMeasurementChallenge"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:RiskMeasurementChallenge"
    class_name: ClassVar[str] = "RiskMeasurementChallenge"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.RiskMeasurementChallenge

    id: Union[str, RiskMeasurementChallengeId] = None
    challenge_kind: Union[str, "RiskMeasurementChallengeEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RiskMeasurementChallengeId):
            self.id = RiskMeasurementChallengeId(self.id)

        if self._is_empty(self.challenge_kind):
            self.MissingRequiredField("challenge_kind")
        if not isinstance(self.challenge_kind, RiskMeasurementChallengeEnum):
            self.challenge_kind = RiskMeasurementChallengeEnum(self.challenge_kind)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class TrustworthinessCharacteristic(NamedThing):
    """
    A characteristic of a trustworthy AI system (Figure 4 / Part 1
    §3). The seven characteristics are inter-related; addressing them
    individually does not guarantee trustworthiness, and tradeoffs
    are usually involved.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["TrustworthinessCharacteristic"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:TrustworthinessCharacteristic"
    class_name: ClassVar[str] = "TrustworthinessCharacteristic"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.TrustworthinessCharacteristic

    id: Union[str, TrustworthinessCharacteristicId] = None
    characteristic_kind: Union[str, "TrustworthinessCharacteristicEnum"] = None
    is_base_condition: Optional[Union[bool, Bool]] = None
    is_cross_cutting: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, TrustworthinessCharacteristicId):
            self.id = TrustworthinessCharacteristicId(self.id)

        if self._is_empty(self.characteristic_kind):
            self.MissingRequiredField("characteristic_kind")
        if not isinstance(self.characteristic_kind, TrustworthinessCharacteristicEnum):
            self.characteristic_kind = TrustworthinessCharacteristicEnum(self.characteristic_kind)

        if self.is_base_condition is not None and not isinstance(self.is_base_condition, Bool):
            self.is_base_condition = Bool(self.is_base_condition)

        if self.is_cross_cutting is not None and not isinstance(self.is_cross_cutting, Bool):
            self.is_cross_cutting = Bool(self.is_cross_cutting)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Bias(NamedThing):
    """
    A form of AI bias - a deviation that may be perpetuated or
    amplified by AI systems. NIST identifies three major categories:
    systemic, computational/statistical, and human-cognitive
    (Part 1 §3.7; NIST SP 1270).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Bias"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Bias"
    class_name: ClassVar[str] = "Bias"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.Bias

    id: Union[str, BiasId] = None
    bias_category: Optional[Union[Union[str, "BiasCategoryEnum"], list[Union[str, "BiasCategoryEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, BiasId):
            self.id = BiasId(self.id)

        if not isinstance(self.bias_category, list):
            self.bias_category = [self.bias_category] if self.bias_category is not None else []
        self.bias_category = [v if isinstance(v, BiasCategoryEnum) else BiasCategoryEnum(v) for v in self.bias_category]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Function(NamedThing):
    """
    A top-level AI RMF Core function. Each function organizes AI risk
    management activities at the highest level. GOVERN applies across
    all stages; MAP, MEASURE, and MANAGE apply to AI-system-specific
    contexts and lifecycle stages.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Function"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Function"
    class_name: ClassVar[str] = "Function"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.Function

    id: Union[str, FunctionId] = None
    function_code: Union[str, FunctionCode] = None
    categories: Optional[Union[dict[Union[str, CategoryId], Union[dict, "Category"]], list[Union[dict, "Category"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, FunctionId):
            self.id = FunctionId(self.id)

        if self._is_empty(self.function_code):
            self.MissingRequiredField("function_code")
        if not isinstance(self.function_code, FunctionCode):
            self.function_code = FunctionCode(self.function_code)

        self._normalize_inlined_as_list(slot_name="categories", slot_type=Category, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Category(NamedThing):
    """
    A category within an AI RMF Core function (e.g., "GOVERN 1:
    Policies, processes, procedures, and practices ... are in place,
    transparent, and implemented effectively"). Categories group
    related subcategories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Category"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Category"
    class_name: ClassVar[str] = "Category"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.Category

    id: Union[str, CategoryId] = None
    category_id: Optional[Union[str, CategoryCode]] = None
    outcome: Optional[str] = None
    subcategories: Optional[Union[dict[Union[str, SubcategoryId], Union[dict, "Subcategory"]], list[Union[dict, "Subcategory"]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, CategoryId):
            self.id = CategoryId(self.id)

        if self.category_id is not None and not isinstance(self.category_id, CategoryCode):
            self.category_id = CategoryCode(self.category_id)

        if self.outcome is not None and not isinstance(self.outcome, str):
            self.outcome = str(self.outcome)

        self._normalize_inlined_as_list(slot_name="subcategories", slot_type=Subcategory, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class Subcategory(NamedThing):
    """
    A subcategory within an AI RMF Core category (e.g., "GOVERN 1.1:
    Legal and regulatory requirements involving AI are understood,
    managed, and documented"). Subcategories express specific
    outcomes.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Subcategory"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Subcategory"
    class_name: ClassVar[str] = "Subcategory"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.Subcategory

    id: Union[str, SubcategoryId] = None
    subcategory_id: Optional[Union[str, SubcategoryCode]] = None
    outcome: Optional[str] = None
    trustworthiness_characteristic: Optional[Union[Union[str, "TrustworthinessCharacteristicEnum"], list[Union[str, "TrustworthinessCharacteristicEnum"]]]] = empty_list()
    lifecycle_stage: Optional[Union[Union[str, "AiLifecycleStageEnum"], list[Union[str, "AiLifecycleStageEnum"]]]] = empty_list()
    about_text: Optional[str] = None
    suggested_actions_text: Optional[str] = None
    documentation_questions: Optional[str] = None
    references_text: Optional[str] = None
    topics: Optional[Union[str, list[str]]] = empty_list()
    ai_actor_categories: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SubcategoryId):
            self.id = SubcategoryId(self.id)

        if self.subcategory_id is not None and not isinstance(self.subcategory_id, SubcategoryCode):
            self.subcategory_id = SubcategoryCode(self.subcategory_id)

        if self.outcome is not None and not isinstance(self.outcome, str):
            self.outcome = str(self.outcome)

        if not isinstance(self.trustworthiness_characteristic, list):
            self.trustworthiness_characteristic = [self.trustworthiness_characteristic] if self.trustworthiness_characteristic is not None else []
        self.trustworthiness_characteristic = [v if isinstance(v, TrustworthinessCharacteristicEnum) else TrustworthinessCharacteristicEnum(v) for v in self.trustworthiness_characteristic]

        if not isinstance(self.lifecycle_stage, list):
            self.lifecycle_stage = [self.lifecycle_stage] if self.lifecycle_stage is not None else []
        self.lifecycle_stage = [v if isinstance(v, AiLifecycleStageEnum) else AiLifecycleStageEnum(v) for v in self.lifecycle_stage]

        if self.about_text is not None and not isinstance(self.about_text, str):
            self.about_text = str(self.about_text)

        if self.suggested_actions_text is not None and not isinstance(self.suggested_actions_text, str):
            self.suggested_actions_text = str(self.suggested_actions_text)

        if self.documentation_questions is not None and not isinstance(self.documentation_questions, str):
            self.documentation_questions = str(self.documentation_questions)

        if self.references_text is not None and not isinstance(self.references_text, str):
            self.references_text = str(self.references_text)

        if not isinstance(self.topics, list):
            self.topics = [self.topics] if self.topics is not None else []
        self.topics = [v if isinstance(v, str) else str(v) for v in self.topics]

        if not isinstance(self.ai_actor_categories, list):
            self.ai_actor_categories = [self.ai_actor_categories] if self.ai_actor_categories is not None else []
        self.ai_actor_categories = [v if isinstance(v, str) else str(v) for v in self.ai_actor_categories]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfProfile(NamedThing):
    """
    An implementation of the AI RMF Functions, Categories, and
    Subcategories for a specific setting or application based on the
    requirements, risk tolerance, and resources of the user (§6).
    Profiles may be use-case-specific, temporal (current or target),
    or cross-sectoral.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiRmfProfile"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiRmfProfile"
    class_name: ClassVar[str] = "AiRmfProfile"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfProfile

    id: Union[str, AiRmfProfileId] = None
    profile_type: Union[str, "ProfileTypeEnum"] = None
    current_state: Optional[str] = None
    target_state: Optional[str] = None
    sector: Optional[str] = None
    addresses: Optional[Union[Union[str, SubcategoryId], list[Union[str, SubcategoryId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiRmfProfileId):
            self.id = AiRmfProfileId(self.id)

        if self._is_empty(self.profile_type):
            self.MissingRequiredField("profile_type")
        if not isinstance(self.profile_type, ProfileTypeEnum):
            self.profile_type = ProfileTypeEnum(self.profile_type)

        if self.current_state is not None and not isinstance(self.current_state, str):
            self.current_state = str(self.current_state)

        if self.target_state is not None and not isinstance(self.target_state, str):
            self.target_state = str(self.target_state)

        if self.sector is not None and not isinstance(self.sector, str):
            self.sector = str(self.sector)

        if not isinstance(self.addresses, list):
            self.addresses = [self.addresses] if self.addresses is not None else []
        self.addresses = [v if isinstance(v, SubcategoryId) else SubcategoryId(v) for v in self.addresses]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class RmfAttribute(NamedThing):
    """
    A design attribute of the AI RMF (Appendix D) - one of the
    qualities the Framework strives to embody (e.g., risk-based,
    consensus-driven, plain language, common language, easily usable,
    universally applicable, outcome-focused, leveraging existing
    standards, law- and regulation-agnostic, living document).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["RmfAttribute"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:RmfAttribute"
    class_name: ClassVar[str] = "RmfAttribute"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.RmfAttribute

    id: Union[str, RmfAttributeId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, RmfAttributeId):
            self.id = RmfAttributeId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiSpecificRisk(NamedThing):
    """
    A risk that is new or increased for AI-based technology compared
    to traditional software (Appendix B) - e.g., data quality, model
    drift, opacity, scale and complexity, pre-trained model
    uncertainty, emergent properties, privacy aggregation, or
    environmental cost.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiSpecificRisk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiSpecificRisk"
    class_name: ClassVar[str] = "AiSpecificRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiSpecificRisk

    id: Union[str, AiSpecificRiskId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiSpecificRiskId):
            self.id = AiSpecificRiskId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class HumanAiInteractionIssue(NamedThing):
    """
    An issue that merits further consideration in human-AI
    interaction (Appendix C) - e.g., clear human roles and
    responsibilities, systemic and human-cognitive biases in design,
    variability of human-AI interaction outcomes, complexity of
    presenting AI system information to humans.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["HumanAiInteractionIssue"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:HumanAiInteractionIssue"
    class_name: ClassVar[str] = "HumanAiInteractionIssue"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.HumanAiInteractionIssue

    id: Union[str, HumanAiInteractionIssueId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, HumanAiInteractionIssueId):
            self.id = HumanAiInteractionIssueId(self.id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfDocument(NamedThing):
    """
    Publication metadata for an instance of the AI RMF (e.g., NIST
    AI 100-1, January 2023). The Framework is intended to be a
    living document, employing a two-number versioning system (major.minor).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiRmfDocument"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiRmfDocument"
    class_name: ClassVar[str] = "AiRmfDocument"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfDocument

    id: Union[str, AiRmfDocumentId] = None
    version: Optional[str] = None
    publisher: Optional[str] = None
    doi: Optional[Union[str, URIorCURIE]] = None
    published_date: Optional[Union[str, XSDDate]] = None
    source: Optional[Union[str, URIorCURIE]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiRmfDocumentId):
            self.id = AiRmfDocumentId(self.id)

        if self.version is not None and not isinstance(self.version, str):
            self.version = str(self.version)

        if self.publisher is not None and not isinstance(self.publisher, str):
            self.publisher = str(self.publisher)

        if self.doi is not None and not isinstance(self.doi, URIorCURIE):
            self.doi = URIorCURIE(self.doi)

        if self.published_date is not None and not isinstance(self.published_date, XSDDate):
            self.published_date = XSDDate(self.published_date)

        if self.source is not None and not isinstance(self.source, URIorCURIE):
            self.source = URIorCURIE(self.source)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfFramework(NamedThing):
    """
    Root container that bundles the AI RMF Core (Functions) with
    foundational concepts (trustworthiness characteristics,
    lifecycle, actors, risks, harms), profiles, and Framework
    attributes. Designed for serialising the Framework or a tailored
    instance of it as a single JSON / YAML document.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiRmfFramework"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiRmfFramework"
    class_name: ClassVar[str] = "AiRmfFramework"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfFramework

    id: Union[str, AiRmfFrameworkId] = None
    document: Optional[Union[dict, AiRmfDocument]] = None
    functions: Optional[Union[dict[Union[str, FunctionId], Union[dict, Function]], list[Union[dict, Function]]]] = empty_dict()
    trustworthiness_characteristics: Optional[Union[dict[Union[str, TrustworthinessCharacteristicId], Union[dict, TrustworthinessCharacteristic]], list[Union[dict, TrustworthinessCharacteristic]]]] = empty_dict()
    lifecycle_stages: Optional[Union[dict[Union[str, AiLifecycleStageId], Union[dict, AiLifecycleStage]], list[Union[dict, AiLifecycleStage]]]] = empty_dict()
    dimensions: Optional[Union[dict[Union[str, AiSystemDimensionId], Union[dict, AiSystemDimension]], list[Union[dict, AiSystemDimension]]]] = empty_dict()
    actor_tasks: Optional[Union[dict[Union[str, AiActorTaskId], Union[dict, AiActorTask]], list[Union[dict, AiActorTask]]]] = empty_dict()
    profiles: Optional[Union[dict[Union[str, AiRmfProfileId], Union[dict, AiRmfProfile]], list[Union[dict, AiRmfProfile]]]] = empty_dict()
    attributes: Optional[Union[dict[Union[str, RmfAttributeId], Union[dict, RmfAttribute]], list[Union[dict, RmfAttribute]]]] = empty_dict()
    risk_measurement_challenges: Optional[Union[dict[Union[str, RiskMeasurementChallengeId], Union[dict, RiskMeasurementChallenge]], list[Union[dict, RiskMeasurementChallenge]]]] = empty_dict()
    ai_specific_risks: Optional[Union[dict[Union[str, AiSpecificRiskId], Union[dict, AiSpecificRisk]], list[Union[dict, AiSpecificRisk]]]] = empty_dict()
    human_ai_interaction_issues: Optional[Union[dict[Union[str, HumanAiInteractionIssueId], Union[dict, HumanAiInteractionIssue]], list[Union[dict, HumanAiInteractionIssue]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiRmfFrameworkId):
            self.id = AiRmfFrameworkId(self.id)

        if self.document is not None and not isinstance(self.document, AiRmfDocument):
            self.document = AiRmfDocument(**as_dict(self.document))

        self._normalize_inlined_as_list(slot_name="functions", slot_type=Function, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="trustworthiness_characteristics", slot_type=TrustworthinessCharacteristic, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="lifecycle_stages", slot_type=AiLifecycleStage, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="dimensions", slot_type=AiSystemDimension, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="actor_tasks", slot_type=AiActorTask, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="profiles", slot_type=AiRmfProfile, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="attributes", slot_type=RmfAttribute, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="risk_measurement_challenges", slot_type=RiskMeasurementChallenge, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="ai_specific_risks", slot_type=AiSpecificRisk, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="human_ai_interaction_issues", slot_type=HumanAiInteractionIssue, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiRisk(NamedThing):
    """
    A risk that is novel to or exacerbated by Generative AI.
    Each instance corresponds to one of the 12 risk categories
    enumerated in NIST AI 600-1 Section 2.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["GaiRisk"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:GaiRisk"
    class_name: ClassVar[str] = "GaiRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiRisk

    id: Union[str, GaiRiskId] = None
    gai_risk_kind: Optional[Union[str, "GaiRiskCategoryEnum"]] = None
    risk_categorization: Optional[Union[str, "GaiRiskCategorizationEnum"]] = None
    risk_scope: Optional[Union[Union[str, "GaiRiskScopeEnum"], list[Union[str, "GaiRiskScopeEnum"]]]] = empty_list()
    risk_sources: Optional[Union[Union[str, "GaiRiskSourceEnum"], list[Union[str, "GaiRiskSourceEnum"]]]] = empty_list()
    time_scale: Optional[Union[Union[str, "GaiRiskTimeScaleEnum"], list[Union[str, "GaiRiskTimeScaleEnum"]]]] = empty_list()
    trustworthiness_characteristic: Optional[Union[Union[str, "TrustworthinessCharacteristicEnum"], list[Union[str, "TrustworthinessCharacteristicEnum"]]]] = empty_list()
    addressed_by_actions: Optional[Union[Union[str, SuggestedActionId], list[Union[str, SuggestedActionId]]]] = empty_list()
    lifecycle_stage: Optional[Union[Union[str, "GaiLifecycleStageEnum"], list[Union[str, "GaiLifecycleStageEnum"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GaiRiskId):
            self.id = GaiRiskId(self.id)

        if self.gai_risk_kind is not None and not isinstance(self.gai_risk_kind, GaiRiskCategoryEnum):
            self.gai_risk_kind = GaiRiskCategoryEnum(self.gai_risk_kind)

        if self.risk_categorization is not None and not isinstance(self.risk_categorization, GaiRiskCategorizationEnum):
            self.risk_categorization = GaiRiskCategorizationEnum(self.risk_categorization)

        if not isinstance(self.risk_scope, list):
            self.risk_scope = [self.risk_scope] if self.risk_scope is not None else []
        self.risk_scope = [v if isinstance(v, GaiRiskScopeEnum) else GaiRiskScopeEnum(v) for v in self.risk_scope]

        if not isinstance(self.risk_sources, list):
            self.risk_sources = [self.risk_sources] if self.risk_sources is not None else []
        self.risk_sources = [v if isinstance(v, GaiRiskSourceEnum) else GaiRiskSourceEnum(v) for v in self.risk_sources]

        if not isinstance(self.time_scale, list):
            self.time_scale = [self.time_scale] if self.time_scale is not None else []
        self.time_scale = [v if isinstance(v, GaiRiskTimeScaleEnum) else GaiRiskTimeScaleEnum(v) for v in self.time_scale]

        if not isinstance(self.trustworthiness_characteristic, list):
            self.trustworthiness_characteristic = [self.trustworthiness_characteristic] if self.trustworthiness_characteristic is not None else []
        self.trustworthiness_characteristic = [v if isinstance(v, TrustworthinessCharacteristicEnum) else TrustworthinessCharacteristicEnum(v) for v in self.trustworthiness_characteristic]

        if not isinstance(self.addressed_by_actions, list):
            self.addressed_by_actions = [self.addressed_by_actions] if self.addressed_by_actions is not None else []
        self.addressed_by_actions = [v if isinstance(v, SuggestedActionId) else SuggestedActionId(v) for v in self.addressed_by_actions]

        if not isinstance(self.lifecycle_stage, list):
            self.lifecycle_stage = [self.lifecycle_stage] if self.lifecycle_stage is not None else []
        self.lifecycle_stage = [v if isinstance(v, GaiLifecycleStageEnum) else GaiLifecycleStageEnum(v) for v in self.lifecycle_stage]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class SuggestedAction(NamedThing):
    """
    A suggested action an organisation can take to manage GAI
    risks. Each action is identified by an Action ID, linked to an
    AI RMF subcategory, and may be relevant to one or more GAI
    risks and AI actor tasks (NIST AI 600-1 Section 3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["SuggestedAction"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:SuggestedAction"
    class_name: ClassVar[str] = "SuggestedAction"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.SuggestedAction

    id: Union[str, SuggestedActionId] = None
    action_id: Union[str, GaiActionId] = None
    function_prefix: Optional[Union[str, "GaiActionFunctionPrefixEnum"]] = None
    applies_to_subcategory: Optional[Union[str, SubcategoryCode]] = None
    gai_risks: Optional[Union[Union[str, "GaiRiskCategoryEnum"], list[Union[str, "GaiRiskCategoryEnum"]]]] = empty_list()
    actor_task: Optional[Union[Union[str, "GaiActorTaskEnum"], list[Union[str, "GaiActorTaskEnum"]]]] = empty_list()
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, SuggestedActionId):
            self.id = SuggestedActionId(self.id)

        if self._is_empty(self.action_id):
            self.MissingRequiredField("action_id")
        if not isinstance(self.action_id, GaiActionId):
            self.action_id = GaiActionId(self.action_id)

        if self.function_prefix is not None and not isinstance(self.function_prefix, GaiActionFunctionPrefixEnum):
            self.function_prefix = GaiActionFunctionPrefixEnum(self.function_prefix)

        if self.applies_to_subcategory is not None and not isinstance(self.applies_to_subcategory, SubcategoryCode):
            self.applies_to_subcategory = SubcategoryCode(self.applies_to_subcategory)

        if not isinstance(self.gai_risks, list):
            self.gai_risks = [self.gai_risks] if self.gai_risks is not None else []
        self.gai_risks = [v if isinstance(v, GaiRiskCategoryEnum) else GaiRiskCategoryEnum(v) for v in self.gai_risks]

        if not isinstance(self.actor_task, list):
            self.actor_task = [self.actor_task] if self.actor_task is not None else []
        self.actor_task = [v if isinstance(v, GaiActorTaskEnum) else GaiActorTaskEnum(v) for v in self.actor_task]

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class PrimaryGaiConsideration(NamedThing):
    """
    An overarching consideration derived from the NIST GAI PWG
    consultation process (Appendix A). The `consideration_kind`
    attribute discriminates between the four primary
    considerations: Governance, Pre-Deployment Testing, Content
    Provenance, and Incident Disclosure.

    All consideration-specific attributes are optional and apply
    to the appropriate `consideration_kind`:
    * GOVERNANCE: governance_practices, third_party_considerations
    * PRE_DEPLOYMENT_TESTING: limitations_of_current_approaches
    * CONTENT_PROVENANCE: provenance_techniques
    * INCIDENT_DISCLOSURE: ai_incident_definition
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["PrimaryGaiConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:PrimaryGaiConsideration"
    class_name: ClassVar[str] = "PrimaryGaiConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.PrimaryGaiConsideration

    id: Union[str, PrimaryGaiConsiderationId] = None
    consideration_kind: Union[str, "PrimaryConsiderationEnum"] = None
    governance_practices: Optional[Union[Union[str, "GovernancePracticeEnum"], list[Union[str, "GovernancePracticeEnum"]]]] = empty_list()
    third_party_considerations: Optional[str] = None
    limitations_of_current_approaches: Optional[str] = None
    provenance_techniques: Optional[Union[Union[str, "ProvenanceTechniqueEnum"], list[Union[str, "ProvenanceTechniqueEnum"]]]] = empty_list()
    ai_incident_definition: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, PrimaryGaiConsiderationId):
            self.id = PrimaryGaiConsiderationId(self.id)

        if self._is_empty(self.consideration_kind):
            self.MissingRequiredField("consideration_kind")
        if not isinstance(self.consideration_kind, PrimaryConsiderationEnum):
            self.consideration_kind = PrimaryConsiderationEnum(self.consideration_kind)

        if not isinstance(self.governance_practices, list):
            self.governance_practices = [self.governance_practices] if self.governance_practices is not None else []
        self.governance_practices = [v if isinstance(v, GovernancePracticeEnum) else GovernancePracticeEnum(v) for v in self.governance_practices]

        if self.third_party_considerations is not None and not isinstance(self.third_party_considerations, str):
            self.third_party_considerations = str(self.third_party_considerations)

        if self.limitations_of_current_approaches is not None and not isinstance(self.limitations_of_current_approaches, str):
            self.limitations_of_current_approaches = str(self.limitations_of_current_approaches)

        if not isinstance(self.provenance_techniques, list):
            self.provenance_techniques = [self.provenance_techniques] if self.provenance_techniques is not None else []
        self.provenance_techniques = [v if isinstance(v, ProvenanceTechniqueEnum) else ProvenanceTechniqueEnum(v) for v in self.provenance_techniques]

        if self.ai_incident_definition is not None and not isinstance(self.ai_incident_definition, str):
            self.ai_incident_definition = str(self.ai_incident_definition)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class StructuredPublicFeedback(NamedThing):
    """
    Methods used to evaluate whether GAI systems are performing as
    intended and to calibrate and verify traditional measurement
    methods (A.1.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["StructuredPublicFeedback"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:StructuredPublicFeedback"
    class_name: ClassVar[str] = "StructuredPublicFeedback"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.StructuredPublicFeedback

    id: Union[str, StructuredPublicFeedbackId] = None
    feedback_method_kind: Union[str, "StructuredFeedbackMethodEnum"] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, StructuredPublicFeedbackId):
            self.id = StructuredPublicFeedbackId(self.id)

        if self._is_empty(self.feedback_method_kind):
            self.MissingRequiredField("feedback_method_kind")
        if not isinstance(self.feedback_method_kind, StructuredFeedbackMethodEnum):
            self.feedback_method_kind = StructuredFeedbackMethodEnum(self.feedback_method_kind)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRedTeaming(StructuredPublicFeedback):
    """
    A structured testing exercise used to probe an AI system to
    find flaws and vulnerabilities such as inaccurate, harmful, or
    discriminatory outputs, often in a controlled environment and
    in collaboration with system developers (A.1.5).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["AiRedTeaming"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:AiRedTeaming"
    class_name: ClassVar[str] = "AiRedTeaming"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRedTeaming

    id: Union[str, AiRedTeamingId] = None
    feedback_method_kind: Union[str, "StructuredFeedbackMethodEnum"] = 'AI_RED_TEAMING'
    red_team_type: Optional[Union[str, "RedTeamingTypeEnum"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, AiRedTeamingId):
            self.id = AiRedTeamingId(self.id)

        if self._is_empty(self.feedback_method_kind):
            self.MissingRequiredField("feedback_method_kind")
        if not isinstance(self.feedback_method_kind, StructuredFeedbackMethodEnum):
            self.feedback_method_kind = StructuredFeedbackMethodEnum(self.feedback_method_kind)

        if self.red_team_type is not None and not isinstance(self.red_team_type, RedTeamingTypeEnum):
            self.red_team_type = RedTeamingTypeEnum(self.red_team_type)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiProfile(NamedThing):
    """
    Root container that bundles the NIST AI 600-1 Generative AI
    Profile: GAI risks (Section 2), suggested actions (Section 3),
    and primary considerations (Appendix A). The GAI Profile is a
    *cross-sectoral* AI RMF profile (Section 1).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["GaiProfile"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:GaiProfile"
    class_name: ClassVar[str] = "GaiProfile"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiProfile

    id: Union[str, GaiProfileId] = None
    gai_risk_catalog: Optional[Union[dict[Union[str, GaiRiskId], Union[dict, GaiRisk]], list[Union[dict, GaiRisk]]]] = empty_dict()
    suggested_actions: Optional[Union[dict[Union[str, SuggestedActionId], Union[dict, SuggestedAction]], list[Union[dict, SuggestedAction]]]] = empty_dict()
    primary_considerations: Optional[Union[dict[Union[str, PrimaryGaiConsiderationId], Union[dict, PrimaryGaiConsideration]], list[Union[dict, PrimaryGaiConsideration]]]] = empty_dict()
    structured_feedback_methods: Optional[Union[dict[Union[str, StructuredPublicFeedbackId], Union[dict, StructuredPublicFeedback]], list[Union[dict, StructuredPublicFeedback]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GaiProfileId):
            self.id = GaiProfileId(self.id)

        self._normalize_inlined_as_list(slot_name="gai_risk_catalog", slot_type=GaiRisk, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="suggested_actions", slot_type=SuggestedAction, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="primary_considerations", slot_type=PrimaryGaiConsideration, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="structured_feedback_methods", slot_type=StructuredPublicFeedback, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


# Enumerations
class FunctionEnum(EnumDefinitionImpl):
    """
    The four high-level AI RMF Core functions. GOVERN is a
    cross-cutting function applied throughout; MAP, MEASURE, and MANAGE
    operate on specific AI systems and lifecycle stages.
    """
    GOVERN = PermissibleValue(
        text="GOVERN",
        description="""Cultivates and implements a culture of risk management; outlines
processes, documents, and organizational schemes that anticipate,
identify, and manage AI risks.""")
    MAP = PermissibleValue(
        text="MAP",
        description="""Establishes the context to frame risks related to an AI system;
identifies risks based on intended purposes, capabilities, and
contextual factors.""")
    MEASURE = PermissibleValue(
        text="MEASURE",
        description="""Employs quantitative, qualitative, or mixed-method tools to
analyze, assess, benchmark, and monitor AI risk and related impacts.""")
    MANAGE = PermissibleValue(
        text="MANAGE",
        description="""Allocates risk resources to mapped and measured risks on a
regular basis and as defined by the GOVERN function; risk
treatment includes plans to respond to, recover from, and
communicate about incidents or events.""")

    _defn = EnumDefinition(
        name="FunctionEnum",
        description="""The four high-level AI RMF Core functions. GOVERN is a
cross-cutting function applied throughout; MAP, MEASURE, and MANAGE
operate on specific AI systems and lifecycle stages.""",
    )

class CategoryEnum(EnumDefinitionImpl):
    """
    The AI RMF Core categories (Part 2, §5) - the second-level groupings
    within each Function, keyed by the compact "FUNCTION-N" code. Cross-
    framework alignments (EU AI Act, SOC 2, OWASP LLM/ASI, Microsoft AGT
    ATF) are attached as SSSOM mappings and are sourced from
    src/nist_ai_100_1/mappings/nist_ai_rmf.sssom.tsv.
    """
    _defn = EnumDefinition(
        name="CategoryEnum",
        description="""The AI RMF Core categories (Part 2, §5) - the second-level groupings
within each Function, keyed by the compact \"FUNCTION-N\" code. Cross-
framework alignments (EU AI Act, SOC 2, OWASP LLM/ASI, Microsoft AGT
ATF) are attached as SSSOM mappings and are sourced from
src/nist_ai_100_1/mappings/nist_ai_rmf.sssom.tsv.""",
    )

    @classmethod
    def _addvals(cls):
        setattr(cls, "GOVERN-1",
            PermissibleValue(
                text="GOVERN-1",
                description="""Policies, processes, procedures, and practices across the organization
related to the mapping, measuring, and managing of AI risks are in
place, transparent, and implemented effectively."""))
        setattr(cls, "GOVERN-2",
            PermissibleValue(
                text="GOVERN-2",
                description="""Accountability structures are in place so that the appropriate teams
and individuals are empowered, responsible, and trained for mapping,
measuring, and managing AI risks."""))
        setattr(cls, "GOVERN-3",
            PermissibleValue(
                text="GOVERN-3",
                description="""Workforce diversity, equity, inclusion, and accessibility processes
are prioritized in the mapping, measuring, and managing of AI risks
throughout the lifecycle."""))
        setattr(cls, "GOVERN-4",
            PermissibleValue(
                text="GOVERN-4",
                description="""Organizational teams are committed to a culture that considers and
communicates AI risk."""))
        setattr(cls, "GOVERN-5",
            PermissibleValue(
                text="GOVERN-5",
                description="Processes are in place for robust engagement with relevant AI actors."))
        setattr(cls, "GOVERN-6",
            PermissibleValue(
                text="GOVERN-6",
                description="""Policies and procedures are in place to address AI risks and benefits
arising from third-party software and data and other supply chain
issues."""))
        setattr(cls, "MAP-1",
            PermissibleValue(
                text="MAP-1",
                description="Context is established and understood."))
        setattr(cls, "MAP-2",
            PermissibleValue(
                text="MAP-2",
                description="Categorization of the AI system is performed."))
        setattr(cls, "MAP-3",
            PermissibleValue(
                text="MAP-3",
                description="""AI capabilities, targeted usage, goals, and expected benefits and
costs compared with appropriate benchmarks are understood."""))
        setattr(cls, "MAP-4",
            PermissibleValue(
                text="MAP-4",
                description="""Risks and benefits are mapped for all components of the AI system
including third-party software and data."""))
        setattr(cls, "MAP-5",
            PermissibleValue(
                text="MAP-5",
                description="""Impacts to individuals, groups, communities, organizations, and
society are characterized."""))
        setattr(cls, "MEASURE-1",
            PermissibleValue(
                text="MEASURE-1",
                description="Appropriate methods and metrics are identified and applied."))
        setattr(cls, "MEASURE-2",
            PermissibleValue(
                text="MEASURE-2",
                description="AI systems are evaluated for trustworthy characteristics."))
        setattr(cls, "MEASURE-3",
            PermissibleValue(
                text="MEASURE-3",
                description="Mechanisms for tracking identified AI risks over time are in place."))
        setattr(cls, "MEASURE-4",
            PermissibleValue(
                text="MEASURE-4",
                description="Feedback about efficacy of measurement is gathered and assessed."))
        setattr(cls, "MANAGE-1",
            PermissibleValue(
                text="MANAGE-1",
                description="""AI risks based on assessments and other analytical output from the MAP
and MEASURE functions are prioritized, responded to, and managed."""))
        setattr(cls, "MANAGE-2",
            PermissibleValue(
                text="MANAGE-2",
                description="""Strategies to maximize AI benefits and minimize negative impacts are
planned, prepared, implemented, documented, and informed by input from
relevant AI actors."""))
        setattr(cls, "MANAGE-3",
            PermissibleValue(
                text="MANAGE-3",
                description="AI risks and benefits from third-party entities are managed."))
        setattr(cls, "MANAGE-4",
            PermissibleValue(
                text="MANAGE-4",
                description="""Risk treatments, including response and recovery, and communication
plans for the identified and measured AI risks are documented and
monitored regularly."""))

class AiLifecycleStageEnum(EnumDefinitionImpl):
    """
    AI lifecycle stages as defined in Figure 2 (modified from
    OECD 2022). Each stage corresponds to one of the AI system
    dimensions (see AiSystemDimensionEnum).
    """
    PLAN_AND_DESIGN = PermissibleValue(
        text="PLAN_AND_DESIGN",
        description="""Articulate and document the system's concept and objectives,
underlying assumptions, context, and requirements (Application
Context dimension).""")
    COLLECT_AND_PROCESS_DATA = PermissibleValue(
        text="COLLECT_AND_PROCESS_DATA",
        description="""Gather, validate, and clean data and document the metadata and
characteristics of the dataset (Data and Input dimension).""")
    BUILD_AND_USE_MODEL = PermissibleValue(
        text="BUILD_AND_USE_MODEL",
        description="Create or select algorithms; train models (AI Model dimension).")
    VERIFY_AND_VALIDATE = PermissibleValue(
        text="VERIFY_AND_VALIDATE",
        description="""Verify, validate, calibrate, and interpret model output
(AI Model dimension).""")
    DEPLOY_AND_USE = PermissibleValue(
        text="DEPLOY_AND_USE",
        description="""Pilot; check compatibility with legacy systems; verify regulatory
compliance; manage organizational change; and evaluate user
experience (Task and Output dimension).""")
    OPERATE_AND_MONITOR = PermissibleValue(
        text="OPERATE_AND_MONITOR",
        description="""Operate the AI system and continuously assess its recommendations
and impacts (both intended and unintended) in light of objectives,
legal and regulatory requirements, and ethical considerations
(Application Context dimension).""")

    _defn = EnumDefinition(
        name="AiLifecycleStageEnum",
        description="""AI lifecycle stages as defined in Figure 2 (modified from
OECD 2022). Each stage corresponds to one of the AI system
dimensions (see AiSystemDimensionEnum).""",
    )

class AiSystemDimensionEnum(EnumDefinitionImpl):
    """
    Key socio-technical dimensions of an AI system (Figure 2).
    People and Planet sits at the centre representing human and
    societal well-being.
    """
    APPLICATION_CONTEXT = PermissibleValue(
        text="APPLICATION_CONTEXT",
        description="""The setting in which an AI system is deployed - includes legal,
regulatory, ethical, and societal considerations.""")
    DATA_AND_INPUT = PermissibleValue(
        text="DATA_AND_INPUT",
        description="""The data and inputs an AI system uses, including training,
validation, test data, and operational inputs.""")
    AI_MODEL = PermissibleValue(
        text="AI_MODEL",
        description="The model(s) and algorithms at the heart of an AI system.")
    TASK_AND_OUTPUT = PermissibleValue(
        text="TASK_AND_OUTPUT",
        description="""The task the AI system is designed to perform and the outputs
it produces (predictions, recommendations, decisions).""")
    PEOPLE_AND_PLANET = PermissibleValue(
        text="PEOPLE_AND_PLANET",
        description="""Human rights and the broader well-being of society and the
planet - centred in Figure 2.""")

    _defn = EnumDefinition(
        name="AiSystemDimensionEnum",
        description="""Key socio-technical dimensions of an AI system (Figure 2).
People and Planet sits at the centre representing human and
societal well-being.""",
    )

class AiActorTaskEnum(EnumDefinitionImpl):
    """
    Categories of AI actor tasks as described in Appendix A and
    illustrated in Figure 3.
    """
    AI_DESIGN = PermissibleValue(
        text="AI_DESIGN",
        description="""Performed during the Application Context and Data and Input
phases; create the concept and objectives of AI systems and are
responsible for planning, design, and data collection.""")
    AI_DEVELOPMENT = PermissibleValue(
        text="AI_DEVELOPMENT",
        description="""Performed during the AI Model phase; provide the initial
infrastructure of AI systems (model building, selection,
calibration, training, testing).""")
    AI_DEPLOYMENT = PermissibleValue(
        text="AI_DEPLOYMENT",
        description="""Performed during the Task and Output phase; responsible for
contextual decisions on how the AI system is used and for
assuring deployment into production.""")
    OPERATION_AND_MONITORING = PermissibleValue(
        text="OPERATION_AND_MONITORING",
        description="""Performed in the Application Context / Operate and Monitor
phase; operating the AI system and regularly assessing system
output and impacts.""")
    TEVV = PermissibleValue(
        text="TEVV",
        description="""Test, Evaluation, Verification, and Validation tasks performed
throughout the AI lifecycle; examine the AI system or its
components, and detect and remediate problems.""")
    HUMAN_FACTORS = PermissibleValue(
        text="HUMAN_FACTORS",
        description="""Human-centered design practices and methodologies; promoting
active involvement of end users and other interested parties;
incorporating context-specific norms and values.""")
    DOMAIN_EXPERT = PermissibleValue(
        text="DOMAIN_EXPERT",
        description="""Input from multidisciplinary practitioners or scholars who
provide knowledge or expertise in - and about - an industry
sector, context, or application area.""")
    AI_IMPACT_ASSESSMENT = PermissibleValue(
        text="AI_IMPACT_ASSESSMENT",
        description="""Assess and evaluate requirements for AI system accountability,
combat harmful bias, examine impacts, product safety, liability,
and security.""")
    PROCUREMENT = PermissibleValue(
        text="PROCUREMENT",
        description="""Conducted by AI actors with financial, legal, or policy
management authority for acquisition of AI models, products, or
services from a third party.""")
    GOVERNANCE_AND_OVERSIGHT = PermissibleValue(
        text="GOVERNANCE_AND_OVERSIGHT",
        description="""Assumed by AI actors with management, fiduciary, and legal
authority for the organization, including senior leadership and
the Board of Directors.""")
    THIRD_PARTY_ENTITIES = PermissibleValue(
        text="THIRD_PARTY_ENTITIES",
        description="""Providers, developers, vendors, and evaluators of data,
algorithms, models, and/or systems and related services external
to the deploying organization.""")
    END_USERS = PermissibleValue(
        text="END_USERS",
        description="""Individuals or groups that use the AI system for specific
purposes; range in competency from AI experts to first-time
users.""")
    AFFECTED_INDIVIDUALS_OR_COMMUNITIES = PermissibleValue(
        text="AFFECTED_INDIVIDUALS_OR_COMMUNITIES",
        description="""All individuals, groups, communities, or organizations directly
or indirectly affected by AI systems or decisions based on the
output of AI systems.""")
    OTHER_AI_ACTORS = PermissibleValue(
        text="OTHER_AI_ACTORS",
        description="""Provide formal or quasi-formal norms or guidance - includes
trade associations, standards developing organizations, advocacy
groups, researchers, environmental groups, and civil society
organizations.""")
    GENERAL_PUBLIC = PermissibleValue(
        text="GENERAL_PUBLIC",
        description="""Most likely to directly experience positive and negative impacts
of AI technologies; provides motivation for actions taken by
other AI actors.""")

    _defn = EnumDefinition(
        name="AiActorTaskEnum",
        description="""Categories of AI actor tasks as described in Appendix A and
illustrated in Figure 3.""",
    )

class HarmCategoryEnum(EnumDefinitionImpl):
    """
    High-level categories of harm related to AI systems (Figure 1).
    """
    HARM_TO_PEOPLE = PermissibleValue(
        text="HARM_TO_PEOPLE",
        description="""Harm to individuals, groups/communities, or society at large
(including civil liberties, rights, physical or psychological
safety, economic opportunity, democratic participation, and
educational access).""")
    HARM_TO_AN_ORGANIZATION = PermissibleValue(
        text="HARM_TO_AN_ORGANIZATION",
        description="""Harm to an organization's business operations, security
breaches or monetary loss, or reputation.""")
    HARM_TO_AN_ECOSYSTEM = PermissibleValue(
        text="HARM_TO_AN_ECOSYSTEM",
        description="""Harm to interconnected and interdependent elements and
resources, the global financial system, supply chain, natural
resources, the environment, and the planet.""")

    _defn = EnumDefinition(
        name="HarmCategoryEnum",
        description="High-level categories of harm related to AI systems (Figure 1).",
    )

class HarmToPeopleSubcategoryEnum(EnumDefinitionImpl):
    """
    Sub-categories of harm to people, per Figure 1.
    """
    INDIVIDUAL = PermissibleValue(
        text="INDIVIDUAL",
        description="""Harm to a person's civil liberties, rights, physical or
psychological safety, or economic opportunity.""")
    GROUP_OR_COMMUNITY = PermissibleValue(
        text="GROUP_OR_COMMUNITY",
        description="""Harm to a group such as discrimination against a population
sub-group.""")
    SOCIETAL = PermissibleValue(
        text="SOCIETAL",
        description="Harm to democratic participation or educational access.")

    _defn = EnumDefinition(
        name="HarmToPeopleSubcategoryEnum",
        description="Sub-categories of harm to people, per Figure 1.",
    )

class BiasCategoryEnum(EnumDefinitionImpl):
    """
    The three major categories of AI bias identified by NIST
    (Part 1 §3.7; see NIST SP 1270).
    """
    SYSTEMIC = PermissibleValue(
        text="SYSTEMIC",
        description="""Bias present in AI datasets, organizational norms, practices,
and processes across the AI lifecycle, and the broader society
that uses AI systems.""")
    COMPUTATIONAL_AND_STATISTICAL = PermissibleValue(
        text="COMPUTATIONAL_AND_STATISTICAL",
        description="""Bias present in AI datasets and algorithmic processes; often
stems from systematic errors due to non-representative samples.""")
    HUMAN_COGNITIVE = PermissibleValue(
        text="HUMAN_COGNITIVE",
        description="""Bias related to how an individual or group perceives AI system
information to make a decision or fill in missing information;
omnipresent in decision-making across the AI lifecycle.""")

    _defn = EnumDefinition(
        name="BiasCategoryEnum",
        description="""The three major categories of AI bias identified by NIST
(Part 1 §3.7; see NIST SP 1270).""",
    )

class RiskMeasurementChallengeEnum(EnumDefinitionImpl):
    """
    Challenges that complicate AI risk measurement (Part 1 §1.2.1).
    """
    THIRD_PARTY_SOFTWARE_HARDWARE_AND_DATA = PermissibleValue(
        text="THIRD_PARTY_SOFTWARE_HARDWARE_AND_DATA",
        description="""Risks related to third-party software, hardware, and data,
including misalignment of risk metrics or methodologies between
developers, deployers, and operators.""")
    TRACKING_EMERGENT_RISKS = PermissibleValue(
        text="TRACKING_EMERGENT_RISKS",
        description="""Identifying and tracking emergent risks and considering
techniques for measuring them; impact assessment helps
understand context-specific harms.""")
    AVAILABILITY_OF_RELIABLE_METRICS = PermissibleValue(
        text="AVAILABILITY_OF_RELIABLE_METRICS",
        description="""Lack of consensus on robust and verifiable measurement methods
for risk and trustworthiness, and their applicability to
different use cases.""")
    RISK_AT_DIFFERENT_LIFECYCLE_STAGES = PermissibleValue(
        text="RISK_AT_DIFFERENT_LIFECYCLE_STAGES",
        description="""Measuring risk at different stages may yield different results;
some risks may be latent and increase as systems adapt and
evolve.""")
    RISK_IN_REAL_WORLD_SETTINGS = PermissibleValue(
        text="RISK_IN_REAL_WORLD_SETTINGS",
        description="""Lab measurements may differ from risks that emerge in
operational, real-world settings.""")
    INSCRUTABILITY = PermissibleValue(
        text="INSCRUTABILITY",
        description="""Opaque systems with limited explainability or interpretability,
poor documentation, or inherent uncertainty complicate risk
measurement.""")
    HUMAN_BASELINE = PermissibleValue(
        text="HUMAN_BASELINE",
        description="""AI systems intended to augment or replace human activity
require a human baseline for comparison, which is difficult to
systematize.""")

    _defn = EnumDefinition(
        name="RiskMeasurementChallengeEnum",
        description="Challenges that complicate AI risk measurement (Part 1 §1.2.1).",
    )

class RiskResponseEnum(EnumDefinitionImpl):
    """
    Treatment options for AI risks (MANAGE 1.3).
    """
    MITIGATING = PermissibleValue(
        text="MITIGATING",
        description="Reducing the likelihood or magnitude of the risk.")
    TRANSFERRING = PermissibleValue(
        text="TRANSFERRING",
        description="Shifting the risk to another party (e.g., via insurance or contract).")
    AVOIDING = PermissibleValue(
        text="AVOIDING",
        description="Choosing not to engage in the activity that creates the risk.")
    ACCEPTING = PermissibleValue(
        text="ACCEPTING",
        description="Acknowledging the risk and taking no further action.")

    _defn = EnumDefinition(
        name="RiskResponseEnum",
        description="Treatment options for AI risks (MANAGE 1.3).",
    )

class ProfileTypeEnum(EnumDefinitionImpl):
    """
    Types of AI RMF Profile (§6).
    """
    USE_CASE = PermissibleValue(
        text="USE_CASE",
        description="""Implementation of the AI RMF Core for a specific setting or
application (e.g., a hiring profile, a fair housing profile).""")
    TEMPORAL_CURRENT = PermissibleValue(
        text="TEMPORAL_CURRENT",
        description="""Description of the current state of AI risk management
activities within a sector, industry, organization, or
application context.""")
    TEMPORAL_TARGET = PermissibleValue(
        text="TEMPORAL_TARGET",
        description="""Description of the desired or target state of AI risk
management activities.""")
    CROSS_SECTORAL = PermissibleValue(
        text="CROSS_SECTORAL",
        description="""Risks of models or applications used across use cases or
sectors (e.g., large language models, cloud-based services,
acquisition).""")

    _defn = EnumDefinition(
        name="ProfileTypeEnum",
        description="Types of AI RMF Profile (§6).",
    )

class AudienceEnum(EnumDefinitionImpl):
    """
    Audience categorisation for the AI RMF (Part 1 §2).
    """
    PRIMARY = PermissibleValue(
        text="PRIMARY",
        description="""AI actors who perform or manage the design, development,
deployment, evaluation, and use of AI systems and drive AI
risk management efforts.""")
    INFORMING = PermissibleValue(
        text="INFORMING",
        description="""AI actors in the People and Planet dimension who *inform* the
primary audience - trade associations, standards developers,
researchers, advocacy groups, civil society organisations,
end users, and impacted individuals or communities.""")

    _defn = EnumDefinition(
        name="AudienceEnum",
        description="Audience categorisation for the AI RMF (Part 1 §2).",
    )

class ImpactSignEnum(EnumDefinitionImpl):
    """
    Whether an impact of an AI system is positive, negative, or both
    (Part 1 §1.1).
    """
    POSITIVE = PermissibleValue(
        text="POSITIVE",
        description="A beneficial impact or opportunity.")
    NEGATIVE = PermissibleValue(
        text="NEGATIVE",
        description="A harmful impact or threat.")
    MIXED = PermissibleValue(
        text="MIXED",
        description="An impact that is both positive and negative.")

    _defn = EnumDefinition(
        name="ImpactSignEnum",
        description="""Whether an impact of an AI system is positive, negative, or both
(Part 1 §1.1).""",
    )

class GaiLifecycleStageEnum(EnumDefinitionImpl):
    """
    AI lifecycle stages enumerated in NIST AI 600-1 Section 2:
    "Risks can arise during design, development, deployment,
    operation, and/or decommissioning." Distinct from the six-stage
    `AiLifecycleStageEnum` of NIST AI 100-1 (see `related_mappings`).
    """
    DESIGN = PermissibleValue(
        text="DESIGN",
        description="Articulating system concept, objectives, requirements.")
    DEVELOPMENT = PermissibleValue(
        text="DEVELOPMENT",
        description="Building, training, and tuning the GAI model or system.")
    DEPLOYMENT = PermissibleValue(
        text="DEPLOYMENT",
        description="Placing the GAI system into a production environment.")
    OPERATION = PermissibleValue(
        text="OPERATION",
        description="Running and monitoring the GAI system in use.")
    DECOMMISSIONING = PermissibleValue(
        text="DECOMMISSIONING",
        description="Retiring or phasing out the GAI system.")

    _defn = EnumDefinition(
        name="GaiLifecycleStageEnum",
        description="""AI lifecycle stages enumerated in NIST AI 600-1 Section 2:
\"Risks can arise during design, development, deployment,
operation, and/or decommissioning.\" Distinct from the six-stage
`AiLifecycleStageEnum` of NIST AI 100-1 (see `related_mappings`).""",
    )

class GaiActorTaskEnum(EnumDefinitionImpl):
    """
    AI Actor Tasks referenced by the Suggested Actions tables in
    NIST AI 600-1 Section 3 (and defined in NIST AI 100-1
    Appendix A).
    """
    GOVERNANCE_AND_OVERSIGHT = PermissibleValue(
        text="GOVERNANCE_AND_OVERSIGHT",
        description="Management, fiduciary, and legal authority for the organization.")
    AI_DESIGN = PermissibleValue(
        text="AI_DESIGN",
        description="Concept, objectives, planning, design, and data collection.")
    AI_DEVELOPMENT = PermissibleValue(
        text="AI_DEVELOPMENT",
        description="Model building, selection, calibration, training, and testing.")
    AI_DEPLOYMENT = PermissibleValue(
        text="AI_DEPLOYMENT",
        description="Contextual decisions on how the AI system is used and deployed.")
    AI_IMPACT_ASSESSMENT = PermissibleValue(
        text="AI_IMPACT_ASSESSMENT",
        description="Assessing accountability, bias, impacts, safety, liability, security.")
    OPERATION_AND_MONITORING = PermissibleValue(
        text="OPERATION_AND_MONITORING",
        description="Operating the AI system and assessing system output and impacts.")
    TEVV = PermissibleValue(
        text="TEVV",
        description="Test, Evaluation, Verification, and Validation tasks.")
    DOMAIN_EXPERTS = PermissibleValue(
        text="DOMAIN_EXPERTS",
        description="Multidisciplinary practitioners with sector or context expertise.")
    END_USERS = PermissibleValue(
        text="END_USERS",
        description="Individuals or groups using the AI system for specific purposes.")
    HUMAN_FACTORS = PermissibleValue(
        text="HUMAN_FACTORS",
        description="Human-centered design practices and end-user involvement.")
    AFFECTED_INDIVIDUALS_AND_COMMUNITIES = PermissibleValue(
        text="AFFECTED_INDIVIDUALS_AND_COMMUNITIES",
        description="Individuals, groups, or communities directly or indirectly affected.")
    PROCUREMENT = PermissibleValue(
        text="PROCUREMENT",
        description="Acquisition of AI models, products, or services from third parties.")
    THIRD_PARTY_ENTITIES = PermissibleValue(
        text="THIRD_PARTY_ENTITIES",
        description="Providers, developers, vendors, and evaluators external to the deploying organization.")

    _defn = EnumDefinition(
        name="GaiActorTaskEnum",
        description="""AI Actor Tasks referenced by the Suggested Actions tables in
NIST AI 600-1 Section 3 (and defined in NIST AI 100-1
Appendix A).""",
    )

class GaiRiskCategoryEnum(EnumDefinitionImpl):
    """
    The 12 risks unique to or exacerbated by Generative AI as
    enumerated in NIST AI 600-1 Section 2.
    """
    CBRN_INFORMATION_OR_CAPABILITIES = PermissibleValue(
        text="CBRN_INFORMATION_OR_CAPABILITIES",
        description="""Eased access to or synthesis of materially nefarious
information or design capabilities related to chemical,
biological, radiological, or nuclear (CBRN) weapons or
other dangerous materials or agents.""")
    CONFABULATION = PermissibleValue(
        text="CONFABULATION",
        description="""The production of confidently stated but erroneous or
false content (colloquially \"hallucinations\" or
\"fabrications\") by which users may be misled or deceived.""")
    DANGEROUS_VIOLENT_OR_HATEFUL_CONTENT = PermissibleValue(
        text="DANGEROUS_VIOLENT_OR_HATEFUL_CONTENT",
        description="""Eased production of and access to violent, inciting,
radicalizing, or threatening content as well as
recommendations to carry out self-harm or conduct illegal
activities. Includes difficulty controlling public
exposure to hateful and disparaging or stereotyping
content.""")
    DATA_PRIVACY = PermissibleValue(
        text="DATA_PRIVACY",
        description="""Impacts due to leakage and unauthorized use, disclosure, or
de-anonymization of biometric, health, location, or other
personally identifiable information or sensitive data.""")
    ENVIRONMENTAL_IMPACTS = PermissibleValue(
        text="ENVIRONMENTAL_IMPACTS",
        description="""Impacts due to high compute resource utilization in
training or operating GAI models, and related outcomes that
may adversely impact ecosystems.""")
    HARMFUL_BIAS_OR_HOMOGENIZATION = PermissibleValue(
        text="HARMFUL_BIAS_OR_HOMOGENIZATION",
        description="""Amplification and exacerbation of historical, societal,
and systemic biases; performance disparities between
sub-groups or languages, possibly due to non-representative
training data, resulting in discrimination, amplification
of biases, or incorrect presumptions about performance;
undesired homogeneity that skews system or model outputs.""")
    HUMAN_AI_CONFIGURATION = PermissibleValue(
        text="HUMAN_AI_CONFIGURATION",
        description="""Arrangements of or interactions between a human and an AI
system which can result in the human inappropriately
anthropomorphising GAI systems or experiencing algorithmic
aversion, automation bias, over-reliance, or emotional
entanglement with GAI systems.""")
    INFORMATION_INTEGRITY = PermissibleValue(
        text="INFORMATION_INTEGRITY",
        description="""Lowered barrier to entry to generate and support the
exchange and consumption of content which may not
distinguish fact from opinion or fiction or acknowledge
uncertainties, or could be leveraged for large-scale
dis- and mis-information campaigns.""")
    INFORMATION_SECURITY = PermissibleValue(
        text="INFORMATION_SECURITY",
        description="""Lowered barriers for offensive cyber capabilities,
including via automated discovery and exploitation of
vulnerabilities; increased attack surface for targeted
cyberattacks, which may compromise a system's availability
or the confidentiality or integrity of training data,
code, or model weights.""")
    INTELLECTUAL_PROPERTY = PermissibleValue(
        text="INTELLECTUAL_PROPERTY",
        description="""Eased production or replication of alleged copyrighted,
trademarked, or licensed content without authorization
(possibly outside fair use); eased exposure of trade
secrets; or plagiarism or illegal replication.""")
    OBSCENE_DEGRADING_OR_ABUSIVE_CONTENT = PermissibleValue(
        text="OBSCENE_DEGRADING_OR_ABUSIVE_CONTENT",
        description="""Eased production of and access to obscene, degrading,
and/or abusive imagery which can cause harm, including
synthetic child sexual abuse material (CSAM) and
nonconsensual intimate images (NCII) of adults.""")
    VALUE_CHAIN_AND_COMPONENT_INTEGRATION = PermissibleValue(
        text="VALUE_CHAIN_AND_COMPONENT_INTEGRATION",
        description="""Non-transparent or untraceable integration of upstream
third-party components, including data that has been
improperly obtained or not processed and cleaned due to
increased automation from GAI; improper supplier vetting
across the AI lifecycle; or other issues that diminish
transparency or accountability for downstream users.""")

    _defn = EnumDefinition(
        name="GaiRiskCategoryEnum",
        description="""The 12 risks unique to or exacerbated by Generative AI as
enumerated in NIST AI 600-1 Section 2.""",
    )

class GaiRiskCategorizationEnum(EnumDefinitionImpl):
    """
    Higher-level grouping of GAI risks, derived from the UK's
    International Scientific Report on the Safety of Advanced AI
    (NIST AI 600-1 Section 2, footnote 5).
    """
    TECHNICAL_OR_MODEL_RISKS = PermissibleValue(
        text="TECHNICAL_OR_MODEL_RISKS",
        description="""Risks from malfunction. Examples include confabulation;
dangerous or violent recommendations; data privacy; value
chain and component integration; harmful bias and
homogenization.""")
    MISUSE_BY_HUMANS = PermissibleValue(
        text="MISUSE_BY_HUMANS",
        description="""Risks from malicious use. Examples include CBRN information
or capabilities; data privacy; human-AI configuration;
obscene, degrading, and/or abusive content; information
integrity; information security.""")
    ECOSYSTEM_OR_SOCIETAL_RISKS = PermissibleValue(
        text="ECOSYSTEM_OR_SOCIETAL_RISKS",
        description="""Systemic risks. Examples include data privacy;
environmental impacts; intellectual property.""")

    _defn = EnumDefinition(
        name="GaiRiskCategorizationEnum",
        description="""Higher-level grouping of GAI risks, derived from the UK's
International Scientific Report on the Safety of Advanced AI
(NIST AI 600-1 Section 2, footnote 5).""",
    )

class GaiRiskScopeEnum(EnumDefinitionImpl):
    """
    The scope at which a GAI risk may manifest (Section 2).
    """
    MODEL_OR_SYSTEM = PermissibleValue(
        text="MODEL_OR_SYSTEM",
        description="Individual GAI model or system level.")
    APPLICATION_OR_IMPLEMENTATION = PermissibleValue(
        text="APPLICATION_OR_IMPLEMENTATION",
        description="""Specific application or implementation - i.e., a particular
use case.""")
    ECOSYSTEM = PermissibleValue(
        text="ECOSYSTEM",
        description="""Beyond a single system or organizational context - e.g.,
algorithmic monocultures, labor-market impacts, creative
economies.""")

    _defn = EnumDefinition(
        name="GaiRiskScopeEnum",
        description="The scope at which a GAI risk may manifest (Section 2).",
    )

class GaiRiskSourceEnum(EnumDefinitionImpl):
    """
    The source(s) from which a GAI risk may emerge (Section 2).
    """
    DESIGN = PermissibleValue(
        text="DESIGN",
        description="From decisions made during model or system design.")
    TRAINING = PermissibleValue(
        text="TRAINING",
        description="From the training data or training process.")
    OPERATION = PermissibleValue(
        text="OPERATION",
        description="From operating the GAI model or system.")
    MODEL_INPUTS = PermissibleValue(
        text="MODEL_INPUTS",
        description="From inputs supplied to the model at inference time.")
    MODEL_OUTPUTS = PermissibleValue(
        text="MODEL_OUTPUTS",
        description="From the GAI system's generated outputs.")
    HUMAN_BEHAVIOR = PermissibleValue(
        text="HUMAN_BEHAVIOR",
        description="""From human behaviour - abuse, misuse, or unsafe repurposing
by humans (adversarial or not).""")
    HUMAN_AI_INTERACTION = PermissibleValue(
        text="HUMAN_AI_INTERACTION",
        description="From interactions between a human and the AI system.")

    _defn = EnumDefinition(
        name="GaiRiskSourceEnum",
        description="The source(s) from which a GAI risk may emerge (Section 2).",
    )

class GaiRiskTimeScaleEnum(EnumDefinitionImpl):
    """
    The time scale over which a GAI risk may materialise
    (Section 2).
    """
    IMMEDIATE = PermissibleValue(
        text="IMMEDIATE",
        description="Materialises abruptly (e.g., distribution of deepfakes).")
    PROLONGED = PermissibleValue(
        text="PROLONGED",
        description="""Materialises across extended periods (e.g., long-term
effect of disinformation on societal trust).""")

    _defn = EnumDefinition(
        name="GaiRiskTimeScaleEnum",
        description="""The time scale over which a GAI risk may materialise
(Section 2).""",
    )

class GaiActionFunctionPrefixEnum(EnumDefinitionImpl):
    """
    Two-letter function prefix used in GAI Action IDs.
    """
    GV = PermissibleValue(
        text="GV",
        description="Govern function.")
    MP = PermissibleValue(
        text="MP",
        description="Map function.")
    MS = PermissibleValue(
        text="MS",
        description="Measure function.")
    MG = PermissibleValue(
        text="MG",
        description="Manage function.")

    _defn = EnumDefinition(
        name="GaiActionFunctionPrefixEnum",
        description="Two-letter function prefix used in GAI Action IDs.",
    )

class PrimaryConsiderationEnum(EnumDefinitionImpl):
    """
    The four overarching themes derived from the GAI PWG
    consultation process (Appendix A).
    """
    GOVERNANCE = PermissibleValue(
        text="GOVERNANCE",
        description="""How organizational governance regimes may be re-evaluated
and adjusted for GAI contexts (A.1).""")
    PRE_DEPLOYMENT_TESTING = PermissibleValue(
        text="PRE_DEPLOYMENT_TESTING",
        description="""Test, evaluation, validation, and verification practices
appropriate for GAI prior to deployment (A.1.4).""")
    CONTENT_PROVENANCE = PermissibleValue(
        text="CONTENT_PROVENANCE",
        description="""Digital transparency mechanisms (provenance data tracking,
watermarking, synthetic content detection) for tracing
origin and history of content (A.1.6 - A.1.7).""")
    INCIDENT_DISCLOSURE = PermissibleValue(
        text="INCIDENT_DISCLOSURE",
        description="""Documenting, reporting, and sharing information about AI
incidents to mitigate harm and improve risk management
(A.1.8).""")

    _defn = EnumDefinition(
        name="PrimaryConsiderationEnum",
        description="""The four overarching themes derived from the GAI PWG
consultation process (Appendix A).""",
    )

class StructuredFeedbackMethodEnum(EnumDefinitionImpl):
    """
    Categories of structured public feedback for GAI risk
    management (Appendix A.1.5).
    """
    PARTICIPATORY_ENGAGEMENT_METHODS = PermissibleValue(
        text="PARTICIPATORY_ENGAGEMENT_METHODS",
        description="""Methods used to solicit feedback from civil society groups,
affected communities, and users (focus groups, small user
studies, surveys).""")
    FIELD_TESTING = PermissibleValue(
        text="FIELD_TESTING",
        description="""Methods used to determine how people interact with,
consume, use, and make sense of AI-generated information
(UX, usability, randomised experiments).""")
    AI_RED_TEAMING = PermissibleValue(
        text="AI_RED_TEAMING",
        description="""A structured testing exercise used to probe an AI system
to find flaws and vulnerabilities such as inaccurate,
harmful, or discriminatory outputs.""")

    _defn = EnumDefinition(
        name="StructuredFeedbackMethodEnum",
        description="""Categories of structured public feedback for GAI risk
management (Appendix A.1.5).""",
    )

class RedTeamingTypeEnum(EnumDefinitionImpl):
    """
    Types of AI red-teaming exercises (Appendix A.1.5).
    """
    GENERAL_PUBLIC = PermissibleValue(
        text="GENERAL_PUBLIC",
        description="""Performed by general users not necessarily having AI or
technical expertise.""")
    EXPERT = PermissibleValue(
        text="EXPERT",
        description="""Performed by specialists with expertise in the domain or
specific red-teaming context (medicine, biotech,
cybersecurity).""")
    COMBINATION = PermissibleValue(
        text="COMBINATION",
        description="""Hybrid exercises using both expert and general-public
participants.""")
    HUMAN_AND_AI = PermissibleValue(
        text="HUMAN_AND_AI",
        description="""Performed by GAI in combination with specialist or
non-specialist human teams.""")

    _defn = EnumDefinition(
        name="RedTeamingTypeEnum",
        description="Types of AI red-teaming exercises (Appendix A.1.5).",
    )

class ProvenanceTechniqueEnum(EnumDefinitionImpl):
    """
    Provenance data tracking techniques for GAI content
    (Appendix A.1.6). "Some well-known techniques for provenance
    data tracking include digital watermarking, metadata
    recording, digital fingerprinting, and human authentication,
    among others."
    """
    DIGITAL_WATERMARKING = PermissibleValue(
        text="DIGITAL_WATERMARKING",
        description="""Overt or covert digital watermarks embedded in content to
allow downstream verification of origin.""")
    METADATA_RECORDING = PermissibleValue(
        text="METADATA_RECORDING",
        description="""Recording metadata about content (creator, date/time,
location, modifications, sources) for text, image, video,
audio, or underlying datasets.""")
    DIGITAL_FINGERPRINTING = PermissibleValue(
        text="DIGITAL_FINGERPRINTING",
        description="""Computing a content-derived identifier that can be matched
against a reference store to detect known content.""")
    HUMAN_AUTHENTICATION = PermissibleValue(
        text="HUMAN_AUTHENTICATION",
        description="""Human-mediated verification of content origin or
authenticity.""")

    _defn = EnumDefinition(
        name="ProvenanceTechniqueEnum",
        description="""Provenance data tracking techniques for GAI content
(Appendix A.1.6). \"Some well-known techniques for provenance
data tracking include digital watermarking, metadata
recording, digital fingerprinting, and human authentication,
among others.\"""",
    )

class GovernancePracticeEnum(EnumDefinitionImpl):
    """
    Governance plans and actions for GAI systems enumerated in
    NIST AI 600-1 Appendix A.1.2 ("Organizational Governance").
    """
    ACCESSIBILITY_AND_REASONABLE_ACCOMMODATIONS = PermissibleValue(
        text="ACCESSIBILITY_AND_REASONABLE_ACCOMMODATIONS",
        description="Accessibility and reasonable accommodations.")
    AI_ACTOR_CREDENTIALS_AND_QUALIFICATIONS = PermissibleValue(
        text="AI_ACTOR_CREDENTIALS_AND_QUALIFICATIONS",
        description="AI actor credentials and qualifications.")
    ALIGNMENT_TO_ORGANIZATIONAL_VALUES = PermissibleValue(
        text="ALIGNMENT_TO_ORGANIZATIONAL_VALUES",
        description="Alignment to organizational values.")
    AUDITING_AND_ASSESSMENT = PermissibleValue(
        text="AUDITING_AND_ASSESSMENT",
        description="Auditing and assessment.")
    CHANGE_MANAGEMENT_CONTROLS = PermissibleValue(
        text="CHANGE_MANAGEMENT_CONTROLS",
        description="Change-management controls.")
    COMMERCIAL_USE = PermissibleValue(
        text="COMMERCIAL_USE",
        description="Commercial use governance.")
    DATA_PROVENANCE = PermissibleValue(
        text="DATA_PROVENANCE",
        description="Data provenance.")
    DATA_PROTECTION = PermissibleValue(
        text="DATA_PROTECTION",
        description="Data protection.")
    DATA_RETENTION = PermissibleValue(
        text="DATA_RETENTION",
        description="Data retention.")
    CONSISTENCY_IN_USE_OF_DEFINING_KEY_TERMS = PermissibleValue(
        text="CONSISTENCY_IN_USE_OF_DEFINING_KEY_TERMS",
        description="Consistency in use of defining key terms.")
    DECOMMISSIONING = PermissibleValue(
        text="DECOMMISSIONING",
        description="Decommissioning practices.")
    DISCOURAGING_ANONYMOUS_USE = PermissibleValue(
        text="DISCOURAGING_ANONYMOUS_USE",
        description="Discouraging anonymous use.")
    EDUCATION = PermissibleValue(
        text="EDUCATION",
        description="Education on GAI risks and responsible use.")
    IMPACT_ASSESSMENTS = PermissibleValue(
        text="IMPACT_ASSESSMENTS",
        description="Impact assessments.")
    INCIDENT_RESPONSE = PermissibleValue(
        text="INCIDENT_RESPONSE",
        description="Incident response procedures.")
    MONITORING = PermissibleValue(
        text="MONITORING",
        description="Ongoing monitoring of GAI systems.")
    OPT_OUTS = PermissibleValue(
        text="OPT_OUTS",
        description="User opt-out mechanisms.")
    RISK_BASED_CONTROLS = PermissibleValue(
        text="RISK_BASED_CONTROLS",
        description="Risk-based controls.")
    RISK_MAPPING_AND_MEASUREMENT = PermissibleValue(
        text="RISK_MAPPING_AND_MEASUREMENT",
        description="Risk mapping and measurement.")
    SCIENCE_BACKED_TEVV_PRACTICES = PermissibleValue(
        text="SCIENCE_BACKED_TEVV_PRACTICES",
        description="Science-backed test, evaluation, validation, and verification practices.")
    SECURE_SOFTWARE_DEVELOPMENT_PRACTICES = PermissibleValue(
        text="SECURE_SOFTWARE_DEVELOPMENT_PRACTICES",
        description="Secure software development practices.")
    STAKEHOLDER_ENGAGEMENT = PermissibleValue(
        text="STAKEHOLDER_ENGAGEMENT",
        description="Stakeholder engagement.")
    SYNTHETIC_CONTENT_DETECTION_AND_LABELING = PermissibleValue(
        text="SYNTHETIC_CONTENT_DETECTION_AND_LABELING",
        description="Synthetic content detection and labeling tools and techniques.")
    WHISTLEBLOWER_PROTECTIONS = PermissibleValue(
        text="WHISTLEBLOWER_PROTECTIONS",
        description="Whistleblower protections.")
    WORKFORCE_DIVERSITY_AND_INTERDISCIPLINARY_TEAMS = PermissibleValue(
        text="WORKFORCE_DIVERSITY_AND_INTERDISCIPLINARY_TEAMS",
        description="Workforce diversity and interdisciplinary teams.")

    _defn = EnumDefinition(
        name="GovernancePracticeEnum",
        description="""Governance plans and actions for GAI systems enumerated in
NIST AI 600-1 Appendix A.1.2 (\"Organizational Governance\").""",
    )

class TrustworthinessCharacteristicEnum(EnumDefinitionImpl):
    """
    The seven characteristics of trustworthy AI systems described in
    Figure 4 and Part 1 §3.
    """
    VALID_AND_RELIABLE = PermissibleValue(
        text="VALID_AND_RELIABLE",
        description="""Confirmation that requirements for a specific intended use have
been fulfilled (validation) and that the system performs as
required without failure (reliability). A necessary condition of
trustworthiness and the base for other characteristics.""")
    SAFE = PermissibleValue(
        text="SAFE",
        description="""The system does not, under defined conditions, lead to a state
in which human life, health, property, or the environment is
endangered.""")
    SECURE_AND_RESILIENT = PermissibleValue(
        text="SECURE_AND_RESILIENT",
        description="""The system can withstand unexpected adverse events or changes
(resilient) and maintain confidentiality, integrity, and
availability through protection mechanisms (secure).""")
    ACCOUNTABLE_AND_TRANSPARENT = PermissibleValue(
        text="ACCOUNTABLE_AND_TRANSPARENT",
        description="""Trustworthy AI depends on accountability, which presupposes
transparency - the extent to which information about an AI
system and its outputs is available to those interacting with
it.""")
    EXPLAINABLE_AND_INTERPRETABLE = PermissibleValue(
        text="EXPLAINABLE_AND_INTERPRETABLE",
        description="""Explainability concerns the mechanisms underlying an AI system's
operation; interpretability concerns the meaning of its output
in context.""")
    PRIVACY_ENHANCED = PermissibleValue(
        text="PRIVACY_ENHANCED",
        description="""Norms and practices that help safeguard human autonomy,
identity, and dignity - including anonymity, confidentiality,
and control over personal information.""")
    FAIR_WITH_HARMFUL_BIAS_MANAGED = PermissibleValue(
        text="FAIR_WITH_HARMFUL_BIAS_MANAGED",
        description="""Concerns for equality and equity by addressing issues such as
harmful bias and discrimination, and recognising that
perceptions of fairness differ across cultures and
applications.""")

    _defn = EnumDefinition(
        name="TrustworthinessCharacteristicEnum",
        description="""The seven characteristics of trustworthy AI systems described in
Figure 4 and Part 1 §3.""",
    )

# Slots
class slots:
    pass

slots.source = Slot(uri=DCTERMS.source, name="source", curie=DCTERMS.curie('source'),
                   model_uri=NIST_AI_RMF.source, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.function_code = Slot(uri=NIST_AI_100_1.function_code, name="function_code", curie=NIST_AI_100_1.curie('function_code'),
                   model_uri=NIST_AI_RMF.function_code, domain=None, range=Union[str, FunctionCode])

slots.categories = Slot(uri=NIST_AI_100_1.categories, name="categories", curie=NIST_AI_100_1.curie('categories'),
                   model_uri=NIST_AI_RMF.categories, domain=None, range=Optional[Union[dict[Union[str, CategoryId], Union[dict, Category]], list[Union[dict, Category]]]])

slots.subcategories = Slot(uri=NIST_AI_100_1.subcategories, name="subcategories", curie=NIST_AI_100_1.curie('subcategories'),
                   model_uri=NIST_AI_RMF.subcategories, domain=None, range=Optional[Union[dict[Union[str, SubcategoryId], Union[dict, Subcategory]], list[Union[dict, Subcategory]]]])

slots.category_id = Slot(uri=NIST_AI_100_1.category_id, name="category_id", curie=NIST_AI_100_1.curie('category_id'),
                   model_uri=NIST_AI_RMF.category_id, domain=None, range=Optional[Union[str, CategoryCode]])

slots.subcategory_id = Slot(uri=NIST_AI_100_1.subcategory_id, name="subcategory_id", curie=NIST_AI_100_1.curie('subcategory_id'),
                   model_uri=NIST_AI_RMF.subcategory_id, domain=None, range=Optional[Union[str, SubcategoryCode]])

slots.outcome = Slot(uri=NIST_AI_100_1.outcome, name="outcome", curie=NIST_AI_100_1.curie('outcome'),
                   model_uri=NIST_AI_RMF.outcome, domain=None, range=Optional[str])

slots.impact_sign = Slot(uri=NIST_AI_100_1.impact_sign, name="impact_sign", curie=NIST_AI_100_1.curie('impact_sign'),
                   model_uri=NIST_AI_RMF.impact_sign, domain=None, range=Optional[Union[str, "ImpactSignEnum"]])

slots.likelihood = Slot(uri=NIST_AI_100_1.likelihood, name="likelihood", curie=NIST_AI_100_1.curie('likelihood'),
                   model_uri=NIST_AI_RMF.likelihood, domain=None, range=Optional[float])

slots.magnitude = Slot(uri=NIST_AI_100_1.magnitude, name="magnitude", curie=NIST_AI_100_1.curie('magnitude'),
                   model_uri=NIST_AI_RMF.magnitude, domain=None, range=Optional[str])

slots.harm_category = Slot(uri=NIST_AI_100_1.harm_category, name="harm_category", curie=NIST_AI_100_1.curie('harm_category'),
                   model_uri=NIST_AI_RMF.harm_category, domain=None, range=Optional[Union[str, "HarmCategoryEnum"]])

slots.harm_to_people_subcategory = Slot(uri=NIST_AI_100_1.harm_to_people_subcategory, name="harm_to_people_subcategory", curie=NIST_AI_100_1.curie('harm_to_people_subcategory'),
                   model_uri=NIST_AI_RMF.harm_to_people_subcategory, domain=None, range=Optional[Union[str, "HarmToPeopleSubcategoryEnum"]])

slots.affects = Slot(uri=NIST_AI_100_1.affects, name="affects", curie=NIST_AI_100_1.curie('affects'),
                   model_uri=NIST_AI_RMF.affects, domain=None, range=Optional[Union[Union[str, NamedThingId], list[Union[str, NamedThingId]]]])

slots.risk_response = Slot(uri=NIST_AI_100_1.risk_response, name="risk_response", curie=NIST_AI_100_1.curie('risk_response'),
                   model_uri=NIST_AI_RMF.risk_response, domain=None, range=Optional[Union[str, "RiskResponseEnum"]])

slots.is_residual = Slot(uri=NIST_AI_100_1.is_residual, name="is_residual", curie=NIST_AI_100_1.curie('is_residual'),
                   model_uri=NIST_AI_RMF.is_residual, domain=None, range=Optional[Union[bool, Bool]])

slots.lifecycle_stage = Slot(uri=NIST_AI_100_1.lifecycle_stage, name="lifecycle_stage", curie=NIST_AI_100_1.curie('lifecycle_stage'),
                   model_uri=NIST_AI_RMF.lifecycle_stage, domain=None, range=Optional[Union[Union[str, "AiLifecycleStageEnum"], list[Union[str, "AiLifecycleStageEnum"]]]])

slots.ai_dimension = Slot(uri=NIST_AI_100_1.ai_dimension, name="ai_dimension", curie=NIST_AI_100_1.curie('ai_dimension'),
                   model_uri=NIST_AI_RMF.ai_dimension, domain=None, range=Optional[Union[Union[str, "AiSystemDimensionEnum"], list[Union[str, "AiSystemDimensionEnum"]]]])

slots.actor_task = Slot(uri=NIST_AI_100_1.actor_task, name="actor_task", curie=NIST_AI_100_1.curie('actor_task'),
                   model_uri=NIST_AI_RMF.actor_task, domain=None, range=Optional[Union[Union[str, "AiActorTaskEnum"], list[Union[str, "AiActorTaskEnum"]]]])

slots.is_tevv = Slot(uri=NIST_AI_100_1.is_tevv, name="is_tevv", curie=NIST_AI_100_1.curie('is_tevv'),
                   model_uri=NIST_AI_RMF.is_tevv, domain=None, range=Optional[Union[bool, Bool]])

slots.audience = Slot(uri=NIST_AI_100_1.audience, name="audience", curie=NIST_AI_100_1.curie('audience'),
                   model_uri=NIST_AI_RMF.audience, domain=None, range=Optional[Union[str, "AudienceEnum"]])

slots.bias_category = Slot(uri=NIST_AI_100_1.bias_category, name="bias_category", curie=NIST_AI_100_1.curie('bias_category'),
                   model_uri=NIST_AI_RMF.bias_category, domain=None, range=Optional[Union[Union[str, "BiasCategoryEnum"], list[Union[str, "BiasCategoryEnum"]]]])

slots.profile_type = Slot(uri=NIST_AI_100_1.profile_type, name="profile_type", curie=NIST_AI_100_1.curie('profile_type'),
                   model_uri=NIST_AI_RMF.profile_type, domain=None, range=Union[str, "ProfileTypeEnum"])

slots.target_state = Slot(uri=NIST_AI_100_1.target_state, name="target_state", curie=NIST_AI_100_1.curie('target_state'),
                   model_uri=NIST_AI_RMF.target_state, domain=None, range=Optional[str])

slots.current_state = Slot(uri=NIST_AI_100_1.current_state, name="current_state", curie=NIST_AI_100_1.curie('current_state'),
                   model_uri=NIST_AI_RMF.current_state, domain=None, range=Optional[str])

slots.publisher = Slot(uri=DCTERMS.publisher, name="publisher", curie=DCTERMS.curie('publisher'),
                   model_uri=NIST_AI_RMF.publisher, domain=None, range=Optional[str])

slots.doi = Slot(uri=NIST_AI_100_1.doi, name="doi", curie=NIST_AI_100_1.curie('doi'),
                   model_uri=NIST_AI_RMF.doi, domain=None, range=Optional[Union[str, URIorCURIE]])

slots.published_date = Slot(uri=DCTERMS.issued, name="published_date", curie=DCTERMS.curie('issued'),
                   model_uri=NIST_AI_RMF.published_date, domain=None, range=Optional[Union[str, XSDDate]])

slots.version = Slot(uri=SCHEMA.version, name="version", curie=SCHEMA.curie('version'),
                   model_uri=NIST_AI_RMF.version, domain=None, range=Optional[str])

slots.about_text = Slot(uri=NIST_AI_100_1.about_text, name="about_text", curie=NIST_AI_100_1.curie('about_text'),
                   model_uri=NIST_AI_RMF.about_text, domain=None, range=Optional[str])

slots.suggested_actions_text = Slot(uri=NIST_AI_100_1.suggested_actions_text, name="suggested_actions_text", curie=NIST_AI_100_1.curie('suggested_actions_text'),
                   model_uri=NIST_AI_RMF.suggested_actions_text, domain=None, range=Optional[str])

slots.documentation_questions = Slot(uri=NIST_AI_100_1.documentation_questions, name="documentation_questions", curie=NIST_AI_100_1.curie('documentation_questions'),
                   model_uri=NIST_AI_RMF.documentation_questions, domain=None, range=Optional[str])

slots.references_text = Slot(uri=NIST_AI_100_1.references_text, name="references_text", curie=NIST_AI_100_1.curie('references_text'),
                   model_uri=NIST_AI_RMF.references_text, domain=None, range=Optional[str])

slots.topics = Slot(uri=NIST_AI_100_1.topics, name="topics", curie=NIST_AI_100_1.curie('topics'),
                   model_uri=NIST_AI_RMF.topics, domain=None, range=Optional[Union[str, list[str]]])

slots.ai_actor_categories = Slot(uri=NIST_AI_100_1.ai_actor_categories, name="ai_actor_categories", curie=NIST_AI_100_1.curie('ai_actor_categories'),
                   model_uri=NIST_AI_RMF.ai_actor_categories, domain=None, range=Optional[Union[str, list[str]]])

slots.function_kind = Slot(uri=NIST_AI_100_1.function_kind, name="function_kind", curie=NIST_AI_100_1.curie('function_kind'),
                   model_uri=NIST_AI_RMF.function_kind, domain=None, range=Optional[Union[str, "FunctionEnum"]])

slots.category_code = Slot(uri=NIST_AI_100_1.category_code, name="category_code", curie=NIST_AI_100_1.curie('category_code'),
                   model_uri=NIST_AI_RMF.category_code, domain=None, range=Optional[Union[str, "CategoryEnum"]])

slots.dimension_kind = Slot(uri=NIST_AI_100_1.dimension_kind, name="dimension_kind", curie=NIST_AI_100_1.curie('dimension_kind'),
                   model_uri=NIST_AI_RMF.dimension_kind, domain=None, range=Union[str, "AiSystemDimensionEnum"])

slots.stage_kind = Slot(uri=NIST_AI_100_1.stage_kind, name="stage_kind", curie=NIST_AI_100_1.curie('stage_kind'),
                   model_uri=NIST_AI_RMF.stage_kind, domain=None, range=Union[str, "AiLifecycleStageEnum"])

slots.includes_tevv = Slot(uri=NIST_AI_100_1.includes_tevv, name="includes_tevv", curie=NIST_AI_100_1.curie('includes_tevv'),
                   model_uri=NIST_AI_RMF.includes_tevv, domain=None, range=Optional[Union[bool, Bool]])

slots.task_kind = Slot(uri=NIST_AI_100_1.task_kind, name="task_kind", curie=NIST_AI_100_1.curie('task_kind'),
                   model_uri=NIST_AI_RMF.task_kind, domain=None, range=Union[str, "AiActorTaskEnum"])

slots.typical_actors = Slot(uri=NIST_AI_100_1.typical_actors, name="typical_actors", curie=NIST_AI_100_1.curie('typical_actors'),
                   model_uri=NIST_AI_RMF.typical_actors, domain=None, range=Optional[Union[str, list[str]]])

slots.challenge_kind = Slot(uri=NIST_AI_100_1.challenge_kind, name="challenge_kind", curie=NIST_AI_100_1.curie('challenge_kind'),
                   model_uri=NIST_AI_RMF.challenge_kind, domain=None, range=Union[str, "RiskMeasurementChallengeEnum"])

slots.characteristic_kind = Slot(uri=NIST_AI_100_1.characteristic_kind, name="characteristic_kind", curie=NIST_AI_100_1.curie('characteristic_kind'),
                   model_uri=NIST_AI_RMF.characteristic_kind, domain=None, range=Union[str, "TrustworthinessCharacteristicEnum"])

slots.is_base_condition = Slot(uri=NIST_AI_100_1.is_base_condition, name="is_base_condition", curie=NIST_AI_100_1.curie('is_base_condition'),
                   model_uri=NIST_AI_RMF.is_base_condition, domain=None, range=Optional[Union[bool, Bool]])

slots.is_cross_cutting = Slot(uri=NIST_AI_100_1.is_cross_cutting, name="is_cross_cutting", curie=NIST_AI_100_1.curie('is_cross_cutting'),
                   model_uri=NIST_AI_RMF.is_cross_cutting, domain=None, range=Optional[Union[bool, Bool]])

slots.related_impacts = Slot(uri=NIST_AI_100_1.related_impacts, name="related_impacts", curie=NIST_AI_100_1.curie('related_impacts'),
                   model_uri=NIST_AI_RMF.related_impacts, domain=None, range=Optional[Union[dict[Union[str, ImpactId], Union[dict, Impact]], list[Union[dict, Impact]]]])

slots.affects_system = Slot(uri=NIST_AI_100_1.affects_system, name="affects_system", curie=NIST_AI_100_1.curie('affects_system'),
                   model_uri=NIST_AI_RMF.affects_system, domain=None, range=Optional[Union[str, AiSystemId]])

slots.tolerance_statement = Slot(uri=NIST_AI_100_1.tolerance_statement, name="tolerance_statement", curie=NIST_AI_100_1.curie('tolerance_statement'),
                   model_uri=NIST_AI_RMF.tolerance_statement, domain=None, range=Optional[str])

slots.legal_basis = Slot(uri=NIST_AI_100_1.legal_basis, name="legal_basis", curie=NIST_AI_100_1.curie('legal_basis'),
                   model_uri=NIST_AI_RMF.legal_basis, domain=None, range=Optional[str])

slots.sector = Slot(uri=NIST_AI_100_1.sector, name="sector", curie=NIST_AI_100_1.curie('sector'),
                   model_uri=NIST_AI_RMF.sector, domain=None, range=Optional[str])

slots.addresses = Slot(uri=NIST_AI_100_1.addresses, name="addresses", curie=NIST_AI_100_1.curie('addresses'),
                   model_uri=NIST_AI_RMF.addresses, domain=None, range=Optional[Union[Union[str, SubcategoryId], list[Union[str, SubcategoryId]]]])

slots.entries = Slot(uri=NIST_AI_100_1.entries, name="entries", curie=NIST_AI_100_1.curie('entries'),
                   model_uri=NIST_AI_RMF.entries, domain=None, range=Optional[Union[Union[dict, PlaybookEntry], list[Union[dict, PlaybookEntry]]]])

slots.document = Slot(uri=NIST_AI_100_1.document, name="document", curie=NIST_AI_100_1.curie('document'),
                   model_uri=NIST_AI_RMF.document, domain=None, range=Optional[Union[dict, AiRmfDocument]])

slots.functions = Slot(uri=NIST_AI_100_1.functions, name="functions", curie=NIST_AI_100_1.curie('functions'),
                   model_uri=NIST_AI_RMF.functions, domain=None, range=Optional[Union[dict[Union[str, FunctionId], Union[dict, Function]], list[Union[dict, Function]]]])

slots.trustworthiness_characteristics = Slot(uri=NIST_AI_100_1.trustworthiness_characteristics, name="trustworthiness_characteristics", curie=NIST_AI_100_1.curie('trustworthiness_characteristics'),
                   model_uri=NIST_AI_RMF.trustworthiness_characteristics, domain=None, range=Optional[Union[dict[Union[str, TrustworthinessCharacteristicId], Union[dict, TrustworthinessCharacteristic]], list[Union[dict, TrustworthinessCharacteristic]]]])

slots.lifecycle_stages = Slot(uri=NIST_AI_100_1.lifecycle_stages, name="lifecycle_stages", curie=NIST_AI_100_1.curie('lifecycle_stages'),
                   model_uri=NIST_AI_RMF.lifecycle_stages, domain=None, range=Optional[Union[dict[Union[str, AiLifecycleStageId], Union[dict, AiLifecycleStage]], list[Union[dict, AiLifecycleStage]]]])

slots.dimensions = Slot(uri=NIST_AI_100_1.dimensions, name="dimensions", curie=NIST_AI_100_1.curie('dimensions'),
                   model_uri=NIST_AI_RMF.dimensions, domain=None, range=Optional[Union[dict[Union[str, AiSystemDimensionId], Union[dict, AiSystemDimension]], list[Union[dict, AiSystemDimension]]]])

slots.actor_tasks = Slot(uri=NIST_AI_100_1.actor_tasks, name="actor_tasks", curie=NIST_AI_100_1.curie('actor_tasks'),
                   model_uri=NIST_AI_RMF.actor_tasks, domain=None, range=Optional[Union[dict[Union[str, AiActorTaskId], Union[dict, AiActorTask]], list[Union[dict, AiActorTask]]]])

slots.profiles = Slot(uri=NIST_AI_100_1.profiles, name="profiles", curie=NIST_AI_100_1.curie('profiles'),
                   model_uri=NIST_AI_RMF.profiles, domain=None, range=Optional[Union[dict[Union[str, AiRmfProfileId], Union[dict, AiRmfProfile]], list[Union[dict, AiRmfProfile]]]])

slots.attributes = Slot(uri=NIST_AI_100_1.attributes, name="attributes", curie=NIST_AI_100_1.curie('attributes'),
                   model_uri=NIST_AI_RMF.attributes, domain=None, range=Optional[Union[dict[Union[str, RmfAttributeId], Union[dict, RmfAttribute]], list[Union[dict, RmfAttribute]]]])

slots.risk_measurement_challenges = Slot(uri=NIST_AI_100_1.risk_measurement_challenges, name="risk_measurement_challenges", curie=NIST_AI_100_1.curie('risk_measurement_challenges'),
                   model_uri=NIST_AI_RMF.risk_measurement_challenges, domain=None, range=Optional[Union[dict[Union[str, RiskMeasurementChallengeId], Union[dict, RiskMeasurementChallenge]], list[Union[dict, RiskMeasurementChallenge]]]])

slots.ai_specific_risks = Slot(uri=NIST_AI_100_1.ai_specific_risks, name="ai_specific_risks", curie=NIST_AI_100_1.curie('ai_specific_risks'),
                   model_uri=NIST_AI_RMF.ai_specific_risks, domain=None, range=Optional[Union[dict[Union[str, AiSpecificRiskId], Union[dict, AiSpecificRisk]], list[Union[dict, AiSpecificRisk]]]])

slots.human_ai_interaction_issues = Slot(uri=NIST_AI_100_1.human_ai_interaction_issues, name="human_ai_interaction_issues", curie=NIST_AI_100_1.curie('human_ai_interaction_issues'),
                   model_uri=NIST_AI_RMF.human_ai_interaction_issues, domain=None, range=Optional[Union[dict[Union[str, HumanAiInteractionIssueId], Union[dict, HumanAiInteractionIssue]], list[Union[dict, HumanAiInteractionIssue]]]])

slots.gai_risk_kind = Slot(uri=NIST_AI_600_1.gai_risk_kind, name="gai_risk_kind", curie=NIST_AI_600_1.curie('gai_risk_kind'),
                   model_uri=NIST_AI_RMF.gai_risk_kind, domain=None, range=Optional[Union[str, "GaiRiskCategoryEnum"]])

slots.gai_risks = Slot(uri=NIST_AI_600_1.gai_risks, name="gai_risks", curie=NIST_AI_600_1.curie('gai_risks'),
                   model_uri=NIST_AI_RMF.gai_risks, domain=None, range=Optional[Union[Union[str, "GaiRiskCategoryEnum"], list[Union[str, "GaiRiskCategoryEnum"]]]])

slots.risk_categorization = Slot(uri=NIST_AI_600_1.risk_categorization, name="risk_categorization", curie=NIST_AI_600_1.curie('risk_categorization'),
                   model_uri=NIST_AI_RMF.risk_categorization, domain=None, range=Optional[Union[str, "GaiRiskCategorizationEnum"]])

slots.risk_scope = Slot(uri=NIST_AI_600_1.risk_scope, name="risk_scope", curie=NIST_AI_600_1.curie('risk_scope'),
                   model_uri=NIST_AI_RMF.risk_scope, domain=None, range=Optional[Union[Union[str, "GaiRiskScopeEnum"], list[Union[str, "GaiRiskScopeEnum"]]]])

slots.risk_sources = Slot(uri=NIST_AI_600_1.risk_sources, name="risk_sources", curie=NIST_AI_600_1.curie('risk_sources'),
                   model_uri=NIST_AI_RMF.risk_sources, domain=None, range=Optional[Union[Union[str, "GaiRiskSourceEnum"], list[Union[str, "GaiRiskSourceEnum"]]]])

slots.time_scale = Slot(uri=NIST_AI_600_1.time_scale, name="time_scale", curie=NIST_AI_600_1.curie('time_scale'),
                   model_uri=NIST_AI_RMF.time_scale, domain=None, range=Optional[Union[Union[str, "GaiRiskTimeScaleEnum"], list[Union[str, "GaiRiskTimeScaleEnum"]]]])

slots.action_id = Slot(uri=NIST_AI_600_1.action_id, name="action_id", curie=NIST_AI_600_1.curie('action_id'),
                   model_uri=NIST_AI_RMF.action_id, domain=None, range=Union[str, GaiActionId])

slots.function_prefix = Slot(uri=NIST_AI_600_1.function_prefix, name="function_prefix", curie=NIST_AI_600_1.curie('function_prefix'),
                   model_uri=NIST_AI_RMF.function_prefix, domain=None, range=Optional[Union[str, "GaiActionFunctionPrefixEnum"]])

slots.applies_to_subcategory = Slot(uri=NIST_AI_600_1.applies_to_subcategory, name="applies_to_subcategory", curie=NIST_AI_600_1.curie('applies_to_subcategory'),
                   model_uri=NIST_AI_RMF.applies_to_subcategory, domain=None, range=Optional[Union[str, SubcategoryCode]])

slots.consideration_kind = Slot(uri=NIST_AI_600_1.consideration_kind, name="consideration_kind", curie=NIST_AI_600_1.curie('consideration_kind'),
                   model_uri=NIST_AI_RMF.consideration_kind, domain=None, range=Union[str, "PrimaryConsiderationEnum"])

slots.feedback_method_kind = Slot(uri=NIST_AI_600_1.feedback_method_kind, name="feedback_method_kind", curie=NIST_AI_600_1.curie('feedback_method_kind'),
                   model_uri=NIST_AI_RMF.feedback_method_kind, domain=None, range=Union[str, "StructuredFeedbackMethodEnum"])

slots.red_team_type = Slot(uri=NIST_AI_600_1.red_team_type, name="red_team_type", curie=NIST_AI_600_1.curie('red_team_type'),
                   model_uri=NIST_AI_RMF.red_team_type, domain=None, range=Optional[Union[str, "RedTeamingTypeEnum"]])

slots.addressed_by_actions = Slot(uri=NIST_AI_600_1.addressed_by_actions, name="addressed_by_actions", curie=NIST_AI_600_1.curie('addressed_by_actions'),
                   model_uri=NIST_AI_RMF.addressed_by_actions, domain=None, range=Optional[Union[Union[str, SuggestedActionId], list[Union[str, SuggestedActionId]]]])

slots.governance_practices = Slot(uri=NIST_AI_600_1.governance_practices, name="governance_practices", curie=NIST_AI_600_1.curie('governance_practices'),
                   model_uri=NIST_AI_RMF.governance_practices, domain=None, range=Optional[Union[Union[str, "GovernancePracticeEnum"], list[Union[str, "GovernancePracticeEnum"]]]])

slots.third_party_considerations = Slot(uri=NIST_AI_600_1.third_party_considerations, name="third_party_considerations", curie=NIST_AI_600_1.curie('third_party_considerations'),
                   model_uri=NIST_AI_RMF.third_party_considerations, domain=None, range=Optional[str])

slots.limitations_of_current_approaches = Slot(uri=NIST_AI_600_1.limitations_of_current_approaches, name="limitations_of_current_approaches", curie=NIST_AI_600_1.curie('limitations_of_current_approaches'),
                   model_uri=NIST_AI_RMF.limitations_of_current_approaches, domain=None, range=Optional[str])

slots.provenance_techniques = Slot(uri=NIST_AI_600_1.provenance_techniques, name="provenance_techniques", curie=NIST_AI_600_1.curie('provenance_techniques'),
                   model_uri=NIST_AI_RMF.provenance_techniques, domain=None, range=Optional[Union[Union[str, "ProvenanceTechniqueEnum"], list[Union[str, "ProvenanceTechniqueEnum"]]]])

slots.ai_incident_definition = Slot(uri=NIST_AI_600_1.ai_incident_definition, name="ai_incident_definition", curie=NIST_AI_600_1.curie('ai_incident_definition'),
                   model_uri=NIST_AI_RMF.ai_incident_definition, domain=None, range=Optional[str])

slots.gai_risk_catalog = Slot(uri=NIST_AI_600_1.gai_risk_catalog, name="gai_risk_catalog", curie=NIST_AI_600_1.curie('gai_risk_catalog'),
                   model_uri=NIST_AI_RMF.gai_risk_catalog, domain=None, range=Optional[Union[dict[Union[str, GaiRiskId], Union[dict, GaiRisk]], list[Union[dict, GaiRisk]]]])

slots.suggested_actions = Slot(uri=NIST_AI_600_1.suggested_actions, name="suggested_actions", curie=NIST_AI_600_1.curie('suggested_actions'),
                   model_uri=NIST_AI_RMF.suggested_actions, domain=None, range=Optional[Union[dict[Union[str, SuggestedActionId], Union[dict, SuggestedAction]], list[Union[dict, SuggestedAction]]]])

slots.primary_considerations = Slot(uri=NIST_AI_600_1.primary_considerations, name="primary_considerations", curie=NIST_AI_600_1.curie('primary_considerations'),
                   model_uri=NIST_AI_RMF.primary_considerations, domain=None, range=Optional[Union[dict[Union[str, PrimaryGaiConsiderationId], Union[dict, PrimaryGaiConsideration]], list[Union[dict, PrimaryGaiConsideration]]]])

slots.structured_feedback_methods = Slot(uri=NIST_AI_600_1.structured_feedback_methods, name="structured_feedback_methods", curie=NIST_AI_600_1.curie('structured_feedback_methods'),
                   model_uri=NIST_AI_RMF.structured_feedback_methods, domain=None, range=Optional[Union[dict[Union[str, StructuredPublicFeedbackId], Union[dict, StructuredPublicFeedback]], list[Union[dict, StructuredPublicFeedback]]]])

slots.id = Slot(uri=SCHEMA.identifier, name="id", curie=SCHEMA.curie('identifier'),
                   model_uri=NIST_AI_RMF.id, domain=None, range=URIRef)

slots.name = Slot(uri=RDFS.label, name="name", curie=RDFS.curie('label'),
                   model_uri=NIST_AI_RMF.name, domain=None, range=Optional[str])

slots.title = Slot(uri=DCTERMS.title, name="title", curie=DCTERMS.curie('title'),
                   model_uri=NIST_AI_RMF.title, domain=None, range=Optional[str])

slots.description = Slot(uri=DCTERMS.description, name="description", curie=DCTERMS.curie('description'),
                   model_uri=NIST_AI_RMF.description, domain=None, range=Optional[str])

slots.see_also = Slot(uri=RDFS.seeAlso, name="see_also", curie=RDFS.curie('seeAlso'),
                   model_uri=NIST_AI_RMF.see_also, domain=None, range=Optional[Union[Union[str, URIorCURIE], list[Union[str, URIorCURIE]]]])

slots.trustworthiness_characteristic = Slot(uri=NIST_AI_100_1.trustworthiness_characteristic, name="trustworthiness_characteristic", curie=NIST_AI_100_1.curie('trustworthiness_characteristic'),
                   model_uri=NIST_AI_RMF.trustworthiness_characteristic, domain=None, range=Optional[Union[Union[str, "TrustworthinessCharacteristicEnum"], list[Union[str, "TrustworthinessCharacteristicEnum"]]]])

slots.playbookEntry__type = Slot(uri=NIST_AI_100_1.type, name="playbookEntry__type", curie=NIST_AI_100_1.curie('type'),
                   model_uri=NIST_AI_RMF.playbookEntry__type, domain=None, range=Optional[str])

slots.playbookEntry__title = Slot(uri=NIST_AI_100_1.title, name="playbookEntry__title", curie=NIST_AI_100_1.curie('title'),
                   model_uri=NIST_AI_RMF.playbookEntry__title, domain=None, range=Optional[str])

slots.playbookEntry__category = Slot(uri=NIST_AI_100_1.category, name="playbookEntry__category", curie=NIST_AI_100_1.curie('category'),
                   model_uri=NIST_AI_RMF.playbookEntry__category, domain=None, range=Optional[str])

slots.playbookEntry__description = Slot(uri=NIST_AI_100_1.description, name="playbookEntry__description", curie=NIST_AI_100_1.curie('description'),
                   model_uri=NIST_AI_RMF.playbookEntry__description, domain=None, range=Optional[str])

slots.playbookEntry__section_about = Slot(uri=NIST_AI_100_1.section_about, name="playbookEntry__section_about", curie=NIST_AI_100_1.curie('section_about'),
                   model_uri=NIST_AI_RMF.playbookEntry__section_about, domain=None, range=Optional[str])

slots.playbookEntry__section_actions = Slot(uri=NIST_AI_100_1.section_actions, name="playbookEntry__section_actions", curie=NIST_AI_100_1.curie('section_actions'),
                   model_uri=NIST_AI_RMF.playbookEntry__section_actions, domain=None, range=Optional[str])

slots.playbookEntry__section_doc = Slot(uri=NIST_AI_100_1.section_doc, name="playbookEntry__section_doc", curie=NIST_AI_100_1.curie('section_doc'),
                   model_uri=NIST_AI_RMF.playbookEntry__section_doc, domain=None, range=Optional[str])

slots.playbookEntry__section_ref = Slot(uri=NIST_AI_100_1.section_ref, name="playbookEntry__section_ref", curie=NIST_AI_100_1.curie('section_ref'),
                   model_uri=NIST_AI_RMF.playbookEntry__section_ref, domain=None, range=Optional[str])

slots.playbookEntry__ai_actors = Slot(uri=NIST_AI_100_1.ai_actors, name="playbookEntry__ai_actors", curie=NIST_AI_100_1.curie('ai_actors'),
                   model_uri=NIST_AI_RMF.playbookEntry__ai_actors, domain=None, range=Optional[Union[str, list[str]]])

slots.playbookEntry__topic = Slot(uri=NIST_AI_100_1.topic, name="playbookEntry__topic", curie=NIST_AI_100_1.curie('topic'),
                   model_uri=NIST_AI_RMF.playbookEntry__topic, domain=None, range=Optional[Union[str, list[str]]])

slots.gaiRisk__lifecycle_stage = Slot(uri=NIST_AI_600_1.lifecycle_stage, name="gaiRisk__lifecycle_stage", curie=NIST_AI_600_1.curie('lifecycle_stage'),
                   model_uri=NIST_AI_RMF.gaiRisk__lifecycle_stage, domain=None, range=Optional[Union[Union[str, "GaiLifecycleStageEnum"], list[Union[str, "GaiLifecycleStageEnum"]]]])

slots.suggestedAction__actor_task = Slot(uri=NIST_AI_600_1.actor_task, name="suggestedAction__actor_task", curie=NIST_AI_600_1.curie('actor_task'),
                   model_uri=NIST_AI_RMF.suggestedAction__actor_task, domain=None, range=Optional[Union[Union[str, "GaiActorTaskEnum"], list[Union[str, "GaiActorTaskEnum"]]]])

slots.ResidualRisk_is_residual = Slot(uri=NIST_AI_100_1.is_residual, name="ResidualRisk_is_residual", curie=NIST_AI_100_1.curie('is_residual'),
                   model_uri=NIST_AI_RMF.ResidualRisk_is_residual, domain=ResidualRisk, range=Optional[Union[bool, Bool]])

slots.Function_categories = Slot(uri=NIST_AI_100_1.categories, name="Function_categories", curie=NIST_AI_100_1.curie('categories'),
                   model_uri=NIST_AI_RMF.Function_categories, domain=Function, range=Optional[Union[dict[Union[str, CategoryId], Union[dict, "Category"]], list[Union[dict, "Category"]]]])

slots.Category_id = Slot(uri=SCHEMA.identifier, name="Category_id", curie=SCHEMA.curie('identifier'),
                   model_uri=NIST_AI_RMF.Category_id, domain=Category, range=Union[str, CategoryId])

slots.Category_subcategories = Slot(uri=NIST_AI_100_1.subcategories, name="Category_subcategories", curie=NIST_AI_100_1.curie('subcategories'),
                   model_uri=NIST_AI_RMF.Category_subcategories, domain=Category, range=Optional[Union[dict[Union[str, SubcategoryId], Union[dict, "Subcategory"]], list[Union[dict, "Subcategory"]]]])

slots.Subcategory_id = Slot(uri=SCHEMA.identifier, name="Subcategory_id", curie=SCHEMA.curie('identifier'),
                   model_uri=NIST_AI_RMF.Subcategory_id, domain=Subcategory, range=Union[str, SubcategoryId])

slots.SuggestedAction_id = Slot(uri=SCHEMA.identifier, name="SuggestedAction_id", curie=SCHEMA.curie('identifier'),
                   model_uri=NIST_AI_RMF.SuggestedAction_id, domain=SuggestedAction, range=Union[str, SuggestedActionId])

slots.SuggestedAction_description = Slot(uri=DCTERMS.description, name="SuggestedAction_description", curie=DCTERMS.curie('description'),
                   model_uri=NIST_AI_RMF.SuggestedAction_description, domain=SuggestedAction, range=Optional[str])

slots.AiRedTeaming_feedback_method_kind = Slot(uri=NIST_AI_600_1.feedback_method_kind, name="AiRedTeaming_feedback_method_kind", curie=NIST_AI_600_1.curie('feedback_method_kind'),
                   model_uri=NIST_AI_RMF.AiRedTeaming_feedback_method_kind, domain=AiRedTeaming, range=Union[str, "StructuredFeedbackMethodEnum"])
