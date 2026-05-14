export type NamedThingId = string;
export type AiSystemId = string;
export type AiSystemDimensionId = string;
export type AiLifecycleStageId = string;
export type AiActorId = string;
export type AiActorTaskId = string;
export type RiskId = string;
export type ImpactId = string;
export type HarmId = string;
export type ResidualRiskId = string;
export type RiskToleranceId = string;
export type RiskMeasurementChallengeId = string;
export type TrustworthinessCharacteristicId = string;
export type BiasId = string;
export type FunctionId = string;
export type CategoryId = string;
export type SubcategoryId = string;
export type AiRmfProfileId = string;
export type RmfAttributeId = string;
export type AiSpecificRiskId = string;
export type HumanAiInteractionIssueId = string;
export type AiRmfDocumentId = string;
export type AiRmfFrameworkId = string;
export type GaiRiskId = string;
export type SuggestedActionId = string;
export type PrimaryGaiConsiderationId = string;
export type StructuredPublicFeedbackId = string;
export type AiRedTeamingId = string;
export type GaiProfileId = string;
/**
* The four high-level AI RMF Core functions. GOVERN is a
cross-cutting function applied throughout; MAP, MEASURE, and MANAGE
operate on specific AI systems and lifecycle stages.
*/
export enum FunctionEnum {
    
    /** Cultivates and implements a culture of risk management; outlines
processes, documents, and organizational schemes that anticipate,
identify, and manage AI risks. */
    GOVERN = "GOVERN",
    /** Establishes the context to frame risks related to an AI system;
identifies risks based on intended purposes, capabilities, and
contextual factors. */
    MAP = "MAP",
    /** Employs quantitative, qualitative, or mixed-method tools to
analyze, assess, benchmark, and monitor AI risk and related impacts. */
    MEASURE = "MEASURE",
    /** Allocates risk resources to mapped and measured risks on a
regular basis and as defined by the GOVERN function; risk
treatment includes plans to respond to, recover from, and
communicate about incidents or events. */
    MANAGE = "MANAGE",
};
/**
* AI lifecycle stages as defined in Figure 2 (modified from
OECD 2022). Each stage corresponds to one of the AI system
dimensions (see AiSystemDimensionEnum).
*/
export enum AiLifecycleStageEnum {
    
    /** Articulate and document the system's concept and objectives,
underlying assumptions, context, and requirements (Application
Context dimension). */
    PLAN_AND_DESIGN = "PLAN_AND_DESIGN",
    /** Gather, validate, and clean data and document the metadata and
characteristics of the dataset (Data and Input dimension). */
    COLLECT_AND_PROCESS_DATA = "COLLECT_AND_PROCESS_DATA",
    /** Create or select algorithms; train models (AI Model dimension). */
    BUILD_AND_USE_MODEL = "BUILD_AND_USE_MODEL",
    /** Verify, validate, calibrate, and interpret model output
(AI Model dimension). */
    VERIFY_AND_VALIDATE = "VERIFY_AND_VALIDATE",
    /** Pilot; check compatibility with legacy systems; verify regulatory
compliance; manage organizational change; and evaluate user
experience (Task and Output dimension). */
    DEPLOY_AND_USE = "DEPLOY_AND_USE",
    /** Operate the AI system and continuously assess its recommendations
and impacts (both intended and unintended) in light of objectives,
legal and regulatory requirements, and ethical considerations
(Application Context dimension). */
    OPERATE_AND_MONITOR = "OPERATE_AND_MONITOR",
};
/**
* Key socio-technical dimensions of an AI system (Figure 2).
People and Planet sits at the centre representing human and
societal well-being.
*/
export enum AiSystemDimensionEnum {
    
    /** The setting in which an AI system is deployed - includes legal,
regulatory, ethical, and societal considerations. */
    APPLICATION_CONTEXT = "APPLICATION_CONTEXT",
    /** The data and inputs an AI system uses, including training,
validation, test data, and operational inputs. */
    DATA_AND_INPUT = "DATA_AND_INPUT",
    /** The model(s) and algorithms at the heart of an AI system. */
    AI_MODEL = "AI_MODEL",
    /** The task the AI system is designed to perform and the outputs
it produces (predictions, recommendations, decisions). */
    TASK_AND_OUTPUT = "TASK_AND_OUTPUT",
    /** Human rights and the broader well-being of society and the
planet - centred in Figure 2. */
    PEOPLE_AND_PLANET = "PEOPLE_AND_PLANET",
};
/**
* Categories of AI actor tasks as described in Appendix A and
illustrated in Figure 3.
*/
export enum AiActorTaskEnum {
    
    /** Performed during the Application Context and Data and Input
phases; create the concept and objectives of AI systems and are
responsible for planning, design, and data collection. */
    AI_DESIGN = "AI_DESIGN",
    /** Performed during the AI Model phase; provide the initial
infrastructure of AI systems (model building, selection,
calibration, training, testing). */
    AI_DEVELOPMENT = "AI_DEVELOPMENT",
    /** Performed during the Task and Output phase; responsible for
contextual decisions on how the AI system is used and for
assuring deployment into production. */
    AI_DEPLOYMENT = "AI_DEPLOYMENT",
    /** Performed in the Application Context / Operate and Monitor
phase; operating the AI system and regularly assessing system
output and impacts. */
    OPERATION_AND_MONITORING = "OPERATION_AND_MONITORING",
    /** Test, Evaluation, Verification, and Validation tasks performed
throughout the AI lifecycle; examine the AI system or its
components, and detect and remediate problems. */
    TEVV = "TEVV",
    /** Human-centered design practices and methodologies; promoting
active involvement of end users and other interested parties;
incorporating context-specific norms and values. */
    HUMAN_FACTORS = "HUMAN_FACTORS",
    /** Input from multidisciplinary practitioners or scholars who
provide knowledge or expertise in - and about - an industry
sector, context, or application area. */
    DOMAIN_EXPERT = "DOMAIN_EXPERT",
    /** Assess and evaluate requirements for AI system accountability,
combat harmful bias, examine impacts, product safety, liability,
and security. */
    AI_IMPACT_ASSESSMENT = "AI_IMPACT_ASSESSMENT",
    /** Conducted by AI actors with financial, legal, or policy
management authority for acquisition of AI models, products, or
services from a third party. */
    PROCUREMENT = "PROCUREMENT",
    /** Assumed by AI actors with management, fiduciary, and legal
authority for the organization, including senior leadership and
the Board of Directors. */
    GOVERNANCE_AND_OVERSIGHT = "GOVERNANCE_AND_OVERSIGHT",
    /** Providers, developers, vendors, and evaluators of data,
algorithms, models, and/or systems and related services external
to the deploying organization. */
    THIRD_PARTY_ENTITIES = "THIRD_PARTY_ENTITIES",
    /** Individuals or groups that use the AI system for specific
purposes; range in competency from AI experts to first-time
users. */
    END_USERS = "END_USERS",
    /** All individuals, groups, communities, or organizations directly
or indirectly affected by AI systems or decisions based on the
output of AI systems. */
    AFFECTED_INDIVIDUALS_OR_COMMUNITIES = "AFFECTED_INDIVIDUALS_OR_COMMUNITIES",
    /** Provide formal or quasi-formal norms or guidance - includes
trade associations, standards developing organizations, advocacy
groups, researchers, environmental groups, and civil society
organizations. */
    OTHER_AI_ACTORS = "OTHER_AI_ACTORS",
    /** Most likely to directly experience positive and negative impacts
of AI technologies; provides motivation for actions taken by
other AI actors. */
    GENERAL_PUBLIC = "GENERAL_PUBLIC",
};
/**
* The seven characteristics of trustworthy AI systems described in
Figure 4 and Part 1 §3.
*/
export enum TrustworthinessCharacteristicEnum {
    
    /** Confirmation that requirements for a specific intended use have
been fulfilled (validation) and that the system performs as
required without failure (reliability). A necessary condition of
trustworthiness and the base for other characteristics. */
    VALID_AND_RELIABLE = "VALID_AND_RELIABLE",
    /** The system does not, under defined conditions, lead to a state
in which human life, health, property, or the environment is
endangered. */
    SAFE = "SAFE",
    /** The system can withstand unexpected adverse events or changes
(resilient) and maintain confidentiality, integrity, and
availability through protection mechanisms (secure). */
    SECURE_AND_RESILIENT = "SECURE_AND_RESILIENT",
    /** Trustworthy AI depends on accountability, which presupposes
transparency - the extent to which information about an AI
system and its outputs is available to those interacting with
it. */
    ACCOUNTABLE_AND_TRANSPARENT = "ACCOUNTABLE_AND_TRANSPARENT",
    /** Explainability concerns the mechanisms underlying an AI system's
operation; interpretability concerns the meaning of its output
in context. */
    EXPLAINABLE_AND_INTERPRETABLE = "EXPLAINABLE_AND_INTERPRETABLE",
    /** Norms and practices that help safeguard human autonomy,
identity, and dignity - including anonymity, confidentiality,
and control over personal information. */
    PRIVACY_ENHANCED = "PRIVACY_ENHANCED",
    /** Concerns for equality and equity by addressing issues such as
harmful bias and discrimination, and recognising that
perceptions of fairness differ across cultures and
applications. */
    FAIR_WITH_HARMFUL_BIAS_MANAGED = "FAIR_WITH_HARMFUL_BIAS_MANAGED",
};
/**
* High-level categories of harm related to AI systems (Figure 1).
*/
export enum HarmCategoryEnum {
    
    /** Harm to individuals, groups/communities, or society at large
(including civil liberties, rights, physical or psychological
safety, economic opportunity, democratic participation, and
educational access). */
    HARM_TO_PEOPLE = "HARM_TO_PEOPLE",
    /** Harm to an organization's business operations, security
breaches or monetary loss, or reputation. */
    HARM_TO_AN_ORGANIZATION = "HARM_TO_AN_ORGANIZATION",
    /** Harm to interconnected and interdependent elements and
resources, the global financial system, supply chain, natural
resources, the environment, and the planet. */
    HARM_TO_AN_ECOSYSTEM = "HARM_TO_AN_ECOSYSTEM",
};
/**
* Sub-categories of harm to people, per Figure 1.
*/
export enum HarmToPeopleSubcategoryEnum {
    
    /** Harm to a person's civil liberties, rights, physical or
psychological safety, or economic opportunity. */
    INDIVIDUAL = "INDIVIDUAL",
    /** Harm to a group such as discrimination against a population
sub-group. */
    GROUP_OR_COMMUNITY = "GROUP_OR_COMMUNITY",
    /** Harm to democratic participation or educational access. */
    SOCIETAL = "SOCIETAL",
};
/**
* The three major categories of AI bias identified by NIST
(Part 1 §3.7; see NIST SP 1270).
*/
export enum BiasCategoryEnum {
    
    /** Bias present in AI datasets, organizational norms, practices,
and processes across the AI lifecycle, and the broader society
that uses AI systems. */
    SYSTEMIC = "SYSTEMIC",
    /** Bias present in AI datasets and algorithmic processes; often
stems from systematic errors due to non-representative samples. */
    COMPUTATIONAL_AND_STATISTICAL = "COMPUTATIONAL_AND_STATISTICAL",
    /** Bias related to how an individual or group perceives AI system
information to make a decision or fill in missing information;
omnipresent in decision-making across the AI lifecycle. */
    HUMAN_COGNITIVE = "HUMAN_COGNITIVE",
};
/**
* Challenges that complicate AI risk measurement (Part 1 §1.2.1).
*/
export enum RiskMeasurementChallengeEnum {
    
    /** Risks related to third-party software, hardware, and data,
including misalignment of risk metrics or methodologies between
developers, deployers, and operators. */
    THIRD_PARTY_SOFTWARE_HARDWARE_AND_DATA = "THIRD_PARTY_SOFTWARE_HARDWARE_AND_DATA",
    /** Identifying and tracking emergent risks and considering
techniques for measuring them; impact assessment helps
understand context-specific harms. */
    TRACKING_EMERGENT_RISKS = "TRACKING_EMERGENT_RISKS",
    /** Lack of consensus on robust and verifiable measurement methods
for risk and trustworthiness, and their applicability to
different use cases. */
    AVAILABILITY_OF_RELIABLE_METRICS = "AVAILABILITY_OF_RELIABLE_METRICS",
    /** Measuring risk at different stages may yield different results;
some risks may be latent and increase as systems adapt and
evolve. */
    RISK_AT_DIFFERENT_LIFECYCLE_STAGES = "RISK_AT_DIFFERENT_LIFECYCLE_STAGES",
    /** Lab measurements may differ from risks that emerge in
operational, real-world settings. */
    RISK_IN_REAL_WORLD_SETTINGS = "RISK_IN_REAL_WORLD_SETTINGS",
    /** Opaque systems with limited explainability or interpretability,
poor documentation, or inherent uncertainty complicate risk
measurement. */
    INSCRUTABILITY = "INSCRUTABILITY",
    /** AI systems intended to augment or replace human activity
require a human baseline for comparison, which is difficult to
systematize. */
    HUMAN_BASELINE = "HUMAN_BASELINE",
};
/**
* Treatment options for AI risks (MANAGE 1.3).
*/
export enum RiskResponseEnum {
    
    /** Reducing the likelihood or magnitude of the risk. */
    MITIGATING = "MITIGATING",
    /** Shifting the risk to another party (e.g., via insurance or contract). */
    TRANSFERRING = "TRANSFERRING",
    /** Choosing not to engage in the activity that creates the risk. */
    AVOIDING = "AVOIDING",
    /** Acknowledging the risk and taking no further action. */
    ACCEPTING = "ACCEPTING",
};
/**
* Types of AI RMF Profile (§6).
*/
export enum ProfileTypeEnum {
    
    /** Implementation of the AI RMF Core for a specific setting or
application (e.g., a hiring profile, a fair housing profile). */
    USE_CASE = "USE_CASE",
    /** Description of the current state of AI risk management
activities within a sector, industry, organization, or
application context. */
    TEMPORAL_CURRENT = "TEMPORAL_CURRENT",
    /** Description of the desired or target state of AI risk
management activities. */
    TEMPORAL_TARGET = "TEMPORAL_TARGET",
    /** Risks of models or applications used across use cases or
sectors (e.g., large language models, cloud-based services,
acquisition). */
    CROSS_SECTORAL = "CROSS_SECTORAL",
};
/**
* Audience categorisation for the AI RMF (Part 1 §2).
*/
export enum AudienceEnum {
    
    /** AI actors who perform or manage the design, development,
deployment, evaluation, and use of AI systems and drive AI
risk management efforts. */
    PRIMARY = "PRIMARY",
    /** AI actors in the People and Planet dimension who *inform* the
primary audience - trade associations, standards developers,
researchers, advocacy groups, civil society organisations,
end users, and impacted individuals or communities. */
    INFORMING = "INFORMING",
};
/**
* Whether an impact of an AI system is positive, negative, or both
(Part 1 §1.1).
*/
export enum ImpactSignEnum {
    
    /** A beneficial impact or opportunity. */
    POSITIVE = "POSITIVE",
    /** A harmful impact or threat. */
    NEGATIVE = "NEGATIVE",
    /** An impact that is both positive and negative. */
    MIXED = "MIXED",
};
/**
* The 12 risks unique to or exacerbated by Generative AI as
enumerated in NIST AI 600-1 Section 2.
*/
export enum GaiRiskCategoryEnum {
    
    /** Eased access to or synthesis of materially nefarious
information or design capabilities related to chemical,
biological, radiological, or nuclear (CBRN) weapons or
other dangerous materials or agents. */
    CBRN_INFORMATION_OR_CAPABILITIES = "CBRN_INFORMATION_OR_CAPABILITIES",
    /** The production of confidently stated but erroneous or
false content (colloquially "hallucinations" or
"fabrications") by which users may be misled or deceived. */
    CONFABULATION = "CONFABULATION",
    /** Eased production of and access to violent, inciting,
radicalizing, or threatening content as well as
recommendations to carry out self-harm or conduct illegal
activities. Includes difficulty controlling public
exposure to hateful and disparaging or stereotyping
content. */
    DANGEROUS_VIOLENT_OR_HATEFUL_CONTENT = "DANGEROUS_VIOLENT_OR_HATEFUL_CONTENT",
    /** Impacts due to leakage and unauthorized use, disclosure, or
de-anonymization of biometric, health, location, or other
personally identifiable information or sensitive data. */
    DATA_PRIVACY = "DATA_PRIVACY",
    /** Impacts due to high compute resource utilization in
training or operating GAI models, and related outcomes that
may adversely impact ecosystems. */
    ENVIRONMENTAL_IMPACTS = "ENVIRONMENTAL_IMPACTS",
    /** Amplification and exacerbation of historical, societal,
and systemic biases; performance disparities between
sub-groups or languages, possibly due to non-representative
training data, resulting in discrimination, amplification
of biases, or incorrect presumptions about performance;
undesired homogeneity that skews system or model outputs. */
    HARMFUL_BIAS_OR_HOMOGENIZATION = "HARMFUL_BIAS_OR_HOMOGENIZATION",
    /** Arrangements of or interactions between a human and an AI
system which can result in the human inappropriately
anthropomorphising GAI systems or experiencing algorithmic
aversion, automation bias, over-reliance, or emotional
entanglement with GAI systems. */
    HUMAN_AI_CONFIGURATION = "HUMAN_AI_CONFIGURATION",
    /** Lowered barrier to entry to generate and support the
exchange and consumption of content which may not
distinguish fact from opinion or fiction or acknowledge
uncertainties, or could be leveraged for large-scale
dis- and mis-information campaigns. */
    INFORMATION_INTEGRITY = "INFORMATION_INTEGRITY",
    /** Lowered barriers for offensive cyber capabilities,
including via automated discovery and exploitation of
vulnerabilities; increased attack surface for targeted
cyberattacks, which may compromise a system's availability
or the confidentiality or integrity of training data,
code, or model weights. */
    INFORMATION_SECURITY = "INFORMATION_SECURITY",
    /** Eased production or replication of alleged copyrighted,
trademarked, or licensed content without authorization
(possibly outside fair use); eased exposure of trade
secrets; or plagiarism or illegal replication. */
    INTELLECTUAL_PROPERTY = "INTELLECTUAL_PROPERTY",
    /** Eased production of and access to obscene, degrading,
and/or abusive imagery which can cause harm, including
synthetic child sexual abuse material (CSAM) and
nonconsensual intimate images (NCII) of adults. */
    OBSCENE_DEGRADING_OR_ABUSIVE_CONTENT = "OBSCENE_DEGRADING_OR_ABUSIVE_CONTENT",
    /** Non-transparent or untraceable integration of upstream
third-party components, including data that has been
improperly obtained or not processed and cleaned due to
increased automation from GAI; improper supplier vetting
across the AI lifecycle; or other issues that diminish
transparency or accountability for downstream users. */
    VALUE_CHAIN_AND_COMPONENT_INTEGRATION = "VALUE_CHAIN_AND_COMPONENT_INTEGRATION",
};
/**
* Higher-level grouping of GAI risks, derived from the UK's
International Scientific Report on the Safety of Advanced AI
(NIST AI 600-1 Section 2, footnote 5).
*/
export enum GaiRiskCategorizationEnum {
    
    /** Risks from malfunction. Examples include confabulation;
dangerous or violent recommendations; data privacy; value
chain and component integration; harmful bias and
homogenization. */
    TECHNICAL_OR_MODEL_RISKS = "TECHNICAL_OR_MODEL_RISKS",
    /** Risks from malicious use. Examples include CBRN information
or capabilities; data privacy; human-AI configuration;
obscene, degrading, and/or abusive content; information
integrity; information security. */
    MISUSE_BY_HUMANS = "MISUSE_BY_HUMANS",
    /** Systemic risks. Examples include data privacy;
environmental impacts; intellectual property. */
    ECOSYSTEM_OR_SOCIETAL_RISKS = "ECOSYSTEM_OR_SOCIETAL_RISKS",
};
/**
* The scope at which a GAI risk may manifest (Section 2).
*/
export enum GaiRiskScopeEnum {
    
    /** Individual GAI model or system level. */
    MODEL_OR_SYSTEM = "MODEL_OR_SYSTEM",
    /** Specific application or implementation - i.e., a particular
use case. */
    APPLICATION_OR_IMPLEMENTATION = "APPLICATION_OR_IMPLEMENTATION",
    /** Beyond a single system or organizational context - e.g.,
algorithmic monocultures, labor-market impacts, creative
economies. */
    ECOSYSTEM = "ECOSYSTEM",
};
/**
* The source(s) from which a GAI risk may emerge (Section 2).
*/
export enum GaiRiskSourceEnum {
    
    /** From decisions made during model or system design. */
    DESIGN = "DESIGN",
    /** From the training data or training process. */
    TRAINING = "TRAINING",
    /** From operating the GAI model or system. */
    OPERATION = "OPERATION",
    /** From inputs supplied to the model at inference time. */
    MODEL_INPUTS = "MODEL_INPUTS",
    /** From the GAI system's generated outputs. */
    MODEL_OUTPUTS = "MODEL_OUTPUTS",
    /** From human behaviour - abuse, misuse, or unsafe repurposing
by humans (adversarial or not). */
    HUMAN_BEHAVIOR = "HUMAN_BEHAVIOR",
    /** From interactions between a human and the AI system. */
    HUMAN_AI_INTERACTION = "HUMAN_AI_INTERACTION",
};
/**
* The time scale over which a GAI risk may materialise
(Section 2).
*/
export enum GaiRiskTimeScaleEnum {
    
    /** Materialises abruptly (e.g., distribution of deepfakes). */
    IMMEDIATE = "IMMEDIATE",
    /** Materialises across extended periods (e.g., long-term
effect of disinformation on societal trust). */
    PROLONGED = "PROLONGED",
};
/**
* Two-letter function prefix used in GAI Action IDs.
*/
export enum GaiActionFunctionPrefixEnum {
    
    /** Govern function. */
    GV = "GV",
    /** Map function. */
    MP = "MP",
    /** Measure function. */
    MS = "MS",
    /** Manage function. */
    MG = "MG",
};
/**
* The four overarching themes derived from the GAI PWG
consultation process (Appendix A).
*/
export enum PrimaryConsiderationEnum {
    
    /** How organizational governance regimes may be re-evaluated
and adjusted for GAI contexts (A.1). */
    GOVERNANCE = "GOVERNANCE",
    /** Test, evaluation, validation, and verification practices
appropriate for GAI prior to deployment (A.1.4). */
    PRE_DEPLOYMENT_TESTING = "PRE_DEPLOYMENT_TESTING",
    /** Digital transparency mechanisms (provenance data tracking,
watermarking, synthetic content detection) for tracing
origin and history of content (A.1.6 - A.1.7). */
    CONTENT_PROVENANCE = "CONTENT_PROVENANCE",
    /** Documenting, reporting, and sharing information about AI
incidents to mitigate harm and improve risk management
(A.1.8). */
    INCIDENT_DISCLOSURE = "INCIDENT_DISCLOSURE",
};
/**
* Categories of structured public feedback for GAI risk
management (Appendix A.1.5).
*/
export enum StructuredFeedbackMethodEnum {
    
    /** Methods used to solicit feedback from civil society groups,
affected communities, and users (focus groups, small user
studies, surveys). */
    PARTICIPATORY_ENGAGEMENT_METHODS = "PARTICIPATORY_ENGAGEMENT_METHODS",
    /** Methods used to determine how people interact with,
consume, use, and make sense of AI-generated information
(UX, usability, randomised experiments). */
    FIELD_TESTING = "FIELD_TESTING",
    /** A structured testing exercise used to probe an AI system
to find flaws and vulnerabilities such as inaccurate,
harmful, or discriminatory outputs. */
    AI_RED_TEAMING = "AI_RED_TEAMING",
};
/**
* Types of AI red-teaming exercises (Appendix A.1.5).
*/
export enum RedTeamingTypeEnum {
    
    /** Performed by general users not necessarily having AI or
technical expertise. */
    GENERAL_PUBLIC = "GENERAL_PUBLIC",
    /** Performed by specialists with expertise in the domain or
specific red-teaming context (medicine, biotech,
cybersecurity). */
    EXPERT = "EXPERT",
    /** Hybrid exercises using both expert and general-public
participants. */
    COMBINATION = "COMBINATION",
    /** Performed by GAI in combination with specialist or
non-specialist human teams. */
    HUMAN_AND_AI = "HUMAN_AND_AI",
};


/**
 * A generic grouping for any identifiable AI RMF element.
 */
export interface NamedThing {
    /** A unique identifier for an element. */
    id: string,
    /** A short human-readable name. */
    name?: string,
    /** A human-readable title. */
    title?: string,
    /** A human-readable description. */
    description?: string,
    /** Related references. */
    see_also?: string[],
}


/**
 * An engineered or machine-based system that can, for a given set
of objectives, generate outputs such as predictions,
recommendations, or decisions influencing real or virtual
environments. AI systems are designed to operate with varying
levels of autonomy (Adapted from OECD Recommendation on AI:2019;
ISO/IEC 22989:2022).
 */
export interface AiSystem extends NamedThing {
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** The AI system dimension the element applies to. */
    ai_dimension?: string,
}


/**
 * A socio-technical dimension of an AI system (Figure 2):
Application Context, Data and Input, AI Model, Task and Output,
or People and Planet.
 */
export interface AiSystemDimension extends NamedThing {
    /** Which of the five dimensions this instance represents. */
    dimension_kind: string,
}


/**
 * A stage of the AI lifecycle (Figure 2): Plan and Design,
Collect and Process Data, Build and Use Model, Verify and
Validate, Deploy and Use, or Operate and Monitor.
 */
export interface AiLifecycleStage extends NamedThing {
    /** Which of the six stages this instance represents. */
    stage_kind: string,
    /** Whether this stage incorporates TEVV activities. */
    includes_tevv?: boolean,
}


/**
 * An organization or individual that plays an active role in the AI
system lifecycle. AI actors include those who deploy or operate
AI as well as those who inform via formal or quasi-formal norms
and guidance (OECD 2019).
 */
export interface AiActor extends NamedThing {
    /** AI actor task category. */
    actor_task?: string,
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** Whether the actor or task is a Test, Evaluation, Verification, and
Validation (TEVV) actor / task. */
    is_tevv?: boolean,
    /** Whether the actor is part of the *primary* AI RMF audience or the
*informing* People-and-Planet audience. */
    audience?: string,
}


/**
 * A category of task performed by AI actors (Appendix A). Each
task is associated with one or more lifecycle stages and a
typical set of actor roles.
 */
export interface AiActorTask extends NamedThing {
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** The AI system dimension the element applies to. */
    ai_dimension?: string,
    /** Which of the actor task categories this is. */
    task_kind: string,
    /** Representative actor roles that perform this task. */
    typical_actors?: string[],
}


/**
 * The composite measure of an event's probability of occurring and
the magnitude or degree of the consequences of that event. When
considering negative impact, risk is a function of (1) the
negative impact or magnitude of harm and (2) the likelihood of
occurrence (Adapted from ISO 31000:2018; OMB Circular A-130:2016).
 */
export interface Risk extends NamedThing {
    /** Estimated probability of the event occurring (0.0 to 1.0). The
AI RMF leaves quantification approaches to the implementer. */
    likelihood?: number,
    /** Magnitude or degree of consequences if the event occurs (free
text or qualitative scale). */
    magnitude?: string,
    /** Whether the impact is positive, negative, or both. */
    impact_sign?: string,
    /** Whether this risk represents risk remaining after risk treatment
(residual risk per ISO Guide 73). */
    is_residual?: boolean,
    /** The chosen risk treatment option. */
    risk_response?: string,
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** Trustworthiness characteristic(s) the element pertains to. */
    trustworthiness_characteristic?: string,
    /** The impacts that contribute to this risk. */
    related_impacts?: Impact[],
    /** The AI system this risk pertains to. */
    affects_system?: AiSystemId,
}


/**
 * A positive, negative, or both consequence of an AI system. Impacts
can manifest as opportunities (positive) or threats (negative).
 */
export interface Impact extends NamedThing {
    /** Whether the impact is positive, negative, or both. */
    impact_sign?: string,
    /** Magnitude or degree of consequences if the event occurs (free
text or qualitative scale). */
    magnitude?: string,
    /** Estimated probability of the event occurring (0.0 to 1.0). The
AI RMF leaves quantification approaches to the implementer. */
    likelihood?: number,
    /** Entities (people, organizations, ecosystems) the risk or harm
may affect. */
    affects?: NamedThingId[],
}


/**
 * A negative impact that may be experienced by individuals,
groups, communities, organizations, society, the environment, or
the planet (Figure 1).
 */
export interface Harm extends NamedThing {
    /** The high-level harm category (people / organization / ecosystem). */
    harm_category?: string,
    /** The sub-category when harm is to people (individual / group / societal). */
    harm_to_people_subcategory?: string,
    /** Magnitude or degree of consequences if the event occurs (free
text or qualitative scale). */
    magnitude?: string,
    /** Entities (people, organizations, ecosystems) the risk or harm
may affect. */
    affects?: NamedThingId[],
}


/**
 * Risk remaining after risk treatment (ISO Guide 73). Documenting
residual risks helps system providers consider risks of deploying
the AI product and informs end users about potential negative
impacts.
 */
export interface ResidualRisk extends Risk {
}


/**
 * The organization's or AI actor's readiness to bear risk in order
to achieve its objectives (Adapted from ISO Guide 73). Risk
tolerance is highly contextual and application- and use-case
specific.
 */
export interface RiskTolerance extends NamedThing {
    /** Free-text statement of the tolerance level or threshold. */
    tolerance_statement?: string,
    /** Legal or regulatory requirements influencing the tolerance. */
    legal_basis?: string,
}


/**
 * A challenge that complicates measurement of AI risks
(Part 1 §1.2.1).
 */
export interface RiskMeasurementChallenge extends NamedThing {
    /** Which measurement challenge this represents. */
    challenge_kind: string,
}


/**
 * A characteristic of a trustworthy AI system (Figure 4 / Part 1
§3). The seven characteristics are inter-related; addressing them
individually does not guarantee trustworthiness, and tradeoffs
are usually involved.
 */
export interface TrustworthinessCharacteristic extends NamedThing {
    /** Which trustworthiness characteristic this instance represents. */
    characteristic_kind: string,
    /** True when this is a necessary condition for trustworthiness
(Valid and Reliable; per Figure 4 it is the base of all other
characteristics). */
    is_base_condition?: boolean,
    /** True when this characteristic relates to all others
(Accountable and Transparent; shown vertically in Figure 4). */
    is_cross_cutting?: boolean,
}


/**
 * A form of AI bias - a deviation that may be perpetuated or
amplified by AI systems. NIST identifies three major categories:
systemic, computational/statistical, and human-cognitive
(Part 1 §3.7; NIST SP 1270).
 */
export interface Bias extends NamedThing {
    /** Category or categories of bias addressed. */
    bias_category?: string,
}


/**
 * A top-level AI RMF Core function. Each function organizes AI risk
management activities at the highest level. GOVERN applies across
all stages; MAP, MEASURE, and MANAGE apply to AI-system-specific
contexts and lifecycle stages.
 */
export interface Function extends NamedThing {
    /** The function code (GOVERN, MAP, MEASURE, or MANAGE). */
    function_code: string,
    /** Categories that belong to a Function. */
    categories?: Category[],
}


/**
 * A category within an AI RMF Core function (e.g., "GOVERN 1:
Policies, processes, procedures, and practices ... are in place,
transparent, and implemented effectively"). Categories group
related subcategories.
 */
export interface Category extends NamedThing {
    /** Identifier of a Category (e.g., "GOVERN 1"). */
    category_id?: string,
    /** The outcome statement of a Category or Subcategory - the desired
result of carrying out its actions. */
    outcome?: string,
    /** Subcategories that belong to a Category. */
    subcategories?: Subcategory[],
}


/**
 * A subcategory within an AI RMF Core category (e.g., "GOVERN 1.1:
Legal and regulatory requirements involving AI are understood,
managed, and documented"). Subcategories express specific
outcomes.
 */
export interface Subcategory extends NamedThing {
    /** Identifier of a Subcategory (e.g., "GOVERN 1.1"). */
    subcategory_id?: string,
    /** The outcome statement of a Category or Subcategory - the desired
result of carrying out its actions. */
    outcome?: string,
    /** Trustworthiness characteristic(s) the element pertains to. */
    trustworthiness_characteristic?: string,
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** Free-text discussion of the subcategory or related concept.
Corresponds to the AI RMF Playbook "About" section. */
    about_text?: string,
    /** Free-text bulleted list of suggested actions an organization can
take. Corresponds to the AI RMF Playbook "Actions" section. */
    suggested_actions_text?: string,
    /** Free-text documentation questions and transparency resources.
Corresponds to the AI RMF Playbook "Documentation" section. */
    documentation_questions?: string,
    /** Free-text list of references, citations, and supporting
resources. Corresponds to the AI RMF Playbook "References"
section. */
    references_text?: string,
    /** Free-text topic tags applied to a playbook entry (e.g.,
"Governance", "Trustworthy Characteristics", "Validity and
Reliability"). */
    topics?: string[],
    /** Free-text list of AI Actor categories the entry applies to,
preserving the original case used in the AI RMF Playbook
(e.g., "Governance and Oversight", "TEVV"). For controlled
enum values see `actor_task` (range AiActorTaskEnum). */
    ai_actor_categories?: string[],
}


/**
 * An implementation of the AI RMF Functions, Categories, and
Subcategories for a specific setting or application based on the
requirements, risk tolerance, and resources of the user (§6).
Profiles may be use-case-specific, temporal (current or target),
or cross-sectoral.
 */
export interface AiRmfProfile extends NamedThing {
    /** The kind of AI RMF Profile. */
    profile_type: string,
    /** For temporal current profiles - how AI is currently being managed
and related risks in terms of current outcomes. */
    current_state?: string,
    /** For temporal target profiles - the outcomes needed to achieve the
desired AI risk management goals. */
    target_state?: string,
    /** The sector, industry, technology, or end-use application the
profile addresses (e.g., "hiring", "fair housing"). */
    sector?: string,
    /** Subcategories that the profile implements or addresses. */
    addresses?: SubcategoryId[],
}


/**
 * A design attribute of the AI RMF (Appendix D) - one of the
qualities the Framework strives to embody (e.g., risk-based,
consensus-driven, plain language, common language, easily usable,
universally applicable, outcome-focused, leveraging existing
standards, law- and regulation-agnostic, living document).
 */
export interface RmfAttribute extends NamedThing {
}


/**
 * A risk that is new or increased for AI-based technology compared
to traditional software (Appendix B) - e.g., data quality, model
drift, opacity, scale and complexity, pre-trained model
uncertainty, emergent properties, privacy aggregation, or
environmental cost.
 */
export interface AiSpecificRisk extends NamedThing {
}


/**
 * An issue that merits further consideration in human-AI
interaction (Appendix C) - e.g., clear human roles and
responsibilities, systemic and human-cognitive biases in design,
variability of human-AI interaction outcomes, complexity of
presenting AI system information to humans.
 */
export interface HumanAiInteractionIssue extends NamedThing {
}


/**
 * A single AI RMF Playbook entry - an enrichment of a Core
subcategory with prose discussion, suggested actions,
documentation questions, references, and topic tags.

Attribute names use the same identifiers found in the published
NIST AI RMF Playbook JSON (e.g., `section_about`,
`section_actions`) so that the data can be loaded directly.
 */
export interface PlaybookEntry {
    /** Function label as serialised in the published Playbook JSON
(Title case - "Govern", "Map", "Measure", "Manage"). For
the controlled enum see `function_kind`. */
    type?: string,
    /** Subcategory identifier (e.g., "GOVERN 1.1"). Mirrors the
AI RMF Subcategory `subcategory_id`. */
    title?: string,
    /** Category code in the form "FUNCTION-N" (e.g., "GOVERN-1")
as used in the Playbook. */
    category?: string,
    /** Outcome statement of the subcategory. */
    description?: string,
    /** Free-text discussion ("About" section). */
    section_about?: string,
    /** Bulleted suggested actions ("Actions" section). */
    section_actions?: string,
    /** Documentation questions and transparency resources
("Documentation" section). */
    section_doc?: string,
    /** References and citations ("References" section). */
    section_ref?: string,
    /** AI actor categories the entry applies to. Free-text to
preserve the casing of the source data (e.g., "Governance
and Oversight"). */
    ai_actors?: string[],
    /** Topic tags (e.g., "Legal and Regulatory", "Validity and
Reliability"). */
    topic?: string[],
}


/**
 * A container for a set of PlaybookEntry instances - the
serialisation root for an AI RMF Playbook companion document.
Validate with ``linkml-validate --target-class PlaybookCollection``;
the canonical tree-root for the schema is ``AiRmfFramework``.
 */
export interface PlaybookCollection {
    /** The Playbook entries in this collection. */
    entries?: PlaybookEntry[],
}


/**
 * Publication metadata for an instance of the AI RMF (e.g., NIST
AI 100-1, January 2023). The Framework is intended to be a
living document, employing a two-number versioning system (major.minor).
 */
export interface AiRmfDocument extends NamedThing {
    /** Version identifier of the document. */
    version?: string,
    /** The publisher of the document (e.g., NIST). */
    publisher?: string,
    /** Digital Object Identifier for the document. */
    doi?: string,
    /** Date the document was published. */
    published_date?: date,
    /** Reference to the source of the element (typically the document
or section it originated from). */
    source?: string,
}


/**
 * Root container that bundles the AI RMF Core (Functions) with
foundational concepts (trustworthiness characteristics,
lifecycle, actors, risks, harms), profiles, and Framework
attributes. Designed for serialising the Framework or a tailored
instance of it as a single JSON / YAML document.
 */
export interface AiRmfFramework extends NamedThing {
    /** Publication metadata. */
    document?: AiRmfDocument,
    /** The four AI RMF Core functions and their content. */
    functions?: Function[],
    /** The seven characteristics of trustworthy AI. */
    trustworthiness_characteristics?: TrustworthinessCharacteristic[],
    /** The AI lifecycle stages (Figure 2). */
    lifecycle_stages?: AiLifecycleStage[],
    /** The AI system dimensions (Figure 2). */
    dimensions?: AiSystemDimension[],
    /** AI actor task categories (Appendix A). */
    actor_tasks?: AiActorTask[],
    /** AI RMF profiles defined alongside this Framework instance. */
    profiles?: AiRmfProfile[],
    /** Design attributes of the AI RMF (Appendix D). */
    attributes_?: RmfAttribute[],
    /** Identified challenges in measuring AI risk. */
    risk_measurement_challenges?: RiskMeasurementChallenge[],
    /** AI-specific risks compared to traditional software (Appendix B). */
    ai_specific_risks?: AiSpecificRisk[],
    /** Human-AI interaction considerations (Appendix C). */
    human_ai_interaction_issues?: HumanAiInteractionIssue[],
}


/**
 * A risk that is novel to or exacerbated by Generative AI.
Each instance corresponds to one of the 12 risk categories
enumerated in NIST AI 600-1 Section 2.
 */
export interface GaiRisk extends AiSpecificRisk {
    /** The GAI risk category this element represents. */
    gai_risk_kind?: string,
    /** Higher-level categorisation - technical/model, misuse, or
ecosystem/societal. */
    risk_categorization?: string,
    /** Scope levels at which the risk may manifest. */
    risk_scope?: string,
    /** Sources from which the risk may emerge. */
    risk_sources?: string,
    /** Time scales over which the risk may materialise. */
    time_scale?: string,
    /** The AI lifecycle stage(s) the element applies to. */
    lifecycle_stage?: string,
    /** Trustworthiness characteristic(s) the element pertains to. */
    trustworthiness_characteristic?: string,
    /** Suggested actions that address this risk (back-reference). */
    addressed_by_actions?: SuggestedActionId[],
}


/**
 * A suggested action an organisation can take to manage GAI
risks. Each action is identified by an Action ID, linked to an
AI RMF subcategory, and may be relevant to one or more GAI
risks and AI actor tasks (NIST AI 600-1 Section 3).
 */
export interface SuggestedAction extends NamedThing {
    /** Identifier of a Suggested Action. */
    action_id: string,
    /** Two-letter function prefix of the action's subcategory. */
    function_prefix?: string,
    /** Identifier of the AI RMF subcategory the action applies to. */
    applies_to_subcategory?: string,
    /** GAI risk categories addressed by a suggested action or
considered by a primary consideration. */
    gai_risks?: string,
    /** AI actor task category. */
    actor_task?: string,
}


/**
 * An overarching consideration derived from the NIST GAI PWG
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
 */
export interface PrimaryGaiConsideration extends NamedThing {
    /** Which primary consideration this element represents. */
    consideration_kind: string,
    /** Governance plans and actions (A.1.2) - e.g., "Auditing and
assessment", "Data provenance", "Incident response",
"Impact assessments", "Stakeholder engagement", "Synthetic
content detection", "Whistleblower protections". */
    governance_practices?: string[],
    /** Considerations for third-party GAI integrations,
procurement, SBOMs, SLAs, and SSAE reports (A.1.3). */
    third_party_considerations?: string,
    /** For Pre-Deployment Testing: free-text discussion of why
current TEVV approaches may be inadequate (A.1.4). */
    limitations_of_current_approaches?: string,
    /** For Content Provenance: provenance data tracking
techniques such as digital watermarking, metadata
recording, digital fingerprinting, human authentication
(A.1.6). */
    provenance_techniques?: string[],
    /** For Incident Disclosure: the definition of AI incident
used by the organisation (A.1.8). */
    ai_incident_definition?: string,
}


/**
 * Methods used to evaluate whether GAI systems are performing as
intended and to calibrate and verify traditional measurement
methods (A.1.5).
 */
export interface StructuredPublicFeedback extends NamedThing {
    /** Which structured feedback method this element represents. */
    feedback_method_kind: string,
}


/**
 * A structured testing exercise used to probe an AI system to
find flaws and vulnerabilities such as inaccurate, harmful, or
discriminatory outputs, often in a controlled environment and
in collaboration with system developers (A.1.5).
 */
export interface AiRedTeaming extends StructuredPublicFeedback {
    /** The type of AI red-teaming exercise. */
    red_team_type?: string,
}


/**
 * Root container that bundles the NIST AI 600-1 Generative AI
Profile: GAI risks (Section 2), suggested actions (Section 3),
and primary considerations (Appendix A).
 */
export interface GaiProfile extends AiRmfProfile {
    /** The catalog of GAI risks (Section 2). */
    gai_risk_catalog?: GaiRisk[],
    /** Suggested actions to manage GAI risks (Section 3). */
    suggested_actions?: SuggestedAction[],
    /** The primary GAI considerations from Appendix A
(Governance, Pre-Deployment Testing, Content Provenance,
Incident Disclosure). Discriminated by
`consideration_kind`. */
    primary_considerations?: PrimaryGaiConsideration[],
    /** Structured public feedback methods relevant to the profile
(A.1.5). */
    structured_feedback_methods?: StructuredPublicFeedback[],
}



