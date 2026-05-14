# Auto generated from nist_ai_rmf_gai.yaml by pythongen.py version: 0.0.1
# Generation date: 2026-05-14T02:28:28
# Schema: nist-ai-rmf-gai
#
# id: https://w3id.org/lmodel/nist-ai-rmf-gai
# description: LinkML schema for NIST AI 600-1, the Generative Artificial Intelligence
#   Profile of the AI Risk Management Framework (July 2024).
#
#   This is a **cross-sectoral profile** and a *companion resource* to
#   NIST AI 100-1 (AI RMF 1.0). It defines risks that are novel to or
#   exacerbated by the use of Generative AI (GAI) and provides a set of
#   suggested actions, organised by AI RMF subcategory, that
#   organisations can take to govern, map, measure, and manage those
#   risks.
#
#   The schema imports the base `nist_ai_rmf` schema and enriches it with:
#     * 12 GAI risk categories (Section 2)
#     * Risk dimensions (lifecycle stage, scope, source, time scale)
#     * `SuggestedAction` entries (Section 3 tables) linked to AI RMF
#       subcategories
#     * Primary GAI Considerations (Appendix A): Governance,
#       Pre-Deployment Testing, Content Provenance, Incident Disclosure
#     * Structured Public Feedback methods and AI Red-teaming types
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

from .nist_ai_rmf_core import AiActorTaskEnum, AiLifecycleStageEnum, AiRmfProfile, AiRmfProfileId, AiSpecificRisk, AiSpecificRiskId, NamedThing, NamedThingId, ProfileTypeEnum, SubcategoryCode, SubcategoryId, TrustworthinessCharacteristicEnum
from linkml_runtime.linkml_model.types import String, Uriorcurie
from linkml_runtime.utils.metamodelcore import URIorCURIE

metamodel_version = "1.11.0"
version = "1.0.0"

# Namespaces
DCTERMS = CurieNamespace('dcterms', 'http://purl.org/dc/terms/')
DOI = CurieNamespace('doi', 'https://doi.org/')
GIST = CurieNamespace('gist', 'https://w3id.org/lmodel/gist/')
ISO27001 = CurieNamespace('iso27001', 'https://w3id.org/lmodel/iso27001/')
ISO29100 = CurieNamespace('iso29100', 'https://w3id.org/lmodel/iso29100/')
LINKML = CurieNamespace('linkml', 'https://w3id.org/linkml/')
NIST_AI_RMF = CurieNamespace('nist_ai_rmf', 'https://w3id.org/lmodel/nist-ai-rmf/')
NIST_AI_RMF_GAI = CurieNamespace('nist_ai_rmf_gai', 'https://w3id.org/lmodel/nist-ai-rmf-gai/')
NIST_CSF = CurieNamespace('nist_csf', 'https://w3id.org/lmodel/nist-csf-v2/')
OSCAL_CATALOG = CurieNamespace('oscal_catalog', 'https://w3id.org/lmodel/oscal_catalog/')
OSCAL_PROFILE = CurieNamespace('oscal_profile', 'https://w3id.org/lmodel/oscal_profile/')
RDF = CurieNamespace('rdf', 'http://www.w3.org/1999/02/22-rdf-syntax-ns#')
RDFS = CurieNamespace('rdfs', 'http://www.w3.org/2000/01/rdf-schema#')
SCHEMA = CurieNamespace('schema', 'http://schema.org/')
SKOS = CurieNamespace('skos', 'http://www.w3.org/2004/02/skos/core#')
STIX = CurieNamespace('stix', 'https://w3id.org/lmodel/stix/')
XSD = CurieNamespace('xsd', 'http://www.w3.org/2001/XMLSchema#')
DEFAULT_ = NIST_AI_RMF_GAI


# Types
class GaiActionId(String):
    """ Action identifier used in NIST AI 600-1 Section 3, of the form
"<prefix>-<category>.<subcategory>-<seq>" - e.g., "GV-1.1-001".
Prefixes: GV (Govern), MP (Map), MS (Measure), MG (Manage). """
    type_class_uri = XSD["string"]
    type_class_curie = "xsd:string"
    type_name = "GaiActionId"
    type_model_uri = NIST_AI_RMF_GAI.GaiActionId


# Class references
class SuggestedActionId(NamedThingId):
    pass


class PrimaryGaiConsiderationId(NamedThingId):
    pass


class StructuredPublicFeedbackId(NamedThingId):
    pass


class AiRedTeamingId(StructuredPublicFeedbackId):
    pass


class GaiProfileId(AiRmfProfileId):
    pass


class GaiRiskId(AiSpecificRiskId):
    pass


@dataclass(repr=False)
class SuggestedAction(NamedThing):
    """
    A suggested action an organisation can take to manage GAI
    risks. Each action is identified by an Action ID, linked to an
    AI RMF subcategory, and may be relevant to one or more GAI
    risks and AI actor tasks (NIST AI 600-1 Section 3).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI["SuggestedAction"]
    class_class_curie: ClassVar[str] = "nist_ai_rmf_gai:SuggestedAction"
    class_name: ClassVar[str] = "SuggestedAction"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI.SuggestedAction

    id: Union[str, SuggestedActionId] = None
    action_id: Union[str, GaiActionId] = None
    function_prefix: Optional[Union[str, "GaiActionFunctionPrefixEnum"]] = None
    applies_to_subcategory: Optional[Union[str, SubcategoryCode]] = None
    gai_risks: Optional[Union[Union[str, "GaiRiskCategoryEnum"], list[Union[str, "GaiRiskCategoryEnum"]]]] = empty_list()
    actor_task: Optional[Union[Union[str, "AiActorTaskEnum"], list[Union[str, "AiActorTaskEnum"]]]] = empty_list()
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
        self.actor_task = [v if isinstance(v, AiActorTaskEnum) else AiActorTaskEnum(v) for v in self.actor_task]

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

    class_class_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI["PrimaryGaiConsideration"]
    class_class_curie: ClassVar[str] = "nist_ai_rmf_gai:PrimaryGaiConsideration"
    class_name: ClassVar[str] = "PrimaryGaiConsideration"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI.PrimaryGaiConsideration

    id: Union[str, PrimaryGaiConsiderationId] = None
    consideration_kind: Union[str, "PrimaryConsiderationEnum"] = None
    governance_practices: Optional[Union[str, list[str]]] = empty_list()
    third_party_considerations: Optional[str] = None
    limitations_of_current_approaches: Optional[str] = None
    provenance_techniques: Optional[Union[str, list[str]]] = empty_list()
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
        self.governance_practices = [v if isinstance(v, str) else str(v) for v in self.governance_practices]

        if self.third_party_considerations is not None and not isinstance(self.third_party_considerations, str):
            self.third_party_considerations = str(self.third_party_considerations)

        if self.limitations_of_current_approaches is not None and not isinstance(self.limitations_of_current_approaches, str):
            self.limitations_of_current_approaches = str(self.limitations_of_current_approaches)

        if not isinstance(self.provenance_techniques, list):
            self.provenance_techniques = [self.provenance_techniques] if self.provenance_techniques is not None else []
        self.provenance_techniques = [v if isinstance(v, str) else str(v) for v in self.provenance_techniques]

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

    class_class_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI["StructuredPublicFeedback"]
    class_class_curie: ClassVar[str] = "nist_ai_rmf_gai:StructuredPublicFeedback"
    class_name: ClassVar[str] = "StructuredPublicFeedback"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI.StructuredPublicFeedback

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

    class_class_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI["AiRedTeaming"]
    class_class_curie: ClassVar[str] = "nist_ai_rmf_gai:AiRedTeaming"
    class_name: ClassVar[str] = "AiRedTeaming"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI.AiRedTeaming

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
class GaiProfile(AiRmfProfile):
    """
    Root container that bundles the NIST AI 600-1 Generative AI
    Profile: GAI risks (Section 2), suggested actions (Section 3),
    and primary considerations (Appendix A).
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI["GaiProfile"]
    class_class_curie: ClassVar[str] = "nist_ai_rmf_gai:GaiProfile"
    class_name: ClassVar[str] = "GaiProfile"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI.GaiProfile

    id: Union[str, GaiProfileId] = None
    profile_type: Union[str, "ProfileTypeEnum"] = 'CROSS_SECTORAL'
    gai_risk_catalog: Optional[Union[dict[Union[str, GaiRiskId], Union[dict, "GaiRisk"]], list[Union[dict, "GaiRisk"]]]] = empty_dict()
    suggested_actions: Optional[Union[dict[Union[str, SuggestedActionId], Union[dict, SuggestedAction]], list[Union[dict, SuggestedAction]]]] = empty_dict()
    primary_considerations: Optional[Union[dict[Union[str, PrimaryGaiConsiderationId], Union[dict, PrimaryGaiConsideration]], list[Union[dict, PrimaryGaiConsideration]]]] = empty_dict()
    structured_feedback_methods: Optional[Union[dict[Union[str, StructuredPublicFeedbackId], Union[dict, StructuredPublicFeedback]], list[Union[dict, StructuredPublicFeedback]]]] = empty_dict()

    def __post_init__(self, *_: str, **kwargs: Any):
        if self._is_empty(self.id):
            self.MissingRequiredField("id")
        if not isinstance(self.id, GaiProfileId):
            self.id = GaiProfileId(self.id)

        if self._is_empty(self.profile_type):
            self.MissingRequiredField("profile_type")
        if not isinstance(self.profile_type, ProfileTypeEnum):
            self.profile_type = ProfileTypeEnum(self.profile_type)

        self._normalize_inlined_as_list(slot_name="gai_risk_catalog", slot_type=GaiRisk, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="suggested_actions", slot_type=SuggestedAction, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="primary_considerations", slot_type=PrimaryGaiConsideration, key_name="id", keyed=True)

        self._normalize_inlined_as_list(slot_name="structured_feedback_methods", slot_type=StructuredPublicFeedback, key_name="id", keyed=True)

        super().__post_init__(**kwargs)


@dataclass(repr=False)
class GaiRisk(AiSpecificRisk):
    """
    A risk that is novel to or exacerbated by Generative AI.
    Each instance corresponds to one of the 12 risk categories
    enumerated in NIST AI 600-1 Section 2.
    """
    _inherited_slots: ClassVar[list[str]] = []

    class_class_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI["GaiRisk"]
    class_class_curie: ClassVar[str] = "nist_ai_rmf_gai:GaiRisk"
    class_name: ClassVar[str] = "GaiRisk"
    class_model_uri: ClassVar[URIRef] = NIST_AI_RMF_GAI.GaiRisk

    id: Union[str, GaiRiskId] = None
    gai_risk_kind: Optional[Union[str, "GaiRiskCategoryEnum"]] = None
    risk_categorization: Optional[Union[str, "GaiRiskCategorizationEnum"]] = None
    risk_scope: Optional[Union[Union[str, "GaiRiskScopeEnum"], list[Union[str, "GaiRiskScopeEnum"]]]] = empty_list()
    risk_sources: Optional[Union[Union[str, "GaiRiskSourceEnum"], list[Union[str, "GaiRiskSourceEnum"]]]] = empty_list()
    time_scale: Optional[Union[Union[str, "GaiRiskTimeScaleEnum"], list[Union[str, "GaiRiskTimeScaleEnum"]]]] = empty_list()
    lifecycle_stage: Optional[Union[Union[str, "AiLifecycleStageEnum"], list[Union[str, "AiLifecycleStageEnum"]]]] = empty_list()
    trustworthiness_characteristic: Optional[Union[Union[str, "TrustworthinessCharacteristicEnum"], list[Union[str, "TrustworthinessCharacteristicEnum"]]]] = empty_list()
    addressed_by_actions: Optional[Union[Union[str, SuggestedActionId], list[Union[str, SuggestedActionId]]]] = empty_list()

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

        if not isinstance(self.lifecycle_stage, list):
            self.lifecycle_stage = [self.lifecycle_stage] if self.lifecycle_stage is not None else []
        self.lifecycle_stage = [v if isinstance(v, AiLifecycleStageEnum) else AiLifecycleStageEnum(v) for v in self.lifecycle_stage]

        if not isinstance(self.trustworthiness_characteristic, list):
            self.trustworthiness_characteristic = [self.trustworthiness_characteristic] if self.trustworthiness_characteristic is not None else []
        self.trustworthiness_characteristic = [v if isinstance(v, TrustworthinessCharacteristicEnum) else TrustworthinessCharacteristicEnum(v) for v in self.trustworthiness_characteristic]

        if not isinstance(self.addressed_by_actions, list):
            self.addressed_by_actions = [self.addressed_by_actions] if self.addressed_by_actions is not None else []
        self.addressed_by_actions = [v if isinstance(v, SuggestedActionId) else SuggestedActionId(v) for v in self.addressed_by_actions]

        super().__post_init__(**kwargs)


# Enumerations
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

# Slots
class slots:
    pass

slots.gai_risk_kind = Slot(uri=NIST_AI_RMF_GAI.gai_risk_kind, name="gai_risk_kind", curie=NIST_AI_RMF_GAI.curie('gai_risk_kind'),
                   model_uri=NIST_AI_RMF_GAI.gai_risk_kind, domain=None, range=Optional[Union[str, "GaiRiskCategoryEnum"]])

slots.gai_risks = Slot(uri=NIST_AI_RMF_GAI.gai_risks, name="gai_risks", curie=NIST_AI_RMF_GAI.curie('gai_risks'),
                   model_uri=NIST_AI_RMF_GAI.gai_risks, domain=None, range=Optional[Union[Union[str, "GaiRiskCategoryEnum"], list[Union[str, "GaiRiskCategoryEnum"]]]])

slots.risk_categorization = Slot(uri=NIST_AI_RMF_GAI.risk_categorization, name="risk_categorization", curie=NIST_AI_RMF_GAI.curie('risk_categorization'),
                   model_uri=NIST_AI_RMF_GAI.risk_categorization, domain=None, range=Optional[Union[str, "GaiRiskCategorizationEnum"]])

slots.risk_scope = Slot(uri=NIST_AI_RMF_GAI.risk_scope, name="risk_scope", curie=NIST_AI_RMF_GAI.curie('risk_scope'),
                   model_uri=NIST_AI_RMF_GAI.risk_scope, domain=None, range=Optional[Union[Union[str, "GaiRiskScopeEnum"], list[Union[str, "GaiRiskScopeEnum"]]]])

slots.risk_sources = Slot(uri=NIST_AI_RMF_GAI.risk_sources, name="risk_sources", curie=NIST_AI_RMF_GAI.curie('risk_sources'),
                   model_uri=NIST_AI_RMF_GAI.risk_sources, domain=None, range=Optional[Union[Union[str, "GaiRiskSourceEnum"], list[Union[str, "GaiRiskSourceEnum"]]]])

slots.time_scale = Slot(uri=NIST_AI_RMF_GAI.time_scale, name="time_scale", curie=NIST_AI_RMF_GAI.curie('time_scale'),
                   model_uri=NIST_AI_RMF_GAI.time_scale, domain=None, range=Optional[Union[Union[str, "GaiRiskTimeScaleEnum"], list[Union[str, "GaiRiskTimeScaleEnum"]]]])

slots.action_id = Slot(uri=NIST_AI_RMF_GAI.action_id, name="action_id", curie=NIST_AI_RMF_GAI.curie('action_id'),
                   model_uri=NIST_AI_RMF_GAI.action_id, domain=None, range=Union[str, GaiActionId])

slots.function_prefix = Slot(uri=NIST_AI_RMF_GAI.function_prefix, name="function_prefix", curie=NIST_AI_RMF_GAI.curie('function_prefix'),
                   model_uri=NIST_AI_RMF_GAI.function_prefix, domain=None, range=Optional[Union[str, "GaiActionFunctionPrefixEnum"]])

slots.applies_to_subcategory = Slot(uri=NIST_AI_RMF_GAI.applies_to_subcategory, name="applies_to_subcategory", curie=NIST_AI_RMF_GAI.curie('applies_to_subcategory'),
                   model_uri=NIST_AI_RMF_GAI.applies_to_subcategory, domain=None, range=Optional[Union[str, SubcategoryCode]])

slots.consideration_kind = Slot(uri=NIST_AI_RMF_GAI.consideration_kind, name="consideration_kind", curie=NIST_AI_RMF_GAI.curie('consideration_kind'),
                   model_uri=NIST_AI_RMF_GAI.consideration_kind, domain=None, range=Union[str, "PrimaryConsiderationEnum"])

slots.feedback_method_kind = Slot(uri=NIST_AI_RMF_GAI.feedback_method_kind, name="feedback_method_kind", curie=NIST_AI_RMF_GAI.curie('feedback_method_kind'),
                   model_uri=NIST_AI_RMF_GAI.feedback_method_kind, domain=None, range=Union[str, "StructuredFeedbackMethodEnum"])

slots.red_team_type = Slot(uri=NIST_AI_RMF_GAI.red_team_type, name="red_team_type", curie=NIST_AI_RMF_GAI.curie('red_team_type'),
                   model_uri=NIST_AI_RMF_GAI.red_team_type, domain=None, range=Optional[Union[str, "RedTeamingTypeEnum"]])

slots.gaiRisk__addressed_by_actions = Slot(uri=NIST_AI_RMF_GAI.addressed_by_actions, name="gaiRisk__addressed_by_actions", curie=NIST_AI_RMF_GAI.curie('addressed_by_actions'),
                   model_uri=NIST_AI_RMF_GAI.gaiRisk__addressed_by_actions, domain=None, range=Optional[Union[Union[str, SuggestedActionId], list[Union[str, SuggestedActionId]]]])

slots.primaryGaiConsideration__governance_practices = Slot(uri=NIST_AI_RMF_GAI.governance_practices, name="primaryGaiConsideration__governance_practices", curie=NIST_AI_RMF_GAI.curie('governance_practices'),
                   model_uri=NIST_AI_RMF_GAI.primaryGaiConsideration__governance_practices, domain=None, range=Optional[Union[str, list[str]]])

slots.primaryGaiConsideration__third_party_considerations = Slot(uri=NIST_AI_RMF_GAI.third_party_considerations, name="primaryGaiConsideration__third_party_considerations", curie=NIST_AI_RMF_GAI.curie('third_party_considerations'),
                   model_uri=NIST_AI_RMF_GAI.primaryGaiConsideration__third_party_considerations, domain=None, range=Optional[str])

slots.primaryGaiConsideration__limitations_of_current_approaches = Slot(uri=NIST_AI_RMF_GAI.limitations_of_current_approaches, name="primaryGaiConsideration__limitations_of_current_approaches", curie=NIST_AI_RMF_GAI.curie('limitations_of_current_approaches'),
                   model_uri=NIST_AI_RMF_GAI.primaryGaiConsideration__limitations_of_current_approaches, domain=None, range=Optional[str])

slots.primaryGaiConsideration__provenance_techniques = Slot(uri=NIST_AI_RMF_GAI.provenance_techniques, name="primaryGaiConsideration__provenance_techniques", curie=NIST_AI_RMF_GAI.curie('provenance_techniques'),
                   model_uri=NIST_AI_RMF_GAI.primaryGaiConsideration__provenance_techniques, domain=None, range=Optional[Union[str, list[str]]])

slots.primaryGaiConsideration__ai_incident_definition = Slot(uri=NIST_AI_RMF_GAI.ai_incident_definition, name="primaryGaiConsideration__ai_incident_definition", curie=NIST_AI_RMF_GAI.curie('ai_incident_definition'),
                   model_uri=NIST_AI_RMF_GAI.primaryGaiConsideration__ai_incident_definition, domain=None, range=Optional[str])

slots.gaiProfile__gai_risk_catalog = Slot(uri=NIST_AI_RMF_GAI.gai_risk_catalog, name="gaiProfile__gai_risk_catalog", curie=NIST_AI_RMF_GAI.curie('gai_risk_catalog'),
                   model_uri=NIST_AI_RMF_GAI.gaiProfile__gai_risk_catalog, domain=None, range=Optional[Union[dict[Union[str, GaiRiskId], Union[dict, GaiRisk]], list[Union[dict, GaiRisk]]]])

slots.gaiProfile__suggested_actions = Slot(uri=NIST_AI_RMF_GAI.suggested_actions, name="gaiProfile__suggested_actions", curie=NIST_AI_RMF_GAI.curie('suggested_actions'),
                   model_uri=NIST_AI_RMF_GAI.gaiProfile__suggested_actions, domain=None, range=Optional[Union[dict[Union[str, SuggestedActionId], Union[dict, SuggestedAction]], list[Union[dict, SuggestedAction]]]])

slots.gaiProfile__primary_considerations = Slot(uri=NIST_AI_RMF_GAI.primary_considerations, name="gaiProfile__primary_considerations", curie=NIST_AI_RMF_GAI.curie('primary_considerations'),
                   model_uri=NIST_AI_RMF_GAI.gaiProfile__primary_considerations, domain=None, range=Optional[Union[dict[Union[str, PrimaryGaiConsiderationId], Union[dict, PrimaryGaiConsideration]], list[Union[dict, PrimaryGaiConsideration]]]])

slots.gaiProfile__structured_feedback_methods = Slot(uri=NIST_AI_RMF_GAI.structured_feedback_methods, name="gaiProfile__structured_feedback_methods", curie=NIST_AI_RMF_GAI.curie('structured_feedback_methods'),
                   model_uri=NIST_AI_RMF_GAI.gaiProfile__structured_feedback_methods, domain=None, range=Optional[Union[dict[Union[str, StructuredPublicFeedbackId], Union[dict, StructuredPublicFeedback]], list[Union[dict, StructuredPublicFeedback]]]])

slots.AiRedTeaming_feedback_method_kind = Slot(uri=NIST_AI_RMF_GAI.feedback_method_kind, name="AiRedTeaming_feedback_method_kind", curie=NIST_AI_RMF_GAI.curie('feedback_method_kind'),
                   model_uri=NIST_AI_RMF_GAI.AiRedTeaming_feedback_method_kind, domain=AiRedTeaming, range=Union[str, "StructuredFeedbackMethodEnum"])

