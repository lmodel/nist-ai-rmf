# Auto generated from nist_ai_rmf.yaml by pythongen.py version: 0.0.1
# Schema: nist_ai_rmf
#
# id: https://w3id.org/lmodel/nist-ai-rmf
# description: One LinkML schema for two NIST publications: the AI Risk Management Framework 1.0 (NIST AI 100-1) and its Generative AI Profile (NIST AI 600-1).
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

from linkml_runtime.linkml_model.types import Boolean, Integer, String, Uri, Uriorcurie
from linkml_runtime.utils.metamodelcore import Bool, URI, URIorCURIE

metamodel_version = "1.12.0"
version = "1.0.0"

# Namespaces
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_AI_100_1 = CurieNamespace('nist_ai_100_1', 'https://w3id.org/lmodel/nist-ai-100-1/')
NIST_AI_600_1 = CurieNamespace('nist_ai_600_1', 'https://w3id.org/lmodel/nist-ai-600-1/')
NIST_AI_RMF = CurieNamespace('nist_ai_rmf', 'https://w3id.org/lmodel/nist-ai-rmf/')
NIST_CSF_V2 = CurieNamespace('nist_csf_v2', 'https://w3id.org/lmodel/nist-csf-v2/')
OSCAL = CurieNamespace('oscal', 'https://w3id.org/lmodel/oscal/')
PROV = CurieNamespace('prov', 'http://www.w3.org/ns/prov#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_AI_RMF


# Types
class AiRmfFunctionIdentifier(String):
    """ The name of one of the four Core functions, written in capitals, such as GOVERN. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_function_identifier"
    type_model_uri = NIST_AI_RMF.AiRmfFunctionIdentifier


class AiRmfCategoryIdentifier(String):
    """ A category's identifier, its function's name and a number, such as GOVERN 1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_category_identifier"
    type_model_uri = NIST_AI_RMF.AiRmfCategoryIdentifier


class AiRmfSubcategoryIdentifier(String):
    """ A subcategory's identifier, its category's identifier, a dot and a number, such as GOVERN 1.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_subcategory_identifier"
    type_model_uri = NIST_AI_RMF.AiRmfSubcategoryIdentifier


class AiRmfSuggestedActionIdentifier(String):
    """ The identifier NIST's catalog gives a Playbook suggested action, such as SA-GOVERN_1.1-1. Each further number, as in SA-GOVERN_1.4-1.2, marks a sub-item. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_suggested_action_identifier"
    type_model_uri = NIST_AI_RMF.AiRmfSuggestedActionIdentifier


class AiRmfDocumentationIdentifier(String):
    """ The identifier NIST's catalog gives a Playbook documentation prompt, such as D-GOVERN_1.1-1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "ai_rmf_documentation_identifier"
    type_model_uri = NIST_AI_RMF.AiRmfDocumentationIdentifier


class GaiActionIdentifier(String):
    """ An Action ID: the function's two letters, its subcategory's numbers and a three-digit number, such as GV-1.1-001 for the first action of GOVERN 1.1. """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "gai_action_identifier"
    type_model_uri = NIST_AI_RMF.GaiActionIdentifier


# Class references
class AiRmfRecordAiRmfId(URIorCURIE):
    pass


class AiRmfSystemAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfActorAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfRiskAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfResidualRiskAiRmfId(AiRmfRiskAiRmfId):
    pass


class AiRmfImpactAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfHarmAiRmfId(AiRmfImpactAiRmfId):
    pass


class AiRmfRiskToleranceAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfBiasAiRmfId(AiRmfRecordAiRmfId):
    pass


class AiRmfProfileAiRmfId(AiRmfRecordAiRmfId):
    pass


class GaiProfileAiRmfId(AiRmfProfileAiRmfId):
    pass


@dataclass(repr=False)
class NistAiRmfFamily(YAMLRoot):
    """
    The two publications held in one document, each as its own schema renders it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_RMF["NistAiRmfFamily"]
    class_class_curie: ClassVar[str] = "nist_ai_rmf:NistAiRmfFamily"
    class_name: ClassVar[str] = "NistAiRmfFamily"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.NistAiRmfFamily

    nist_ai_rmf_framework: Optional[Union[dict, "AiRmfFramework"]] = None
    nist_ai_rmf_generative_ai_profile: Optional[Union[dict, "GaiProfile"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self.nist_ai_rmf_framework is not None and not isinstance(self.nist_ai_rmf_framework, AiRmfFramework):
            self.nist_ai_rmf_framework = AiRmfFramework(**as_dict(self.nist_ai_rmf_framework))

        if self.nist_ai_rmf_generative_ai_profile is not None and not isinstance(self.nist_ai_rmf_generative_ai_profile, GaiProfile):
            self.nist_ai_rmf_generative_ai_profile = GaiProfile(**as_dict(self.nist_ai_rmf_generative_ai_profile))

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfFramework(YAMLRoot):
    """
    One edition of the AI RMF as a whole, with the Core and the lists the publication gives.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Framework"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Framework"
    class_name: ClassVar[str] = "AiRmfFramework"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfFramework

    ai_rmf_version: str = None
    ai_rmf_functions: Union[Union[dict, "AiRmfFunction"], list[Union[dict, "AiRmfFunction"]]] = None
    ai_rmf_characteristics: Optional[Union[Union[dict, "AiRmfTrustworthinessCharacteristic"], list[Union[dict, "AiRmfTrustworthinessCharacteristic"]]]] = empty_list()
    ai_rmf_dimensions: Optional[Union[Union[dict, "AiRmfDimension"], list[Union[dict, "AiRmfDimension"]]]] = empty_list()
    ai_rmf_lifecycle_stages: Optional[Union[Union[dict, "AiRmfLifecycleStage"], list[Union[dict, "AiRmfLifecycleStage"]]]] = empty_list()
    ai_rmf_actor_task_list: Optional[Union[Union[dict, "AiRmfActorTask"], list[Union[dict, "AiRmfActorTask"]]]] = empty_list()
    ai_rmf_management_challenges: Optional[Union[Union[dict, "AiRmfManagementChallenge"], list[Union[dict, "AiRmfManagementChallenge"]]]] = empty_list()
    ai_rmf_specific_risks: Optional[Union[Union[dict, "AiRmfSpecificRisk"], list[Union[dict, "AiRmfSpecificRisk"]]]] = empty_list()
    ai_rmf_human_ai_issues: Optional[Union[Union[dict, "AiRmfHumanAiIssue"], list[Union[dict, "AiRmfHumanAiIssue"]]]] = empty_list()
    ai_rmf_attributes: Optional[Union[Union[dict, "AiRmfAttribute"], list[Union[dict, "AiRmfAttribute"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_version):
            self.MissingRequiredField("ai_rmf_version")
        if not isinstance(self.ai_rmf_version, str):
            self.ai_rmf_version = str(self.ai_rmf_version)

        if self._is_empty(self.ai_rmf_functions):
            self.MissingRequiredField("ai_rmf_functions")
        self._normalize_inlined_as_list(slot_name="ai_rmf_functions", slot_type=AiRmfFunction, key_name="ai_rmf_function_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_characteristics", slot_type=AiRmfTrustworthinessCharacteristic, key_name="ai_rmf_characteristic_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_dimensions", slot_type=AiRmfDimension, key_name="ai_rmf_dimension_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_lifecycle_stages", slot_type=AiRmfLifecycleStage, key_name="ai_rmf_lifecycle_stage_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_actor_task_list", slot_type=AiRmfActorTask, key_name="ai_rmf_actor_task_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_management_challenges", slot_type=AiRmfManagementChallenge, key_name="ai_rmf_management_challenge_name", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_specific_risks", slot_type=AiRmfSpecificRisk, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_human_ai_issues", slot_type=AiRmfHumanAiIssue, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_attributes", slot_type=AiRmfAttribute, key_name="title", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfRecord(YAMLRoot):
    """
    The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct
    from what the publication itself lists.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Record"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Record"
    class_name: ClassVar[str] = "AiRmfRecord"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfRecord

    ai_rmf_id: Union[str, AiRmfRecordAiRmfId] = None
    title: Optional[str] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfRecordAiRmfId):
            self.ai_rmf_id = AiRmfRecordAiRmfId(self.ai_rmf_id)

        if self.title is not None and not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfTrustworthinessCharacteristic(YAMLRoot):
    """
    A characteristic of trustworthy AI systems, each with a subsection of section 3.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["TrustworthinessCharacteristic"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:TrustworthinessCharacteristic"
    class_name: ClassVar[str] = "AiRmfTrustworthinessCharacteristic"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfTrustworthinessCharacteristic

    ai_rmf_characteristic_name: Union[str, "AiRmfCharacteristicName"] = None
    ai_rmf_characteristic_section: str = None
    description: Optional[str] = None
    ai_rmf_characteristic_is_base: Optional[Union[bool, Bool]] = None
    ai_rmf_characteristic_relates_to_all: Optional[Union[bool, Bool]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_characteristic_name):
            self.MissingRequiredField("ai_rmf_characteristic_name")
        if not isinstance(self.ai_rmf_characteristic_name, AiRmfCharacteristicName):
            self.ai_rmf_characteristic_name = AiRmfCharacteristicName(self.ai_rmf_characteristic_name)

        if self._is_empty(self.ai_rmf_characteristic_section):
            self.MissingRequiredField("ai_rmf_characteristic_section")
        if not isinstance(self.ai_rmf_characteristic_section, str):
            self.ai_rmf_characteristic_section = str(self.ai_rmf_characteristic_section)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ai_rmf_characteristic_is_base is not None and not isinstance(self.ai_rmf_characteristic_is_base, Bool):
            self.ai_rmf_characteristic_is_base = Bool(self.ai_rmf_characteristic_is_base)

        if self.ai_rmf_characteristic_relates_to_all is not None and not isinstance(self.ai_rmf_characteristic_relates_to_all, Bool):
            self.ai_rmf_characteristic_relates_to_all = Bool(self.ai_rmf_characteristic_relates_to_all)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfDimension(YAMLRoot):
    """
    One of the five key socio-technical dimensions of an AI system in Figure 2.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Dimension"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Dimension"
    class_name: ClassVar[str] = "AiRmfDimension"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfDimension

    ai_rmf_dimension_name: Union[str, "AiRmfDimensionName"] = None
    ai_rmf_dimension_audience: Union[str, "AiRmfAudience"] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_dimension_name):
            self.MissingRequiredField("ai_rmf_dimension_name")
        if not isinstance(self.ai_rmf_dimension_name, AiRmfDimensionName):
            self.ai_rmf_dimension_name = AiRmfDimensionName(self.ai_rmf_dimension_name)

        if self._is_empty(self.ai_rmf_dimension_audience):
            self.MissingRequiredField("ai_rmf_dimension_audience")
        if not isinstance(self.ai_rmf_dimension_audience, AiRmfAudience):
            self.ai_rmf_dimension_audience = AiRmfAudience(self.ai_rmf_dimension_audience)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfLifecycleStage(YAMLRoot):
    """
    A stage of the AI lifecycle as a column of Figure 3 shows it, under its dimension.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["LifecycleStage"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:LifecycleStage"
    class_name: ClassVar[str] = "AiRmfLifecycleStage"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfLifecycleStage

    ai_rmf_lifecycle_stage_name: Union[str, "AiRmfLifecycleStageName"] = None
    ai_rmf_lifecycle_stage_dimension: Union[str, "AiRmfDimensionName"] = None
    description: Optional[str] = None
    ai_rmf_lifecycle_stage_tevv: Optional[str] = None
    ai_rmf_lifecycle_stage_representative_actors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_lifecycle_stage_name):
            self.MissingRequiredField("ai_rmf_lifecycle_stage_name")
        if not isinstance(self.ai_rmf_lifecycle_stage_name, AiRmfLifecycleStageName):
            self.ai_rmf_lifecycle_stage_name = AiRmfLifecycleStageName(self.ai_rmf_lifecycle_stage_name)

        if self._is_empty(self.ai_rmf_lifecycle_stage_dimension):
            self.MissingRequiredField("ai_rmf_lifecycle_stage_dimension")
        if not isinstance(self.ai_rmf_lifecycle_stage_dimension, AiRmfDimensionName):
            self.ai_rmf_lifecycle_stage_dimension = AiRmfDimensionName(self.ai_rmf_lifecycle_stage_dimension)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ai_rmf_lifecycle_stage_tevv is not None and not isinstance(self.ai_rmf_lifecycle_stage_tevv, str):
            self.ai_rmf_lifecycle_stage_tevv = str(self.ai_rmf_lifecycle_stage_tevv)

        if not isinstance(self.ai_rmf_lifecycle_stage_representative_actors, list):
            self.ai_rmf_lifecycle_stage_representative_actors = [self.ai_rmf_lifecycle_stage_representative_actors] if self.ai_rmf_lifecycle_stage_representative_actors is not None else []
        self.ai_rmf_lifecycle_stage_representative_actors = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_lifecycle_stage_representative_actors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfActorTask(YAMLRoot):
    """
    A task or additional AI actor of Appendix A.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["ActorTask"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:ActorTask"
    class_name: ClassVar[str] = "AiRmfActorTask"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfActorTask

    ai_rmf_actor_task_name: Union[str, "AiRmfActorTaskName"] = None
    description: Optional[str] = None
    ai_rmf_actor_task_is_additional_actor: Optional[Union[bool, Bool]] = None
    ai_rmf_actor_task_representative_actors: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_actor_task_name):
            self.MissingRequiredField("ai_rmf_actor_task_name")
        if not isinstance(self.ai_rmf_actor_task_name, AiRmfActorTaskName):
            self.ai_rmf_actor_task_name = AiRmfActorTaskName(self.ai_rmf_actor_task_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if self.ai_rmf_actor_task_is_additional_actor is not None and not isinstance(self.ai_rmf_actor_task_is_additional_actor, Bool):
            self.ai_rmf_actor_task_is_additional_actor = Bool(self.ai_rmf_actor_task_is_additional_actor)

        if not isinstance(self.ai_rmf_actor_task_representative_actors, list):
            self.ai_rmf_actor_task_representative_actors = [self.ai_rmf_actor_task_representative_actors] if self.ai_rmf_actor_task_representative_actors is not None else []
        self.ai_rmf_actor_task_representative_actors = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_actor_task_representative_actors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfManagementChallenge(YAMLRoot):
    """
    One of the four challenges for AI risk management in section 1.2.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["ManagementChallenge"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:ManagementChallenge"
    class_name: ClassVar[str] = "AiRmfManagementChallenge"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfManagementChallenge

    ai_rmf_management_challenge_name: Union[str, "AiRmfManagementChallengeName"] = None
    description: Optional[str] = None
    ai_rmf_management_challenge_measurement_challenges: Optional[Union[Union[dict, "AiRmfMeasurementChallenge"], list[Union[dict, "AiRmfMeasurementChallenge"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_management_challenge_name):
            self.MissingRequiredField("ai_rmf_management_challenge_name")
        if not isinstance(self.ai_rmf_management_challenge_name, AiRmfManagementChallengeName):
            self.ai_rmf_management_challenge_name = AiRmfManagementChallengeName(self.ai_rmf_management_challenge_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="ai_rmf_management_challenge_measurement_challenges", slot_type=AiRmfMeasurementChallenge, key_name="ai_rmf_measurement_challenge_name", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfMeasurementChallenge(YAMLRoot):
    """
    One of the challenges of measuring AI risk in section 1.2.1.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["MeasurementChallenge"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:MeasurementChallenge"
    class_name: ClassVar[str] = "AiRmfMeasurementChallenge"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfMeasurementChallenge

    ai_rmf_measurement_challenge_name: Union[str, "AiRmfMeasurementChallengeName"] = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_measurement_challenge_name):
            self.MissingRequiredField("ai_rmf_measurement_challenge_name")
        if not isinstance(self.ai_rmf_measurement_challenge_name, AiRmfMeasurementChallengeName):
            self.ai_rmf_measurement_challenge_name = AiRmfMeasurementChallengeName(self.ai_rmf_measurement_challenge_name)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfSpecificRisk(YAMLRoot):
    """
    A risk that Appendix B says is new or increased for AI compared with traditional software.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["SpecificRisk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:SpecificRisk"
    class_name: ClassVar[str] = "AiRmfSpecificRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfSpecificRisk

    title: str = None
    ai_rmf_specific_risk_position: int = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.ai_rmf_specific_risk_position):
            self.MissingRequiredField("ai_rmf_specific_risk_position")
        if not isinstance(self.ai_rmf_specific_risk_position, int):
            self.ai_rmf_specific_risk_position = int(self.ai_rmf_specific_risk_position)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfHumanAiIssue(YAMLRoot):
    """
    An issue of human-AI interaction that Appendix C says merits further consideration and research.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["HumanAiIssue"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:HumanAiIssue"
    class_name: ClassVar[str] = "AiRmfHumanAiIssue"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfHumanAiIssue

    title: str = None
    ai_rmf_human_ai_issue_number: int = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.ai_rmf_human_ai_issue_number):
            self.MissingRequiredField("ai_rmf_human_ai_issue_number")
        if not isinstance(self.ai_rmf_human_ai_issue_number, int):
            self.ai_rmf_human_ai_issue_number = int(self.ai_rmf_human_ai_issue_number)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfAttribute(YAMLRoot):
    """
    A key attribute of the AI RMF in Appendix D, which guided its development.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Attribute"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Attribute"
    class_name: ClassVar[str] = "AiRmfAttribute"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfAttribute

    title: str = None
    ai_rmf_attribute_number: int = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.ai_rmf_attribute_number):
            self.MissingRequiredField("ai_rmf_attribute_number")
        if not isinstance(self.ai_rmf_attribute_number, int):
            self.ai_rmf_attribute_number = int(self.ai_rmf_attribute_number)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfSystem(AiRmfRecord):
    """
    A machine-based system that produces outputs such as predictions or decisions for given objectives, with varying
    autonomy.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiSystem"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiSystem"
    class_name: ClassVar[str] = "AiRmfSystem"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfSystem

    ai_rmf_id: Union[str, AiRmfSystemAiRmfId] = None
    ai_rmf_system_intended_purposes: Optional[Union[str, list[str]]] = empty_list()
    ai_rmf_system_deployment_settings: Optional[Union[str, list[str]]] = empty_list()
    ai_rmf_system_lifecycle_stages: Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]] = empty_list()
    ai_rmf_system_actors: Optional[Union[Union[str, AiRmfActorAiRmfId], list[Union[str, AiRmfActorAiRmfId]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfSystemAiRmfId):
            self.ai_rmf_id = AiRmfSystemAiRmfId(self.ai_rmf_id)

        if not isinstance(self.ai_rmf_system_intended_purposes, list):
            self.ai_rmf_system_intended_purposes = [self.ai_rmf_system_intended_purposes] if self.ai_rmf_system_intended_purposes is not None else []
        self.ai_rmf_system_intended_purposes = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_system_intended_purposes]

        if not isinstance(self.ai_rmf_system_deployment_settings, list):
            self.ai_rmf_system_deployment_settings = [self.ai_rmf_system_deployment_settings] if self.ai_rmf_system_deployment_settings is not None else []
        self.ai_rmf_system_deployment_settings = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_system_deployment_settings]

        if not isinstance(self.ai_rmf_system_lifecycle_stages, list):
            self.ai_rmf_system_lifecycle_stages = [self.ai_rmf_system_lifecycle_stages] if self.ai_rmf_system_lifecycle_stages is not None else []
        self.ai_rmf_system_lifecycle_stages = [v if isinstance(v, AiRmfLifecycleStageName) else AiRmfLifecycleStageName(v) for v in self.ai_rmf_system_lifecycle_stages]

        if not isinstance(self.ai_rmf_system_actors, list):
            self.ai_rmf_system_actors = [self.ai_rmf_system_actors] if self.ai_rmf_system_actors is not None else []
        self.ai_rmf_system_actors = [v if isinstance(v, AiRmfActorAiRmfId) else AiRmfActorAiRmfId(v) for v in self.ai_rmf_system_actors]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfActor(AiRmfRecord):
    """
    An organization or individual with an active role in an AI system's lifecycle.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["AiActor"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:AiActor"
    class_name: ClassVar[str] = "AiRmfActor"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfActor

    ai_rmf_id: Union[str, AiRmfActorAiRmfId] = None
    ai_rmf_actor_tasks: Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]] = empty_list()
    ai_rmf_actor_audience: Optional[Union[str, "AiRmfAudience"]] = None
    ai_rmf_actor_lifecycle_stages: Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfActorAiRmfId):
            self.ai_rmf_id = AiRmfActorAiRmfId(self.ai_rmf_id)

        if not isinstance(self.ai_rmf_actor_tasks, list):
            self.ai_rmf_actor_tasks = [self.ai_rmf_actor_tasks] if self.ai_rmf_actor_tasks is not None else []
        self.ai_rmf_actor_tasks = [v if isinstance(v, AiRmfActorTaskName) else AiRmfActorTaskName(v) for v in self.ai_rmf_actor_tasks]

        if self.ai_rmf_actor_audience is not None and not isinstance(self.ai_rmf_actor_audience, AiRmfAudience):
            self.ai_rmf_actor_audience = AiRmfAudience(self.ai_rmf_actor_audience)

        if not isinstance(self.ai_rmf_actor_lifecycle_stages, list):
            self.ai_rmf_actor_lifecycle_stages = [self.ai_rmf_actor_lifecycle_stages] if self.ai_rmf_actor_lifecycle_stages is not None else []
        self.ai_rmf_actor_lifecycle_stages = [v if isinstance(v, AiRmfLifecycleStageName) else AiRmfLifecycleStageName(v) for v in self.ai_rmf_actor_lifecycle_stages]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfRisk(AiRmfRecord):
    """
    How likely an event is, combined with how severe its consequences are.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Risk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Risk"
    class_name: ClassVar[str] = "AiRmfRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfRisk

    ai_rmf_id: Union[str, AiRmfRiskAiRmfId] = None
    ai_rmf_likelihood: Optional[str] = None
    ai_rmf_magnitude: Optional[str] = None
    ai_rmf_risk_system: Optional[Union[str, AiRmfSystemAiRmfId]] = None
    ai_rmf_risk_impacts: Optional[Union[dict[Union[str, AiRmfImpactAiRmfId], Union[dict, "AiRmfImpact"]], list[Union[dict, "AiRmfImpact"]]]] = empty_dict()
    ai_rmf_risk_characteristics: Optional[Union[Union[str, "AiRmfCharacteristicName"], list[Union[str, "AiRmfCharacteristicName"]]]] = empty_list()
    ai_rmf_risk_lifecycle_stages: Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]] = empty_list()
    ai_rmf_risk_responses: Optional[Union[Union[str, "AiRmfRiskResponse"], list[Union[str, "AiRmfRiskResponse"]]]] = empty_list()
    ai_rmf_risk_priority: Optional[str] = None
    ai_rmf_risk_tolerance: Optional[Union[str, AiRmfRiskToleranceAiRmfId]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfRiskAiRmfId):
            self.ai_rmf_id = AiRmfRiskAiRmfId(self.ai_rmf_id)

        if self.ai_rmf_likelihood is not None and not isinstance(self.ai_rmf_likelihood, str):
            self.ai_rmf_likelihood = str(self.ai_rmf_likelihood)

        if self.ai_rmf_magnitude is not None and not isinstance(self.ai_rmf_magnitude, str):
            self.ai_rmf_magnitude = str(self.ai_rmf_magnitude)

        if self.ai_rmf_risk_system is not None and not isinstance(self.ai_rmf_risk_system, AiRmfSystemAiRmfId):
            self.ai_rmf_risk_system = AiRmfSystemAiRmfId(self.ai_rmf_risk_system)

        self._normalize_inlined_as_list(slot_name="ai_rmf_risk_impacts", slot_type=AiRmfImpact, key_name="ai_rmf_id", keyed=True)

        if not isinstance(self.ai_rmf_risk_characteristics, list):
            self.ai_rmf_risk_characteristics = [self.ai_rmf_risk_characteristics] if self.ai_rmf_risk_characteristics is not None else []
        self.ai_rmf_risk_characteristics = [v if isinstance(v, AiRmfCharacteristicName) else AiRmfCharacteristicName(v) for v in self.ai_rmf_risk_characteristics]

        if not isinstance(self.ai_rmf_risk_lifecycle_stages, list):
            self.ai_rmf_risk_lifecycle_stages = [self.ai_rmf_risk_lifecycle_stages] if self.ai_rmf_risk_lifecycle_stages is not None else []
        self.ai_rmf_risk_lifecycle_stages = [v if isinstance(v, AiRmfLifecycleStageName) else AiRmfLifecycleStageName(v) for v in self.ai_rmf_risk_lifecycle_stages]

        if not isinstance(self.ai_rmf_risk_responses, list):
            self.ai_rmf_risk_responses = [self.ai_rmf_risk_responses] if self.ai_rmf_risk_responses is not None else []
        self.ai_rmf_risk_responses = [v if isinstance(v, AiRmfRiskResponse) else AiRmfRiskResponse(v) for v in self.ai_rmf_risk_responses]

        if self.ai_rmf_risk_priority is not None and not isinstance(self.ai_rmf_risk_priority, str):
            self.ai_rmf_risk_priority = str(self.ai_rmf_risk_priority)

        if self.ai_rmf_risk_tolerance is not None and not isinstance(self.ai_rmf_risk_tolerance, AiRmfRiskToleranceAiRmfId):
            self.ai_rmf_risk_tolerance = AiRmfRiskToleranceAiRmfId(self.ai_rmf_risk_tolerance)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfResidualRisk(AiRmfRisk):
    """
    The risk that remains after risk treatment.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["ResidualRisk"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:ResidualRisk"
    class_name: ClassVar[str] = "AiRmfResidualRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfResidualRisk

    ai_rmf_id: Union[str, AiRmfResidualRiskAiRmfId] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfResidualRiskAiRmfId):
            self.ai_rmf_id = AiRmfResidualRiskAiRmfId(self.ai_rmf_id)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfImpact(AiRmfRecord):
    """
    A consequence of an AI system, which may be an opportunity, a threat or both.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Impact"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Impact"
    class_name: ClassVar[str] = "AiRmfImpact"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfImpact

    ai_rmf_id: Union[str, AiRmfImpactAiRmfId] = None
    ai_rmf_impact_direction: Union[str, "AiRmfImpactDirection"] = None
    ai_rmf_likelihood: Optional[str] = None
    ai_rmf_magnitude: Optional[str] = None
    ai_rmf_impact_affected_parties: Optional[Union[Union[str, "AiRmfAffectedParty"], list[Union[str, "AiRmfAffectedParty"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfImpactAiRmfId):
            self.ai_rmf_id = AiRmfImpactAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_impact_direction):
            self.MissingRequiredField("ai_rmf_impact_direction")
        if not isinstance(self.ai_rmf_impact_direction, AiRmfImpactDirection):
            self.ai_rmf_impact_direction = AiRmfImpactDirection(self.ai_rmf_impact_direction)

        if self.ai_rmf_likelihood is not None and not isinstance(self.ai_rmf_likelihood, str):
            self.ai_rmf_likelihood = str(self.ai_rmf_likelihood)

        if self.ai_rmf_magnitude is not None and not isinstance(self.ai_rmf_magnitude, str):
            self.ai_rmf_magnitude = str(self.ai_rmf_magnitude)

        if not isinstance(self.ai_rmf_impact_affected_parties, list):
            self.ai_rmf_impact_affected_parties = [self.ai_rmf_impact_affected_parties] if self.ai_rmf_impact_affected_parties is not None else []
        self.ai_rmf_impact_affected_parties = [v if isinstance(v, AiRmfAffectedParty) else AiRmfAffectedParty(v) for v in self.ai_rmf_impact_affected_parties]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfHarm(AiRmfImpact):
    """
    A negative impact, sorted as in Figure 1 by whether it falls on people, an organization or an ecosystem.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Harm"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Harm"
    class_name: ClassVar[str] = "AiRmfHarm"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfHarm

    ai_rmf_id: Union[str, AiRmfHarmAiRmfId] = None
    ai_rmf_impact_direction: Union[str, "AiRmfImpactDirection"] = None
    ai_rmf_harm_category: Union[str, "AiRmfHarmCategory"] = None
    ai_rmf_harm_example: Optional[Union[str, "AiRmfHarmExample"]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfHarmAiRmfId):
            self.ai_rmf_id = AiRmfHarmAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_harm_category):
            self.MissingRequiredField("ai_rmf_harm_category")
        if not isinstance(self.ai_rmf_harm_category, AiRmfHarmCategory):
            self.ai_rmf_harm_category = AiRmfHarmCategory(self.ai_rmf_harm_category)

        if self.ai_rmf_harm_example is not None and not isinstance(self.ai_rmf_harm_example, AiRmfHarmExample):
            self.ai_rmf_harm_example = AiRmfHarmExample(self.ai_rmf_harm_example)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfRiskTolerance(AiRmfRecord):
    """
    An organization's or AI actor's readiness to bear risk to achieve its objectives. The AI RMF prescribes none.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["RiskTolerance"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:RiskTolerance"
    class_name: ClassVar[str] = "AiRmfRiskTolerance"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfRiskTolerance

    ai_rmf_id: Union[str, AiRmfRiskToleranceAiRmfId] = None
    ai_rmf_risk_tolerance_holder: Optional[Union[str, AiRmfActorAiRmfId]] = None
    ai_rmf_risk_tolerance_influences: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfRiskToleranceAiRmfId):
            self.ai_rmf_id = AiRmfRiskToleranceAiRmfId(self.ai_rmf_id)

        if self.ai_rmf_risk_tolerance_holder is not None and not isinstance(self.ai_rmf_risk_tolerance_holder, AiRmfActorAiRmfId):
            self.ai_rmf_risk_tolerance_holder = AiRmfActorAiRmfId(self.ai_rmf_risk_tolerance_holder)

        if not isinstance(self.ai_rmf_risk_tolerance_influences, list):
            self.ai_rmf_risk_tolerance_influences = [self.ai_rmf_risk_tolerance_influences] if self.ai_rmf_risk_tolerance_influences is not None else []
        self.ai_rmf_risk_tolerance_influences = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_risk_tolerance_influences]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfBias(AiRmfRecord):
    """
    A bias to consider and manage, sorted into NIST's three major categories.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Bias"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Bias"
    class_name: ClassVar[str] = "AiRmfBias"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfBias

    ai_rmf_id: Union[str, AiRmfBiasAiRmfId] = None
    ai_rmf_bias_categories: Union[Union[str, "AiRmfBiasCategory"], list[Union[str, "AiRmfBiasCategory"]]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfBiasAiRmfId):
            self.ai_rmf_id = AiRmfBiasAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_bias_categories):
            self.MissingRequiredField("ai_rmf_bias_categories")
        if not isinstance(self.ai_rmf_bias_categories, list):
            self.ai_rmf_bias_categories = [self.ai_rmf_bias_categories] if self.ai_rmf_bias_categories is not None else []
        self.ai_rmf_bias_categories = [v if isinstance(v, AiRmfBiasCategory) else AiRmfBiasCategory(v) for v in self.ai_rmf_bias_categories]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfFunction(YAMLRoot):
    """
    One of the four functions that organize AI risk management at the highest level. GOVERN cuts across the other
    three.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Function"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Function"
    class_name: ClassVar[str] = "AiRmfFunction"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfFunction

    ai_rmf_function_id: Union[str, AiRmfFunctionIdentifier] = None
    description: Optional[str] = None
    ai_rmf_function_categories: Optional[Union[Union[dict, "AiRmfCategory"], list[Union[dict, "AiRmfCategory"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_function_id):
            self.MissingRequiredField("ai_rmf_function_id")
        if not isinstance(self.ai_rmf_function_id, AiRmfFunctionIdentifier):
            self.ai_rmf_function_id = AiRmfFunctionIdentifier(self.ai_rmf_function_id)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="ai_rmf_function_categories", slot_type=AiRmfCategory, key_name="ai_rmf_category_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfCategory(YAMLRoot):
    """
    A group of related outcomes within a function, such as GOVERN 1, which Tables 1 to 4 state.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Category"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Category"
    class_name: ClassVar[str] = "AiRmfCategory"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfCategory

    ai_rmf_category_id: Union[str, AiRmfCategoryIdentifier] = None
    description: str = None
    ai_rmf_category_subcategories: Optional[Union[Union[dict, "AiRmfSubcategory"], list[Union[dict, "AiRmfSubcategory"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_category_id):
            self.MissingRequiredField("ai_rmf_category_id")
        if not isinstance(self.ai_rmf_category_id, AiRmfCategoryIdentifier):
            self.ai_rmf_category_id = AiRmfCategoryIdentifier(self.ai_rmf_category_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        self._normalize_inlined_as_list(slot_name="ai_rmf_category_subcategories", slot_type=AiRmfSubcategory, key_name="ai_rmf_subcategory_id", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfSubcategory(YAMLRoot):
    """
    A specific outcome within a category, such as GOVERN 1.1, which Tables 1 to 4 state, and its Playbook material.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Subcategory"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Subcategory"
    class_name: ClassVar[str] = "AiRmfSubcategory"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfSubcategory

    ai_rmf_subcategory_id: Union[str, AiRmfSubcategoryIdentifier] = None
    description: str = None
    ai_rmf_subcategory_about: Optional[Union[str, list[str]]] = empty_list()
    ai_rmf_subcategory_suggested_actions: Optional[Union[Union[dict, "AiRmfSuggestedAction"], list[Union[dict, "AiRmfSuggestedAction"]]]] = empty_list()
    ai_rmf_subcategory_documentation: Optional[Union[Union[dict, "AiRmfDocumentationItem"], list[Union[dict, "AiRmfDocumentationItem"]]]] = empty_list()
    ai_rmf_subcategory_transparency_resources: Optional[Union[Union[dict, "AiRmfResource"], list[Union[dict, "AiRmfResource"]]]] = empty_list()
    ai_rmf_subcategory_references: Optional[Union[Union[dict, "AiRmfResource"], list[Union[dict, "AiRmfResource"]]]] = empty_list()
    ai_rmf_subcategory_ai_actors: Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]] = empty_list()
    ai_rmf_subcategory_topics: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_subcategory_id):
            self.MissingRequiredField("ai_rmf_subcategory_id")
        if not isinstance(self.ai_rmf_subcategory_id, AiRmfSubcategoryIdentifier):
            self.ai_rmf_subcategory_id = AiRmfSubcategoryIdentifier(self.ai_rmf_subcategory_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.ai_rmf_subcategory_about, list):
            self.ai_rmf_subcategory_about = [self.ai_rmf_subcategory_about] if self.ai_rmf_subcategory_about is not None else []
        self.ai_rmf_subcategory_about = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_subcategory_about]

        self._normalize_inlined_as_list(slot_name="ai_rmf_subcategory_suggested_actions", slot_type=AiRmfSuggestedAction, key_name="ai_rmf_suggested_action_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_subcategory_documentation", slot_type=AiRmfDocumentationItem, key_name="ai_rmf_documentation_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_subcategory_transparency_resources", slot_type=AiRmfResource, key_name="title", keyed=False)

        self._normalize_inlined_as_list(slot_name="ai_rmf_subcategory_references", slot_type=AiRmfResource, key_name="title", keyed=False)

        if not isinstance(self.ai_rmf_subcategory_ai_actors, list):
            self.ai_rmf_subcategory_ai_actors = [self.ai_rmf_subcategory_ai_actors] if self.ai_rmf_subcategory_ai_actors is not None else []
        self.ai_rmf_subcategory_ai_actors = [v if isinstance(v, AiRmfActorTaskName) else AiRmfActorTaskName(v) for v in self.ai_rmf_subcategory_ai_actors]

        if not isinstance(self.ai_rmf_subcategory_topics, list):
            self.ai_rmf_subcategory_topics = [self.ai_rmf_subcategory_topics] if self.ai_rmf_subcategory_topics is not None else []
        self.ai_rmf_subcategory_topics = [v if isinstance(v, str) else str(v) for v in self.ai_rmf_subcategory_topics]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfSuggestedAction(YAMLRoot):
    """
    One step the Playbook suggests towards a subcategory's outcome.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["SuggestedAction"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:SuggestedAction"
    class_name: ClassVar[str] = "AiRmfSuggestedAction"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfSuggestedAction

    ai_rmf_suggested_action_id: Union[str, AiRmfSuggestedActionIdentifier] = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_suggested_action_id):
            self.MissingRequiredField("ai_rmf_suggested_action_id")
        if not isinstance(self.ai_rmf_suggested_action_id, AiRmfSuggestedActionIdentifier):
            self.ai_rmf_suggested_action_id = AiRmfSuggestedActionIdentifier(self.ai_rmf_suggested_action_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfDocumentationItem(YAMLRoot):
    """
    One thing the Playbook suggests an organization document for a subcategory.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["DocumentationItem"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:DocumentationItem"
    class_name: ClassVar[str] = "AiRmfDocumentationItem"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfDocumentationItem

    ai_rmf_documentation_id: Union[str, AiRmfDocumentationIdentifier] = None
    description: str = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_documentation_id):
            self.MissingRequiredField("ai_rmf_documentation_id")
        if not isinstance(self.ai_rmf_documentation_id, AiRmfDocumentationIdentifier):
            self.ai_rmf_documentation_id = AiRmfDocumentationIdentifier(self.ai_rmf_documentation_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfResource(YAMLRoot):
    """
    A source the Playbook points to, by the title and address NIST's catalog gives it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Resource"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Resource"
    class_name: ClassVar[str] = "AiRmfResource"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfResource

    title: str = None
    ai_rmf_resource_uuid: str = None
    ai_rmf_resource_address: Optional[Union[str, URI]] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self._is_empty(self.ai_rmf_resource_uuid):
            self.MissingRequiredField("ai_rmf_resource_uuid")
        if not isinstance(self.ai_rmf_resource_uuid, str):
            self.ai_rmf_resource_uuid = str(self.ai_rmf_resource_uuid)

        if self.ai_rmf_resource_address is not None and not isinstance(self.ai_rmf_resource_address, URI):
            self.ai_rmf_resource_address = URI(self.ai_rmf_resource_address)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class AiRmfProfile(AiRmfRecord):
    """
    An implementation of the Core's functions, categories and subcategories for a setting, application or technology,
    based on the adopter's requirements, risk tolerance and resources.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_100_1["Profile"]
    class_class_curie: ClassVar[str] = "nist_ai_100_1:Profile"
    class_name: ClassVar[str] = "AiRmfProfile"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.AiRmfProfile

    ai_rmf_id: Union[str, AiRmfProfileAiRmfId] = None
    ai_rmf_profile_kinds: Union[Union[str, "AiRmfProfileKind"], list[Union[str, "AiRmfProfileKind"]]] = None
    ai_rmf_profile_setting: Optional[str] = None
    ai_rmf_profile_subcategories: Optional[Union[Union[str, AiRmfSubcategoryIdentifier], list[Union[str, AiRmfSubcategoryIdentifier]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, AiRmfProfileAiRmfId):
            self.ai_rmf_id = AiRmfProfileAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.ai_rmf_profile_kinds):
            self.MissingRequiredField("ai_rmf_profile_kinds")
        if not isinstance(self.ai_rmf_profile_kinds, list):
            self.ai_rmf_profile_kinds = [self.ai_rmf_profile_kinds] if self.ai_rmf_profile_kinds is not None else []
        self.ai_rmf_profile_kinds = [v if isinstance(v, AiRmfProfileKind) else AiRmfProfileKind(v) for v in self.ai_rmf_profile_kinds]

        if self.ai_rmf_profile_setting is not None and not isinstance(self.ai_rmf_profile_setting, str):
            self.ai_rmf_profile_setting = str(self.ai_rmf_profile_setting)

        if not isinstance(self.ai_rmf_profile_subcategories, list):
            self.ai_rmf_profile_subcategories = [self.ai_rmf_profile_subcategories] if self.ai_rmf_profile_subcategories is not None else []
        self.ai_rmf_profile_subcategories = [v if isinstance(v, AiRmfSubcategoryIdentifier) else AiRmfSubcategoryIdentifier(v) for v in self.ai_rmf_profile_subcategories]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiProfile(AiRmfProfile):
    """
    The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["Profile"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:Profile"
    class_name: ClassVar[str] = "GaiProfile"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiProfile

    ai_rmf_id: Union[str, GaiProfileAiRmfId] = None
    ai_rmf_profile_kinds: Union[Union[str, "AiRmfProfileKind"], list[Union[str, "AiRmfProfileKind"]]] = None
    gai_risks: Union[Union[dict, "GaiRisk"], list[Union[dict, "GaiRisk"]]] = None
    gai_subcategories: Union[Union[dict, "GaiSubcategory"], list[Union[dict, "GaiSubcategory"]]] = None
    gai_primary_considerations: Optional[Union[Union[dict, "GaiPrimaryConsideration"], list[Union[dict, "GaiPrimaryConsideration"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_id):
            self.MissingRequiredField("ai_rmf_id")
        if not isinstance(self.ai_rmf_id, GaiProfileAiRmfId):
            self.ai_rmf_id = GaiProfileAiRmfId(self.ai_rmf_id)

        if self._is_empty(self.gai_risks):
            self.MissingRequiredField("gai_risks")
        self._normalize_inlined_as_list(slot_name="gai_risks", slot_type=GaiRisk, key_name="gai_risk_name", keyed=False)

        if self._is_empty(self.gai_subcategories):
            self.MissingRequiredField("gai_subcategories")
        self._normalize_inlined_as_list(slot_name="gai_subcategories", slot_type=GaiSubcategory, key_name="ai_rmf_subcategory_id", keyed=False)

        self._normalize_inlined_as_list(slot_name="gai_primary_considerations", slot_type=GaiPrimaryConsideration, key_name="gai_consideration_type", keyed=False)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiRisk(YAMLRoot):
    """
    A risk that section 2 defines as unique to or made worse by the development and use of GAI.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["Risk"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:Risk"
    class_name: ClassVar[str] = "GaiRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiRisk

    gai_risk_name: Union[str, "GaiRiskName"] = None
    gai_risk_section: str = None
    description: Optional[str] = None
    gai_risk_characteristics: Optional[Union[Union[str, "AiRmfCharacteristicName"], list[Union[str, "AiRmfCharacteristicName"]]]] = empty_list()
    gai_risk_groupings: Optional[Union[Union[str, "GaiRiskGrouping"], list[Union[str, "GaiRiskGrouping"]]]] = empty_list()
    gai_risk_lifecycle_stages: Optional[Union[Union[str, "GaiLifecycleStage"], list[Union[str, "GaiLifecycleStage"]]]] = empty_list()
    gai_risk_scopes: Optional[Union[Union[str, "GaiRiskScope"], list[Union[str, "GaiRiskScope"]]]] = empty_list()
    gai_risk_sources: Optional[Union[Union[str, "GaiRiskSource"], list[Union[str, "GaiRiskSource"]]]] = empty_list()
    gai_risk_time_scales: Optional[Union[Union[str, "GaiRiskTimeScale"], list[Union[str, "GaiRiskTimeScale"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gai_risk_name):
            self.MissingRequiredField("gai_risk_name")
        if not isinstance(self.gai_risk_name, GaiRiskName):
            self.gai_risk_name = GaiRiskName(self.gai_risk_name)

        if self._is_empty(self.gai_risk_section):
            self.MissingRequiredField("gai_risk_section")
        if not isinstance(self.gai_risk_section, str):
            self.gai_risk_section = str(self.gai_risk_section)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.gai_risk_characteristics, list):
            self.gai_risk_characteristics = [self.gai_risk_characteristics] if self.gai_risk_characteristics is not None else []
        self.gai_risk_characteristics = [v if isinstance(v, AiRmfCharacteristicName) else AiRmfCharacteristicName(v) for v in self.gai_risk_characteristics]

        if not isinstance(self.gai_risk_groupings, list):
            self.gai_risk_groupings = [self.gai_risk_groupings] if self.gai_risk_groupings is not None else []
        self.gai_risk_groupings = [v if isinstance(v, GaiRiskGrouping) else GaiRiskGrouping(v) for v in self.gai_risk_groupings]

        if not isinstance(self.gai_risk_lifecycle_stages, list):
            self.gai_risk_lifecycle_stages = [self.gai_risk_lifecycle_stages] if self.gai_risk_lifecycle_stages is not None else []
        self.gai_risk_lifecycle_stages = [v if isinstance(v, GaiLifecycleStage) else GaiLifecycleStage(v) for v in self.gai_risk_lifecycle_stages]

        if not isinstance(self.gai_risk_scopes, list):
            self.gai_risk_scopes = [self.gai_risk_scopes] if self.gai_risk_scopes is not None else []
        self.gai_risk_scopes = [v if isinstance(v, GaiRiskScope) else GaiRiskScope(v) for v in self.gai_risk_scopes]

        if not isinstance(self.gai_risk_sources, list):
            self.gai_risk_sources = [self.gai_risk_sources] if self.gai_risk_sources is not None else []
        self.gai_risk_sources = [v if isinstance(v, GaiRiskSource) else GaiRiskSource(v) for v in self.gai_risk_sources]

        if not isinstance(self.gai_risk_time_scales, list):
            self.gai_risk_time_scales = [self.gai_risk_time_scales] if self.gai_risk_time_scales is not None else []
        self.gai_risk_time_scales = [v if isinstance(v, GaiRiskTimeScale) else GaiRiskTimeScale(v) for v in self.gai_risk_time_scales]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiSubcategory(YAMLRoot):
    """
    An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["Subcategory"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:Subcategory"
    class_name: ClassVar[str] = "GaiSubcategory"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiSubcategory

    ai_rmf_subcategory_id: Union[str, AiRmfSubcategoryIdentifier] = None
    description: str = None
    gai_subcategory_actions: Union[Union[dict, "GaiSuggestedAction"], list[Union[dict, "GaiSuggestedAction"]]] = None
    gai_subcategory_actor_tasks: Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.ai_rmf_subcategory_id):
            self.MissingRequiredField("ai_rmf_subcategory_id")
        if not isinstance(self.ai_rmf_subcategory_id, AiRmfSubcategoryIdentifier):
            self.ai_rmf_subcategory_id = AiRmfSubcategoryIdentifier(self.ai_rmf_subcategory_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if self._is_empty(self.gai_subcategory_actions):
            self.MissingRequiredField("gai_subcategory_actions")
        self._normalize_inlined_as_list(slot_name="gai_subcategory_actions", slot_type=GaiSuggestedAction, key_name="gai_action_id", keyed=False)

        if not isinstance(self.gai_subcategory_actor_tasks, list):
            self.gai_subcategory_actor_tasks = [self.gai_subcategory_actor_tasks] if self.gai_subcategory_actor_tasks is not None else []
        self.gai_subcategory_actor_tasks = [v if isinstance(v, AiRmfActorTaskName) else AiRmfActorTaskName(v) for v in self.gai_subcategory_actor_tasks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiSuggestedAction(YAMLRoot):
    """
    A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["SuggestedAction"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:SuggestedAction"
    class_name: ClassVar[str] = "GaiSuggestedAction"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiSuggestedAction

    gai_action_id: Union[str, GaiActionIdentifier] = None
    description: str = None
    gai_action_risks: Optional[Union[Union[str, "GaiRiskName"], list[Union[str, "GaiRiskName"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gai_action_id):
            self.MissingRequiredField("gai_action_id")
        if not isinstance(self.gai_action_id, GaiActionIdentifier):
            self.gai_action_id = GaiActionIdentifier(self.gai_action_id)

        if self._is_empty(self.description):
            self.MissingRequiredField("description")
        if not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.gai_action_risks, list):
            self.gai_action_risks = [self.gai_action_risks] if self.gai_action_risks is not None else []
        self.gai_action_risks = [v if isinstance(v, GaiRiskName) else GaiRiskName(v) for v in self.gai_action_risks]

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiPrimaryConsideration(YAMLRoot):
    """
    One of the four primary considerations of Appendix A, which also inform the suggested actions.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["PrimaryConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:PrimaryConsideration"
    class_name: ClassVar[str] = "GaiPrimaryConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiPrimaryConsideration

    gai_consideration_type: str = None
    title: str = None
    description: Optional[str] = None
    gai_consideration_sections: Optional[Union[str, list[str]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        if not isinstance(self.gai_consideration_sections, list):
            self.gai_consideration_sections = [self.gai_consideration_sections] if self.gai_consideration_sections is not None else []
        self.gai_consideration_sections = [v if isinstance(v, str) else str(v) for v in self.gai_consideration_sections]

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "gai_consideration_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class GaiGovernanceConsideration(GaiPrimaryConsideration):
    """
    How an organization's governance can be revisited for GAI, including across the AI value chain.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["GovernanceConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:GovernanceConsideration"
    class_name: ClassVar[str] = "GaiGovernanceConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiGovernanceConsideration

    gai_consideration_type: str = None
    title: str = None
    gai_governance_plans: Optional[Union[Union[str, "GaiGovernancePlan"], list[Union[str, "GaiGovernancePlan"]]]] = empty_list()
    gai_third_party_controls: Optional[Union[Union[str, "GaiThirdPartyControl"], list[Union[str, "GaiThirdPartyControl"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gai_governance_plans, list):
            self.gai_governance_plans = [self.gai_governance_plans] if self.gai_governance_plans is not None else []
        self.gai_governance_plans = [v if isinstance(v, GaiGovernancePlan) else GaiGovernancePlan(v) for v in self.gai_governance_plans]

        if not isinstance(self.gai_third_party_controls, list):
            self.gai_third_party_controls = [self.gai_third_party_controls] if self.gai_third_party_controls is not None else []
        self.gai_third_party_controls = [v if isinstance(v, GaiThirdPartyControl) else GaiThirdPartyControl(v) for v in self.gai_third_party_controls]

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)


@dataclass(repr=False)
class GaiPreDeploymentTestingConsideration(GaiPrimaryConsideration):
    """
    How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["PreDeploymentTestingConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:PreDeploymentTestingConsideration"
    class_name: ClassVar[str] = "GaiPreDeploymentTestingConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiPreDeploymentTestingConsideration

    gai_consideration_type: str = None
    title: str = None
    gai_structured_feedback: Optional[Union[Union[dict, "GaiStructuredFeedback"], list[Union[dict, "GaiStructuredFeedback"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        self._normalize_inlined_as_list(slot_name="gai_structured_feedback", slot_type=GaiStructuredFeedback, key_name="gai_feedback_type", keyed=False)

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)


@dataclass(repr=False)
class GaiContentProvenanceConsideration(GaiPrimaryConsideration):
    """
    How tracking the origin and history of content helps tell authentic content from synthetic content.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["ContentProvenanceConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:ContentProvenanceConsideration"
    class_name: ClassVar[str] = "GaiContentProvenanceConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiContentProvenanceConsideration

    gai_consideration_type: str = None
    title: str = None
    gai_provenance_techniques: Optional[Union[Union[str, "GaiProvenanceTechnique"], list[Union[str, "GaiProvenanceTechnique"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gai_provenance_techniques, list):
            self.gai_provenance_techniques = [self.gai_provenance_techniques] if self.gai_provenance_techniques is not None else []
        self.gai_provenance_techniques = [v if isinstance(v, GaiProvenanceTechnique) else GaiProvenanceTechnique(v) for v in self.gai_provenance_techniques]

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)


@dataclass(repr=False)
class GaiIncidentDisclosureConsideration(GaiPrimaryConsideration):
    """
    How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["IncidentDisclosureConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:IncidentDisclosureConsideration"
    class_name: ClassVar[str] = "GaiIncidentDisclosureConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiIncidentDisclosureConsideration

    gai_consideration_type: str = None
    title: str = None
    gai_incident_harms: Optional[Union[Union[str, "GaiIncidentHarm"], list[Union[str, "GaiIncidentHarm"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gai_incident_harms, list):
            self.gai_incident_harms = [self.gai_incident_harms] if self.gai_incident_harms is not None else []
        self.gai_incident_harms = [v if isinstance(v, GaiIncidentHarm) else GaiIncidentHarm(v) for v in self.gai_incident_harms]

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_consideration_type):
            self.MissingRequiredField("gai_consideration_type")
        self.gai_consideration_type = str(self.class_name)


@dataclass(repr=False)
class GaiStructuredFeedback(YAMLRoot):
    """
    A way of using structured public feedback to evaluate whether GAI systems perform as intended.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["StructuredFeedback"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:StructuredFeedback"
    class_name: ClassVar[str] = "GaiStructuredFeedback"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiStructuredFeedback

    gai_feedback_type: str = None
    title: str = None
    description: Optional[str] = None

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.gai_feedback_type):
            self.MissingRequiredField("gai_feedback_type")
        self.gai_feedback_type = str(self.class_name)

        if self._is_empty(self.title):
            self.MissingRequiredField("title")
        if not isinstance(self.title, str):
            self.title = str(self.title)

        if self.description is not None and not isinstance(self.description, str):
            self.description = str(self.description)

        super().__post_init__(**kwargs)


    def __new__(cls, *args, **kwargs):

        type_designator = "gai_feedback_type"
        if not type_designator in kwargs:
            return super().__new__(cls,*args,**kwargs)
        else:
            type_designator_value = kwargs[type_designator]
            target_cls = cls._class_for("class_name", type_designator_value)


            if target_cls is None:
                raise ValueError(f"Wrong type designator value: class {cls.__name__} "
                                 f"has no subclass with ['class_name']='{kwargs[type_designator]}'")
            return super().__new__(target_cls,*args,**kwargs)



@dataclass(repr=False)
class GaiParticipatoryEngagement(GaiStructuredFeedback):
    """
    Asking civil society groups, affected communities and users for feedback, such as through focus groups or surveys.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["ParticipatoryEngagement"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:ParticipatoryEngagement"
    class_name: ClassVar[str] = "GaiParticipatoryEngagement"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiParticipatoryEngagement

    gai_feedback_type: str = None
    title: str = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_feedback_type):
            self.MissingRequiredField("gai_feedback_type")
        self.gai_feedback_type = str(self.class_name)


@dataclass(repr=False)
class GaiFieldTesting(GaiStructuredFeedback):
    """
    Structured settings that show how people interact with and use AI-generated information.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["FieldTesting"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:FieldTesting"
    class_name: ClassVar[str] = "GaiFieldTesting"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiFieldTesting

    gai_feedback_type: str = None
    title: str = None

    def __post_init__(self, *_: str, **kwargs: Any):

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_feedback_type):
            self.MissingRequiredField("gai_feedback_type")
        self.gai_feedback_type = str(self.class_name)


@dataclass(repr=False)
class GaiAiRedTeaming(GaiStructuredFeedback):
    """
    A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_600_1["AiRedTeaming"]
    class_class_curie: ClassVar[str] = "nist_ai_600_1:AiRedTeaming"
    class_name: ClassVar[str] = "GaiAiRedTeaming"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF.GaiAiRedTeaming

    gai_feedback_type: str = None
    title: str = None
    gai_red_teaming_types: Optional[Union[Union[str, "GaiRedTeamingType"], list[Union[str, "GaiRedTeamingType"]]]] = empty_list()

    def __post_init__(self, *_: str, **kwargs: Any):
        if not isinstance(self.gai_red_teaming_types, list):
            self.gai_red_teaming_types = [self.gai_red_teaming_types] if self.gai_red_teaming_types is not None else []
        self.gai_red_teaming_types = [v if isinstance(v, GaiRedTeamingType) else GaiRedTeamingType(v) for v in self.gai_red_teaming_types]

        super().__post_init__(**kwargs)
        if self._is_empty(self.gai_feedback_type):
            self.MissingRequiredField("gai_feedback_type")
        self.gai_feedback_type = str(self.class_name)


# Enumerations
class AiRmfCharacteristicName(EnumDefinitionImpl):
    """
    The seven characteristics of trustworthy AI systems in section 3 of the publication.
    """
    valid_and_reliable = PermissibleValue(
        text="valid_and_reliable",
        title="Valid and Reliable",
        description="""Shown by evidence to meet the needs of its intended use, and works without failure over time. Figure 4 makes it a necessary condition for the others.""")
    safe = PermissibleValue(
        text="safe",
        title="Safe",
        description="Keeps people, property and the environment out of danger under defined conditions.")
    secure_and_resilient = PermissibleValue(
        text="secure_and_resilient",
        title="Secure and Resilient",
        description="""Withstands adverse events and recovers from them, and keeps confidentiality, integrity and availability through protections against attack.""")
    accountable_and_transparent = PermissibleValue(
        text="accountable_and_transparent",
        title="Accountable and Transparent",
        description="""Answerable for outcomes, which rests on people being able to get information about the system and its outputs. Figure 4 shows it relating to all the others.""")
    explainable_and_interpretable = PermissibleValue(
        text="explainable_and_interpretable",
        title="Explainable and Interpretable",
        description="""Its working can be represented (how a decision was made) and its output understood in context (why, and what it means for the user).""")
    privacy_enhanced = PermissibleValue(
        text="privacy_enhanced",
        title="Privacy-Enhanced",
        description="""Guided by the norms and practices that protect human autonomy, identity and dignity, such as anonymity, confidentiality and control.""")
    fair_with_harmful_bias_managed = PermissibleValue(
        text="fair_with_harmful_bias_managed",
        title="Fair – with Harmful Bias Managed",
        description="""Addresses equality and equity, including harmful bias and discrimination, knowing that views of fairness differ across cultures and applications.""")

    _defn = EnumDefinition(
        name="AiRmfCharacteristicName",
        description="The seven characteristics of trustworthy AI systems in section 3 of the publication.",
    )

class AiRmfActorTaskName(EnumDefinitionImpl):
    """
    The ten AI actor tasks and five additional AI actors of Appendix A.
    """
    ai_design = PermissibleValue(
        text="ai_design",
        title="AI Design",
        description="""Setting what the system is for, planning and designing it, and gathering and preparing its data.""")
    ai_development = PermissibleValue(
        text="ai_development",
        title="AI Development",
        description="""Providing the initial infrastructure, and creating, selecting, calibrating, training and testing models.""")
    ai_deployment = PermissibleValue(
        text="ai_deployment",
        title="AI Deployment",
        description="""Deciding how the system is used and putting it into production, including pilots and compliance checks.""")
    operation_and_monitoring = PermissibleValue(
        text="operation_and_monitoring",
        title="Operation and Monitoring",
        description="Running the system and regularly assessing its output and impacts.")
    tevv = PermissibleValue(
        text="tevv",
        title="Test, Evaluation, Verification, and Validation (TEVV)",
        description="""Examining the system or its components and finding and fixing problems, throughout the lifecycle.""")
    human_factors = PermissibleValue(
        text="human_factors",
        title="Human Factors",
        description="""Human-centered design and evaluation, involving end users and bringing context-specific norms and values into design.""")
    domain_expert = PermissibleValue(
        text="domain_expert",
        title="Domain Expert",
        description="Giving knowledge of the sector or setting where the system is used.")
    ai_impact_assessment = PermissibleValue(
        text="ai_impact_assessment",
        title="AI Impact Assessment",
        description="Assessing accountability, harmful bias, impacts, product safety, liability and security.")
    procurement = PermissibleValue(
        text="procurement",
        title="Procurement",
        description="Acquiring AI from another party, under financial, legal or policy authority.")
    governance_and_oversight = PermissibleValue(
        text="governance_and_oversight",
        title="Governance and Oversight",
        description="""Holding management, fiduciary and legal authority for the organization where the system is designed, developed or deployed.""")
    third_party_entities = PermissibleValue(
        text="third_party_entities",
        title="Third-party entities",
        description="""Outside organizations that supply or evaluate the data, models, systems or services an organization acquires.""")
    end_users = PermissibleValue(
        text="end_users",
        title="End users",
        description="The people or groups who use the system, whether new to technology or expert in AI.")
    affected_individuals_and_communities = PermissibleValue(
        text="affected_individuals_and_communities",
        title="Affected individuals/communities",
        description="""Those directly or indirectly affected by the system or its output, whether or not they interact with it.""")
    other_ai_actors = PermissibleValue(
        text="other_ai_actors",
        title="Other AI actors",
        description="""Those who may provide norms or guidance on AI risk, such as standards bodies, advocacy groups and researchers.""")
    general_public = PermissibleValue(
        text="general_public",
        title="General public",
        description="""Those most likely to experience the impacts directly, who may motivate what other AI actors do.""")

    _defn = EnumDefinition(
        name="AiRmfActorTaskName",
        description="The ten AI actor tasks and five additional AI actors of Appendix A.",
    )

class AiRmfDimensionName(EnumDefinitionImpl):
    """
    The key dimensions of an AI system in Figure 2.
    """
    application_context = PermissibleValue(
        text="application_context",
        title="Application Context",
        description="The setting the system is planned for and operated in.")
    data_and_input = PermissibleValue(
        text="data_and_input",
        title="Data and Input",
        description="The data the system is built from and takes in.")
    ai_model = PermissibleValue(
        text="ai_model",
        title="AI Model",
        description="The models built, used, verified and validated.")
    task_and_output = PermissibleValue(
        text="task_and_output",
        title="Task and Output",
        description="What the system does and produces once deployed.")
    people_and_planet = PermissibleValue(
        text="people_and_planet",
        title="People and Planet",
        description="Human rights and the well-being of society and the planet, at the center of Figure 2.")

    _defn = EnumDefinition(
        name="AiRmfDimensionName",
        description="The key dimensions of an AI system in Figure 2.",
    )

class AiRmfLifecycleStageName(EnumDefinitionImpl):
    """
    The AI lifecycle stages in Figure 3, of which Figure 2 shows the first six.
    """
    plan_and_design = PermissibleValue(
        text="plan_and_design",
        title="Plan and Design",
        description="Documenting the concept, objectives, assumptions, context and requirements.")
    collect_and_process_data = PermissibleValue(
        text="collect_and_process_data",
        title="Collect and Process Data",
        description="Gathering, validating and cleaning data, and recording what it holds.")
    build_and_use_model = PermissibleValue(
        text="build_and_use_model",
        title="Build and Use Model",
        description="Creating or selecting algorithms and training models.")
    verify_and_validate = PermissibleValue(
        text="verify_and_validate",
        title="Verify and Validate",
        description="Verifying, validating, calibrating and interpreting model output.")
    deploy_and_use = PermissibleValue(
        text="deploy_and_use",
        title="Deploy and Use",
        description="""Piloting, checking compatibility and compliance, managing change and evaluating user experience.""")
    operate_and_monitor = PermissibleValue(
        text="operate_and_monitor",
        title="Operate and Monitor",
        description="Operating the system and continually assessing its recommendations and impacts.")
    use_or_impacted_by = PermissibleValue(
        text="use_or_impacted_by",
        title="Use or Impacted by",
        description="Using the technology or being affected by it, which Figure 3 places under People and Planet.")

    _defn = EnumDefinition(
        name="AiRmfLifecycleStageName",
        description="The AI lifecycle stages in Figure 3, of which Figure 2 shows the first six.",
    )

class AiRmfAudience(EnumDefinitionImpl):
    """
    The two AI RMF audiences of section 2.
    """
    primary = PermissibleValue(
        text="primary",
        title="Primary audience",
        description="AI actors who carry out or manage work on AI systems and drive their risk management.")
    informing = PermissibleValue(
        text="informing",
        title="Informing audience",
        description="AI actors in the People and Planet dimension, who inform the primary audience.")

    _defn = EnumDefinition(
        name="AiRmfAudience",
        description="The two AI RMF audiences of section 2.",
    )

class AiRmfManagementChallengeName(EnumDefinitionImpl):
    """
    The challenges for AI risk management in section 1.2.
    """
    risk_measurement = PermissibleValue(
        text="risk_measurement",
        title="Risk Measurement",
        description="""AI risks that are poorly defined or understood are hard to measure, which does not mean they are high or low.""")
    risk_tolerance = PermissibleValue(
        text="risk_tolerance",
        title="Risk Tolerance",
        description="""The AI RMF can prioritize risk but prescribes no tolerance, which depends on context and changes over time.""")
    risk_prioritization = PermissibleValue(
        text="risk_prioritization",
        title="Risk Prioritization",
        description="""Eliminating all negative risk is unrealistic, so effort goes first to the highest risks in a context of use.""")
    organizational_integration_and_management_of_risk = PermissibleValue(
        text="organizational_integration_and_management_of_risk",
        title="Organizational Integration and Management of Risk",
        description="""AI risk belongs inside broader enterprise risk management, with accountability and commitment from senior levels.""")

    _defn = EnumDefinition(
        name="AiRmfManagementChallengeName",
        description="The challenges for AI risk management in section 1.2.",
    )

class AiRmfMeasurementChallengeName(EnumDefinitionImpl):
    """
    The challenges of measuring AI risk in section 1.2.1.
    """
    third_party_software_hardware_and_data = PermissibleValue(
        text="third_party_software_hardware_and_data",
        title="Risks related to third-party software, hardware, and data",
        description="""Third-party parts can speed work, but their metrics may not match or be disclosed, and how they are used adds risk.""")
    tracking_emergent_risks = PermissibleValue(
        text="tracking_emergent_risks",
        title="Tracking emergent risks",
        description="New risks need identifying, tracking and measuring, which impact assessment helps with.")
    availability_of_reliable_metrics = PermissibleValue(
        text="availability_of_reliable_metrics",
        title="Availability of reliable metrics",
        description="""There is no consensus on robust, verifiable methods, and metrics can be oversimplified or gamed.""")
    risk_at_different_lifecycle_stages = PermissibleValue(
        text="risk_at_different_lifecycle_stages",
        title="Risk at different stages of the AI lifecycle",
        description="Results differ by stage, some risks stay latent, and AI actors see risk differently.")
    risk_in_real_world_settings = PermissibleValue(
        text="risk_in_real_world_settings",
        title="Risk in real-world settings",
        description="What a laboratory measures may differ from what emerges in operation.")
    inscrutability = PermissibleValue(
        text="inscrutability",
        title="Inscrutability",
        description="Opaque systems, poor documentation and inherent uncertainty complicate measurement.")
    human_baseline = PermissibleValue(
        text="human_baseline",
        title="Human baseline",
        description="""A system that augments or replaces human activity needs a baseline, which is hard to systematize.""")

    _defn = EnumDefinition(
        name="AiRmfMeasurementChallengeName",
        description="The challenges of measuring AI risk in section 1.2.1.",
    )

class AiRmfRiskResponse(EnumDefinitionImpl):
    """
    The risk response options MANAGE 1.3 names.
    """
    mitigating = PermissibleValue(
        text="mitigating",
        title="Mitigating",
        description="Reducing the likelihood or magnitude of the risk.")
    transferring = PermissibleValue(
        text="transferring",
        title="Transferring",
        description="Shifting the risk to another party.")
    avoiding = PermissibleValue(
        text="avoiding",
        title="Avoiding",
        description="Not carrying out what creates the risk.")
    accepting = PermissibleValue(
        text="accepting",
        title="Accepting",
        description="Bearing the risk without further action.")

    _defn = EnumDefinition(
        name="AiRmfRiskResponse",
        description="The risk response options MANAGE 1.3 names.",
    )

class AiRmfImpactDirection(EnumDefinitionImpl):
    """
    Whether an impact is positive, negative or both, as section 1.1 puts it.
    """
    positive = PermissibleValue(
        text="positive",
        title="Positive",
        description="An opportunity or benefit.")
    negative = PermissibleValue(
        text="negative",
        title="Negative",
        description="A threat or harm.")
    both = PermissibleValue(
        text="both",
        title="Both",
        description="Positive and negative at once.")

    _defn = EnumDefinition(
        name="AiRmfImpactDirection",
        description="Whether an impact is positive, negative or both, as section 1.1 puts it.",
    )

class AiRmfAffectedParty(EnumDefinitionImpl):
    """
    Who section 1.1 says can experience negative impact or harm.
    """
    individuals = PermissibleValue(
        text="individuals",
        title="Individuals",
        description="Particular people.")
    groups = PermissibleValue(
        text="groups",
        title="Groups",
        description="Groups of people.")
    communities = PermissibleValue(
        text="communities",
        title="Communities",
        description="Communities of people.")
    organizations = PermissibleValue(
        text="organizations",
        title="Organizations",
        description="Organizations.")
    society = PermissibleValue(
        text="society",
        title="Society",
        description="Society at large.")
    environment = PermissibleValue(
        text="environment",
        title="The environment",
        description="The natural environment.")
    planet = PermissibleValue(
        text="planet",
        title="The planet",
        description="The planet as a whole.")

    _defn = EnumDefinition(
        name="AiRmfAffectedParty",
        description="Who section 1.1 says can experience negative impact or harm.",
    )

class AiRmfHarmCategory(EnumDefinitionImpl):
    """
    The three headings of Figure 1.
    """
    people = PermissibleValue(
        text="people",
        title="Harm to People",
        description="Harm that falls on individuals, groups, communities or society.")
    organization = PermissibleValue(
        text="organization",
        title="Harm to an Organization",
        description="Harm that falls on an organization.")
    ecosystem = PermissibleValue(
        text="ecosystem",
        title="Harm to an Ecosystem",
        description="Harm that falls on interconnected systems and resources.")

    _defn = EnumDefinition(
        name="AiRmfHarmCategory",
        description="The three headings of Figure 1.",
    )

class AiRmfHarmExample(EnumDefinitionImpl):
    """
    The examples of potential harm in Figure 1, which NIST offers as examples and not as a closed list.
    """
    individual = PermissibleValue(
        text="individual",
        title="Individual",
        description="To a person's civil liberties, rights, safety or economic opportunity.")
    group_or_community = PermissibleValue(
        text="group_or_community",
        title="Group/Community",
        description="To a group, such as discrimination against a sub-group of a population.")
    societal = PermissibleValue(
        text="societal",
        title="Societal",
        description="To democratic participation or educational access.")
    business_operations = PermissibleValue(
        text="business_operations",
        title="Business operations",
        description="To how an organization operates.")
    security_breach_or_monetary_loss = PermissibleValue(
        text="security_breach_or_monetary_loss",
        title="Security breaches or monetary loss",
        description="To an organization through a breach of security or a loss of money.")
    reputation = PermissibleValue(
        text="reputation",
        title="Reputation",
        description="To an organization's standing.")
    interdependent_elements = PermissibleValue(
        text="interdependent_elements",
        title="Interconnected and interdependent elements and resources",
        description="To parts and resources that depend on each other.")
    financial_or_supply_systems = PermissibleValue(
        text="financial_or_supply_systems",
        title="Global financial system, supply chain, or interrelated systems",
        description="To large systems that link organizations.")
    natural_resources_and_environment = PermissibleValue(
        text="natural_resources_and_environment",
        title="Natural resources, the environment, and planet",
        description="To the natural world.")

    _defn = EnumDefinition(
        name="AiRmfHarmExample",
        description="The examples of potential harm in Figure 1, which NIST offers as examples and not as a closed list.",
    )

class AiRmfBiasCategory(EnumDefinitionImpl):
    """
    The three major categories of AI bias in section 3.7, each of which can occur without prejudice or discriminatory
    intent.
    """
    systemic = PermissibleValue(
        text="systemic",
        title="Systemic",
        description="In datasets, in organizational norms and processes, and in the wider society that uses AI.")
    computational_and_statistical = PermissibleValue(
        text="computational_and_statistical",
        title="Computational and statistical",
        description="""In datasets and algorithms, often from systematic errors due to samples that are not representative.""")
    human_cognitive = PermissibleValue(
        text="human_cognitive",
        title="Human-cognitive",
        description="In how people perceive system information to decide, or think about what a system is for.")

    _defn = EnumDefinition(
        name="AiRmfBiasCategory",
        description="""The three major categories of AI bias in section 3.7, each of which can occur without prejudice or discriminatory intent.""",
    )

class AiRmfProfileKind(EnumDefinitionImpl):
    """
    The kinds of AI RMF profile that section 6 names.
    """
    use_case = PermissibleValue(
        text="use_case",
        title="Use-case profile",
        description="The Core implemented for a specific setting or application.")
    current = PermissibleValue(
        text="current",
        title="Current Profile",
        description="""A temporal profile saying how AI is managed today and the related risks, in terms of current outcomes.""")
    target = PermissibleValue(
        text="target",
        title="Target Profile",
        description="A temporal profile saying which outcomes the desired risk management goals need.")
    cross_sectoral = PermissibleValue(
        text="cross_sectoral",
        title="Cross-sectoral profile",
        description="""Covers risks of models or applications used across use cases or sectors, or activities common to them, such as using large language models.""")

    _defn = EnumDefinition(
        name="AiRmfProfileKind",
        description="The kinds of AI RMF profile that section 6 names.",
    )

class GaiRiskName(EnumDefinitionImpl):
    """
    The 12 risks of section 2.
    """
    cbrn_information_or_capabilities = PermissibleValue(
        text="cbrn_information_or_capabilities",
        title="CBRN Information or Capabilities",
        description="""Easier access to dangerous information or design abilities for chemical, biological, radiological or nuclear weapons.""")
    confabulation = PermissibleValue(
        text="confabulation",
        title="Confabulation",
        description="Confident but wrong output that can mislead users.")
    dangerous_violent_or_hateful_content = PermissibleValue(
        text="dangerous_violent_or_hateful_content",
        title="Dangerous, Violent, or Hateful Content",
        description="Easier production of content that incites or threatens, recommends harm, or disparages.")
    data_privacy = PermissibleValue(
        text="data_privacy",
        title="Data Privacy",
        description="Leaks, misuse or de-anonymization of personal or sensitive data.")
    environmental_impacts = PermissibleValue(
        text="environmental_impacts",
        title="Environmental Impacts",
        description="Effects on ecosystems from the heavy computing that training and operating models need.")
    harmful_bias_or_homogenization = PermissibleValue(
        text="harmful_bias_or_homogenization",
        title="Harmful Bias or Homogenization",
        description="""Worse systemic bias, unequal performance across groups or languages, and output skewed by sameness.""")
    human_ai_configuration = PermissibleValue(
        text="human_ai_configuration",
        title="Human-AI Configuration",
        description="""Interaction that leads people to over-rely on, anthropomorphize or become entangled with a system, or to distrust it.""")
    information_integrity = PermissibleValue(
        text="information_integrity",
        title="Information Integrity",
        description="""Easier creation and spread of content that blurs fact and opinion, or that can drive large disinformation campaigns.""")
    information_security = PermissibleValue(
        text="information_security",
        title="Information Security",
        description="""Easier offensive cyber activity, and a larger attack surface on a system, its data, code or weights.""")
    intellectual_property = PermissibleValue(
        text="intellectual_property",
        title="Intellectual Property",
        description="Easier unauthorized copying of protected content, exposure of trade secrets, and plagiarism.")
    obscene_degrading_or_abusive_content = PermissibleValue(
        text="obscene_degrading_or_abusive_content",
        title="Obscene, Degrading, and/or Abusive Content",
        description="""Easier production of harmful imagery, including synthetic abuse material and intimate images without consent.""")
    value_chain_and_component_integration = PermissibleValue(
        text="value_chain_and_component_integration",
        title="Value Chain and Component Integration",
        description="""Opaque use of third-party components and data, and poor supplier vetting, that weaken accountability downstream.""")

    _defn = EnumDefinition(
        name="GaiRiskName",
        description="The 12 risks of section 2.",
    )

class GaiRiskGrouping(EnumDefinitionImpl):
    """
    The three groups into which footnote 5 says an organization could sort the risks, as one possible way.
    """
    technical_or_model = PermissibleValue(
        text="technical_or_model",
        title="Technical / Model risks",
        description="Risks from malfunction.")
    misuse_by_humans = PermissibleValue(
        text="misuse_by_humans",
        title="Misuse by humans",
        description="Risks from malicious use.")
    ecosystem_or_societal = PermissibleValue(
        text="ecosystem_or_societal",
        title="Ecosystem / societal risks",
        description="Systemic risks.")

    _defn = EnumDefinition(
        name="GaiRiskGrouping",
        description="""The three groups into which footnote 5 says an organization could sort the risks, as one possible way.""",
    )

class GaiLifecycleStage(EnumDefinitionImpl):
    """
    The lifecycle stages section 2 names for GAI. They differ from the seven stages of the AI RMF's Figure 3.
    """
    design = PermissibleValue(
        text="design",
        title="Design",
        description="Setting out the system before it is built.")
    development = PermissibleValue(
        text="development",
        title="Development",
        description="Building and training it.")
    deployment = PermissibleValue(
        text="deployment",
        title="Deployment",
        description="Putting it into use.")
    operation = PermissibleValue(
        text="operation",
        title="Operation",
        description="Running it.")
    decommissioning = PermissibleValue(
        text="decommissioning",
        title="Decommissioning",
        description="Retiring it.")

    _defn = EnumDefinition(
        name="GaiLifecycleStage",
        description="""The lifecycle stages section 2 names for GAI. They differ from the seven stages of the AI RMF's Figure 3.""",
    )

class GaiRiskScope(EnumDefinitionImpl):
    """
    The levels where section 2 says a risk may exist.
    """
    model_or_system = PermissibleValue(
        text="model_or_system",
        title="Model or system",
        description="The level of one model or system.")
    application_or_implementation = PermissibleValue(
        text="application_or_implementation",
        title="Application or implementation",
        description="The level of one specific use case.")
    ecosystem = PermissibleValue(
        text="ecosystem",
        title="Ecosystem",
        description="""Beyond one system or organization, such as algorithmic monocultures or effects on labor markets.""")

    _defn = EnumDefinition(
        name="GaiRiskScope",
        description="The levels where section 2 says a risk may exist.",
    )

class GaiRiskSource(EnumDefinitionImpl):
    """
    Where section 2 says a risk may come from.
    """
    design = PermissibleValue(
        text="design",
        title="Design",
        description="The design of the model itself.")
    training = PermissibleValue(
        text="training",
        title="Training",
        description="The training of the model.")
    operation = PermissibleValue(
        text="operation",
        title="Operation",
        description="The operation of the model.")
    inputs = PermissibleValue(
        text="inputs",
        title="Inputs",
        description="What goes into the model or system.")
    outputs = PermissibleValue(
        text="outputs",
        title="Outputs",
        description="What the system produces.")
    human_behavior = PermissibleValue(
        text="human_behavior",
        title="Human behavior",
        description="Abuse, misuse or unsafe repurposing by people, whether adversarial or not.")
    human_ai_interaction = PermissibleValue(
        text="human_ai_interaction",
        title="Human-AI interaction",
        description="How a person and a system act on each other.")

    _defn = EnumDefinition(
        name="GaiRiskSource",
        description="Where section 2 says a risk may come from.",
    )

class GaiRiskTimeScale(EnumDefinitionImpl):
    """
    How section 2 says a risk may materialize over time.
    """
    abrupt = PermissibleValue(
        text="abrupt",
        title="Abruptly",
        description="All at once, such as immediate emotional harm from a harmful deepfake image.")
    extended = PermissibleValue(
        text="extended",
        title="Across extended periods",
        description="Slowly, such as the long-term effect of disinformation on trust in institutions.")

    _defn = EnumDefinition(
        name="GaiRiskTimeScale",
        description="How section 2 says a risk may materialize over time.",
    )

class GaiGovernancePlan(EnumDefinitionImpl):
    """
    The plans and actions that section A.1.2 says apply to GAI from other AI governance.
    """
    accessibility_and_reasonable_accommodations = PermissibleValue(
        text="accessibility_and_reasonable_accommodations",
        title="Accessibility and reasonable accommodations")
    ai_actor_credentials_and_qualifications = PermissibleValue(
        text="ai_actor_credentials_and_qualifications",
        title="AI actor credentials and qualifications")
    alignment_to_organizational_values = PermissibleValue(
        text="alignment_to_organizational_values",
        title="Alignment to organizational values")
    auditing_and_assessment = PermissibleValue(
        text="auditing_and_assessment",
        title="Auditing and assessment")
    change_management_controls = PermissibleValue(
        text="change_management_controls",
        title="Change-management controls")
    commercial_use = PermissibleValue(
        text="commercial_use",
        title="Commercial use")
    data_provenance = PermissibleValue(
        text="data_provenance",
        title="Data provenance")
    data_protection = PermissibleValue(
        text="data_protection",
        title="Data protection")
    data_retention = PermissibleValue(
        text="data_retention",
        title="Data retention")
    consistency_in_use_of_defining_key_terms = PermissibleValue(
        text="consistency_in_use_of_defining_key_terms",
        title="Consistency in use of defining key terms")
    decommissioning = PermissibleValue(
        text="decommissioning",
        title="Decommissioning")
    discouraging_anonymous_use = PermissibleValue(
        text="discouraging_anonymous_use",
        title="Discouraging anonymous use")
    education = PermissibleValue(
        text="education",
        title="Education")
    impact_assessments = PermissibleValue(
        text="impact_assessments",
        title="Impact assessments")
    incident_response = PermissibleValue(
        text="incident_response",
        title="Incident response")
    monitoring = PermissibleValue(
        text="monitoring",
        title="Monitoring")
    opt_outs = PermissibleValue(
        text="opt_outs",
        title="Opt-outs")
    risk_based_controls = PermissibleValue(
        text="risk_based_controls",
        title="Risk-based controls")
    risk_mapping_and_measurement = PermissibleValue(
        text="risk_mapping_and_measurement",
        title="Risk mapping and measurement")
    science_backed_tevv_practices = PermissibleValue(
        text="science_backed_tevv_practices",
        title="Science-backed TEVV practices")
    secure_software_development_practices = PermissibleValue(
        text="secure_software_development_practices",
        title="Secure software development practices")
    stakeholder_engagement = PermissibleValue(
        text="stakeholder_engagement",
        title="Stakeholder engagement")
    synthetic_content_detection_and_labeling_tools_and_techniques = PermissibleValue(
        text="synthetic_content_detection_and_labeling_tools_and_techniques",
        title="Synthetic content detection and labeling tools and techniques")
    whistleblower_protections = PermissibleValue(
        text="whistleblower_protections",
        title="Whistleblower protections")
    workforce_diversity_and_interdisciplinary_teams = PermissibleValue(
        text="workforce_diversity_and_interdisciplinary_teams",
        title="Workforce diversity and interdisciplinary teams")

    _defn = EnumDefinition(
        name="GaiGovernancePlan",
        description="The plans and actions that section A.1.2 says apply to GAI from other AI governance.",
    )

class GaiThirdPartyControl(EnumDefinitionImpl):
    """
    The existing controls that section A.1.3 says can apply to third-party GAI.
    """
    acquisition_and_procurement_due_diligence = PermissibleValue(
        text="acquisition_and_procurement_due_diligence",
        title="Acquisition and procurement due diligence",
        description="Checking a provider before acquiring its GAI technology or data.")
    software_bills_of_materials = PermissibleValue(
        text="software_bills_of_materials",
        title="Requests for software bills of materials",
        description="Asking a provider what its software is made of.")
    service_level_agreements = PermissibleValue(
        text="service_level_agreements",
        title="Application of service level agreements",
        description="Holding a provider to agreed levels of service.")
    ssae_reports = PermissibleValue(
        text="ssae_reports",
        title="Statement on standards for attestation engagement reports",
        description="Asking for a provider's attestation reports.")

    _defn = EnumDefinition(
        name="GaiThirdPartyControl",
        description="The existing controls that section A.1.3 says can apply to third-party GAI.",
    )

class GaiRedTeamingType(EnumDefinitionImpl):
    """
    The types of AI red-teaming in section A.1.5.
    """
    general_public = PermissibleValue(
        text="general_public",
        title="General Public",
        description="By general users who are not necessarily AI or technical experts.")
    expert = PermissibleValue(
        text="expert",
        title="Expert",
        description="By specialists in the domain or the context of use.")
    combination = PermissibleValue(
        text="combination",
        title="Combination",
        description="By both experts and general public participants.")
    human_ai = PermissibleValue(
        text="human_ai",
        title="Human / AI",
        description="By GAI together with human teams, specialist or not.")

    _defn = EnumDefinition(
        name="GaiRedTeamingType",
        description="The types of AI red-teaming in section A.1.5.",
    )

class GaiProvenanceTechnique(EnumDefinitionImpl):
    """
    The techniques for provenance data tracking in section A.1.6.
    """
    digital_watermarking = PermissibleValue(
        text="digital_watermarking",
        title="Digital watermarking",
        description="Placing visible or hidden marks on content.")
    metadata_recording = PermissibleValue(
        text="metadata_recording",
        title="Metadata recording",
        description="Recording facts about the content, such as its creator, date and sources.")
    digital_fingerprinting = PermissibleValue(
        text="digital_fingerprinting",
        title="Digital fingerprinting",
        description="Identifying content from its own characteristics.")
    human_authentication = PermissibleValue(
        text="human_authentication",
        title="Human authentication",
        description="Having people confirm where content came from.")

    _defn = EnumDefinition(
        name="GaiProvenanceTechnique",
        description="The techniques for provenance data tracking in section A.1.6.",
    )

class GaiIncidentHarm(EnumDefinitionImpl):
    """
    The kinds of harm that section A.1.8's definition of an AI incident names.
    """
    injury_or_harm_to_health = PermissibleValue(
        text="injury_or_harm_to_health",
        title="Injury or harm to health",
        description="To a person or group, including psychological harm and harm to mental health.")
    critical_infrastructure_disruption = PermissibleValue(
        text="critical_infrastructure_disruption",
        title="Disruption of critical infrastructure",
        description="To its management and operation.")
    rights_violations = PermissibleValue(
        text="rights_violations",
        title="Violations of rights or legal obligations",
        description="""Of human rights, or of obligations under law that protects fundamental, labor and intellectual property rights.""")
    harm_to_property_communities_or_environment = PermissibleValue(
        text="harm_to_property_communities_or_environment",
        title="Harm to property, communities, or the environment",
        description="To things and groups beyond the individual.")

    _defn = EnumDefinition(
        name="GaiIncidentHarm",
        description="The kinds of harm that section A.1.8's definition of an AI incident names.",
    )

# Slots
class slots:
    pass

slots.ai_rmf_id = Slot(uri=NIST_AI_100_1.ai_rmf_id, name="ai_rmf_id", curie=NIST_AI_100_1.curie('ai_rmf_id'),
                   model_uri=NIST_AI_RMF.ai_rmf_id, domain=None, range=URIRef)

slots.ai_rmf_subcategory_id = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_id, name="ai_rmf_subcategory_id", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_id'),
                   model_uri=NIST_AI_RMF.ai_rmf_subcategory_id, domain=None, range=Union[str, AiRmfSubcategoryIdentifier])

slots.title = Slot(uri=SCHEMA.name, name="title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_RMF.title, domain=None, range=Optional[str])

slots.description = Slot(uri=SCHEMA.description, name="description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.description, domain=None, range=Optional[str])

slots.ai_rmf_likelihood = Slot(uri=NIST_AI_100_1.ai_rmf_likelihood, name="ai_rmf_likelihood", curie=NIST_AI_100_1.curie('ai_rmf_likelihood'),
                   model_uri=NIST_AI_RMF.ai_rmf_likelihood, domain=None, range=Optional[str])

slots.ai_rmf_magnitude = Slot(uri=NIST_AI_100_1.ai_rmf_magnitude, name="ai_rmf_magnitude", curie=NIST_AI_100_1.curie('ai_rmf_magnitude'),
                   model_uri=NIST_AI_RMF.ai_rmf_magnitude, domain=None, range=Optional[str])

slots.ai_rmf_function_id = Slot(uri=NIST_AI_100_1.ai_rmf_function_id, name="ai_rmf_function_id", curie=NIST_AI_100_1.curie('ai_rmf_function_id'),
                   model_uri=NIST_AI_RMF.ai_rmf_function_id, domain=None, range=Union[str, AiRmfFunctionIdentifier])

slots.ai_rmf_category_id = Slot(uri=NIST_AI_100_1.ai_rmf_category_id, name="ai_rmf_category_id", curie=NIST_AI_100_1.curie('ai_rmf_category_id'),
                   model_uri=NIST_AI_RMF.ai_rmf_category_id, domain=None, range=Union[str, AiRmfCategoryIdentifier])

slots.ai_rmf_suggested_action_id = Slot(uri=NIST_AI_100_1.ai_rmf_suggested_action_id, name="ai_rmf_suggested_action_id", curie=NIST_AI_100_1.curie('ai_rmf_suggested_action_id'),
                   model_uri=NIST_AI_RMF.ai_rmf_suggested_action_id, domain=None, range=Union[str, AiRmfSuggestedActionIdentifier])

slots.ai_rmf_documentation_id = Slot(uri=NIST_AI_100_1.ai_rmf_documentation_id, name="ai_rmf_documentation_id", curie=NIST_AI_100_1.curie('ai_rmf_documentation_id'),
                   model_uri=NIST_AI_RMF.ai_rmf_documentation_id, domain=None, range=Union[str, AiRmfDocumentationIdentifier])

slots.gai_action_id = Slot(uri=NIST_AI_600_1.gai_action_id, name="gai_action_id", curie=NIST_AI_600_1.curie('gai_action_id'),
                   model_uri=NIST_AI_RMF.gai_action_id, domain=None, range=Union[str, GaiActionIdentifier])

slots.gai_consideration_type = Slot(uri=NIST_AI_600_1.gai_consideration_type, name="gai_consideration_type", curie=NIST_AI_600_1.curie('gai_consideration_type'),
                   model_uri=NIST_AI_RMF.gai_consideration_type, domain=None, range=str)

slots.gai_feedback_type = Slot(uri=NIST_AI_600_1.gai_feedback_type, name="gai_feedback_type", curie=NIST_AI_600_1.curie('gai_feedback_type'),
                   model_uri=NIST_AI_RMF.gai_feedback_type, domain=None, range=str)

slots.nistAiRmfFamily__nist_ai_rmf_framework = Slot(uri=NIST_AI_RMF.nist_ai_rmf_framework, name="nistAiRmfFamily__nist_ai_rmf_framework", curie=NIST_AI_RMF.curie('nist_ai_rmf_framework'),
                   model_uri=NIST_AI_RMF.nistAiRmfFamily__nist_ai_rmf_framework, domain=None, range=Optional[Union[dict, AiRmfFramework]])

slots.nistAiRmfFamily__nist_ai_rmf_generative_ai_profile = Slot(uri=NIST_AI_RMF.nist_ai_rmf_generative_ai_profile, name="nistAiRmfFamily__nist_ai_rmf_generative_ai_profile", curie=NIST_AI_RMF.curie('nist_ai_rmf_generative_ai_profile'),
                   model_uri=NIST_AI_RMF.nistAiRmfFamily__nist_ai_rmf_generative_ai_profile, domain=None, range=Optional[Union[dict, GaiProfile]])

slots.aiRmfFramework__ai_rmf_version = Slot(uri=NIST_AI_100_1.ai_rmf_version, name="aiRmfFramework__ai_rmf_version", curie=NIST_AI_100_1.curie('ai_rmf_version'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_version, domain=None, range=str,
                   pattern=re.compile(r'^[0-9]+\.[0-9]+$'))

slots.aiRmfFramework__ai_rmf_functions = Slot(uri=NIST_AI_100_1.ai_rmf_functions, name="aiRmfFramework__ai_rmf_functions", curie=NIST_AI_100_1.curie('ai_rmf_functions'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_functions, domain=None, range=Union[Union[dict, AiRmfFunction], list[Union[dict, AiRmfFunction]]])

slots.aiRmfFramework__ai_rmf_characteristics = Slot(uri=NIST_AI_100_1.ai_rmf_characteristics, name="aiRmfFramework__ai_rmf_characteristics", curie=NIST_AI_100_1.curie('ai_rmf_characteristics'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_characteristics, domain=None, range=Optional[Union[Union[dict, AiRmfTrustworthinessCharacteristic], list[Union[dict, AiRmfTrustworthinessCharacteristic]]]])

slots.aiRmfFramework__ai_rmf_dimensions = Slot(uri=NIST_AI_100_1.ai_rmf_dimensions, name="aiRmfFramework__ai_rmf_dimensions", curie=NIST_AI_100_1.curie('ai_rmf_dimensions'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_dimensions, domain=None, range=Optional[Union[Union[dict, AiRmfDimension], list[Union[dict, AiRmfDimension]]]])

slots.aiRmfFramework__ai_rmf_lifecycle_stages = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stages, name="aiRmfFramework__ai_rmf_lifecycle_stages", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stages'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_lifecycle_stages, domain=None, range=Optional[Union[Union[dict, AiRmfLifecycleStage], list[Union[dict, AiRmfLifecycleStage]]]])

slots.aiRmfFramework__ai_rmf_actor_task_list = Slot(uri=NIST_AI_100_1.ai_rmf_actor_task_list, name="aiRmfFramework__ai_rmf_actor_task_list", curie=NIST_AI_100_1.curie('ai_rmf_actor_task_list'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_actor_task_list, domain=None, range=Optional[Union[Union[dict, AiRmfActorTask], list[Union[dict, AiRmfActorTask]]]])

slots.aiRmfFramework__ai_rmf_management_challenges = Slot(uri=NIST_AI_100_1.ai_rmf_management_challenges, name="aiRmfFramework__ai_rmf_management_challenges", curie=NIST_AI_100_1.curie('ai_rmf_management_challenges'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_management_challenges, domain=None, range=Optional[Union[Union[dict, AiRmfManagementChallenge], list[Union[dict, AiRmfManagementChallenge]]]])

slots.aiRmfFramework__ai_rmf_specific_risks = Slot(uri=NIST_AI_100_1.ai_rmf_specific_risks, name="aiRmfFramework__ai_rmf_specific_risks", curie=NIST_AI_100_1.curie('ai_rmf_specific_risks'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_specific_risks, domain=None, range=Optional[Union[Union[dict, AiRmfSpecificRisk], list[Union[dict, AiRmfSpecificRisk]]]])

slots.aiRmfFramework__ai_rmf_human_ai_issues = Slot(uri=NIST_AI_100_1.ai_rmf_human_ai_issues, name="aiRmfFramework__ai_rmf_human_ai_issues", curie=NIST_AI_100_1.curie('ai_rmf_human_ai_issues'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_human_ai_issues, domain=None, range=Optional[Union[Union[dict, AiRmfHumanAiIssue], list[Union[dict, AiRmfHumanAiIssue]]]])

slots.aiRmfFramework__ai_rmf_attributes = Slot(uri=NIST_AI_100_1.ai_rmf_attributes, name="aiRmfFramework__ai_rmf_attributes", curie=NIST_AI_100_1.curie('ai_rmf_attributes'),
                   model_uri=NIST_AI_RMF.aiRmfFramework__ai_rmf_attributes, domain=None, range=Optional[Union[Union[dict, AiRmfAttribute], list[Union[dict, AiRmfAttribute]]]])

slots.gaiProfile__gai_risks = Slot(uri=NIST_AI_600_1.gai_risks, name="gaiProfile__gai_risks", curie=NIST_AI_600_1.curie('gai_risks'),
                   model_uri=NIST_AI_RMF.gaiProfile__gai_risks, domain=None, range=Union[Union[dict, GaiRisk], list[Union[dict, GaiRisk]]])

slots.gaiProfile__gai_subcategories = Slot(uri=NIST_AI_600_1.gai_subcategories, name="gaiProfile__gai_subcategories", curie=NIST_AI_600_1.curie('gai_subcategories'),
                   model_uri=NIST_AI_RMF.gaiProfile__gai_subcategories, domain=None, range=Union[Union[dict, GaiSubcategory], list[Union[dict, GaiSubcategory]]])

slots.gaiProfile__gai_primary_considerations = Slot(uri=NIST_AI_600_1.gai_primary_considerations, name="gaiProfile__gai_primary_considerations", curie=NIST_AI_600_1.curie('gai_primary_considerations'),
                   model_uri=NIST_AI_RMF.gaiProfile__gai_primary_considerations, domain=None, range=Optional[Union[Union[dict, GaiPrimaryConsideration], list[Union[dict, GaiPrimaryConsideration]]]])

slots.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_name = Slot(uri=NIST_AI_100_1.ai_rmf_characteristic_name, name="aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_name", curie=NIST_AI_100_1.curie('ai_rmf_characteristic_name'),
                   model_uri=NIST_AI_RMF.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_name, domain=None, range=Union[str, "AiRmfCharacteristicName"])

slots.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_section = Slot(uri=NIST_AI_100_1.ai_rmf_characteristic_section, name="aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_section", curie=NIST_AI_100_1.curie('ai_rmf_characteristic_section'),
                   model_uri=NIST_AI_RMF.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_section, domain=None, range=str,
                   pattern=re.compile(r'^3\.[1-7]$'))

slots.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_is_base = Slot(uri=NIST_AI_100_1.ai_rmf_characteristic_is_base, name="aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_is_base", curie=NIST_AI_100_1.curie('ai_rmf_characteristic_is_base'),
                   model_uri=NIST_AI_RMF.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_is_base, domain=None, range=Optional[Union[bool, Bool]])

slots.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_relates_to_all = Slot(uri=NIST_AI_100_1.ai_rmf_characteristic_relates_to_all, name="aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_relates_to_all", curie=NIST_AI_100_1.curie('ai_rmf_characteristic_relates_to_all'),
                   model_uri=NIST_AI_RMF.aiRmfTrustworthinessCharacteristic__ai_rmf_characteristic_relates_to_all, domain=None, range=Optional[Union[bool, Bool]])

slots.aiRmfDimension__ai_rmf_dimension_name = Slot(uri=NIST_AI_100_1.ai_rmf_dimension_name, name="aiRmfDimension__ai_rmf_dimension_name", curie=NIST_AI_100_1.curie('ai_rmf_dimension_name'),
                   model_uri=NIST_AI_RMF.aiRmfDimension__ai_rmf_dimension_name, domain=None, range=Union[str, "AiRmfDimensionName"])

slots.aiRmfDimension__ai_rmf_dimension_audience = Slot(uri=NIST_AI_100_1.ai_rmf_dimension_audience, name="aiRmfDimension__ai_rmf_dimension_audience", curie=NIST_AI_100_1.curie('ai_rmf_dimension_audience'),
                   model_uri=NIST_AI_RMF.aiRmfDimension__ai_rmf_dimension_audience, domain=None, range=Union[str, "AiRmfAudience"])

slots.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_name = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stage_name, name="aiRmfLifecycleStage__ai_rmf_lifecycle_stage_name", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stage_name'),
                   model_uri=NIST_AI_RMF.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_name, domain=None, range=Union[str, "AiRmfLifecycleStageName"])

slots.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_dimension = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stage_dimension, name="aiRmfLifecycleStage__ai_rmf_lifecycle_stage_dimension", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stage_dimension'),
                   model_uri=NIST_AI_RMF.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_dimension, domain=None, range=Union[str, "AiRmfDimensionName"])

slots.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_tevv = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stage_tevv, name="aiRmfLifecycleStage__ai_rmf_lifecycle_stage_tevv", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stage_tevv'),
                   model_uri=NIST_AI_RMF.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_tevv, domain=None, range=Optional[str])

slots.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_representative_actors = Slot(uri=NIST_AI_100_1.ai_rmf_lifecycle_stage_representative_actors, name="aiRmfLifecycleStage__ai_rmf_lifecycle_stage_representative_actors", curie=NIST_AI_100_1.curie('ai_rmf_lifecycle_stage_representative_actors'),
                   model_uri=NIST_AI_RMF.aiRmfLifecycleStage__ai_rmf_lifecycle_stage_representative_actors, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfActorTask__ai_rmf_actor_task_name = Slot(uri=NIST_AI_100_1.ai_rmf_actor_task_name, name="aiRmfActorTask__ai_rmf_actor_task_name", curie=NIST_AI_100_1.curie('ai_rmf_actor_task_name'),
                   model_uri=NIST_AI_RMF.aiRmfActorTask__ai_rmf_actor_task_name, domain=None, range=Union[str, "AiRmfActorTaskName"])

slots.aiRmfActorTask__ai_rmf_actor_task_is_additional_actor = Slot(uri=NIST_AI_100_1.ai_rmf_actor_task_is_additional_actor, name="aiRmfActorTask__ai_rmf_actor_task_is_additional_actor", curie=NIST_AI_100_1.curie('ai_rmf_actor_task_is_additional_actor'),
                   model_uri=NIST_AI_RMF.aiRmfActorTask__ai_rmf_actor_task_is_additional_actor, domain=None, range=Optional[Union[bool, Bool]])

slots.aiRmfActorTask__ai_rmf_actor_task_representative_actors = Slot(uri=NIST_AI_100_1.ai_rmf_actor_task_representative_actors, name="aiRmfActorTask__ai_rmf_actor_task_representative_actors", curie=NIST_AI_100_1.curie('ai_rmf_actor_task_representative_actors'),
                   model_uri=NIST_AI_RMF.aiRmfActorTask__ai_rmf_actor_task_representative_actors, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfManagementChallenge__ai_rmf_management_challenge_name = Slot(uri=NIST_AI_100_1.ai_rmf_management_challenge_name, name="aiRmfManagementChallenge__ai_rmf_management_challenge_name", curie=NIST_AI_100_1.curie('ai_rmf_management_challenge_name'),
                   model_uri=NIST_AI_RMF.aiRmfManagementChallenge__ai_rmf_management_challenge_name, domain=None, range=Union[str, "AiRmfManagementChallengeName"])

slots.aiRmfManagementChallenge__ai_rmf_management_challenge_measurement_challenges = Slot(uri=NIST_AI_100_1.ai_rmf_management_challenge_measurement_challenges, name="aiRmfManagementChallenge__ai_rmf_management_challenge_measurement_challenges", curie=NIST_AI_100_1.curie('ai_rmf_management_challenge_measurement_challenges'),
                   model_uri=NIST_AI_RMF.aiRmfManagementChallenge__ai_rmf_management_challenge_measurement_challenges, domain=None, range=Optional[Union[Union[dict, AiRmfMeasurementChallenge], list[Union[dict, AiRmfMeasurementChallenge]]]])

slots.aiRmfMeasurementChallenge__ai_rmf_measurement_challenge_name = Slot(uri=NIST_AI_100_1.ai_rmf_measurement_challenge_name, name="aiRmfMeasurementChallenge__ai_rmf_measurement_challenge_name", curie=NIST_AI_100_1.curie('ai_rmf_measurement_challenge_name'),
                   model_uri=NIST_AI_RMF.aiRmfMeasurementChallenge__ai_rmf_measurement_challenge_name, domain=None, range=Union[str, "AiRmfMeasurementChallengeName"])

slots.aiRmfSpecificRisk__ai_rmf_specific_risk_position = Slot(uri=NIST_AI_100_1.ai_rmf_specific_risk_position, name="aiRmfSpecificRisk__ai_rmf_specific_risk_position", curie=NIST_AI_100_1.curie('ai_rmf_specific_risk_position'),
                   model_uri=NIST_AI_RMF.aiRmfSpecificRisk__ai_rmf_specific_risk_position, domain=None, range=int)

slots.aiRmfHumanAiIssue__ai_rmf_human_ai_issue_number = Slot(uri=NIST_AI_100_1.ai_rmf_human_ai_issue_number, name="aiRmfHumanAiIssue__ai_rmf_human_ai_issue_number", curie=NIST_AI_100_1.curie('ai_rmf_human_ai_issue_number'),
                   model_uri=NIST_AI_RMF.aiRmfHumanAiIssue__ai_rmf_human_ai_issue_number, domain=None, range=int)

slots.aiRmfAttribute__ai_rmf_attribute_number = Slot(uri=NIST_AI_100_1.ai_rmf_attribute_number, name="aiRmfAttribute__ai_rmf_attribute_number", curie=NIST_AI_100_1.curie('ai_rmf_attribute_number'),
                   model_uri=NIST_AI_RMF.aiRmfAttribute__ai_rmf_attribute_number, domain=None, range=int)

slots.aiRmfSystem__ai_rmf_system_intended_purposes = Slot(uri=NIST_AI_100_1.ai_rmf_system_intended_purposes, name="aiRmfSystem__ai_rmf_system_intended_purposes", curie=NIST_AI_100_1.curie('ai_rmf_system_intended_purposes'),
                   model_uri=NIST_AI_RMF.aiRmfSystem__ai_rmf_system_intended_purposes, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfSystem__ai_rmf_system_deployment_settings = Slot(uri=NIST_AI_100_1.ai_rmf_system_deployment_settings, name="aiRmfSystem__ai_rmf_system_deployment_settings", curie=NIST_AI_100_1.curie('ai_rmf_system_deployment_settings'),
                   model_uri=NIST_AI_RMF.aiRmfSystem__ai_rmf_system_deployment_settings, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfSystem__ai_rmf_system_lifecycle_stages = Slot(uri=NIST_AI_100_1.ai_rmf_system_lifecycle_stages, name="aiRmfSystem__ai_rmf_system_lifecycle_stages", curie=NIST_AI_100_1.curie('ai_rmf_system_lifecycle_stages'),
                   model_uri=NIST_AI_RMF.aiRmfSystem__ai_rmf_system_lifecycle_stages, domain=None, range=Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]])

slots.aiRmfSystem__ai_rmf_system_actors = Slot(uri=NIST_AI_100_1.ai_rmf_system_actors, name="aiRmfSystem__ai_rmf_system_actors", curie=NIST_AI_100_1.curie('ai_rmf_system_actors'),
                   model_uri=NIST_AI_RMF.aiRmfSystem__ai_rmf_system_actors, domain=None, range=Optional[Union[Union[str, AiRmfActorAiRmfId], list[Union[str, AiRmfActorAiRmfId]]]])

slots.aiRmfActor__ai_rmf_actor_tasks = Slot(uri=NIST_AI_100_1.ai_rmf_actor_tasks, name="aiRmfActor__ai_rmf_actor_tasks", curie=NIST_AI_100_1.curie('ai_rmf_actor_tasks'),
                   model_uri=NIST_AI_RMF.aiRmfActor__ai_rmf_actor_tasks, domain=None, range=Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]])

slots.aiRmfActor__ai_rmf_actor_audience = Slot(uri=NIST_AI_100_1.ai_rmf_actor_audience, name="aiRmfActor__ai_rmf_actor_audience", curie=NIST_AI_100_1.curie('ai_rmf_actor_audience'),
                   model_uri=NIST_AI_RMF.aiRmfActor__ai_rmf_actor_audience, domain=None, range=Optional[Union[str, "AiRmfAudience"]])

slots.aiRmfActor__ai_rmf_actor_lifecycle_stages = Slot(uri=NIST_AI_100_1.ai_rmf_actor_lifecycle_stages, name="aiRmfActor__ai_rmf_actor_lifecycle_stages", curie=NIST_AI_100_1.curie('ai_rmf_actor_lifecycle_stages'),
                   model_uri=NIST_AI_RMF.aiRmfActor__ai_rmf_actor_lifecycle_stages, domain=None, range=Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]])

slots.aiRmfRisk__ai_rmf_risk_system = Slot(uri=NIST_AI_100_1.ai_rmf_risk_system, name="aiRmfRisk__ai_rmf_risk_system", curie=NIST_AI_100_1.curie('ai_rmf_risk_system'),
                   model_uri=NIST_AI_RMF.aiRmfRisk__ai_rmf_risk_system, domain=None, range=Optional[Union[str, AiRmfSystemAiRmfId]])

slots.aiRmfRisk__ai_rmf_risk_impacts = Slot(uri=NIST_AI_100_1.ai_rmf_risk_impacts, name="aiRmfRisk__ai_rmf_risk_impacts", curie=NIST_AI_100_1.curie('ai_rmf_risk_impacts'),
                   model_uri=NIST_AI_RMF.aiRmfRisk__ai_rmf_risk_impacts, domain=None, range=Optional[Union[dict[Union[str, AiRmfImpactAiRmfId], Union[dict, AiRmfImpact]], list[Union[dict, AiRmfImpact]]]])

slots.aiRmfRisk__ai_rmf_risk_characteristics = Slot(uri=NIST_AI_100_1.ai_rmf_risk_characteristics, name="aiRmfRisk__ai_rmf_risk_characteristics", curie=NIST_AI_100_1.curie('ai_rmf_risk_characteristics'),
                   model_uri=NIST_AI_RMF.aiRmfRisk__ai_rmf_risk_characteristics, domain=None, range=Optional[Union[Union[str, "AiRmfCharacteristicName"], list[Union[str, "AiRmfCharacteristicName"]]]])

slots.aiRmfRisk__ai_rmf_risk_lifecycle_stages = Slot(uri=NIST_AI_100_1.ai_rmf_risk_lifecycle_stages, name="aiRmfRisk__ai_rmf_risk_lifecycle_stages", curie=NIST_AI_100_1.curie('ai_rmf_risk_lifecycle_stages'),
                   model_uri=NIST_AI_RMF.aiRmfRisk__ai_rmf_risk_lifecycle_stages, domain=None, range=Optional[Union[Union[str, "AiRmfLifecycleStageName"], list[Union[str, "AiRmfLifecycleStageName"]]]])

slots.aiRmfRisk__ai_rmf_risk_responses = Slot(uri=NIST_AI_100_1.ai_rmf_risk_responses, name="aiRmfRisk__ai_rmf_risk_responses", curie=NIST_AI_100_1.curie('ai_rmf_risk_responses'),
                   model_uri=NIST_AI_RMF.aiRmfRisk__ai_rmf_risk_responses, domain=None, range=Optional[Union[Union[str, "AiRmfRiskResponse"], list[Union[str, "AiRmfRiskResponse"]]]])

slots.aiRmfRisk__ai_rmf_risk_priority = Slot(uri=NIST_AI_100_1.ai_rmf_risk_priority, name="aiRmfRisk__ai_rmf_risk_priority", curie=NIST_AI_100_1.curie('ai_rmf_risk_priority'),
                   model_uri=NIST_AI_RMF.aiRmfRisk__ai_rmf_risk_priority, domain=None, range=Optional[str])

slots.aiRmfRisk__ai_rmf_risk_tolerance = Slot(uri=NIST_AI_100_1.ai_rmf_risk_tolerance, name="aiRmfRisk__ai_rmf_risk_tolerance", curie=NIST_AI_100_1.curie('ai_rmf_risk_tolerance'),
                   model_uri=NIST_AI_RMF.aiRmfRisk__ai_rmf_risk_tolerance, domain=None, range=Optional[Union[str, AiRmfRiskToleranceAiRmfId]])

slots.aiRmfImpact__ai_rmf_impact_direction = Slot(uri=NIST_AI_100_1.ai_rmf_impact_direction, name="aiRmfImpact__ai_rmf_impact_direction", curie=NIST_AI_100_1.curie('ai_rmf_impact_direction'),
                   model_uri=NIST_AI_RMF.aiRmfImpact__ai_rmf_impact_direction, domain=None, range=Union[str, "AiRmfImpactDirection"])

slots.aiRmfImpact__ai_rmf_impact_affected_parties = Slot(uri=NIST_AI_100_1.ai_rmf_impact_affected_parties, name="aiRmfImpact__ai_rmf_impact_affected_parties", curie=NIST_AI_100_1.curie('ai_rmf_impact_affected_parties'),
                   model_uri=NIST_AI_RMF.aiRmfImpact__ai_rmf_impact_affected_parties, domain=None, range=Optional[Union[Union[str, "AiRmfAffectedParty"], list[Union[str, "AiRmfAffectedParty"]]]])

slots.aiRmfHarm__ai_rmf_harm_category = Slot(uri=NIST_AI_100_1.ai_rmf_harm_category, name="aiRmfHarm__ai_rmf_harm_category", curie=NIST_AI_100_1.curie('ai_rmf_harm_category'),
                   model_uri=NIST_AI_RMF.aiRmfHarm__ai_rmf_harm_category, domain=None, range=Union[str, "AiRmfHarmCategory"])

slots.aiRmfHarm__ai_rmf_harm_example = Slot(uri=NIST_AI_100_1.ai_rmf_harm_example, name="aiRmfHarm__ai_rmf_harm_example", curie=NIST_AI_100_1.curie('ai_rmf_harm_example'),
                   model_uri=NIST_AI_RMF.aiRmfHarm__ai_rmf_harm_example, domain=None, range=Optional[Union[str, "AiRmfHarmExample"]])

slots.aiRmfRiskTolerance__ai_rmf_risk_tolerance_holder = Slot(uri=NIST_AI_100_1.ai_rmf_risk_tolerance_holder, name="aiRmfRiskTolerance__ai_rmf_risk_tolerance_holder", curie=NIST_AI_100_1.curie('ai_rmf_risk_tolerance_holder'),
                   model_uri=NIST_AI_RMF.aiRmfRiskTolerance__ai_rmf_risk_tolerance_holder, domain=None, range=Optional[Union[str, AiRmfActorAiRmfId]])

slots.aiRmfRiskTolerance__ai_rmf_risk_tolerance_influences = Slot(uri=NIST_AI_100_1.ai_rmf_risk_tolerance_influences, name="aiRmfRiskTolerance__ai_rmf_risk_tolerance_influences", curie=NIST_AI_100_1.curie('ai_rmf_risk_tolerance_influences'),
                   model_uri=NIST_AI_RMF.aiRmfRiskTolerance__ai_rmf_risk_tolerance_influences, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfBias__ai_rmf_bias_categories = Slot(uri=NIST_AI_100_1.ai_rmf_bias_categories, name="aiRmfBias__ai_rmf_bias_categories", curie=NIST_AI_100_1.curie('ai_rmf_bias_categories'),
                   model_uri=NIST_AI_RMF.aiRmfBias__ai_rmf_bias_categories, domain=None, range=Union[Union[str, "AiRmfBiasCategory"], list[Union[str, "AiRmfBiasCategory"]]])

slots.aiRmfFunction__ai_rmf_function_categories = Slot(uri=NIST_AI_100_1.ai_rmf_function_categories, name="aiRmfFunction__ai_rmf_function_categories", curie=NIST_AI_100_1.curie('ai_rmf_function_categories'),
                   model_uri=NIST_AI_RMF.aiRmfFunction__ai_rmf_function_categories, domain=None, range=Optional[Union[Union[dict, AiRmfCategory], list[Union[dict, AiRmfCategory]]]])

slots.aiRmfCategory__ai_rmf_category_subcategories = Slot(uri=NIST_AI_100_1.ai_rmf_category_subcategories, name="aiRmfCategory__ai_rmf_category_subcategories", curie=NIST_AI_100_1.curie('ai_rmf_category_subcategories'),
                   model_uri=NIST_AI_RMF.aiRmfCategory__ai_rmf_category_subcategories, domain=None, range=Optional[Union[Union[dict, AiRmfSubcategory], list[Union[dict, AiRmfSubcategory]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_about = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_about, name="aiRmfSubcategory__ai_rmf_subcategory_about", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_about'),
                   model_uri=NIST_AI_RMF.aiRmfSubcategory__ai_rmf_subcategory_about, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_suggested_actions = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_suggested_actions, name="aiRmfSubcategory__ai_rmf_subcategory_suggested_actions", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_suggested_actions'),
                   model_uri=NIST_AI_RMF.aiRmfSubcategory__ai_rmf_subcategory_suggested_actions, domain=None, range=Optional[Union[Union[dict, AiRmfSuggestedAction], list[Union[dict, AiRmfSuggestedAction]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_documentation = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_documentation, name="aiRmfSubcategory__ai_rmf_subcategory_documentation", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_documentation'),
                   model_uri=NIST_AI_RMF.aiRmfSubcategory__ai_rmf_subcategory_documentation, domain=None, range=Optional[Union[Union[dict, AiRmfDocumentationItem], list[Union[dict, AiRmfDocumentationItem]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_transparency_resources = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_transparency_resources, name="aiRmfSubcategory__ai_rmf_subcategory_transparency_resources", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_transparency_resources'),
                   model_uri=NIST_AI_RMF.aiRmfSubcategory__ai_rmf_subcategory_transparency_resources, domain=None, range=Optional[Union[Union[dict, AiRmfResource], list[Union[dict, AiRmfResource]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_references = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_references, name="aiRmfSubcategory__ai_rmf_subcategory_references", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_references'),
                   model_uri=NIST_AI_RMF.aiRmfSubcategory__ai_rmf_subcategory_references, domain=None, range=Optional[Union[Union[dict, AiRmfResource], list[Union[dict, AiRmfResource]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_ai_actors = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_ai_actors, name="aiRmfSubcategory__ai_rmf_subcategory_ai_actors", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_ai_actors'),
                   model_uri=NIST_AI_RMF.aiRmfSubcategory__ai_rmf_subcategory_ai_actors, domain=None, range=Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]])

slots.aiRmfSubcategory__ai_rmf_subcategory_topics = Slot(uri=NIST_AI_100_1.ai_rmf_subcategory_topics, name="aiRmfSubcategory__ai_rmf_subcategory_topics", curie=NIST_AI_100_1.curie('ai_rmf_subcategory_topics'),
                   model_uri=NIST_AI_RMF.aiRmfSubcategory__ai_rmf_subcategory_topics, domain=None, range=Optional[Union[str, list[str]]])

slots.aiRmfResource__ai_rmf_resource_uuid = Slot(uri=NIST_AI_100_1.ai_rmf_resource_uuid, name="aiRmfResource__ai_rmf_resource_uuid", curie=NIST_AI_100_1.curie('ai_rmf_resource_uuid'),
                   model_uri=NIST_AI_RMF.aiRmfResource__ai_rmf_resource_uuid, domain=None, range=str,
                   pattern=re.compile(r'^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$'))

slots.aiRmfResource__ai_rmf_resource_address = Slot(uri=NIST_AI_100_1.ai_rmf_resource_address, name="aiRmfResource__ai_rmf_resource_address", curie=NIST_AI_100_1.curie('ai_rmf_resource_address'),
                   model_uri=NIST_AI_RMF.aiRmfResource__ai_rmf_resource_address, domain=None, range=Optional[Union[str, URI]])

slots.aiRmfProfile__ai_rmf_profile_kinds = Slot(uri=NIST_AI_100_1.ai_rmf_profile_kinds, name="aiRmfProfile__ai_rmf_profile_kinds", curie=NIST_AI_100_1.curie('ai_rmf_profile_kinds'),
                   model_uri=NIST_AI_RMF.aiRmfProfile__ai_rmf_profile_kinds, domain=None, range=Union[Union[str, "AiRmfProfileKind"], list[Union[str, "AiRmfProfileKind"]]])

slots.aiRmfProfile__ai_rmf_profile_setting = Slot(uri=NIST_AI_100_1.ai_rmf_profile_setting, name="aiRmfProfile__ai_rmf_profile_setting", curie=NIST_AI_100_1.curie('ai_rmf_profile_setting'),
                   model_uri=NIST_AI_RMF.aiRmfProfile__ai_rmf_profile_setting, domain=None, range=Optional[str])

slots.aiRmfProfile__ai_rmf_profile_subcategories = Slot(uri=NIST_AI_100_1.ai_rmf_profile_subcategories, name="aiRmfProfile__ai_rmf_profile_subcategories", curie=NIST_AI_100_1.curie('ai_rmf_profile_subcategories'),
                   model_uri=NIST_AI_RMF.aiRmfProfile__ai_rmf_profile_subcategories, domain=None, range=Optional[Union[Union[str, AiRmfSubcategoryIdentifier], list[Union[str, AiRmfSubcategoryIdentifier]]]])

slots.gaiRisk__gai_risk_name = Slot(uri=NIST_AI_600_1.gai_risk_name, name="gaiRisk__gai_risk_name", curie=NIST_AI_600_1.curie('gai_risk_name'),
                   model_uri=NIST_AI_RMF.gaiRisk__gai_risk_name, domain=None, range=Union[str, "GaiRiskName"])

slots.gaiRisk__gai_risk_section = Slot(uri=NIST_AI_600_1.gai_risk_section, name="gaiRisk__gai_risk_section", curie=NIST_AI_600_1.curie('gai_risk_section'),
                   model_uri=NIST_AI_RMF.gaiRisk__gai_risk_section, domain=None, range=str,
                   pattern=re.compile(r'^2\.([1-9]|1[0-2])$'))

slots.gaiRisk__gai_risk_characteristics = Slot(uri=NIST_AI_600_1.gai_risk_characteristics, name="gaiRisk__gai_risk_characteristics", curie=NIST_AI_600_1.curie('gai_risk_characteristics'),
                   model_uri=NIST_AI_RMF.gaiRisk__gai_risk_characteristics, domain=None, range=Optional[Union[Union[str, "AiRmfCharacteristicName"], list[Union[str, "AiRmfCharacteristicName"]]]])

slots.gaiRisk__gai_risk_groupings = Slot(uri=NIST_AI_600_1.gai_risk_groupings, name="gaiRisk__gai_risk_groupings", curie=NIST_AI_600_1.curie('gai_risk_groupings'),
                   model_uri=NIST_AI_RMF.gaiRisk__gai_risk_groupings, domain=None, range=Optional[Union[Union[str, "GaiRiskGrouping"], list[Union[str, "GaiRiskGrouping"]]]])

slots.gaiRisk__gai_risk_lifecycle_stages = Slot(uri=NIST_AI_600_1.gai_risk_lifecycle_stages, name="gaiRisk__gai_risk_lifecycle_stages", curie=NIST_AI_600_1.curie('gai_risk_lifecycle_stages'),
                   model_uri=NIST_AI_RMF.gaiRisk__gai_risk_lifecycle_stages, domain=None, range=Optional[Union[Union[str, "GaiLifecycleStage"], list[Union[str, "GaiLifecycleStage"]]]])

slots.gaiRisk__gai_risk_scopes = Slot(uri=NIST_AI_600_1.gai_risk_scopes, name="gaiRisk__gai_risk_scopes", curie=NIST_AI_600_1.curie('gai_risk_scopes'),
                   model_uri=NIST_AI_RMF.gaiRisk__gai_risk_scopes, domain=None, range=Optional[Union[Union[str, "GaiRiskScope"], list[Union[str, "GaiRiskScope"]]]])

slots.gaiRisk__gai_risk_sources = Slot(uri=NIST_AI_600_1.gai_risk_sources, name="gaiRisk__gai_risk_sources", curie=NIST_AI_600_1.curie('gai_risk_sources'),
                   model_uri=NIST_AI_RMF.gaiRisk__gai_risk_sources, domain=None, range=Optional[Union[Union[str, "GaiRiskSource"], list[Union[str, "GaiRiskSource"]]]])

slots.gaiRisk__gai_risk_time_scales = Slot(uri=NIST_AI_600_1.gai_risk_time_scales, name="gaiRisk__gai_risk_time_scales", curie=NIST_AI_600_1.curie('gai_risk_time_scales'),
                   model_uri=NIST_AI_RMF.gaiRisk__gai_risk_time_scales, domain=None, range=Optional[Union[Union[str, "GaiRiskTimeScale"], list[Union[str, "GaiRiskTimeScale"]]]])

slots.gaiSubcategory__gai_subcategory_actions = Slot(uri=NIST_AI_600_1.gai_subcategory_actions, name="gaiSubcategory__gai_subcategory_actions", curie=NIST_AI_600_1.curie('gai_subcategory_actions'),
                   model_uri=NIST_AI_RMF.gaiSubcategory__gai_subcategory_actions, domain=None, range=Union[Union[dict, GaiSuggestedAction], list[Union[dict, GaiSuggestedAction]]])

slots.gaiSubcategory__gai_subcategory_actor_tasks = Slot(uri=NIST_AI_600_1.gai_subcategory_actor_tasks, name="gaiSubcategory__gai_subcategory_actor_tasks", curie=NIST_AI_600_1.curie('gai_subcategory_actor_tasks'),
                   model_uri=NIST_AI_RMF.gaiSubcategory__gai_subcategory_actor_tasks, domain=None, range=Optional[Union[Union[str, "AiRmfActorTaskName"], list[Union[str, "AiRmfActorTaskName"]]]])

slots.gaiSuggestedAction__gai_action_risks = Slot(uri=NIST_AI_600_1.gai_action_risks, name="gaiSuggestedAction__gai_action_risks", curie=NIST_AI_600_1.curie('gai_action_risks'),
                   model_uri=NIST_AI_RMF.gaiSuggestedAction__gai_action_risks, domain=None, range=Optional[Union[Union[str, "GaiRiskName"], list[Union[str, "GaiRiskName"]]]])

slots.gaiPrimaryConsideration__gai_consideration_sections = Slot(uri=NIST_AI_600_1.gai_consideration_sections, name="gaiPrimaryConsideration__gai_consideration_sections", curie=NIST_AI_600_1.curie('gai_consideration_sections'),
                   model_uri=NIST_AI_RMF.gaiPrimaryConsideration__gai_consideration_sections, domain=None, range=Optional[Union[str, list[str]]],
                   pattern=re.compile(r'^A\.1(\.[1-8])?$'))

slots.gaiGovernanceConsideration__gai_governance_plans = Slot(uri=NIST_AI_600_1.gai_governance_plans, name="gaiGovernanceConsideration__gai_governance_plans", curie=NIST_AI_600_1.curie('gai_governance_plans'),
                   model_uri=NIST_AI_RMF.gaiGovernanceConsideration__gai_governance_plans, domain=None, range=Optional[Union[Union[str, "GaiGovernancePlan"], list[Union[str, "GaiGovernancePlan"]]]])

slots.gaiGovernanceConsideration__gai_third_party_controls = Slot(uri=NIST_AI_600_1.gai_third_party_controls, name="gaiGovernanceConsideration__gai_third_party_controls", curie=NIST_AI_600_1.curie('gai_third_party_controls'),
                   model_uri=NIST_AI_RMF.gaiGovernanceConsideration__gai_third_party_controls, domain=None, range=Optional[Union[Union[str, "GaiThirdPartyControl"], list[Union[str, "GaiThirdPartyControl"]]]])

slots.gaiPreDeploymentTestingConsideration__gai_structured_feedback = Slot(uri=NIST_AI_600_1.gai_structured_feedback, name="gaiPreDeploymentTestingConsideration__gai_structured_feedback", curie=NIST_AI_600_1.curie('gai_structured_feedback'),
                   model_uri=NIST_AI_RMF.gaiPreDeploymentTestingConsideration__gai_structured_feedback, domain=None, range=Optional[Union[Union[dict, GaiStructuredFeedback], list[Union[dict, GaiStructuredFeedback]]]])

slots.gaiContentProvenanceConsideration__gai_provenance_techniques = Slot(uri=NIST_AI_600_1.gai_provenance_techniques, name="gaiContentProvenanceConsideration__gai_provenance_techniques", curie=NIST_AI_600_1.curie('gai_provenance_techniques'),
                   model_uri=NIST_AI_RMF.gaiContentProvenanceConsideration__gai_provenance_techniques, domain=None, range=Optional[Union[Union[str, "GaiProvenanceTechnique"], list[Union[str, "GaiProvenanceTechnique"]]]])

slots.gaiIncidentDisclosureConsideration__gai_incident_harms = Slot(uri=NIST_AI_600_1.gai_incident_harms, name="gaiIncidentDisclosureConsideration__gai_incident_harms", curie=NIST_AI_600_1.curie('gai_incident_harms'),
                   model_uri=NIST_AI_RMF.gaiIncidentDisclosureConsideration__gai_incident_harms, domain=None, range=Optional[Union[Union[str, "GaiIncidentHarm"], list[Union[str, "GaiIncidentHarm"]]]])

slots.gaiAiRedTeaming__gai_red_teaming_types = Slot(uri=NIST_AI_600_1.gai_red_teaming_types, name="gaiAiRedTeaming__gai_red_teaming_types", curie=NIST_AI_600_1.curie('gai_red_teaming_types'),
                   model_uri=NIST_AI_RMF.gaiAiRedTeaming__gai_red_teaming_types, domain=None, range=Optional[Union[Union[str, "GaiRedTeamingType"], list[Union[str, "GaiRedTeamingType"]]]])

slots.AiRmfSpecificRisk_title = Slot(uri=SCHEMA.name, name="AiRmfSpecificRisk_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_RMF.AiRmfSpecificRisk_title, domain=AiRmfSpecificRisk, range=str)

slots.AiRmfHumanAiIssue_title = Slot(uri=SCHEMA.name, name="AiRmfHumanAiIssue_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_RMF.AiRmfHumanAiIssue_title, domain=AiRmfHumanAiIssue, range=str)

slots.AiRmfAttribute_title = Slot(uri=SCHEMA.name, name="AiRmfAttribute_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_RMF.AiRmfAttribute_title, domain=AiRmfAttribute, range=str)

slots.AiRmfFunction_description = Slot(uri=SCHEMA.description, name="AiRmfFunction_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.AiRmfFunction_description, domain=AiRmfFunction, range=Optional[str])

slots.AiRmfCategory_description = Slot(uri=SCHEMA.description, name="AiRmfCategory_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.AiRmfCategory_description, domain=AiRmfCategory, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AiRmfSubcategory_description = Slot(uri=SCHEMA.description, name="AiRmfSubcategory_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.AiRmfSubcategory_description, domain=AiRmfSubcategory, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AiRmfSuggestedAction_description = Slot(uri=SCHEMA.description, name="AiRmfSuggestedAction_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.AiRmfSuggestedAction_description, domain=AiRmfSuggestedAction, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AiRmfDocumentationItem_description = Slot(uri=SCHEMA.description, name="AiRmfDocumentationItem_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.AiRmfDocumentationItem_description, domain=AiRmfDocumentationItem, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.AiRmfResource_title = Slot(uri=SCHEMA.name, name="AiRmfResource_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_RMF.AiRmfResource_title, domain=AiRmfResource, range=str)

slots.GaiRisk_description = Slot(uri=SCHEMA.description, name="GaiRisk_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.GaiRisk_description, domain=GaiRisk, range=Optional[str])

slots.GaiSubcategory_description = Slot(uri=SCHEMA.description, name="GaiSubcategory_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.GaiSubcategory_description, domain=GaiSubcategory, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.GaiSuggestedAction_description = Slot(uri=SCHEMA.description, name="GaiSuggestedAction_description", curie=SCHEMA.curie('description'),
                   model_uri=NIST_AI_RMF.GaiSuggestedAction_description, domain=GaiSuggestedAction, range=str,
                   pattern=re.compile(r'^\s*\S'))

slots.GaiPrimaryConsideration_title = Slot(uri=SCHEMA.name, name="GaiPrimaryConsideration_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_RMF.GaiPrimaryConsideration_title, domain=GaiPrimaryConsideration, range=str)

slots.GaiStructuredFeedback_title = Slot(uri=SCHEMA.name, name="GaiStructuredFeedback_title", curie=SCHEMA.curie('name'),
                   model_uri=NIST_AI_RMF.GaiStructuredFeedback_title, domain=GaiStructuredFeedback, range=str)
