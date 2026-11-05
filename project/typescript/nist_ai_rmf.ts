export type AiRmfRecordAiRmfId = string;
export type AiRmfSystemAiRmfId = string;
export type AiRmfActorAiRmfId = string;
export type AiRmfRiskAiRmfId = string;
export type AiRmfResidualRiskAiRmfId = string;
export type AiRmfImpactAiRmfId = string;
export type AiRmfHarmAiRmfId = string;
export type AiRmfRiskToleranceAiRmfId = string;
export type AiRmfBiasAiRmfId = string;
export type AiRmfProfileAiRmfId = string;
export type GaiProfileAiRmfId = string;
/**
* The seven characteristics of trustworthy AI systems in section 3 of the publication.
*/
export enum AiRmfCharacteristicName {
    
    /** Shown by evidence to meet the needs of its intended use, and works without failure over time. Figure 4 makes it a necessary condition for the others. */
    Valid_and_Reliable = "valid_and_reliable",
    /** Keeps people, property and the environment out of danger under defined conditions. */
    Safe = "safe",
    /** Withstands adverse events and recovers from them, and keeps confidentiality, integrity and availability through protections against attack. */
    Secure_and_Resilient = "secure_and_resilient",
    /** Answerable for outcomes, which rests on people being able to get information about the system and its outputs. Figure 4 shows it relating to all the others. */
    Accountable_and_Transparent = "accountable_and_transparent",
    /** Its working can be represented (how a decision was made) and its output understood in context (why, and what it means for the user). */
    Explainable_and_Interpretable = "explainable_and_interpretable",
    /** Guided by the norms and practices that protect human autonomy, identity and dignity, such as anonymity, confidentiality and control. */
    Privacy_Enhanced = "privacy_enhanced",
    /** Addresses equality and equity, including harmful bias and discrimination, knowing that views of fairness differ across cultures and applications. */
    Fair_EN_DASH_with_Harmful_Bias_Managed = "fair_with_harmful_bias_managed",
};
/**
* The ten AI actor tasks and five additional AI actors of Appendix A.
*/
export enum AiRmfActorTaskName {
    
    /** Setting what the system is for, planning and designing it, and gathering and preparing its data. */
    AI_Design = "ai_design",
    /** Providing the initial infrastructure, and creating, selecting, calibrating, training and testing models. */
    AI_Development = "ai_development",
    /** Deciding how the system is used and putting it into production, including pilots and compliance checks. */
    AI_Deployment = "ai_deployment",
    /** Running the system and regularly assessing its output and impacts. */
    Operation_and_Monitoring = "operation_and_monitoring",
    /** Examining the system or its components and finding and fixing problems, throughout the lifecycle. */
    Test_Evaluation_Verification_and_Validation_LEFT_PARENTHESISTEVVRIGHT_PARENTHESIS = "tevv",
    /** Human-centered design and evaluation, involving end users and bringing context-specific norms and values into design. */
    Human_Factors = "human_factors",
    /** Giving knowledge of the sector or setting where the system is used. */
    Domain_Expert = "domain_expert",
    /** Assessing accountability, harmful bias, impacts, product safety, liability and security. */
    AI_Impact_Assessment = "ai_impact_assessment",
    /** Acquiring AI from another party, under financial, legal or policy authority. */
    Procurement = "procurement",
    /** Holding management, fiduciary and legal authority for the organization where the system is designed, developed or deployed. */
    Governance_and_Oversight = "governance_and_oversight",
    /** Outside organizations that supply or evaluate the data, models, systems or services an organization acquires. */
    Third_party_entities = "third_party_entities",
    /** The people or groups who use the system, whether new to technology or expert in AI. */
    End_users = "end_users",
    /** Those directly or indirectly affected by the system or its output, whether or not they interact with it. */
    Affected_individualsSOLIDUScommunities = "affected_individuals_and_communities",
    /** Those who may provide norms or guidance on AI risk, such as standards bodies, advocacy groups and researchers. */
    Other_AI_actors = "other_ai_actors",
    /** Those most likely to experience the impacts directly, who may motivate what other AI actors do. */
    General_public = "general_public",
};
/**
* The key dimensions of an AI system in Figure 2.
*/
export enum AiRmfDimensionName {
    
    /** The setting the system is planned for and operated in. */
    Application_Context = "application_context",
    /** The data the system is built from and takes in. */
    Data_and_Input = "data_and_input",
    /** The models built, used, verified and validated. */
    AI_Model = "ai_model",
    /** What the system does and produces once deployed. */
    Task_and_Output = "task_and_output",
    /** Human rights and the well-being of society and the planet, at the center of Figure 2. */
    People_and_Planet = "people_and_planet",
};
/**
* The AI lifecycle stages in Figure 3, of which Figure 2 shows the first six.
*/
export enum AiRmfLifecycleStageName {
    
    /** Documenting the concept, objectives, assumptions, context and requirements. */
    Plan_and_Design = "plan_and_design",
    /** Gathering, validating and cleaning data, and recording what it holds. */
    Collect_and_Process_Data = "collect_and_process_data",
    /** Creating or selecting algorithms and training models. */
    Build_and_Use_Model = "build_and_use_model",
    /** Verifying, validating, calibrating and interpreting model output. */
    Verify_and_Validate = "verify_and_validate",
    /** Piloting, checking compatibility and compliance, managing change and evaluating user experience. */
    Deploy_and_Use = "deploy_and_use",
    /** Operating the system and continually assessing its recommendations and impacts. */
    Operate_and_Monitor = "operate_and_monitor",
    /** Using the technology or being affected by it, which Figure 3 places under People and Planet. */
    Use_or_Impacted_by = "use_or_impacted_by",
};
/**
* The two AI RMF audiences of section 2.
*/
export enum AiRmfAudience {
    
    /** AI actors who carry out or manage work on AI systems and drive their risk management. */
    Primary_audience = "primary",
    /** AI actors in the People and Planet dimension, who inform the primary audience. */
    Informing_audience = "informing",
};
/**
* The challenges for AI risk management in section 1.2.
*/
export enum AiRmfManagementChallengeName {
    
    /** AI risks that are poorly defined or understood are hard to measure, which does not mean they are high or low. */
    Risk_Measurement = "risk_measurement",
    /** The AI RMF can prioritize risk but prescribes no tolerance, which depends on context and changes over time. */
    Risk_Tolerance = "risk_tolerance",
    /** Eliminating all negative risk is unrealistic, so effort goes first to the highest risks in a context of use. */
    Risk_Prioritization = "risk_prioritization",
    /** AI risk belongs inside broader enterprise risk management, with accountability and commitment from senior levels. */
    Organizational_Integration_and_Management_of_Risk = "organizational_integration_and_management_of_risk",
};
/**
* The challenges of measuring AI risk in section 1.2.1.
*/
export enum AiRmfMeasurementChallengeName {
    
    /** Third-party parts can speed work, but their metrics may not match or be disclosed, and how they are used adds risk. */
    Risks_related_to_third_party_software_hardware_and_data = "third_party_software_hardware_and_data",
    /** New risks need identifying, tracking and measuring, which impact assessment helps with. */
    Tracking_emergent_risks = "tracking_emergent_risks",
    /** There is no consensus on robust, verifiable methods, and metrics can be oversimplified or gamed. */
    Availability_of_reliable_metrics = "availability_of_reliable_metrics",
    /** Results differ by stage, some risks stay latent, and AI actors see risk differently. */
    Risk_at_different_stages_of_the_AI_lifecycle = "risk_at_different_lifecycle_stages",
    /** What a laboratory measures may differ from what emerges in operation. */
    Risk_in_real_world_settings = "risk_in_real_world_settings",
    /** Opaque systems, poor documentation and inherent uncertainty complicate measurement. */
    Inscrutability = "inscrutability",
    /** A system that augments or replaces human activity needs a baseline, which is hard to systematize. */
    Human_baseline = "human_baseline",
};
/**
* The risk response options MANAGE 1.3 names.
*/
export enum AiRmfRiskResponse {
    
    /** Reducing the likelihood or magnitude of the risk. */
    Mitigating = "mitigating",
    /** Shifting the risk to another party. */
    Transferring = "transferring",
    /** Not carrying out what creates the risk. */
    Avoiding = "avoiding",
    /** Bearing the risk without further action. */
    Accepting = "accepting",
};
/**
* Whether an impact is positive, negative or both, as section 1.1 puts it.
*/
export enum AiRmfImpactDirection {
    
    /** An opportunity or benefit. */
    Positive = "positive",
    /** A threat or harm. */
    Negative = "negative",
    /** Positive and negative at once. */
    Both = "both",
};
/**
* Who section 1.1 says can experience negative impact or harm.
*/
export enum AiRmfAffectedParty {
    
    /** Particular people. */
    Individuals = "individuals",
    /** Groups of people. */
    Groups = "groups",
    /** Communities of people. */
    Communities = "communities",
    /** Organizations. */
    Organizations = "organizations",
    /** Society at large. */
    Society = "society",
    /** The natural environment. */
    The_environment = "environment",
    /** The planet as a whole. */
    The_planet = "planet",
};
/**
* The three headings of Figure 1.
*/
export enum AiRmfHarmCategory {
    
    /** Harm that falls on individuals, groups, communities or society. */
    Harm_to_People = "people",
    /** Harm that falls on an organization. */
    Harm_to_an_Organization = "organization",
    /** Harm that falls on interconnected systems and resources. */
    Harm_to_an_Ecosystem = "ecosystem",
};
/**
* The examples of potential harm in Figure 1, which NIST offers as examples and not as a closed list.
*/
export enum AiRmfHarmExample {
    
    /** To a person's civil liberties, rights, safety or economic opportunity. */
    Individual = "individual",
    /** To a group, such as discrimination against a sub-group of a population. */
    GroupSOLIDUSCommunity = "group_or_community",
    /** To democratic participation or educational access. */
    Societal = "societal",
    /** To how an organization operates. */
    Business_operations = "business_operations",
    /** To an organization through a breach of security or a loss of money. */
    Security_breaches_or_monetary_loss = "security_breach_or_monetary_loss",
    /** To an organization's standing. */
    Reputation = "reputation",
    /** To parts and resources that depend on each other. */
    Interconnected_and_interdependent_elements_and_resources = "interdependent_elements",
    /** To large systems that link organizations. */
    Global_financial_system_supply_chain_or_interrelated_systems = "financial_or_supply_systems",
    /** To the natural world. */
    Natural_resources_the_environment_and_planet = "natural_resources_and_environment",
};
/**
* The three major categories of AI bias in section 3.7, each of which can occur without prejudice or discriminatory intent.
*/
export enum AiRmfBiasCategory {
    
    /** In datasets, in organizational norms and processes, and in the wider society that uses AI. */
    Systemic = "systemic",
    /** In datasets and algorithms, often from systematic errors due to samples that are not representative. */
    Computational_and_statistical = "computational_and_statistical",
    /** In how people perceive system information to decide, or think about what a system is for. */
    Human_cognitive = "human_cognitive",
};
/**
* The kinds of AI RMF profile that section 6 names.
*/
export enum AiRmfProfileKind {
    
    /** The Core implemented for a specific setting or application. */
    Use_case_profile = "use_case",
    /** A temporal profile saying how AI is managed today and the related risks, in terms of current outcomes. */
    Current_Profile = "current",
    /** A temporal profile saying which outcomes the desired risk management goals need. */
    Target_Profile = "target",
    /** Covers risks of models or applications used across use cases or sectors, or activities common to them, such as using large language models. */
    Cross_sectoral_profile = "cross_sectoral",
};
/**
* The 12 risks of section 2.
*/
export enum GaiRiskName {
    
    /** Easier access to dangerous information or design abilities for chemical, biological, radiological or nuclear weapons. */
    CBRN_Information_or_Capabilities = "cbrn_information_or_capabilities",
    /** Confident but wrong output that can mislead users. */
    Confabulation = "confabulation",
    /** Easier production of content that incites or threatens, recommends harm, or disparages. */
    Dangerous_Violent_or_Hateful_Content = "dangerous_violent_or_hateful_content",
    /** Leaks, misuse or de-anonymization of personal or sensitive data. */
    Data_Privacy = "data_privacy",
    /** Effects on ecosystems from the heavy computing that training and operating models need. */
    Environmental_Impacts = "environmental_impacts",
    /** Worse systemic bias, unequal performance across groups or languages, and output skewed by sameness. */
    Harmful_Bias_or_Homogenization = "harmful_bias_or_homogenization",
    /** Interaction that leads people to over-rely on, anthropomorphize or become entangled with a system, or to distrust it. */
    Human_AI_Configuration = "human_ai_configuration",
    /** Easier creation and spread of content that blurs fact and opinion, or that can drive large disinformation campaigns. */
    Information_Integrity = "information_integrity",
    /** Easier offensive cyber activity, and a larger attack surface on a system, its data, code or weights. */
    Information_Security = "information_security",
    /** Easier unauthorized copying of protected content, exposure of trade secrets, and plagiarism. */
    Intellectual_Property = "intellectual_property",
    /** Easier production of harmful imagery, including synthetic abuse material and intimate images without consent. */
    Obscene_Degrading_andSOLIDUSor_Abusive_Content = "obscene_degrading_or_abusive_content",
    /** Opaque use of third-party components and data, and poor supplier vetting, that weaken accountability downstream. */
    Value_Chain_and_Component_Integration = "value_chain_and_component_integration",
};
/**
* The three groups into which footnote 5 says an organization could sort the risks, as one possible way.
*/
export enum GaiRiskGrouping {
    
    /** Risks from malfunction. */
    Technical_SOLIDUS_Model_risks = "technical_or_model",
    /** Risks from malicious use. */
    Misuse_by_humans = "misuse_by_humans",
    /** Systemic risks. */
    Ecosystem_SOLIDUS_societal_risks = "ecosystem_or_societal",
};
/**
* The lifecycle stages section 2 names for GAI. They differ from the seven stages of the AI RMF's Figure 3.
*/
export enum GaiLifecycleStage {
    
    /** Setting out the system before it is built. */
    Design = "design",
    /** Building and training it. */
    Development = "development",
    /** Putting it into use. */
    Deployment = "deployment",
    /** Running it. */
    Operation = "operation",
    /** Retiring it. */
    Decommissioning = "decommissioning",
};
/**
* The levels where section 2 says a risk may exist.
*/
export enum GaiRiskScope {
    
    /** The level of one model or system. */
    Model_or_system = "model_or_system",
    /** The level of one specific use case. */
    Application_or_implementation = "application_or_implementation",
    /** Beyond one system or organization, such as algorithmic monocultures or effects on labor markets. */
    Ecosystem = "ecosystem",
};
/**
* Where section 2 says a risk may come from.
*/
export enum GaiRiskSource {
    
    /** The design of the model itself. */
    Design = "design",
    /** The training of the model. */
    Training = "training",
    /** The operation of the model. */
    Operation = "operation",
    /** What goes into the model or system. */
    Inputs = "inputs",
    /** What the system produces. */
    Outputs = "outputs",
    /** Abuse, misuse or unsafe repurposing by people, whether adversarial or not. */
    Human_behavior = "human_behavior",
    /** How a person and a system act on each other. */
    Human_AI_interaction = "human_ai_interaction",
};
/**
* How section 2 says a risk may materialize over time.
*/
export enum GaiRiskTimeScale {
    
    /** All at once, such as immediate emotional harm from a harmful deepfake image. */
    Abruptly = "abrupt",
    /** Slowly, such as the long-term effect of disinformation on trust in institutions. */
    Across_extended_periods = "extended",
};
/**
* The plans and actions that section A.1.2 says apply to GAI from other AI governance.
*/
export enum GaiGovernancePlan {
    
    Accessibility_and_reasonable_accommodations = "accessibility_and_reasonable_accommodations",
    AI_actor_credentials_and_qualifications = "ai_actor_credentials_and_qualifications",
    Alignment_to_organizational_values = "alignment_to_organizational_values",
    Auditing_and_assessment = "auditing_and_assessment",
    Change_management_controls = "change_management_controls",
    Commercial_use = "commercial_use",
    Data_provenance = "data_provenance",
    Data_protection = "data_protection",
    Data_retention = "data_retention",
    Consistency_in_use_of_defining_key_terms = "consistency_in_use_of_defining_key_terms",
    Decommissioning = "decommissioning",
    Discouraging_anonymous_use = "discouraging_anonymous_use",
    Education = "education",
    Impact_assessments = "impact_assessments",
    Incident_response = "incident_response",
    Monitoring = "monitoring",
    Opt_outs = "opt_outs",
    Risk_based_controls = "risk_based_controls",
    Risk_mapping_and_measurement = "risk_mapping_and_measurement",
    Science_backed_TEVV_practices = "science_backed_tevv_practices",
    Secure_software_development_practices = "secure_software_development_practices",
    Stakeholder_engagement = "stakeholder_engagement",
    Synthetic_content_detection_and_labeling_tools_and_techniques = "synthetic_content_detection_and_labeling_tools_and_techniques",
    Whistleblower_protections = "whistleblower_protections",
    Workforce_diversity_and_interdisciplinary_teams = "workforce_diversity_and_interdisciplinary_teams",
};
/**
* The existing controls that section A.1.3 says can apply to third-party GAI.
*/
export enum GaiThirdPartyControl {
    
    /** Checking a provider before acquiring its GAI technology or data. */
    Acquisition_and_procurement_due_diligence = "acquisition_and_procurement_due_diligence",
    /** Asking a provider what its software is made of. */
    Requests_for_software_bills_of_materials = "software_bills_of_materials",
    /** Holding a provider to agreed levels of service. */
    Application_of_service_level_agreements = "service_level_agreements",
    /** Asking for a provider's attestation reports. */
    Statement_on_standards_for_attestation_engagement_reports = "ssae_reports",
};
/**
* The types of AI red-teaming in section A.1.5.
*/
export enum GaiRedTeamingType {
    
    /** By general users who are not necessarily AI or technical experts. */
    General_Public = "general_public",
    /** By specialists in the domain or the context of use. */
    Expert = "expert",
    /** By both experts and general public participants. */
    Combination = "combination",
    /** By GAI together with human teams, specialist or not. */
    Human_SOLIDUS_AI = "human_ai",
};
/**
* The techniques for provenance data tracking in section A.1.6.
*/
export enum GaiProvenanceTechnique {
    
    /** Placing visible or hidden marks on content. */
    Digital_watermarking = "digital_watermarking",
    /** Recording facts about the content, such as its creator, date and sources. */
    Metadata_recording = "metadata_recording",
    /** Identifying content from its own characteristics. */
    Digital_fingerprinting = "digital_fingerprinting",
    /** Having people confirm where content came from. */
    Human_authentication = "human_authentication",
};
/**
* The kinds of harm that section A.1.8's definition of an AI incident names.
*/
export enum GaiIncidentHarm {
    
    /** To a person or group, including psychological harm and harm to mental health. */
    Injury_or_harm_to_health = "injury_or_harm_to_health",
    /** To its management and operation. */
    Disruption_of_critical_infrastructure = "critical_infrastructure_disruption",
    /** Of human rights, or of obligations under law that protects fundamental, labor and intellectual property rights. */
    Violations_of_rights_or_legal_obligations = "rights_violations",
    /** To things and groups beyond the individual. */
    Harm_to_property_communities_or_the_environment = "harm_to_property_communities_or_environment",
};


/**
 * The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct from what the publication itself lists.
 */
export interface AiRmfRecord {
    /** The identifier an adopter gives a record of its own. */
    ai_rmf_id: string,
    /** The element's name. */
    title?: string,
    /** What the element says or is. */
    description?: string,
}


/**
 * A characteristic of trustworthy AI systems, each with a subsection of section 3.
 */
export interface AiRmfTrustworthinessCharacteristic {
    /** What the element says or is. */
    description?: string,
    /** Which characteristic this is. */
    ai_rmf_characteristic_name: string,
    /** The subsection of the publication that describes it, such as 3.1. */
    ai_rmf_characteristic_section: string,
    /** Whether Figure 4 shows it as the necessary condition under the others. */
    ai_rmf_characteristic_is_base?: boolean,
    /** Whether Figure 4 shows it relating to all the others. */
    ai_rmf_characteristic_relates_to_all?: boolean,
}


/**
 * One of the five key socio-technical dimensions of an AI system in Figure 2.
 */
export interface AiRmfDimension {
    /** What the element says or is. */
    description?: string,
    /** Which dimension this is. */
    ai_rmf_dimension_name: string,
    /** The AI RMF audience formed by the AI actors in this dimension. */
    ai_rmf_dimension_audience: string,
}


/**
 * A stage of the AI lifecycle as a column of Figure 3 shows it, under its dimension.
 */
export interface AiRmfLifecycleStage {
    /** What the element says or is. */
    description?: string,
    /** Which stage this is. */
    ai_rmf_lifecycle_stage_name: string,
    /** The dimension Figure 3 places the stage under. */
    ai_rmf_lifecycle_stage_dimension: string,
    /** The testing, evaluation, verification and validation (TEVV) Figure 3 gives the stage. */
    ai_rmf_lifecycle_stage_tevv?: string,
    /** The representative AI actors Figure 3 lists for the stage. */
    ai_rmf_lifecycle_stage_representative_actors?: string[],
}


/**
 * A task or additional AI actor of Appendix A.
 */
export interface AiRmfActorTask {
    /** What the element says or is. */
    description?: string,
    /** Which task or additional AI actor this is. */
    ai_rmf_actor_task_name: string,
    /** Whether Appendix A lists it under Additional AI Actors rather than as a task. */
    ai_rmf_actor_task_is_additional_actor?: boolean,
    /** The AI actors that Appendix A says carry out the task. */
    ai_rmf_actor_task_representative_actors?: string[],
}


/**
 * One of the four challenges for AI risk management in section 1.2.
 */
export interface AiRmfManagementChallenge {
    /** What the element says or is. */
    description?: string,
    /** Which challenge this is. */
    ai_rmf_management_challenge_name: string,
    /** The risk measurement challenges of section 1.2.1, under the challenge of risk measurement. */
    ai_rmf_management_challenge_measurement_challenges?: AiRmfMeasurementChallenge[],
}


/**
 * One of the challenges of measuring AI risk in section 1.2.1.
 */
export interface AiRmfMeasurementChallenge {
    /** What the element says or is. */
    description?: string,
    /** Which challenge this is. */
    ai_rmf_measurement_challenge_name: string,
}


/**
 * A risk that Appendix B says is new or increased for AI compared with traditional software.
 */
export interface AiRmfSpecificRisk {
    /** This project's short name for the item. Appendix B gives its items no names. */
    title: string,
    /** What the element says or is. */
    description?: string,
    /** The item's position in Appendix B's list, which is not numbered. */
    ai_rmf_specific_risk_position: number,
}


/**
 * An issue of human-AI interaction that Appendix C says merits further consideration and research.
 */
export interface AiRmfHumanAiIssue {
    /** The element's name. */
    title: string,
    /** What the element says or is. */
    description?: string,
    /** The issue's number in Appendix C. */
    ai_rmf_human_ai_issue_number: number,
}


/**
 * A key attribute of the AI RMF in Appendix D, which guided its development.
 */
export interface AiRmfAttribute {
    /** The element's name. */
    title: string,
    /** What the element says or is. */
    description?: string,
    /** The attribute's number in Appendix D. */
    ai_rmf_attribute_number: number,
}


/**
 * A machine-based system that produces outputs such as predictions or decisions for given objectives, with varying autonomy.
 */
export interface AiRmfSystem extends AiRmfRecord {
    /** What the system is for, and its potentially beneficial uses, which MAP 1.1 asks an adopter to document. */
    ai_rmf_system_intended_purposes?: string[],
    /** The settings the system is or will be deployed in, which MAP 1.1 asks an adopter to document. */
    ai_rmf_system_deployment_settings?: string[],
    /** The lifecycle stages the record covers. */
    ai_rmf_system_lifecycle_stages?: string,
    /** The AI actors with a role in the system's lifecycle, such as those MAP 1.6 says elicit its requirements. */
    ai_rmf_system_actors?: AiRmfActorAiRmfId[],
}


/**
 * An organization or individual with an active role in an AI system's lifecycle.
 */
export interface AiRmfActor extends AiRmfRecord {
    /** The tasks the actor carries out, or the additional AI actor it is. */
    ai_rmf_actor_tasks?: string,
    /** The AI RMF audience the actor belongs to. */
    ai_rmf_actor_audience?: string,
    /** The lifecycle stages the actor works in. */
    ai_rmf_actor_lifecycle_stages?: string,
}


/**
 * How likely an event is, combined with how severe its consequences are.
 */
export interface AiRmfRisk extends AiRmfRecord {
    /** How likely the event or impact is, on whatever scale the adopter uses. */
    ai_rmf_likelihood?: string,
    /** How large the consequences are, on whatever scale the adopter uses. */
    ai_rmf_magnitude?: string,
    /** The AI system the risk concerns. */
    ai_rmf_risk_system?: AiRmfSystemAiRmfId,
    /** The impacts that contribute to the risk. */
    ai_rmf_risk_impacts?: AiRmfImpact[],
    /** The trustworthiness characteristics the risk bears on. */
    ai_rmf_risk_characteristics?: string,
    /** The lifecycle stages where the risk is measured or arises. */
    ai_rmf_risk_lifecycle_stages?: string,
    /** The responses chosen for the risk. */
    ai_rmf_risk_responses?: string,
    /** The priority the adopter gives the risk's treatment, on whatever scale it uses, as MANAGE 1.2 asks. */
    ai_rmf_risk_priority?: string,
    /** The risk tolerance the risk is judged against, which GOVERN 1.3 and MAP 1.5 ask an adopter to document. */
    ai_rmf_risk_tolerance?: AiRmfRiskToleranceAiRmfId,
}


/**
 * The risk that remains after risk treatment.
 */
export interface AiRmfResidualRisk extends AiRmfRisk {
}


/**
 * A consequence of an AI system, which may be an opportunity, a threat or both.
 */
export interface AiRmfImpact extends AiRmfRecord {
    /** How likely the event or impact is, on whatever scale the adopter uses. */
    ai_rmf_likelihood?: string,
    /** How large the consequences are, on whatever scale the adopter uses. */
    ai_rmf_magnitude?: string,
    /** Whether the consequence is positive, negative or both. */
    ai_rmf_impact_direction: string,
    /** Who or what experiences the consequence. */
    ai_rmf_impact_affected_parties?: string,
}


/**
 * A negative impact, sorted as in Figure 1 by whether it falls on people, an organization or an ecosystem.
 */
export interface AiRmfHarm extends AiRmfImpact {
    /** The heading of Figure 1 the harm falls under. */
    ai_rmf_harm_category: string,
    /** The example of Figure 1 the harm matches, which must sit under the harm's category. */
    ai_rmf_harm_example?: string,
}


/**
 * An organization's or AI actor's readiness to bear risk to achieve its objectives. The AI RMF prescribes none.
 */
export interface AiRmfRiskTolerance extends AiRmfRecord {
    /** The organization or AI actor whose tolerance this is. */
    ai_rmf_risk_tolerance_holder?: AiRmfActorAiRmfId,
    /** What influences it, such as a law, a regulation, a policy or a norm. */
    ai_rmf_risk_tolerance_influences?: string[],
}


/**
 * A bias to consider and manage, sorted into NIST's three major categories.
 */
export interface AiRmfBias extends AiRmfRecord {
    /** The categories it falls under. */
    ai_rmf_bias_categories: string,
}


/**
 * One of the four functions that organize AI risk management at the highest level. GOVERN cuts across the other three.
 */
export interface AiRmfFunction {
    /** The function's name, such as GOVERN. */
    ai_rmf_function_id: string,
    /** The one-sentence overview in NIST's catalog. The publication gives each function a section of its own instead. */
    description?: string,
    /** The categories of the function. A knowledge bundle relates a category to its function with isPartOf instead. */
    ai_rmf_function_categories?: AiRmfCategory[],
}


/**
 * A group of related outcomes within a function, such as GOVERN 1, which Tables 1 to 4 state.
 */
export interface AiRmfCategory {
    /** The category's identifier, such as GOVERN 1. */
    ai_rmf_category_id: string,
    /** The category's statement in the publication. */
    description: string,
    /** The subcategories of the category. A knowledge bundle relates a subcategory to its category with isPartOf instead. */
    ai_rmf_category_subcategories?: AiRmfSubcategory[],
}


/**
 * A specific outcome within a category, such as GOVERN 1.1, which Tables 1 to 4 state, and its Playbook material.
 */
export interface AiRmfSubcategory {
    /** The subcategory's identifier, such as GOVERN 1.1. */
    ai_rmf_subcategory_id: string,
    /** The subcategory's statement in the publication. */
    description: string,
    /** The Playbook's discussion of the outcome. */
    ai_rmf_subcategory_about?: string[],
    /** The steps the Playbook suggests towards the outcome. They are voluntary and are not a checklist. */
    ai_rmf_subcategory_suggested_actions?: AiRmfSuggestedAction[],
    /** What the Playbook suggests an organization document, mostly as questions. */
    ai_rmf_subcategory_documentation?: AiRmfDocumentationItem[],
    /** The sources the Playbook names as AI transparency resources. */
    ai_rmf_subcategory_transparency_resources?: AiRmfResource[],
    /** The Playbook's references for the outcome. */
    ai_rmf_subcategory_references?: AiRmfResource[],
    /** The AI actors the Playbook tags the outcome with. */
    ai_rmf_subcategory_ai_actors?: string,
    /** The topics the Playbook tags the outcome with. NIST keeps no closed list of them. */
    ai_rmf_subcategory_topics?: string[],
}


/**
 * One step the Playbook suggests towards a subcategory's outcome.
 */
export interface AiRmfSuggestedAction {
    /** The suggested action's identifier, such as SA-GOVERN_1.1-1. */
    ai_rmf_suggested_action_id: string,
    /** What the element says or is. */
    description: string,
}


/**
 * One thing the Playbook suggests an organization document for a subcategory.
 */
export interface AiRmfDocumentationItem {
    /** The documentation prompt's identifier, such as D-GOVERN_1.1-1. */
    ai_rmf_documentation_id: string,
    /** What the element says or is. */
    description: string,
}


/**
 * A source the Playbook points to, by the title and address NIST's catalog gives it.
 */
export interface AiRmfResource {
    /** The element's name. */
    title: string,
    /** The UUID of the resource in the back matter of NIST's catalog. */
    ai_rmf_resource_uuid: string,
    /** The address NIST's catalog gives the source. The catalog gives none for a few. */
    ai_rmf_resource_address?: string,
}


/**
 * An implementation of the Core's functions, categories and subcategories for a setting, application or technology, based on the adopter's requirements, risk tolerance and resources.
 */
export interface AiRmfProfile extends AiRmfRecord {
    /** Which of the publication's kinds of profile this is. A current profile for one use case is both. */
    ai_rmf_profile_kinds: string,
    /** The sector, industry, technology, organization or end use the profile covers, such as hiring. */
    ai_rmf_profile_setting?: string,
    /** The subcategories the profile selects. An adopter may select from them rather than apply all. */
    ai_rmf_profile_subcategories?: string[],
}


/**
 * One edition of the AI RMF as a whole, with the Core and the lists the publication gives.
 */
export interface AiRmfFramework {
    /** The edition in NIST's two-number form, such as 1.0. */
    ai_rmf_version: string,
    /** The four functions, in the publication's order. */
    ai_rmf_functions: AiRmfFunction[],
    /** The trustworthiness characteristics of section 3. */
    ai_rmf_characteristics?: AiRmfTrustworthinessCharacteristic[],
    /** The key dimensions of Figure 2. */
    ai_rmf_dimensions?: AiRmfDimension[],
    /** The lifecycle stages of Figure 3. */
    ai_rmf_lifecycle_stages?: AiRmfLifecycleStage[],
    /** The AI actor tasks and additional AI actors of Appendix A. */
    ai_rmf_actor_task_list?: AiRmfActorTask[],
    /** The challenges for AI risk management of section 1.2. */
    ai_rmf_management_challenges?: AiRmfManagementChallenge[],
    /** The AI-specific risks of Appendix B. */
    ai_rmf_specific_risks?: AiRmfSpecificRisk[],
    /** The human-AI interaction issues of Appendix C. */
    ai_rmf_human_ai_issues?: AiRmfHumanAiIssue[],
    /** The attributes of the AI RMF in Appendix D. */
    ai_rmf_attributes?: AiRmfAttribute[],
}


/**
 * A risk that section 2 defines as unique to or made worse by the development and use of GAI.
 */
export interface GaiRisk {
    /** The risk's definition in section 2. */
    description?: string,
    /** Which of the 12 risks this is. */
    gai_risk_name: string,
    /** The subsection of section 2 that discusses the risk, such as 2.1. */
    gai_risk_section: string,
    /** The AI RMF's trustworthiness characteristics that the subsection names for the risk. */
    gai_risk_characteristics?: string,
    /** The groups footnote 5 suggests for the risk. The footnote lists Data Privacy under all three. */
    gai_risk_groupings?: string,
    /** The lifecycle stages where the risk can arise for the adopter's model, system or use case. */
    gai_risk_lifecycle_stages?: string,
    /** The levels where the risk exists for the adopter's model, system or use case. */
    gai_risk_scopes?: string,
    /** Where the risk comes from for the adopter's model, system or use case. */
    gai_risk_sources?: string,
    /** How the risk materializes over time for the adopter's model, system or use case. */
    gai_risk_time_scales?: string,
}


/**
 * An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
 */
export interface GaiSubcategory {
    /** The subcategory's identifier, such as GOVERN 1.1. */
    ai_rmf_subcategory_id: string,
    /** The subcategory's statement as the table restates it. */
    description: string,
    /** The suggested actions the table lists. */
    gai_subcategory_actions: GaiSuggestedAction[],
    /** The AI actor tasks the table names. They belong to the table and not to one action: the publication says not every task applies to every action. */
    gai_subcategory_actor_tasks?: string,
}


/**
 * A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
 */
export interface GaiSuggestedAction {
    /** The action's identifier, such as GV-1.1-001. */
    gai_action_id: string,
    /** The action's text in the table. */
    description: string,
    /** The GAI risks the row tags the action with. */
    gai_action_risks?: string,
}


/**
 * One of the four primary considerations of Appendix A, which also inform the suggested actions.
 */
export interface GaiPrimaryConsideration {
    /** Which of the four classes this record is. */
    gai_consideration_type: string,
    /** The element's name. */
    title: string,
    /** What the element says or is. */
    description?: string,
    /** The subsections of Appendix A that discuss the consideration, such as A.1.2. */
    gai_consideration_sections?: string[],
}


/**
 * How an organization's governance can be revisited for GAI, including across the AI value chain.
 */
export interface GaiGovernanceConsideration extends GaiPrimaryConsideration {
    /** The plans and actions that section A.1.2 lists from other AI governance. */
    gai_governance_plans?: string,
    /** The existing controls that section A.1.3 says can apply to third-party GAI. */
    gai_third_party_controls?: string,
}


/**
 * How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
 */
export interface GaiPreDeploymentTestingConsideration extends GaiPrimaryConsideration {
    /** The kinds of structured public feedback section A.1.5 gives as examples. */
    gai_structured_feedback?: GaiStructuredFeedback[],
}


/**
 * How tracking the origin and history of content helps tell authentic content from synthetic content.
 */
export interface GaiContentProvenanceConsideration extends GaiPrimaryConsideration {
    /** The well-known techniques for provenance data tracking that section A.1.6 names. */
    gai_provenance_techniques?: string,
}


/**
 * How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
 */
export interface GaiIncidentDisclosureConsideration extends GaiPrimaryConsideration {
    /** The kinds of harm that section A.1.8's definition of an AI incident names. */
    gai_incident_harms?: string,
}


/**
 * A way of using structured public feedback to evaluate whether GAI systems perform as intended.
 */
export interface GaiStructuredFeedback {
    /** Which of the three classes this record is. */
    gai_feedback_type: string,
    /** The element's name. */
    title: string,
    /** What the element says or is. */
    description?: string,
}


/**
 * Asking civil society groups, affected communities and users for feedback, such as through focus groups or surveys.
 */
export interface GaiParticipatoryEngagement extends GaiStructuredFeedback {
}


/**
 * Structured settings that show how people interact with and use AI-generated information.
 */
export interface GaiFieldTesting extends GaiStructuredFeedback {
}


/**
 * A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
 */
export interface GaiAiRedTeaming extends GaiStructuredFeedback {
    /** The kinds of AI red-teaming that may suit the use case. */
    gai_red_teaming_types?: string,
}


/**
 * The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
 */
export interface GaiProfile extends AiRmfProfile {
    /** The 12 risks of section 2. */
    gai_risks: GaiRisk[],
    /** The tables of section 3, in the publication's order. */
    gai_subcategories: GaiSubcategory[],
    /** The four primary considerations of Appendix A. */
    gai_primary_considerations?: GaiPrimaryConsideration[],
}


/**
 * The two publications held in one document, each as its own schema renders it.
 */
export interface NistAiRmfFamily {
    /** The AI RMF, as lmodel/nist-ai-100-1 renders it. */
    nist_ai_rmf_framework?: AiRmfFramework,
    /** The Generative AI Profile, as lmodel/nist-ai-600-1 renders it. */
    nist_ai_rmf_generative_ai_profile?: GaiProfile,
}



