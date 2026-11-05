from __future__ import annotations

import re
import sys
from datetime import (
    date,
    datetime,
    time
)
from decimal import Decimal
from enum import Enum
from typing import (
    Any,
    ClassVar,
    Literal,
    Optional,
    Union
)

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    RootModel,
    SerializationInfo,
    SerializerFunctionWrapHandler,
    field_validator,
    model_serializer
)


metamodel_version = "1.12.0"
version = "1.0.0"


class ConfiguredBaseModel(BaseModel):
    model_config = ConfigDict(
        serialize_by_alias = True,
        validate_by_name = True,
        validate_assignment = True,
        validate_default = True,
        extra = "forbid",
        arbitrary_types_allowed = True,
        use_enum_values = True,
        strict = False,
    )





class LinkMLMeta(RootModel):
    root: dict[str, Any] = {}
    model_config = ConfigDict(frozen=True)

    def __getattr__(self, key:str):
        return getattr(self.root, key)

    def __getitem__(self, key:str):
        return self.root[key]

    def __setitem__(self, key:str, value):
        self.root[key] = value

    def __contains__(self, key:str) -> bool:
        return key in self.root


linkml_meta = LinkMLMeta({'comments': ['The version is the 1.0.0 both publications carry, and source is '
                  "NIST's page for the framework. The release tags are the "
                  "schema's own versions.",
                  'Every module of lmodel/nist-ai-100-1 and lmodel/nist-ai-600-1 '
                  'is vendored in this folder as released, so the schema needs no '
                  'network, and tests/test_upstream.py holds them to their hashes. '
                  'Each element keeps the IRI of its publication, and this schema '
                  'adds only the class below.',
                  'The AI RMF to ISO/IEC 42001 crosswalk pairs records, not schema '
                  'elements, so it is no mapping of this schema. '
                  'scripts/build_crosswalk.py writes it as SSSOM under tmp/, and '
                  'the repository carries neither it nor its PDF, which states no '
                  'licence.'],
     'default_prefix': 'nist_ai_rmf',
     'default_range': 'string',
     'description': 'One LinkML schema for two NIST publications: the AI Risk '
                    'Management Framework 1.0 (NIST AI 100-1) and its Generative '
                    'AI Profile (NIST AI 600-1).',
     'id': 'https://w3id.org/lmodel/nist-ai-rmf',
     'imports': ['linkml:types',
                 './nist_ai_100_1/nist_ai_100_1',
                 './nist_ai_600_1'],
     'license': 'Apache-2.0',
     'name': 'nist_ai_rmf',
     'prefixes': {'linkml': {'prefix_prefix': 'linkml',
                             'prefix_reference': 'https://w3id.org/linkml/'},
                  'nist_ai_rmf': {'prefix_prefix': 'nist_ai_rmf',
                                  'prefix_reference': 'https://w3id.org/lmodel/nist-ai-rmf/'}},
     'see_also': ['https://lmodel.github.io/nist-ai-rmf',
                  'https://w3id.org/lmodel/nist-ai-100-1',
                  'https://w3id.org/lmodel/nist-ai-600-1'],
     'source': 'https://www.nist.gov/itl/ai-risk-management-framework',
     'source_file': 'src/nist_ai_rmf/schema/nist_ai_rmf.yaml',
     'title': 'NIST AI Risk Management Framework family'} )

class AiRmfCharacteristicName(str, Enum):
    """
    The seven characteristics of trustworthy AI systems in section 3 of the publication.
    """
    Valid_and_Reliable = "valid_and_reliable"
    """
    Shown by evidence to meet the needs of its intended use, and works without failure over time. Figure 4 makes it a necessary condition for the others.
    """
    Safe = "safe"
    """
    Keeps people, property and the environment out of danger under defined conditions.
    """
    Secure_and_Resilient = "secure_and_resilient"
    """
    Withstands adverse events and recovers from them, and keeps confidentiality, integrity and availability through protections against attack.
    """
    Accountable_and_Transparent = "accountable_and_transparent"
    """
    Answerable for outcomes, which rests on people being able to get information about the system and its outputs. Figure 4 shows it relating to all the others.
    """
    Explainable_and_Interpretable = "explainable_and_interpretable"
    """
    Its working can be represented (how a decision was made) and its output understood in context (why, and what it means for the user).
    """
    Privacy_Enhanced = "privacy_enhanced"
    """
    Guided by the norms and practices that protect human autonomy, identity and dignity, such as anonymity, confidentiality and control.
    """
    Fair_EN_DASH_with_Harmful_Bias_Managed = "fair_with_harmful_bias_managed"
    """
    Addresses equality and equity, including harmful bias and discrimination, knowing that views of fairness differ across cultures and applications.
    """


class AiRmfActorTaskName(str, Enum):
    """
    The ten AI actor tasks and five additional AI actors of Appendix A.
    """
    AI_Design = "ai_design"
    """
    Setting what the system is for, planning and designing it, and gathering and preparing its data.
    """
    AI_Development = "ai_development"
    """
    Providing the initial infrastructure, and creating, selecting, calibrating, training and testing models.
    """
    AI_Deployment = "ai_deployment"
    """
    Deciding how the system is used and putting it into production, including pilots and compliance checks.
    """
    Operation_and_Monitoring = "operation_and_monitoring"
    """
    Running the system and regularly assessing its output and impacts.
    """
    Test_Evaluation_Verification_and_Validation_LEFT_PARENTHESISTEVVRIGHT_PARENTHESIS = "tevv"
    """
    Examining the system or its components and finding and fixing problems, throughout the lifecycle.
    """
    Human_Factors = "human_factors"
    """
    Human-centered design and evaluation, involving end users and bringing context-specific norms and values into design.
    """
    Domain_Expert = "domain_expert"
    """
    Giving knowledge of the sector or setting where the system is used.
    """
    AI_Impact_Assessment = "ai_impact_assessment"
    """
    Assessing accountability, harmful bias, impacts, product safety, liability and security.
    """
    Procurement = "procurement"
    """
    Acquiring AI from another party, under financial, legal or policy authority.
    """
    Governance_and_Oversight = "governance_and_oversight"
    """
    Holding management, fiduciary and legal authority for the organization where the system is designed, developed or deployed.
    """
    Third_party_entities = "third_party_entities"
    """
    Outside organizations that supply or evaluate the data, models, systems or services an organization acquires.
    """
    End_users = "end_users"
    """
    The people or groups who use the system, whether new to technology or expert in AI.
    """
    Affected_individualsSOLIDUScommunities = "affected_individuals_and_communities"
    """
    Those directly or indirectly affected by the system or its output, whether or not they interact with it.
    """
    Other_AI_actors = "other_ai_actors"
    """
    Those who may provide norms or guidance on AI risk, such as standards bodies, advocacy groups and researchers.
    """
    General_public = "general_public"
    """
    Those most likely to experience the impacts directly, who may motivate what other AI actors do.
    """


class AiRmfDimensionName(str, Enum):
    """
    The key dimensions of an AI system in Figure 2.
    """
    Application_Context = "application_context"
    """
    The setting the system is planned for and operated in.
    """
    Data_and_Input = "data_and_input"
    """
    The data the system is built from and takes in.
    """
    AI_Model = "ai_model"
    """
    The models built, used, verified and validated.
    """
    Task_and_Output = "task_and_output"
    """
    What the system does and produces once deployed.
    """
    People_and_Planet = "people_and_planet"
    """
    Human rights and the well-being of society and the planet, at the center of Figure 2.
    """


class AiRmfLifecycleStageName(str, Enum):
    """
    The AI lifecycle stages in Figure 3, of which Figure 2 shows the first six.
    """
    Plan_and_Design = "plan_and_design"
    """
    Documenting the concept, objectives, assumptions, context and requirements.
    """
    Collect_and_Process_Data = "collect_and_process_data"
    """
    Gathering, validating and cleaning data, and recording what it holds.
    """
    Build_and_Use_Model = "build_and_use_model"
    """
    Creating or selecting algorithms and training models.
    """
    Verify_and_Validate = "verify_and_validate"
    """
    Verifying, validating, calibrating and interpreting model output.
    """
    Deploy_and_Use = "deploy_and_use"
    """
    Piloting, checking compatibility and compliance, managing change and evaluating user experience.
    """
    Operate_and_Monitor = "operate_and_monitor"
    """
    Operating the system and continually assessing its recommendations and impacts.
    """
    Use_or_Impacted_by = "use_or_impacted_by"
    """
    Using the technology or being affected by it, which Figure 3 places under People and Planet.
    """


class AiRmfAudience(str, Enum):
    """
    The two AI RMF audiences of section 2.
    """
    Primary_audience = "primary"
    """
    AI actors who carry out or manage work on AI systems and drive their risk management.
    """
    Informing_audience = "informing"
    """
    AI actors in the People and Planet dimension, who inform the primary audience.
    """


class AiRmfManagementChallengeName(str, Enum):
    """
    The challenges for AI risk management in section 1.2.
    """
    Risk_Measurement = "risk_measurement"
    """
    AI risks that are poorly defined or understood are hard to measure, which does not mean they are high or low.
    """
    Risk_Tolerance = "risk_tolerance"
    """
    The AI RMF can prioritize risk but prescribes no tolerance, which depends on context and changes over time.
    """
    Risk_Prioritization = "risk_prioritization"
    """
    Eliminating all negative risk is unrealistic, so effort goes first to the highest risks in a context of use.
    """
    Organizational_Integration_and_Management_of_Risk = "organizational_integration_and_management_of_risk"
    """
    AI risk belongs inside broader enterprise risk management, with accountability and commitment from senior levels.
    """


class AiRmfMeasurementChallengeName(str, Enum):
    """
    The challenges of measuring AI risk in section 1.2.1.
    """
    Risks_related_to_third_party_software_hardware_and_data = "third_party_software_hardware_and_data"
    """
    Third-party parts can speed work, but their metrics may not match or be disclosed, and how they are used adds risk.
    """
    Tracking_emergent_risks = "tracking_emergent_risks"
    """
    New risks need identifying, tracking and measuring, which impact assessment helps with.
    """
    Availability_of_reliable_metrics = "availability_of_reliable_metrics"
    """
    There is no consensus on robust, verifiable methods, and metrics can be oversimplified or gamed.
    """
    Risk_at_different_stages_of_the_AI_lifecycle = "risk_at_different_lifecycle_stages"
    """
    Results differ by stage, some risks stay latent, and AI actors see risk differently.
    """
    Risk_in_real_world_settings = "risk_in_real_world_settings"
    """
    What a laboratory measures may differ from what emerges in operation.
    """
    Inscrutability = "inscrutability"
    """
    Opaque systems, poor documentation and inherent uncertainty complicate measurement.
    """
    Human_baseline = "human_baseline"
    """
    A system that augments or replaces human activity needs a baseline, which is hard to systematize.
    """


class AiRmfRiskResponse(str, Enum):
    """
    The risk response options MANAGE 1.3 names.
    """
    Mitigating = "mitigating"
    """
    Reducing the likelihood or magnitude of the risk.
    """
    Transferring = "transferring"
    """
    Shifting the risk to another party.
    """
    Avoiding = "avoiding"
    """
    Not carrying out what creates the risk.
    """
    Accepting = "accepting"
    """
    Bearing the risk without further action.
    """


class AiRmfImpactDirection(str, Enum):
    """
    Whether an impact is positive, negative or both, as section 1.1 puts it.
    """
    Positive = "positive"
    """
    An opportunity or benefit.
    """
    Negative = "negative"
    """
    A threat or harm.
    """
    Both = "both"
    """
    Positive and negative at once.
    """


class AiRmfAffectedParty(str, Enum):
    """
    Who section 1.1 says can experience negative impact or harm.
    """
    Individuals = "individuals"
    """
    Particular people.
    """
    Groups = "groups"
    """
    Groups of people.
    """
    Communities = "communities"
    """
    Communities of people.
    """
    Organizations = "organizations"
    """
    Organizations.
    """
    Society = "society"
    """
    Society at large.
    """
    The_environment = "environment"
    """
    The natural environment.
    """
    The_planet = "planet"
    """
    The planet as a whole.
    """


class AiRmfHarmCategory(str, Enum):
    """
    The three headings of Figure 1.
    """
    Harm_to_People = "people"
    """
    Harm that falls on individuals, groups, communities or society.
    """
    Harm_to_an_Organization = "organization"
    """
    Harm that falls on an organization.
    """
    Harm_to_an_Ecosystem = "ecosystem"
    """
    Harm that falls on interconnected systems and resources.
    """


class AiRmfHarmExample(str, Enum):
    """
    The examples of potential harm in Figure 1, which NIST offers as examples and not as a closed list.
    """
    Individual = "individual"
    """
    To a person's civil liberties, rights, safety or economic opportunity.
    """
    GroupSOLIDUSCommunity = "group_or_community"
    """
    To a group, such as discrimination against a sub-group of a population.
    """
    Societal = "societal"
    """
    To democratic participation or educational access.
    """
    Business_operations = "business_operations"
    """
    To how an organization operates.
    """
    Security_breaches_or_monetary_loss = "security_breach_or_monetary_loss"
    """
    To an organization through a breach of security or a loss of money.
    """
    Reputation = "reputation"
    """
    To an organization's standing.
    """
    Interconnected_and_interdependent_elements_and_resources = "interdependent_elements"
    """
    To parts and resources that depend on each other.
    """
    Global_financial_system_supply_chain_or_interrelated_systems = "financial_or_supply_systems"
    """
    To large systems that link organizations.
    """
    Natural_resources_the_environment_and_planet = "natural_resources_and_environment"
    """
    To the natural world.
    """


class AiRmfBiasCategory(str, Enum):
    """
    The three major categories of AI bias in section 3.7, each of which can occur without prejudice or discriminatory intent.
    """
    Systemic = "systemic"
    """
    In datasets, in organizational norms and processes, and in the wider society that uses AI.
    """
    Computational_and_statistical = "computational_and_statistical"
    """
    In datasets and algorithms, often from systematic errors due to samples that are not representative.
    """
    Human_cognitive = "human_cognitive"
    """
    In how people perceive system information to decide, or think about what a system is for.
    """


class AiRmfProfileKind(str, Enum):
    """
    The kinds of AI RMF profile that section 6 names.
    """
    Use_case_profile = "use_case"
    """
    The Core implemented for a specific setting or application.
    """
    Current_Profile = "current"
    """
    A temporal profile saying how AI is managed today and the related risks, in terms of current outcomes.
    """
    Target_Profile = "target"
    """
    A temporal profile saying which outcomes the desired risk management goals need.
    """
    Cross_sectoral_profile = "cross_sectoral"
    """
    Covers risks of models or applications used across use cases or sectors, or activities common to them, such as using large language models.
    """


class GaiRiskName(str, Enum):
    """
    The 12 risks of section 2.
    """
    CBRN_Information_or_Capabilities = "cbrn_information_or_capabilities"
    """
    Easier access to dangerous information or design abilities for chemical, biological, radiological or nuclear weapons.
    """
    Confabulation = "confabulation"
    """
    Confident but wrong output that can mislead users.
    """
    Dangerous_Violent_or_Hateful_Content = "dangerous_violent_or_hateful_content"
    """
    Easier production of content that incites or threatens, recommends harm, or disparages.
    """
    Data_Privacy = "data_privacy"
    """
    Leaks, misuse or de-anonymization of personal or sensitive data.
    """
    Environmental_Impacts = "environmental_impacts"
    """
    Effects on ecosystems from the heavy computing that training and operating models need.
    """
    Harmful_Bias_or_Homogenization = "harmful_bias_or_homogenization"
    """
    Worse systemic bias, unequal performance across groups or languages, and output skewed by sameness.
    """
    Human_AI_Configuration = "human_ai_configuration"
    """
    Interaction that leads people to over-rely on, anthropomorphize or become entangled with a system, or to distrust it.
    """
    Information_Integrity = "information_integrity"
    """
    Easier creation and spread of content that blurs fact and opinion, or that can drive large disinformation campaigns.
    """
    Information_Security = "information_security"
    """
    Easier offensive cyber activity, and a larger attack surface on a system, its data, code or weights.
    """
    Intellectual_Property = "intellectual_property"
    """
    Easier unauthorized copying of protected content, exposure of trade secrets, and plagiarism.
    """
    Obscene_Degrading_andSOLIDUSor_Abusive_Content = "obscene_degrading_or_abusive_content"
    """
    Easier production of harmful imagery, including synthetic abuse material and intimate images without consent.
    """
    Value_Chain_and_Component_Integration = "value_chain_and_component_integration"
    """
    Opaque use of third-party components and data, and poor supplier vetting, that weaken accountability downstream.
    """


class GaiRiskGrouping(str, Enum):
    """
    The three groups into which footnote 5 says an organization could sort the risks, as one possible way.
    """
    Technical_SOLIDUS_Model_risks = "technical_or_model"
    """
    Risks from malfunction.
    """
    Misuse_by_humans = "misuse_by_humans"
    """
    Risks from malicious use.
    """
    Ecosystem_SOLIDUS_societal_risks = "ecosystem_or_societal"
    """
    Systemic risks.
    """


class GaiLifecycleStage(str, Enum):
    """
    The lifecycle stages section 2 names for GAI. They differ from the seven stages of the AI RMF's Figure 3.
    """
    Design = "design"
    """
    Setting out the system before it is built.
    """
    Development = "development"
    """
    Building and training it.
    """
    Deployment = "deployment"
    """
    Putting it into use.
    """
    Operation = "operation"
    """
    Running it.
    """
    Decommissioning = "decommissioning"
    """
    Retiring it.
    """


class GaiRiskScope(str, Enum):
    """
    The levels where section 2 says a risk may exist.
    """
    Model_or_system = "model_or_system"
    """
    The level of one model or system.
    """
    Application_or_implementation = "application_or_implementation"
    """
    The level of one specific use case.
    """
    Ecosystem = "ecosystem"
    """
    Beyond one system or organization, such as algorithmic monocultures or effects on labor markets.
    """


class GaiRiskSource(str, Enum):
    """
    Where section 2 says a risk may come from.
    """
    Design = "design"
    """
    The design of the model itself.
    """
    Training = "training"
    """
    The training of the model.
    """
    Operation = "operation"
    """
    The operation of the model.
    """
    Inputs = "inputs"
    """
    What goes into the model or system.
    """
    Outputs = "outputs"
    """
    What the system produces.
    """
    Human_behavior = "human_behavior"
    """
    Abuse, misuse or unsafe repurposing by people, whether adversarial or not.
    """
    Human_AI_interaction = "human_ai_interaction"
    """
    How a person and a system act on each other.
    """


class GaiRiskTimeScale(str, Enum):
    """
    How section 2 says a risk may materialize over time.
    """
    Abruptly = "abrupt"
    """
    All at once, such as immediate emotional harm from a harmful deepfake image.
    """
    Across_extended_periods = "extended"
    """
    Slowly, such as the long-term effect of disinformation on trust in institutions.
    """


class GaiGovernancePlan(str, Enum):
    """
    The plans and actions that section A.1.2 says apply to GAI from other AI governance.
    """
    Accessibility_and_reasonable_accommodations = "accessibility_and_reasonable_accommodations"
    AI_actor_credentials_and_qualifications = "ai_actor_credentials_and_qualifications"
    Alignment_to_organizational_values = "alignment_to_organizational_values"
    Auditing_and_assessment = "auditing_and_assessment"
    Change_management_controls = "change_management_controls"
    Commercial_use = "commercial_use"
    Data_provenance = "data_provenance"
    Data_protection = "data_protection"
    Data_retention = "data_retention"
    Consistency_in_use_of_defining_key_terms = "consistency_in_use_of_defining_key_terms"
    Decommissioning = "decommissioning"
    Discouraging_anonymous_use = "discouraging_anonymous_use"
    Education = "education"
    Impact_assessments = "impact_assessments"
    Incident_response = "incident_response"
    Monitoring = "monitoring"
    Opt_outs = "opt_outs"
    Risk_based_controls = "risk_based_controls"
    Risk_mapping_and_measurement = "risk_mapping_and_measurement"
    Science_backed_TEVV_practices = "science_backed_tevv_practices"
    Secure_software_development_practices = "secure_software_development_practices"
    Stakeholder_engagement = "stakeholder_engagement"
    Synthetic_content_detection_and_labeling_tools_and_techniques = "synthetic_content_detection_and_labeling_tools_and_techniques"
    Whistleblower_protections = "whistleblower_protections"
    Workforce_diversity_and_interdisciplinary_teams = "workforce_diversity_and_interdisciplinary_teams"


class GaiThirdPartyControl(str, Enum):
    """
    The existing controls that section A.1.3 says can apply to third-party GAI.
    """
    Acquisition_and_procurement_due_diligence = "acquisition_and_procurement_due_diligence"
    """
    Checking a provider before acquiring its GAI technology or data.
    """
    Requests_for_software_bills_of_materials = "software_bills_of_materials"
    """
    Asking a provider what its software is made of.
    """
    Application_of_service_level_agreements = "service_level_agreements"
    """
    Holding a provider to agreed levels of service.
    """
    Statement_on_standards_for_attestation_engagement_reports = "ssae_reports"
    """
    Asking for a provider's attestation reports.
    """


class GaiRedTeamingType(str, Enum):
    """
    The types of AI red-teaming in section A.1.5.
    """
    General_Public = "general_public"
    """
    By general users who are not necessarily AI or technical experts.
    """
    Expert = "expert"
    """
    By specialists in the domain or the context of use.
    """
    Combination = "combination"
    """
    By both experts and general public participants.
    """
    Human_SOLIDUS_AI = "human_ai"
    """
    By GAI together with human teams, specialist or not.
    """


class GaiProvenanceTechnique(str, Enum):
    """
    The techniques for provenance data tracking in section A.1.6.
    """
    Digital_watermarking = "digital_watermarking"
    """
    Placing visible or hidden marks on content.
    """
    Metadata_recording = "metadata_recording"
    """
    Recording facts about the content, such as its creator, date and sources.
    """
    Digital_fingerprinting = "digital_fingerprinting"
    """
    Identifying content from its own characteristics.
    """
    Human_authentication = "human_authentication"
    """
    Having people confirm where content came from.
    """


class GaiIncidentHarm(str, Enum):
    """
    The kinds of harm that section A.1.8's definition of an AI incident names.
    """
    Injury_or_harm_to_health = "injury_or_harm_to_health"
    """
    To a person or group, including psychological harm and harm to mental health.
    """
    Disruption_of_critical_infrastructure = "critical_infrastructure_disruption"
    """
    To its management and operation.
    """
    Violations_of_rights_or_legal_obligations = "rights_violations"
    """
    Of human rights, or of obligations under law that protects fundamental, labor and intellectual property rights.
    """
    Harm_to_property_communities_or_the_environment = "harm_to_property_communities_or_environment"
    """
    To things and groups beyond the individual.
    """



class AiRmfRecord(ConfiguredBaseModel):
    """
    The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct from what the publication itself lists.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nist_ai_100_1:Record',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_base'})

    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfTrustworthinessCharacteristic(ConfiguredBaseModel):
    """
    A characteristic of trustworthy AI systems, each with a subsection of section 3.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:TrustworthinessCharacteristic',
         'comments': ['Addressing the characteristics one by one does not make a '
                      'system trustworthy, since they trade off against each other.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_characteristic_name: AiRmfCharacteristicName = Field(default=..., description="""Which characteristic this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfTrustworthinessCharacteristic']} })
    ai_rmf_characteristic_section: str = Field(default=..., description="""The subsection of the publication that describes it, such as 3.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfTrustworthinessCharacteristic']} })
    ai_rmf_characteristic_is_base: Optional[bool] = Field(default=None, description="""Whether Figure 4 shows it as the necessary condition under the others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfTrustworthinessCharacteristic']} })
    ai_rmf_characteristic_relates_to_all: Optional[bool] = Field(default=None, description="""Whether Figure 4 shows it relating to all the others.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfTrustworthinessCharacteristic']} })

    @field_validator('ai_rmf_characteristic_section')
    def pattern_ai_rmf_characteristic_section(cls, v):
        pattern=re.compile(r"^3\.[1-7]$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid ai_rmf_characteristic_section format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid ai_rmf_characteristic_section format: {v}"
            raise ValueError(err_msg)
        return v


class AiRmfDimension(ConfiguredBaseModel):
    """
    One of the five key socio-technical dimensions of an AI system in Figure 2.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:Dimension',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_dimension_name: AiRmfDimensionName = Field(default=..., description="""Which dimension this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfDimension']} })
    ai_rmf_dimension_audience: AiRmfAudience = Field(default=..., description="""The AI RMF audience formed by the AI actors in this dimension.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfDimension']} })


class AiRmfLifecycleStage(ConfiguredBaseModel):
    """
    A stage of the AI lifecycle as a column of Figure 3 shows it, under its dimension.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:LifecycleStage',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_lifecycle_stage_name: AiRmfLifecycleStageName = Field(default=..., description="""Which stage this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfLifecycleStage']} })
    ai_rmf_lifecycle_stage_dimension: AiRmfDimensionName = Field(default=..., description="""The dimension Figure 3 places the stage under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfLifecycleStage']} })
    ai_rmf_lifecycle_stage_tevv: Optional[str] = Field(default=None, description="""The testing, evaluation, verification and validation (TEVV) Figure 3 gives the stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfLifecycleStage']} })
    ai_rmf_lifecycle_stage_representative_actors: Optional[list[str]] = Field(default=None, description="""The representative AI actors Figure 3 lists for the stage.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfLifecycleStage']} })


class AiRmfActorTask(ConfiguredBaseModel):
    """
    A task or additional AI actor of Appendix A.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:ActorTask',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_actor_task_name: AiRmfActorTaskName = Field(default=..., description="""Which task or additional AI actor this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfActorTask']} })
    ai_rmf_actor_task_is_additional_actor: Optional[bool] = Field(default=None, description="""Whether Appendix A lists it under Additional AI Actors rather than as a task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfActorTask']} })
    ai_rmf_actor_task_representative_actors: Optional[list[str]] = Field(default=None, description="""The AI actors that Appendix A says carry out the task.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfActorTask']} })


class AiRmfManagementChallenge(ConfiguredBaseModel):
    """
    One of the four challenges for AI risk management in section 1.2.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:ManagementChallenge',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_management_challenge_name: AiRmfManagementChallengeName = Field(default=..., description="""Which challenge this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfManagementChallenge']} })
    ai_rmf_management_challenge_measurement_challenges: Optional[list[AiRmfMeasurementChallenge]] = Field(default=None, description="""The risk measurement challenges of section 1.2.1, under the challenge of risk measurement.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfManagementChallenge']} })


class AiRmfMeasurementChallenge(ConfiguredBaseModel):
    """
    One of the challenges of measuring AI risk in section 1.2.1.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:MeasurementChallenge',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_measurement_challenge_name: AiRmfMeasurementChallengeName = Field(default=..., description="""Which challenge this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfMeasurementChallenge']} })


class AiRmfSpecificRisk(ConfiguredBaseModel):
    """
    A risk that Appendix B says is new or increased for AI compared with traditional software.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:SpecificRisk',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations',
         'slot_usage': {'title': {'description': "This project's short name for the "
                                                 'item. Appendix B gives its items no '
                                                 'names.',
                                  'name': 'title',
                                  'required': True}}})

    title: str = Field(default=..., description="""This project's short name for the item. Appendix B gives its items no names.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_specific_risk_position: int = Field(default=..., description="""The item's position in Appendix B's list, which is not numbered.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSpecificRisk']} })


class AiRmfHumanAiIssue(ConfiguredBaseModel):
    """
    An issue of human-AI interaction that Appendix C says merits further consideration and research.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:HumanAiIssue',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations',
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_human_ai_issue_number: int = Field(default=..., description="""The issue's number in Appendix C.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfHumanAiIssue']} })


class AiRmfAttribute(ConfiguredBaseModel):
    """
    A key attribute of the AI RMF in Appendix D, which guided its development.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:Attribute',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations',
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_attribute_number: int = Field(default=..., description="""The attribute's number in Appendix D.""", ge=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfAttribute']} })


class AiRmfSystem(AiRmfRecord):
    """
    A machine-based system that produces outputs such as predictions or decisions for given objectives, with varying autonomy.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:AiSystem',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    ai_rmf_system_intended_purposes: Optional[list[str]] = Field(default=None, description="""What the system is for, and its potentially beneficial uses, which MAP 1.1 asks an adopter to document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSystem']} })
    ai_rmf_system_deployment_settings: Optional[list[str]] = Field(default=None, description="""The settings the system is or will be deployed in, which MAP 1.1 asks an adopter to document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSystem']} })
    ai_rmf_system_lifecycle_stages: Optional[list[AiRmfLifecycleStageName]] = Field(default=None, description="""The lifecycle stages the record covers.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSystem']} })
    ai_rmf_system_actors: Optional[list[str]] = Field(default=None, description="""The AI actors with a role in the system's lifecycle, such as those MAP 1.6 says elicit its requirements.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSystem']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfActor(AiRmfRecord):
    """
    An organization or individual with an active role in an AI system's lifecycle.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['prov:Agent'],
         'class_uri': 'nist_ai_100_1:AiActor',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    ai_rmf_actor_tasks: Optional[list[AiRmfActorTaskName]] = Field(default=None, description="""The tasks the actor carries out, or the additional AI actor it is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfActor']} })
    ai_rmf_actor_audience: Optional[AiRmfAudience] = Field(default=None, description="""The AI RMF audience the actor belongs to.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfActor']} })
    ai_rmf_actor_lifecycle_stages: Optional[list[AiRmfLifecycleStageName]] = Field(default=None, description="""The lifecycle stages the actor works in.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfActor']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfRisk(AiRmfRecord):
    """
    How likely an event is, combined with how severe its consequences are.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:Risk',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations',
         'related_mappings': ['iso27001:IsmsRisk']})

    ai_rmf_likelihood: Optional[str] = Field(default=None, description="""How likely the event or impact is, on whatever scale the adopter uses.""", json_schema_extra = { "linkml_meta": {'comments': ['The publication sets no scale, and the Playbook allows '
                      'qualitative ones, so this is text rather than a probability.'],
         'domain_of': ['AiRmfRisk', 'AiRmfImpact']} })
    ai_rmf_magnitude: Optional[str] = Field(default=None, description="""How large the consequences are, on whatever scale the adopter uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk', 'AiRmfImpact']} })
    ai_rmf_risk_system: Optional[str] = Field(default=None, description="""The AI system the risk concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_impacts: Optional[list[AiRmfImpact]] = Field(default=None, description="""The impacts that contribute to the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_characteristics: Optional[list[AiRmfCharacteristicName]] = Field(default=None, description="""The trustworthiness characteristics the risk bears on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_lifecycle_stages: Optional[list[AiRmfLifecycleStageName]] = Field(default=None, description="""The lifecycle stages where the risk is measured or arises.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_responses: Optional[list[AiRmfRiskResponse]] = Field(default=None, description="""The responses chosen for the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_priority: Optional[str] = Field(default=None, description="""The priority the adopter gives the risk's treatment, on whatever scale it uses, as MANAGE 1.2 asks.""", json_schema_extra = { "linkml_meta": {'comments': ['MANAGE 1.3 speaks of risks deemed high priority and the '
                      'publication sets no scale, so this is text.'],
         'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_tolerance: Optional[str] = Field(default=None, description="""The risk tolerance the risk is judged against, which GOVERN 1.3 and MAP 1.5 ask an adopter to document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfResidualRisk(AiRmfRisk):
    """
    The risk that remains after risk treatment.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:ResidualRisk',
         'comments': ['Section 1.2.3 defines residual risk this way, after ISO Guide '
                      '73. MANAGE 1.4 instead calls negative residual risks the sum of '
                      'all unmitigated risks.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    ai_rmf_likelihood: Optional[str] = Field(default=None, description="""How likely the event or impact is, on whatever scale the adopter uses.""", json_schema_extra = { "linkml_meta": {'comments': ['The publication sets no scale, and the Playbook allows '
                      'qualitative ones, so this is text rather than a probability.'],
         'domain_of': ['AiRmfRisk', 'AiRmfImpact']} })
    ai_rmf_magnitude: Optional[str] = Field(default=None, description="""How large the consequences are, on whatever scale the adopter uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk', 'AiRmfImpact']} })
    ai_rmf_risk_system: Optional[str] = Field(default=None, description="""The AI system the risk concerns.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_impacts: Optional[list[AiRmfImpact]] = Field(default=None, description="""The impacts that contribute to the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_characteristics: Optional[list[AiRmfCharacteristicName]] = Field(default=None, description="""The trustworthiness characteristics the risk bears on.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_lifecycle_stages: Optional[list[AiRmfLifecycleStageName]] = Field(default=None, description="""The lifecycle stages where the risk is measured or arises.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_responses: Optional[list[AiRmfRiskResponse]] = Field(default=None, description="""The responses chosen for the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_priority: Optional[str] = Field(default=None, description="""The priority the adopter gives the risk's treatment, on whatever scale it uses, as MANAGE 1.2 asks.""", json_schema_extra = { "linkml_meta": {'comments': ['MANAGE 1.3 speaks of risks deemed high priority and the '
                      'publication sets no scale, so this is text.'],
         'domain_of': ['AiRmfRisk']} })
    ai_rmf_risk_tolerance: Optional[str] = Field(default=None, description="""The risk tolerance the risk is judged against, which GOVERN 1.3 and MAP 1.5 ask an adopter to document.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfImpact(AiRmfRecord):
    """
    A consequence of an AI system, which may be an opportunity, a threat or both.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:Impact',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    ai_rmf_likelihood: Optional[str] = Field(default=None, description="""How likely the event or impact is, on whatever scale the adopter uses.""", json_schema_extra = { "linkml_meta": {'comments': ['The publication sets no scale, and the Playbook allows '
                      'qualitative ones, so this is text rather than a probability.'],
         'domain_of': ['AiRmfRisk', 'AiRmfImpact']} })
    ai_rmf_magnitude: Optional[str] = Field(default=None, description="""How large the consequences are, on whatever scale the adopter uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk', 'AiRmfImpact']} })
    ai_rmf_impact_direction: AiRmfImpactDirection = Field(default=..., description="""Whether the consequence is positive, negative or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfImpact']} })
    ai_rmf_impact_affected_parties: Optional[list[AiRmfAffectedParty]] = Field(default=None, description="""Who or what experiences the consequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfImpact']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfHarm(AiRmfImpact):
    """
    A negative impact, sorted as in Figure 1 by whether it falls on people, an organization or an ecosystem.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:Harm',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations',
         'rules': [{'description': 'A harm is a negative impact.',
                    'postconditions': {'slot_conditions': {'ai_rmf_impact_direction': {'equals_string': 'negative',
                                                                                       'name': 'ai_rmf_impact_direction'}}},
                    'preconditions': {'slot_conditions': {'ai_rmf_harm_category': {'name': 'ai_rmf_harm_category',
                                                                                   'value_presence': 'PRESENT'}}}},
                   {'description': 'An example of harm to people goes with harm to '
                                   'people.',
                    'postconditions': {'slot_conditions': {'ai_rmf_harm_example': {'any_of': [{'equals_string': 'individual'},
                                                                                              {'equals_string': 'group_or_community'},
                                                                                              {'equals_string': 'societal'}],
                                                                                   'name': 'ai_rmf_harm_example'}}},
                    'preconditions': {'slot_conditions': {'ai_rmf_harm_category': {'equals_string': 'people',
                                                                                   'name': 'ai_rmf_harm_category'},
                                                          'ai_rmf_harm_example': {'name': 'ai_rmf_harm_example',
                                                                                  'value_presence': 'PRESENT'}}}},
                   {'description': 'An example of harm to an organization goes with '
                                   'harm to an organization.',
                    'postconditions': {'slot_conditions': {'ai_rmf_harm_example': {'any_of': [{'equals_string': 'business_operations'},
                                                                                              {'equals_string': 'security_breach_or_monetary_loss'},
                                                                                              {'equals_string': 'reputation'}],
                                                                                   'name': 'ai_rmf_harm_example'}}},
                    'preconditions': {'slot_conditions': {'ai_rmf_harm_category': {'equals_string': 'organization',
                                                                                   'name': 'ai_rmf_harm_category'},
                                                          'ai_rmf_harm_example': {'name': 'ai_rmf_harm_example',
                                                                                  'value_presence': 'PRESENT'}}}},
                   {'description': 'An example of harm to an ecosystem goes with harm '
                                   'to an ecosystem.',
                    'postconditions': {'slot_conditions': {'ai_rmf_harm_example': {'any_of': [{'equals_string': 'interdependent_elements'},
                                                                                              {'equals_string': 'financial_or_supply_systems'},
                                                                                              {'equals_string': 'natural_resources_and_environment'}],
                                                                                   'name': 'ai_rmf_harm_example'}}},
                    'preconditions': {'slot_conditions': {'ai_rmf_harm_category': {'equals_string': 'ecosystem',
                                                                                   'name': 'ai_rmf_harm_category'},
                                                          'ai_rmf_harm_example': {'name': 'ai_rmf_harm_example',
                                                                                  'value_presence': 'PRESENT'}}}}]})

    ai_rmf_harm_category: AiRmfHarmCategory = Field(default=..., description="""The heading of Figure 1 the harm falls under.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfHarm']} })
    ai_rmf_harm_example: Optional[AiRmfHarmExample] = Field(default=None, description="""The example of Figure 1 the harm matches, which must sit under the harm's category.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfHarm']} })
    ai_rmf_likelihood: Optional[str] = Field(default=None, description="""How likely the event or impact is, on whatever scale the adopter uses.""", json_schema_extra = { "linkml_meta": {'comments': ['The publication sets no scale, and the Playbook allows '
                      'qualitative ones, so this is text rather than a probability.'],
         'domain_of': ['AiRmfRisk', 'AiRmfImpact']} })
    ai_rmf_magnitude: Optional[str] = Field(default=None, description="""How large the consequences are, on whatever scale the adopter uses.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRisk', 'AiRmfImpact']} })
    ai_rmf_impact_direction: AiRmfImpactDirection = Field(default=..., description="""Whether the consequence is positive, negative or both.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfImpact']} })
    ai_rmf_impact_affected_parties: Optional[list[AiRmfAffectedParty]] = Field(default=None, description="""Who or what experiences the consequence.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfImpact']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfRiskTolerance(AiRmfRecord):
    """
    An organization's or AI actor's readiness to bear risk to achieve its objectives. The AI RMF prescribes none.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:RiskTolerance',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations'})

    ai_rmf_risk_tolerance_holder: Optional[str] = Field(default=None, description="""The organization or AI actor whose tolerance this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRiskTolerance']} })
    ai_rmf_risk_tolerance_influences: Optional[list[str]] = Field(default=None, description="""What influences it, such as a law, a regulation, a policy or a norm.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRiskTolerance']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfBias(AiRmfRecord):
    """
    A bias to consider and manage, sorted into NIST's three major categories.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:Bias',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_foundations',
         'see_also': ['https://doi.org/10.6028/NIST.SP.1270']})

    ai_rmf_bias_categories: list[AiRmfBiasCategory] = Field(default=..., description="""The categories it falls under.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfBias']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfFunction(ConfiguredBaseModel):
    """
    One of the four functions that organize AI risk management at the highest level. GOVERN cuts across the other three.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Group'],
         'class_uri': 'nist_ai_100_1:Function',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_rmf_core',
         'related_mappings': ['nist_csf_v2:Function'],
         'slot_usage': {'description': {'description': 'The one-sentence overview in '
                                                       "NIST's catalog. The "
                                                       'publication gives each '
                                                       'function a section of its own '
                                                       'instead.',
                                        'name': 'description'}}})

    ai_rmf_function_id: str = Field(default=..., description="""The function's name, such as GOVERN.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFunction']} })
    description: Optional[str] = Field(default=None, description="""The one-sentence overview in NIST's catalog. The publication gives each function a section of its own instead.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_function_categories: Optional[list[AiRmfCategory]] = Field(default=None, description="""The categories of the function. A knowledge bundle relates a category to its function with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFunction']} })


class AiRmfCategory(ConfiguredBaseModel):
    """
    A group of related outcomes within a function, such as GOVERN 1, which Tables 1 to 4 state.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_ai_100_1:Category',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_rmf_core',
         'related_mappings': ['nist_csf_v2:Category'],
         'slot_usage': {'description': {'description': "The category's statement in "
                                                       'the publication.',
                                        'name': 'description',
                                        'pattern': '^\\s*\\S',
                                        'required': True}}})

    ai_rmf_category_id: str = Field(default=..., description="""The category's identifier, such as GOVERN 1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfCategory']} })
    description: str = Field(default=..., description="""The category's statement in the publication.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_category_subcategories: Optional[list[AiRmfSubcategory]] = Field(default=None, description="""The subcategories of the category. A knowledge bundle relates a subcategory to its category with isPartOf instead.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfCategory']} })

    @field_validator('description')
    def pattern_description(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid description format: {v}"
            raise ValueError(err_msg)
        return v


class AiRmfSubcategory(ConfiguredBaseModel):
    """
    A specific outcome within a category, such as GOVERN 1.1, which Tables 1 to 4 state, and its Playbook material.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Control'],
         'class_uri': 'nist_ai_100_1:Subcategory',
         'comments': ['Everything but the identifier and the statement comes from the '
                      'Playbook, a companion NIST updates apart from the publication.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_rmf_core',
         'related_mappings': ['nist_csf_v2:Subcategory'],
         'slot_usage': {'description': {'description': "The subcategory's statement in "
                                                       'the publication.',
                                        'name': 'description',
                                        'pattern': '^\\s*\\S',
                                        'required': True}}})

    ai_rmf_subcategory_id: str = Field(default=..., description="""The subcategory's identifier, such as GOVERN 1.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory', 'GaiSubcategory']} })
    description: str = Field(default=..., description="""The subcategory's statement in the publication.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    ai_rmf_subcategory_about: Optional[list[str]] = Field(default=None, description="""The Playbook's discussion of the outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory']} })
    ai_rmf_subcategory_suggested_actions: Optional[list[AiRmfSuggestedAction]] = Field(default=None, description="""The steps the Playbook suggests towards the outcome. They are voluntary and are not a checklist.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory']} })
    ai_rmf_subcategory_documentation: Optional[list[AiRmfDocumentationItem]] = Field(default=None, description="""What the Playbook suggests an organization document, mostly as questions.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory']} })
    ai_rmf_subcategory_transparency_resources: Optional[list[AiRmfResource]] = Field(default=None, description="""The sources the Playbook names as AI transparency resources.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory']} })
    ai_rmf_subcategory_references: Optional[list[AiRmfResource]] = Field(default=None, description="""The Playbook's references for the outcome.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory']} })
    ai_rmf_subcategory_ai_actors: Optional[list[AiRmfActorTaskName]] = Field(default=None, description="""The AI actors the Playbook tags the outcome with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory']} })
    ai_rmf_subcategory_topics: Optional[list[str]] = Field(default=None, description="""The topics the Playbook tags the outcome with. NIST keeps no closed list of them.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory']} })

    @field_validator('description')
    def pattern_description(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid description format: {v}"
            raise ValueError(err_msg)
        return v


class AiRmfSuggestedAction(ConfiguredBaseModel):
    """
    One step the Playbook suggests towards a subcategory's outcome.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_ai_100_1:SuggestedAction',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_rmf_core',
         'slot_usage': {'description': {'name': 'description',
                                        'pattern': '^\\s*\\S',
                                        'required': True}}})

    ai_rmf_suggested_action_id: str = Field(default=..., description="""The suggested action's identifier, such as SA-GOVERN_1.1-1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSuggestedAction']} })
    description: str = Field(default=..., description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })

    @field_validator('description')
    def pattern_description(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid description format: {v}"
            raise ValueError(err_msg)
        return v


class AiRmfDocumentationItem(ConfiguredBaseModel):
    """
    One thing the Playbook suggests an organization document for a subcategory.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_ai_100_1:DocumentationItem',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_rmf_core',
         'slot_usage': {'description': {'name': 'description',
                                        'pattern': '^\\s*\\S',
                                        'required': True}}})

    ai_rmf_documentation_id: str = Field(default=..., description="""The documentation prompt's identifier, such as D-GOVERN_1.1-1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfDocumentationItem']} })
    description: str = Field(default=..., description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })

    @field_validator('description')
    def pattern_description(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid description format: {v}"
            raise ValueError(err_msg)
        return v


class AiRmfResource(ConfiguredBaseModel):
    """
    A source the Playbook points to, by the title and address NIST's catalog gives it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Resource'],
         'class_uri': 'nist_ai_100_1:Resource',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_rmf_core',
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    ai_rmf_resource_uuid: str = Field(default=..., description="""The UUID of the resource in the back matter of NIST's catalog.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfResource']} })
    ai_rmf_resource_address: Optional[str] = Field(default=None, description="""The address NIST's catalog gives the source. The catalog gives none for a few.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfResource']} })

    @field_validator('ai_rmf_resource_uuid')
    def pattern_ai_rmf_resource_uuid(cls, v):
        pattern=re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid ai_rmf_resource_uuid format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid ai_rmf_resource_uuid format: {v}"
            raise ValueError(err_msg)
        return v


class AiRmfProfile(AiRmfRecord):
    """
    An implementation of the Core's functions, categories and subcategories for a setting, application or technology, based on the adopter's requirements, risk tolerance and resources.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_100_1:Profile',
         'comments': ['The publication prescribes no profile template, so only the '
                      'kinds and the subcategories are structured.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1/nist_ai_100_1_profiles',
         'related_mappings': ['oscal:Profile']})

    ai_rmf_profile_kinds: list[AiRmfProfileKind] = Field(default=..., description="""Which of the publication's kinds of profile this is. A current profile for one use case is both.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_profile_setting: Optional[str] = Field(default=None, description="""The sector, industry, technology, organization or end use the profile covers, such as hiring.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_profile_subcategories: Optional[list[str]] = Field(default=None, description="""The subcategories the profile selects. An adopter may select from them rather than apply all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class AiRmfFramework(ConfiguredBaseModel):
    """
    One edition of the AI RMF as a whole, with the Core and the lists the publication gives.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Catalog'],
         'class_uri': 'nist_ai_100_1:Framework',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-100-1',
         'tree_root': True})

    ai_rmf_version: str = Field(default=..., description="""The edition in NIST's two-number form, such as 1.0.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_functions: list[AiRmfFunction] = Field(default=..., description="""The four functions, in the publication's order.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_characteristics: Optional[list[AiRmfTrustworthinessCharacteristic]] = Field(default=None, description="""The trustworthiness characteristics of section 3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_dimensions: Optional[list[AiRmfDimension]] = Field(default=None, description="""The key dimensions of Figure 2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_lifecycle_stages: Optional[list[AiRmfLifecycleStage]] = Field(default=None, description="""The lifecycle stages of Figure 3.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_actor_task_list: Optional[list[AiRmfActorTask]] = Field(default=None, description="""The AI actor tasks and additional AI actors of Appendix A.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_management_challenges: Optional[list[AiRmfManagementChallenge]] = Field(default=None, description="""The challenges for AI risk management of section 1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_specific_risks: Optional[list[AiRmfSpecificRisk]] = Field(default=None, description="""The AI-specific risks of Appendix B.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_human_ai_issues: Optional[list[AiRmfHumanAiIssue]] = Field(default=None, description="""The human-AI interaction issues of Appendix C.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })
    ai_rmf_attributes: Optional[list[AiRmfAttribute]] = Field(default=None, description="""The attributes of the AI RMF in Appendix D.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfFramework']} })

    @field_validator('ai_rmf_version')
    def pattern_ai_rmf_version(cls, v):
        pattern=re.compile(r"^[0-9]+\.[0-9]+$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid ai_rmf_version format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid ai_rmf_version format: {v}"
            raise ValueError(err_msg)
        return v


class GaiRisk(ConfiguredBaseModel):
    """
    A risk that section 2 defines as unique to or made worse by the development and use of GAI.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:Risk',
         'comments': ['The publication gives a risk its section, its definition, its '
                      'trustworthiness characteristics and, in a footnote, its '
                      'groupings. It assigns no lifecycle stage, scope, source or time '
                      'scale to a risk, since those depend on the model, system or use '
                      'case. An adopter fills them in.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_risks',
         'related_mappings': ['nist_ai_100_1:Risk'],
         'slot_usage': {'description': {'description': "The risk's definition in "
                                                       'section 2.',
                                        'name': 'description'}}})

    description: Optional[str] = Field(default=None, description="""The risk's definition in section 2.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_risk_name: GaiRiskName = Field(default=..., description="""Which of the 12 risks this is.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_section: str = Field(default=..., description="""The subsection of section 2 that discusses the risk, such as 2.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_characteristics: Optional[list[AiRmfCharacteristicName]] = Field(default=None, description="""The AI RMF's trustworthiness characteristics that the subsection names for the risk.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_groupings: Optional[list[GaiRiskGrouping]] = Field(default=None, description="""The groups footnote 5 suggests for the risk. The footnote lists Data Privacy under all three.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_lifecycle_stages: Optional[list[GaiLifecycleStage]] = Field(default=None, description="""The lifecycle stages where the risk can arise for the adopter's model, system or use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_scopes: Optional[list[GaiRiskScope]] = Field(default=None, description="""The levels where the risk exists for the adopter's model, system or use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_sources: Optional[list[GaiRiskSource]] = Field(default=None, description="""Where the risk comes from for the adopter's model, system or use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })
    gai_risk_time_scales: Optional[list[GaiRiskTimeScale]] = Field(default=None, description="""How the risk materializes over time for the adopter's model, system or use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiRisk']} })

    @field_validator('gai_risk_section')
    def pattern_gai_risk_section(cls, v):
        pattern=re.compile(r"^2\.([1-9]|1[0-2])$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_risk_section format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_risk_section format: {v}"
            raise ValueError(err_msg)
        return v


class GaiSubcategory(ConfiguredBaseModel):
    """
    An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:Subcategory',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_actions',
         'related_mappings': ['nist_ai_100_1:Subcategory'],
         'slot_usage': {'description': {'description': "The subcategory's statement as "
                                                       'the table restates it.',
                                        'name': 'description',
                                        'pattern': '^\\s*\\S',
                                        'required': True}}})

    ai_rmf_subcategory_id: str = Field(default=..., description="""The subcategory's identifier, such as GOVERN 1.1.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfSubcategory', 'GaiSubcategory']} })
    description: str = Field(default=..., description="""The subcategory's statement as the table restates it.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_subcategory_actions: list[GaiSuggestedAction] = Field(default=..., description="""The suggested actions the table lists.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSubcategory']} })
    gai_subcategory_actor_tasks: Optional[list[AiRmfActorTaskName]] = Field(default=None, description="""The AI actor tasks the table names. They belong to the table and not to one action: the publication says not every task applies to every action.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSubcategory']} })

    @field_validator('description')
    def pattern_description(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid description format: {v}"
            raise ValueError(err_msg)
        return v


class GaiSuggestedAction(ConfiguredBaseModel):
    """
    A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'broad_mappings': ['oscal:Part'],
         'class_uri': 'nist_ai_600_1:SuggestedAction',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_actions',
         'related_mappings': ['nist_ai_100_1:SuggestedAction',
                              'stix:StixCourseOfAction'],
         'slot_usage': {'description': {'description': "The action's text in the "
                                                       'table.',
                                        'name': 'description',
                                        'pattern': '^\\s*\\S',
                                        'required': True}}})

    gai_action_id: str = Field(default=..., description="""The action's identifier, such as GV-1.1-001.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSuggestedAction']} })
    description: str = Field(default=..., description="""The action's text in the table.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_action_risks: Optional[list[GaiRiskName]] = Field(default=None, description="""The GAI risks the row tags the action with.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiSuggestedAction']} })

    @field_validator('description')
    def pattern_description(cls, v):
        pattern=re.compile(r"^\s*\S")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid description format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid description format: {v}"
            raise ValueError(err_msg)
        return v


class GaiPrimaryConsideration(ConfiguredBaseModel):
    """
    One of the four primary considerations of Appendix A, which also inform the suggested actions.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nist_ai_600_1:PrimaryConsideration',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations',
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    gai_consideration_type: Literal["GaiPrimaryConsideration"] = Field(default="GaiPrimaryConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiGovernanceConsideration(GaiPrimaryConsideration):
    """
    How an organization's governance can be revisited for GAI, including across the AI value chain.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:GovernanceConsideration',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_governance_plans: Optional[list[GaiGovernancePlan]] = Field(default=None, description="""The plans and actions that section A.1.2 lists from other AI governance.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiGovernanceConsideration']} })
    gai_third_party_controls: Optional[list[GaiThirdPartyControl]] = Field(default=None, description="""The existing controls that section A.1.3 says can apply to third-party GAI.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiGovernanceConsideration']} })
    gai_consideration_type: Literal["GaiGovernanceConsideration"] = Field(default="GaiGovernanceConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiPreDeploymentTestingConsideration(GaiPrimaryConsideration):
    """
    How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:PreDeploymentTestingConsideration',
         'comments': ['Section A.1.7 calls the feedback approaches of section A.1.5 '
                      'part of this consideration.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_structured_feedback: Optional[list[Union[GaiParticipatoryEngagement,GaiFieldTesting,GaiAiRedTeaming]]] = Field(default=None, description="""The kinds of structured public feedback section A.1.5 gives as examples.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPreDeploymentTestingConsideration']} })
    gai_consideration_type: Literal["GaiPreDeploymentTestingConsideration"] = Field(default="GaiPreDeploymentTestingConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiContentProvenanceConsideration(GaiPrimaryConsideration):
    """
    How tracking the origin and history of content helps tell authentic content from synthetic content.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:ContentProvenanceConsideration',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_provenance_techniques: Optional[list[GaiProvenanceTechnique]] = Field(default=None, description="""The well-known techniques for provenance data tracking that section A.1.6 names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiContentProvenanceConsideration']} })
    gai_consideration_type: Literal["GaiContentProvenanceConsideration"] = Field(default="GaiContentProvenanceConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiIncidentDisclosureConsideration(GaiPrimaryConsideration):
    """
    How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:IncidentDisclosureConsideration',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_incident_harms: Optional[list[GaiIncidentHarm]] = Field(default=None, description="""The kinds of harm that section A.1.8's definition of an AI incident names.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiIncidentDisclosureConsideration']} })
    gai_consideration_type: Literal["GaiIncidentDisclosureConsideration"] = Field(default="GaiIncidentDisclosureConsideration", description="""Which of the four classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiPrimaryConsideration']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })
    gai_consideration_sections: Optional[list[str]] = Field(default=None, description="""The subsections of Appendix A that discuss the consideration, such as A.1.2.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiPrimaryConsideration']} })

    @field_validator('gai_consideration_sections')
    def pattern_gai_consideration_sections(cls, v):
        pattern=re.compile(r"^A\.1(\.[1-8])?$")
        if isinstance(v, list):
            for element in v:
                if isinstance(element, str) and not pattern.search(element):
                    err_msg = f"Invalid gai_consideration_sections format: {element}"
                    raise ValueError(err_msg)
        elif isinstance(v, str) and not pattern.search(v):
            err_msg = f"Invalid gai_consideration_sections format: {v}"
            raise ValueError(err_msg)
        return v


class GaiStructuredFeedback(ConfiguredBaseModel):
    """
    A way of using structured public feedback to evaluate whether GAI systems perform as intended.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'abstract': True,
         'class_uri': 'nist_ai_600_1:StructuredFeedback',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations',
         'slot_usage': {'title': {'name': 'title', 'required': True}}})

    gai_feedback_type: Literal["GaiStructuredFeedback"] = Field(default="GaiStructuredFeedback", description="""Which of the three classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiStructuredFeedback']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiParticipatoryEngagement(GaiStructuredFeedback):
    """
    Asking civil society groups, affected communities and users for feedback, such as through focus groups or surveys.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:ParticipatoryEngagement',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_feedback_type: Literal["GaiParticipatoryEngagement"] = Field(default="GaiParticipatoryEngagement", description="""Which of the three classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiStructuredFeedback']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiFieldTesting(GaiStructuredFeedback):
    """
    Structured settings that show how people interact with and use AI-generated information.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:FieldTesting',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_feedback_type: Literal["GaiFieldTesting"] = Field(default="GaiFieldTesting", description="""Which of the three classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiStructuredFeedback']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiAiRedTeaming(GaiStructuredFeedback):
    """
    A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:AiRedTeaming',
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1/nist_ai_600_1_considerations'})

    gai_red_teaming_types: Optional[list[GaiRedTeamingType]] = Field(default=None, description="""The kinds of AI red-teaming that may suit the use case.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiAiRedTeaming']} })
    gai_feedback_type: Literal["GaiAiRedTeaming"] = Field(default="GaiAiRedTeaming", description="""Which of the three classes this record is.""", json_schema_extra = { "linkml_meta": {'designates_type': True, 'domain_of': ['GaiStructuredFeedback']} })
    title: str = Field(default=..., description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class GaiProfile(AiRmfProfile):
    """
    The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'class_uri': 'nist_ai_600_1:Profile',
         'comments': ['It holds actions for only some subcategories, and the '
                      'publication says more may be added later.'],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-600-1',
         'tree_root': True})

    gai_risks: list[GaiRisk] = Field(default=..., description="""The 12 risks of section 2.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile']} })
    gai_subcategories: list[GaiSubcategory] = Field(default=..., description="""The tables of section 3, in the publication's order.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile']} })
    gai_primary_considerations: Optional[list[Union[GaiGovernanceConsideration,GaiPreDeploymentTestingConsideration,GaiContentProvenanceConsideration,GaiIncidentDisclosureConsideration]]] = Field(default=None, description="""The four primary considerations of Appendix A.""", json_schema_extra = { "linkml_meta": {'domain_of': ['GaiProfile']} })
    ai_rmf_profile_kinds: list[AiRmfProfileKind] = Field(default=..., description="""Which of the publication's kinds of profile this is. A current profile for one use case is both.""", min_length=1, json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_profile_setting: Optional[str] = Field(default=None, description="""The sector, industry, technology, organization or end use the profile covers, such as hiring.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_profile_subcategories: Optional[list[str]] = Field(default=None, description="""The subcategories the profile selects. An adopter may select from them rather than apply all.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfProfile']} })
    ai_rmf_id: str = Field(default=..., description="""The identifier an adopter gives a record of its own.""", json_schema_extra = { "linkml_meta": {'domain_of': ['AiRmfRecord']} })
    title: Optional[str] = Field(default=None, description="""The element's name.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's title, so lokf adapt folds it into "
                      "LOKF's slot and a knowledge bundle reads one title key."],
         'domain_of': ['AiRmfRecord',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfResource',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:name'} })
    description: Optional[str] = Field(default=None, description="""What the element says or is.""", json_schema_extra = { "linkml_meta": {'comments': ["It carries the IRI of LOKF's description, so lokf adapt folds "
                      "it into LOKF's slot and a knowledge bundle reads one "
                      'description key.'],
         'domain_of': ['AiRmfRecord',
                       'AiRmfTrustworthinessCharacteristic',
                       'AiRmfDimension',
                       'AiRmfLifecycleStage',
                       'AiRmfActorTask',
                       'AiRmfManagementChallenge',
                       'AiRmfMeasurementChallenge',
                       'AiRmfSpecificRisk',
                       'AiRmfHumanAiIssue',
                       'AiRmfAttribute',
                       'AiRmfFunction',
                       'AiRmfCategory',
                       'AiRmfSubcategory',
                       'AiRmfSuggestedAction',
                       'AiRmfDocumentationItem',
                       'GaiRisk',
                       'GaiSubcategory',
                       'GaiSuggestedAction',
                       'GaiPrimaryConsideration',
                       'GaiStructuredFeedback'],
         'slot_uri': 'schema:description'} })


class NistAiRmfFamily(ConfiguredBaseModel):
    """
    The two publications held in one document, each as its own schema renders it.
    """
    linkml_meta: ClassVar[LinkMLMeta] = LinkMLMeta({'comments': ["Each publication's root stays a root, so a file that holds one "
                      'publication alone validates against AiRmfFramework or '
                      "GaiProfile. The JSON Schema's top level is this class."],
         'from_schema': 'https://w3id.org/lmodel/nist-ai-rmf',
         'tree_root': True})

    nist_ai_rmf_framework: Optional[AiRmfFramework] = Field(default=None, description="""The AI RMF, as lmodel/nist-ai-100-1 renders it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NistAiRmfFamily']} })
    nist_ai_rmf_generative_ai_profile: Optional[GaiProfile] = Field(default=None, description="""The Generative AI Profile, as lmodel/nist-ai-600-1 renders it.""", json_schema_extra = { "linkml_meta": {'domain_of': ['NistAiRmfFamily']} })


# Model rebuild
# see https://pydantic-docs.helpmanual.io/usage/models/#rebuilding-a-model
AiRmfRecord.model_rebuild()
AiRmfTrustworthinessCharacteristic.model_rebuild()
AiRmfDimension.model_rebuild()
AiRmfLifecycleStage.model_rebuild()
AiRmfActorTask.model_rebuild()
AiRmfManagementChallenge.model_rebuild()
AiRmfMeasurementChallenge.model_rebuild()
AiRmfSpecificRisk.model_rebuild()
AiRmfHumanAiIssue.model_rebuild()
AiRmfAttribute.model_rebuild()
AiRmfSystem.model_rebuild()
AiRmfActor.model_rebuild()
AiRmfRisk.model_rebuild()
AiRmfResidualRisk.model_rebuild()
AiRmfImpact.model_rebuild()
AiRmfHarm.model_rebuild()
AiRmfRiskTolerance.model_rebuild()
AiRmfBias.model_rebuild()
AiRmfFunction.model_rebuild()
AiRmfCategory.model_rebuild()
AiRmfSubcategory.model_rebuild()
AiRmfSuggestedAction.model_rebuild()
AiRmfDocumentationItem.model_rebuild()
AiRmfResource.model_rebuild()
AiRmfProfile.model_rebuild()
AiRmfFramework.model_rebuild()
GaiRisk.model_rebuild()
GaiSubcategory.model_rebuild()
GaiSuggestedAction.model_rebuild()
GaiPrimaryConsideration.model_rebuild()
GaiGovernanceConsideration.model_rebuild()
GaiPreDeploymentTestingConsideration.model_rebuild()
GaiContentProvenanceConsideration.model_rebuild()
GaiIncidentDisclosureConsideration.model_rebuild()
GaiStructuredFeedback.model_rebuild()
GaiParticipatoryEngagement.model_rebuild()
GaiFieldTesting.model_rebuild()
GaiAiRedTeaming.model_rebuild()
GaiProfile.model_rebuild()
NistAiRmfFamily.model_rebuild()
