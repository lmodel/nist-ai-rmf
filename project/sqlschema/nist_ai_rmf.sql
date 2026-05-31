-- # Abstract Class: NamedThing Description: A generic grouping for any identifiable AI RMF element.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: AiSystem Description: An engineered or machine-based system that can, for a given setof objectives, generate outputs such as predictions,recommendations, or decisions influencing real or virtualenvironments. AI systems are designed to operate with varyinglevels of autonomy (Adapted from OECD Recommendation on AI:2019;ISO/IEC 22989:2022).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: AiSystemDimension Description: A socio-technical dimension of an AI system (Figure 2):Application Context, Data and Input, AI Model, Task and Output,or People and Planet.
--     * Slot: dimension_kind Description: Which AI system dimension an `AiSystemDimension` instance represents.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiLifecycleStage Description: A stage of the AI lifecycle (Figure 2): Plan and Design,Collect and Process Data, Build and Use Model, Verify andValidate, Deploy and Use, or Operate and Monitor.
--     * Slot: stage_kind Description: Which AI lifecycle stage an `AiLifecycleStage` instance represents.
--     * Slot: includes_tevv Description: Whether the lifecycle stage incorporates TEVV activities.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiActor Description: An organization or individual that plays an active role in the AIsystem lifecycle. AI actors include those who deploy or operateAI as well as those who inform via formal or quasi-formal normsand guidance (OECD 2019).
--     * Slot: is_tevv Description: Whether the actor or task is a Test, Evaluation, Verification, andValidation (TEVV) actor / task.
--     * Slot: audience Description: Whether the actor is part of the *primary* AI RMF audience or the*informing* People-and-Planet audience.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: AiActorTask Description: A category of task performed by AI actors (Appendix A). Eachtask is associated with one or more lifecycle stages and atypical set of actor roles.
--     * Slot: task_kind Description: Which AI actor task category an `AiActorTask` instance represents.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: Risk Description: The composite measure of an event's probability of occurring andthe magnitude or degree of the consequences of that event. Whenconsidering negative impact, risk is a function of (1) thenegative impact or magnitude of harm and (2) the likelihood ofoccurrence (Adapted from ISO 31000:2018; OMB Circular A-130:2016).
--     * Slot: likelihood Description: Estimated probability of the event occurring (0.0 to 1.0). TheAI RMF leaves quantification approaches to the implementer.
--     * Slot: magnitude Description: Magnitude or degree of consequences if the event occurs (freetext or qualitative scale).
--     * Slot: impact_sign Description: Whether the impact is positive, negative, or both.
--     * Slot: is_residual Description: Whether this risk represents risk remaining after risk treatment(residual risk per ISO Guide 73).
--     * Slot: risk_response Description: The chosen risk treatment option.
--     * Slot: affects_system Description: The AI system a risk pertains to.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: Impact Description: A positive, negative, or both consequence of an AI system. Impactscan manifest as opportunities (positive) or threats (negative).
--     * Slot: impact_sign Description: Whether the impact is positive, negative, or both.
--     * Slot: magnitude Description: Magnitude or degree of consequences if the event occurs (freetext or qualitative scale).
--     * Slot: likelihood Description: Estimated probability of the event occurring (0.0 to 1.0). TheAI RMF leaves quantification approaches to the implementer.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: ResidualRisk_id Description: Autocreated FK slot
-- # Class: Harm Description: A negative impact that may be experienced by individuals,groups, communities, organizations, society, the environment, orthe planet (Figure 1).
--     * Slot: harm_category Description: The high-level harm category (people / organization / ecosystem).
--     * Slot: harm_to_people_subcategory Description: The sub-category when harm is to people (individual / group / societal).
--     * Slot: magnitude Description: Magnitude or degree of consequences if the event occurs (freetext or qualitative scale).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: ResidualRisk Description: Risk remaining after risk treatment (ISO Guide 73). Documentingresidual risks helps system providers consider risks of deployingthe AI product and informs end users about potential negativeimpacts.
--     * Slot: likelihood Description: Estimated probability of the event occurring (0.0 to 1.0). TheAI RMF leaves quantification approaches to the implementer.
--     * Slot: magnitude Description: Magnitude or degree of consequences if the event occurs (freetext or qualitative scale).
--     * Slot: impact_sign Description: Whether the impact is positive, negative, or both.
--     * Slot: is_residual Description: Whether this risk represents risk remaining after risk treatment(residual risk per ISO Guide 73).
--     * Slot: risk_response Description: The chosen risk treatment option.
--     * Slot: affects_system Description: The AI system a risk pertains to.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: RiskTolerance Description: The organization's or AI actor's readiness to bear risk in orderto achieve its objectives (Adapted from ISO Guide 73). Risktolerance is highly contextual and application- and use-casespecific.
--     * Slot: tolerance_statement Description: Free-text statement of a risk tolerance level or threshold.
--     * Slot: legal_basis Description: Legal or regulatory requirements influencing a risk tolerance.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: RiskMeasurementChallenge Description: A challenge that complicates measurement of AI risks(Part 1 §1.2.1).
--     * Slot: challenge_kind Description: Which risk-measurement challenge a `RiskMeasurementChallenge` represents.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: TrustworthinessCharacteristic Description: A characteristic of a trustworthy AI system (Figure 4 / Part 1§3). The seven characteristics are inter-related; addressing themindividually does not guarantee trustworthiness, and tradeoffsare usually involved.
--     * Slot: characteristic_kind Description: Which trustworthiness characteristic a `TrustworthinessCharacteristic` represents.
--     * Slot: is_base_condition Description: True when this characteristic is a necessary condition fortrustworthiness (per Figure 4 - Valid and Reliable is the baseof all others).
--     * Slot: is_cross_cutting Description: True when this characteristic relates to all others(Accountable and Transparent; shown vertically in Figure 4).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: Bias Description: A form of AI bias - a deviation that may be perpetuated oramplified by AI systems. NIST identifies three major categories:systemic, computational/statistical, and human-cognitive(Part 1 §3.7; NIST SP 1270).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: Function Description: A top-level AI RMF Core function. Each function organizes AI riskmanagement activities at the highest level. GOVERN applies acrossall stages; MAP, MEASURE, and MANAGE apply to AI-system-specificcontexts and lifecycle stages.
--     * Slot: function_code Description: The function code (GOVERN, MAP, MEASURE, or MANAGE).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: Category Description: A category within an AI RMF Core function (e.g., "GOVERN 1:Policies, processes, procedures, and practices ... are in place,transparent, and implemented effectively"). Categories grouprelated subcategories.
--     * Slot: category_id Description: Identifier of a Category (e.g., "GOVERN 1").
--     * Slot: outcome Description: The outcome statement of a Category or Subcategory - the desiredresult of carrying out its actions.
--     * Slot: id Description: Identifier for the category, typically using the"FUNCTION N" form (e.g., "GOVERN 1").
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: Function_id Description: Autocreated FK slot
-- # Class: Subcategory Description: A subcategory within an AI RMF Core category (e.g., "GOVERN 1.1:Legal and regulatory requirements involving AI are understood,managed, and documented"). Subcategories express specificoutcomes.
--     * Slot: subcategory_id Description: Identifier of a Subcategory (e.g., "GOVERN 1.1").
--     * Slot: outcome Description: The outcome statement of a Category or Subcategory - the desiredresult of carrying out its actions.
--     * Slot: about_text Description: Free-text discussion of the subcategory or related concept.Corresponds to the AI RMF Playbook "About" section.
--     * Slot: suggested_actions_text Description: Free-text bulleted list of suggested actions an organization cantake. Corresponds to the AI RMF Playbook "Actions" section.
--     * Slot: documentation_questions Description: Free-text documentation questions and transparency resources.Corresponds to the AI RMF Playbook "Documentation" section.
--     * Slot: references_text Description: Free-text list of references, citations, and supportingresources. Corresponds to the AI RMF Playbook "References"section.
--     * Slot: id Description: Identifier for the subcategory in the "FUNCTION N.M" form(e.g., "GOVERN 1.1").
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: Category_id Description: Autocreated FK slot
-- # Class: AiRmfProfile Description: An implementation of the AI RMF Functions, Categories, andSubcategories for a specific setting or application based on therequirements, risk tolerance, and resources of the user (§6).Profiles may be use-case-specific, temporal (current or target),or cross-sectoral.
--     * Slot: profile_type Description: The kind of AI RMF Profile.
--     * Slot: current_state Description: For temporal current profiles - how AI is currently being managedand related risks in terms of current outcomes.
--     * Slot: target_state Description: For temporal target profiles - the outcomes needed to achieve thedesired AI risk management goals.
--     * Slot: sector Description: The sector, industry, technology, or end-use application aprofile addresses (e.g., "hiring", "fair housing").
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: RmfAttribute Description: A design attribute of the AI RMF (Appendix D) - one of thequalities the Framework strives to embody (e.g., risk-based,consensus-driven, plain language, common language, easily usable,universally applicable, outcome-focused, leveraging existingstandards, law- and regulation-agnostic, living document).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiSpecificRisk Description: A risk that is new or increased for AI-based technology comparedto traditional software (Appendix B) - e.g., data quality, modeldrift, opacity, scale and complexity, pre-trained modeluncertainty, emergent properties, privacy aggregation, orenvironmental cost.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: HumanAiInteractionIssue Description: An issue that merits further consideration in human-AIinteraction (Appendix C) - e.g., clear human roles andresponsibilities, systemic and human-cognitive biases in design,variability of human-AI interaction outcomes, complexity ofpresenting AI system information to humans.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: PlaybookEntry Description: A single AI RMF Playbook entry - an enrichment of a Coresubcategory with prose discussion, suggested actions,documentation questions, references, and topic tags.Attribute names use the same identifiers found in the publishedNIST AI RMF Playbook JSON (e.g., `section_about`,`section_actions`) so that the data can be loaded directly.
--     * Slot: id
--     * Slot: type Description: Function label as serialised in the published Playbook JSON(Title case - "Govern", "Map", "Measure", "Manage"). Forthe controlled enum see `function_kind`.
--     * Slot: title Description: Subcategory identifier (e.g., "GOVERN 1.1"). Mirrors theAI RMF Subcategory `subcategory_id`.
--     * Slot: category Description: Category code in the form "FUNCTION-N" (e.g., "GOVERN-1")as used in the Playbook.
--     * Slot: description Description: Outcome statement of the subcategory.
--     * Slot: section_about Description: Free-text discussion ("About" section).
--     * Slot: section_actions Description: Bulleted suggested actions ("Actions" section).
--     * Slot: section_doc Description: Documentation questions and transparency resources("Documentation" section).
--     * Slot: section_ref Description: References and citations ("References" section).
--     * Slot: PlaybookCollection_id Description: Autocreated FK slot
-- # Class: PlaybookCollection Description: A container for a set of PlaybookEntry instances - theserialisation root for an AI RMF Playbook companion document.Validate with ``linkml-validate --target-class PlaybookCollection``;the canonical tree-root for the schema is ``AiRmfFramework``.
--     * Slot: id
-- # Class: AiRmfDocument Description: Publication metadata for an instance of the AI RMF (e.g., NISTAI 100-1, January 2023). The Framework is intended to be aliving document, employing a two-number versioning system (major.minor).
--     * Slot: version Description: Version identifier of the document.
--     * Slot: publisher Description: The publisher of the document (e.g., NIST).
--     * Slot: doi Description: Digital Object Identifier for the document.
--     * Slot: published_date Description: Date the document was published.
--     * Slot: source Description: Reference to the source of the element (typically the documentor section it originated from).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: AiRmfFramework Description: Root container that bundles the AI RMF Core (Functions) withfoundational concepts (trustworthiness characteristics,lifecycle, actors, risks, harms), profiles, and Frameworkattributes. Designed for serialising the Framework or a tailoredinstance of it as a single JSON / YAML document.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: document_id Description: Publication metadata of the framework instance.
-- # Class: GaiRisk Description: A risk that is novel to or exacerbated by Generative AI.Each instance corresponds to one of the 12 risk categoriesenumerated in NIST AI 600-1 Section 2.
--     * Slot: gai_risk_kind Description: The GAI risk category this element represents.
--     * Slot: risk_categorization Description: Higher-level categorisation - technical/model, misuse, orecosystem/societal.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: GaiProfile_id Description: Autocreated FK slot
-- # Class: SuggestedAction Description: A suggested action an organisation can take to manage GAIrisks. Each action is identified by an Action ID, linked to anAI RMF subcategory, and may be relevant to one or more GAIrisks and AI actor tasks (NIST AI 600-1 Section 3).
--     * Slot: action_id Description: Identifier of a Suggested Action.
--     * Slot: function_prefix Description: Two-letter function prefix of the action's subcategory.
--     * Slot: applies_to_subcategory Description: Identifier of the AI RMF subcategory the action applies to.
--     * Slot: id Description: Identifier for the action - typically the same as the`action_id` (e.g., "GV-1.1-001").
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: The suggested-action text itself.
--     * Slot: GaiProfile_id Description: Autocreated FK slot
-- # Class: PrimaryGaiConsideration Description: An overarching consideration derived from the NIST GAI PWGconsultation process (Appendix A). The `consideration_kind`attribute discriminates between the four primaryconsiderations: Governance, Pre-Deployment Testing, ContentProvenance, and Incident Disclosure.All consideration-specific attributes are optional and applyto the appropriate `consideration_kind`:  * GOVERNANCE: governance_practices, third_party_considerations  * PRE_DEPLOYMENT_TESTING: limitations_of_current_approaches  * CONTENT_PROVENANCE: provenance_techniques  * INCIDENT_DISCLOSURE: ai_incident_definition
--     * Slot: consideration_kind Description: Which primary consideration this element represents.
--     * Slot: third_party_considerations Description: Considerations for third-party GAI integrations, procurement,SBOMs, SLAs, and SSAE reports (Appendix A.1.3).
--     * Slot: limitations_of_current_approaches Description: For Pre-Deployment Testing: free-text discussion of whycurrent TEVV approaches may be inadequate (Appendix A.1.4).
--     * Slot: ai_incident_definition Description: For Incident Disclosure: the definition of AI incident usedby the organisation (Appendix A.1.8).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: GaiProfile_id Description: Autocreated FK slot
-- # Class: StructuredPublicFeedback Description: Methods used to evaluate whether GAI systems are performing asintended and to calibrate and verify traditional measurementmethods (A.1.5).
--     * Slot: feedback_method_kind Description: Which structured feedback method this element represents.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
--     * Slot: GaiProfile_id Description: Autocreated FK slot
-- # Class: AiRedTeaming Description: A structured testing exercise used to probe an AI system tofind flaws and vulnerabilities such as inaccurate, harmful, ordiscriminatory outputs, often in a controlled environment andin collaboration with system developers (A.1.5).
--     * Slot: red_team_type Description: The type of AI red-teaming exercise.
--     * Slot: feedback_method_kind Description: Which structured feedback method this element represents.
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: GaiProfile Description: Root container that bundles the NIST AI 600-1 Generative AIProfile: GAI risks (Section 2), suggested actions (Section 3),and primary considerations (Appendix A). The GAI Profile is a*cross-sectoral* AI RMF profile (Section 1).
--     * Slot: id Description: A unique identifier for an element.
--     * Slot: name Description: A short human-readable name.
--     * Slot: title Description: A human-readable title.
--     * Slot: description Description: A human-readable description.
-- # Class: NamedThing_see_also
--     * Slot: NamedThing_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiSystem_lifecycle_stage
--     * Slot: AiSystem_id Description: Autocreated FK slot
--     * Slot: lifecycle_stage Description: The AI lifecycle stage(s) the element applies to.
-- # Class: AiSystem_ai_dimension
--     * Slot: AiSystem_id Description: Autocreated FK slot
--     * Slot: ai_dimension Description: The AI system dimension the element applies to.
-- # Class: AiSystem_see_also
--     * Slot: AiSystem_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiSystemDimension_see_also
--     * Slot: AiSystemDimension_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiLifecycleStage_see_also
--     * Slot: AiLifecycleStage_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiActor_actor_task
--     * Slot: AiActor_id Description: Autocreated FK slot
--     * Slot: actor_task Description: AI actor task category.
-- # Class: AiActor_lifecycle_stage
--     * Slot: AiActor_id Description: Autocreated FK slot
--     * Slot: lifecycle_stage Description: The AI lifecycle stage(s) the element applies to.
-- # Class: AiActor_see_also
--     * Slot: AiActor_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiActorTask_typical_actors
--     * Slot: AiActorTask_id Description: Autocreated FK slot
--     * Slot: typical_actors Description: Representative actor roles that perform an AI actor task.
-- # Class: AiActorTask_lifecycle_stage
--     * Slot: AiActorTask_id Description: Autocreated FK slot
--     * Slot: lifecycle_stage Description: The AI lifecycle stage(s) the element applies to.
-- # Class: AiActorTask_ai_dimension
--     * Slot: AiActorTask_id Description: Autocreated FK slot
--     * Slot: ai_dimension Description: The AI system dimension the element applies to.
-- # Class: AiActorTask_see_also
--     * Slot: AiActorTask_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: Risk_lifecycle_stage
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: lifecycle_stage Description: The AI lifecycle stage(s) the element applies to.
-- # Class: Risk_trustworthiness_characteristic
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: trustworthiness_characteristic Description: Trustworthiness characteristic(s) the element pertains to.
-- # Class: Risk_see_also
--     * Slot: Risk_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: Impact_affects
--     * Slot: Impact_id Description: Autocreated FK slot
--     * Slot: affects_id Description: Entities (people, organizations, ecosystems) the risk or harmmay affect.
-- # Class: Impact_see_also
--     * Slot: Impact_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: Harm_affects
--     * Slot: Harm_id Description: Autocreated FK slot
--     * Slot: affects_id Description: Entities (people, organizations, ecosystems) the risk or harmmay affect.
-- # Class: Harm_see_also
--     * Slot: Harm_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: ResidualRisk_lifecycle_stage
--     * Slot: ResidualRisk_id Description: Autocreated FK slot
--     * Slot: lifecycle_stage Description: The AI lifecycle stage(s) the element applies to.
-- # Class: ResidualRisk_trustworthiness_characteristic
--     * Slot: ResidualRisk_id Description: Autocreated FK slot
--     * Slot: trustworthiness_characteristic Description: Trustworthiness characteristic(s) the element pertains to.
-- # Class: ResidualRisk_see_also
--     * Slot: ResidualRisk_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: RiskTolerance_see_also
--     * Slot: RiskTolerance_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: RiskMeasurementChallenge_see_also
--     * Slot: RiskMeasurementChallenge_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: TrustworthinessCharacteristic_see_also
--     * Slot: TrustworthinessCharacteristic_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: Bias_bias_category
--     * Slot: Bias_id Description: Autocreated FK slot
--     * Slot: bias_category Description: Category or categories of bias addressed.
-- # Class: Bias_see_also
--     * Slot: Bias_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: Function_see_also
--     * Slot: Function_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: Category_see_also
--     * Slot: Category_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: Subcategory_trustworthiness_characteristic
--     * Slot: Subcategory_id Description: Autocreated FK slot
--     * Slot: trustworthiness_characteristic Description: Trustworthiness characteristic(s) the element pertains to.
-- # Class: Subcategory_lifecycle_stage
--     * Slot: Subcategory_id Description: Autocreated FK slot
--     * Slot: lifecycle_stage Description: The AI lifecycle stage(s) the element applies to.
-- # Class: Subcategory_topics
--     * Slot: Subcategory_id Description: Autocreated FK slot
--     * Slot: topics Description: Free-text topic tags applied to a playbook entry (e.g.,"Governance", "Trustworthy Characteristics", "Validity andReliability").
-- # Class: Subcategory_ai_actor_categories
--     * Slot: Subcategory_id Description: Autocreated FK slot
--     * Slot: ai_actor_categories Description: Free-text list of AI Actor categories the entry applies to,preserving the original case used in the AI RMF Playbook(e.g., "Governance and Oversight", "TEVV"). For controlledenum values see `actor_task` (range AiActorTaskEnum).
-- # Class: Subcategory_see_also
--     * Slot: Subcategory_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiRmfProfile_addresses
--     * Slot: AiRmfProfile_id Description: Autocreated FK slot
--     * Slot: addresses_id Description: Subcategories that a profile implements or addresses.
-- # Class: AiRmfProfile_see_also
--     * Slot: AiRmfProfile_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: RmfAttribute_see_also
--     * Slot: RmfAttribute_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiSpecificRisk_see_also
--     * Slot: AiSpecificRisk_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: HumanAiInteractionIssue_see_also
--     * Slot: HumanAiInteractionIssue_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: PlaybookEntry_ai_actors
--     * Slot: PlaybookEntry_id Description: Autocreated FK slot
--     * Slot: ai_actors Description: AI actor categories the entry applies to. Free-text topreserve the casing of the source data (e.g., "Governanceand Oversight").
-- # Class: PlaybookEntry_topic
--     * Slot: PlaybookEntry_id Description: Autocreated FK slot
--     * Slot: topic Description: Topic tags (e.g., "Legal and Regulatory", "Validity andReliability").
-- # Class: AiRmfDocument_see_also
--     * Slot: AiRmfDocument_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiRmfFramework_see_also
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: GaiRisk_risk_scope
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: risk_scope Description: Scope levels at which the risk may manifest.
-- # Class: GaiRisk_risk_sources
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: risk_sources Description: Sources from which the risk may emerge.
-- # Class: GaiRisk_time_scale
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: time_scale Description: Time scales over which the risk may materialise.
-- # Class: GaiRisk_trustworthiness_characteristic
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: trustworthiness_characteristic Description: Trustworthiness characteristic(s) the element pertains to.
-- # Class: GaiRisk_addressed_by_actions
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: addressed_by_actions_id Description: Suggested actions that address a GAI risk (back-referencederived from `SuggestedAction.gai_risks`).
-- # Class: GaiRisk_lifecycle_stage
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: lifecycle_stage Description: AI lifecycle stage(s) at which the GAI risk may arise(NIST AI 600-1 Section 2). Uses the GAI five-stagelifecycle (`GaiLifecycleStageEnum`).
-- # Class: GaiRisk_see_also
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: SuggestedAction_gai_risks
--     * Slot: SuggestedAction_id Description: Autocreated FK slot
--     * Slot: gai_risks Description: GAI risk categories addressed by a suggested action orconsidered by a primary consideration.
-- # Class: SuggestedAction_actor_task
--     * Slot: SuggestedAction_id Description: Autocreated FK slot
--     * Slot: actor_task Description: Pertinent AI Actor Task(s) for the suggested action - i.e.,the "AI Actor Tasks" row at the bottom of each Section 3table.
-- # Class: SuggestedAction_see_also
--     * Slot: SuggestedAction_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: PrimaryGaiConsideration_governance_practices
--     * Slot: PrimaryGaiConsideration_id Description: Autocreated FK slot
--     * Slot: governance_practices Description: Governance plans and actions enumerated in NIST AI 600-1Appendix A.1.2 (Organizational Governance).
-- # Class: PrimaryGaiConsideration_provenance_techniques
--     * Slot: PrimaryGaiConsideration_id Description: Autocreated FK slot
--     * Slot: provenance_techniques Description: For Content Provenance: provenance data tracking techniquessuch as digital watermarking, metadata recording, digitalfingerprinting, and human authentication (Appendix A.1.6).
-- # Class: PrimaryGaiConsideration_see_also
--     * Slot: PrimaryGaiConsideration_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: StructuredPublicFeedback_see_also
--     * Slot: StructuredPublicFeedback_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: AiRedTeaming_see_also
--     * Slot: AiRedTeaming_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.
-- # Class: GaiProfile_see_also
--     * Slot: GaiProfile_id Description: Autocreated FK slot
--     * Slot: see_also Description: Related references.

CREATE TABLE "NamedThing" (
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_NamedThing_id" ON "NamedThing" (id);

CREATE TABLE "AiSystem" (
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AiSystem_id" ON "AiSystem" (id);

CREATE TABLE "AiActor" (
	is_tevv BOOLEAN,
	audience VARCHAR(9),
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AiActor_id" ON "AiActor" (id);

CREATE TABLE "Harm" (
	harm_category VARCHAR(23),
	harm_to_people_subcategory VARCHAR(18),
	magnitude TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Harm_id" ON "Harm" (id);

CREATE TABLE "RiskTolerance" (
	tolerance_statement TEXT,
	legal_basis TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_RiskTolerance_id" ON "RiskTolerance" (id);

CREATE TABLE "Bias" (
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_Bias_id" ON "Bias" (id);

CREATE TABLE "PlaybookCollection" (
	id INTEGER NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_PlaybookCollection_id" ON "PlaybookCollection" (id);

CREATE TABLE "AiRmfDocument" (
	version TEXT,
	publisher TEXT,
	doi TEXT,
	published_date DATE,
	source TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AiRmfDocument_id" ON "AiRmfDocument" (id);

CREATE TABLE "AiRedTeaming" (
	red_team_type VARCHAR(14),
	feedback_method_kind VARCHAR(32) NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AiRedTeaming_id" ON "AiRedTeaming" (id);

CREATE TABLE "GaiProfile" (
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiProfile_id" ON "GaiProfile" (id);

CREATE TABLE "Risk" (
	likelihood FLOAT,
	magnitude TEXT,
	impact_sign VARCHAR(8),
	is_residual BOOLEAN,
	risk_response VARCHAR(12),
	affects_system TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(affects_system) REFERENCES "AiSystem" (id)
);
CREATE INDEX "ix_Risk_id" ON "Risk" (id);

CREATE TABLE "ResidualRisk" (
	likelihood FLOAT,
	magnitude TEXT,
	impact_sign VARCHAR(8),
	is_residual BOOLEAN,
	risk_response VARCHAR(12),
	affects_system TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(affects_system) REFERENCES "AiSystem" (id)
);
CREATE INDEX "ix_ResidualRisk_id" ON "ResidualRisk" (id);

CREATE TABLE "PlaybookEntry" (
	id INTEGER NOT NULL,
	type TEXT,
	title TEXT,
	category TEXT,
	description TEXT,
	section_about TEXT,
	section_actions TEXT,
	section_doc TEXT,
	section_ref TEXT,
	"PlaybookCollection_id" INTEGER,
	PRIMARY KEY (id),
	UNIQUE (title),
	FOREIGN KEY("PlaybookCollection_id") REFERENCES "PlaybookCollection" (id)
);
CREATE INDEX "ix_PlaybookEntry_id" ON "PlaybookEntry" (id);
CREATE INDEX "PlaybookEntry_title_idx" ON "PlaybookEntry" (title);

CREATE TABLE "AiRmfFramework" (
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	document_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(document_id) REFERENCES "AiRmfDocument" (id)
);
CREATE INDEX "ix_AiRmfFramework_id" ON "AiRmfFramework" (id);

CREATE TABLE "GaiRisk" (
	gai_risk_kind VARCHAR(37),
	risk_categorization VARCHAR(27),
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"GaiProfile_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_GaiRisk_id" ON "GaiRisk" (id);

CREATE TABLE "SuggestedAction" (
	action_id TEXT NOT NULL,
	function_prefix VARCHAR(2),
	applies_to_subcategory TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"GaiProfile_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_SuggestedAction_id" ON "SuggestedAction" (id);

CREATE TABLE "PrimaryGaiConsideration" (
	consideration_kind VARCHAR(22) NOT NULL,
	third_party_considerations TEXT,
	limitations_of_current_approaches TEXT,
	ai_incident_definition TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"GaiProfile_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_PrimaryGaiConsideration_id" ON "PrimaryGaiConsideration" (id);

CREATE TABLE "StructuredPublicFeedback" (
	feedback_method_kind VARCHAR(32) NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"GaiProfile_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_StructuredPublicFeedback_id" ON "StructuredPublicFeedback" (id);

CREATE TABLE "NamedThing_see_also" (
	"NamedThing_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("NamedThing_id", see_also),
	FOREIGN KEY("NamedThing_id") REFERENCES "NamedThing" (id)
);
CREATE INDEX "ix_NamedThing_see_also_NamedThing_id" ON "NamedThing_see_also" ("NamedThing_id");
CREATE INDEX "ix_NamedThing_see_also_see_also" ON "NamedThing_see_also" (see_also);

CREATE TABLE "AiSystem_lifecycle_stage" (
	"AiSystem_id" TEXT,
	lifecycle_stage VARCHAR(24),
	PRIMARY KEY ("AiSystem_id", lifecycle_stage),
	FOREIGN KEY("AiSystem_id") REFERENCES "AiSystem" (id)
);
CREATE INDEX "ix_AiSystem_lifecycle_stage_AiSystem_id" ON "AiSystem_lifecycle_stage" ("AiSystem_id");
CREATE INDEX "ix_AiSystem_lifecycle_stage_lifecycle_stage" ON "AiSystem_lifecycle_stage" (lifecycle_stage);

CREATE TABLE "AiSystem_ai_dimension" (
	"AiSystem_id" TEXT,
	ai_dimension VARCHAR(19),
	PRIMARY KEY ("AiSystem_id", ai_dimension),
	FOREIGN KEY("AiSystem_id") REFERENCES "AiSystem" (id)
);
CREATE INDEX "ix_AiSystem_ai_dimension_ai_dimension" ON "AiSystem_ai_dimension" (ai_dimension);
CREATE INDEX "ix_AiSystem_ai_dimension_AiSystem_id" ON "AiSystem_ai_dimension" ("AiSystem_id");

CREATE TABLE "AiSystem_see_also" (
	"AiSystem_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiSystem_id", see_also),
	FOREIGN KEY("AiSystem_id") REFERENCES "AiSystem" (id)
);
CREATE INDEX "ix_AiSystem_see_also_AiSystem_id" ON "AiSystem_see_also" ("AiSystem_id");
CREATE INDEX "ix_AiSystem_see_also_see_also" ON "AiSystem_see_also" (see_also);

CREATE TABLE "AiActor_actor_task" (
	"AiActor_id" TEXT,
	actor_task VARCHAR(35),
	PRIMARY KEY ("AiActor_id", actor_task),
	FOREIGN KEY("AiActor_id") REFERENCES "AiActor" (id)
);
CREATE INDEX "ix_AiActor_actor_task_AiActor_id" ON "AiActor_actor_task" ("AiActor_id");
CREATE INDEX "ix_AiActor_actor_task_actor_task" ON "AiActor_actor_task" (actor_task);

CREATE TABLE "AiActor_lifecycle_stage" (
	"AiActor_id" TEXT,
	lifecycle_stage VARCHAR(24),
	PRIMARY KEY ("AiActor_id", lifecycle_stage),
	FOREIGN KEY("AiActor_id") REFERENCES "AiActor" (id)
);
CREATE INDEX "ix_AiActor_lifecycle_stage_AiActor_id" ON "AiActor_lifecycle_stage" ("AiActor_id");
CREATE INDEX "ix_AiActor_lifecycle_stage_lifecycle_stage" ON "AiActor_lifecycle_stage" (lifecycle_stage);

CREATE TABLE "AiActor_see_also" (
	"AiActor_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiActor_id", see_also),
	FOREIGN KEY("AiActor_id") REFERENCES "AiActor" (id)
);
CREATE INDEX "ix_AiActor_see_also_AiActor_id" ON "AiActor_see_also" ("AiActor_id");
CREATE INDEX "ix_AiActor_see_also_see_also" ON "AiActor_see_also" (see_also);

CREATE TABLE "Harm_affects" (
	"Harm_id" TEXT,
	affects_id TEXT,
	PRIMARY KEY ("Harm_id", affects_id),
	FOREIGN KEY("Harm_id") REFERENCES "Harm" (id),
	FOREIGN KEY(affects_id) REFERENCES "NamedThing" (id)
);
CREATE INDEX "ix_Harm_affects_affects_id" ON "Harm_affects" (affects_id);
CREATE INDEX "ix_Harm_affects_Harm_id" ON "Harm_affects" ("Harm_id");

CREATE TABLE "Harm_see_also" (
	"Harm_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("Harm_id", see_also),
	FOREIGN KEY("Harm_id") REFERENCES "Harm" (id)
);
CREATE INDEX "ix_Harm_see_also_Harm_id" ON "Harm_see_also" ("Harm_id");
CREATE INDEX "ix_Harm_see_also_see_also" ON "Harm_see_also" (see_also);

CREATE TABLE "RiskTolerance_see_also" (
	"RiskTolerance_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("RiskTolerance_id", see_also),
	FOREIGN KEY("RiskTolerance_id") REFERENCES "RiskTolerance" (id)
);
CREATE INDEX "ix_RiskTolerance_see_also_RiskTolerance_id" ON "RiskTolerance_see_also" ("RiskTolerance_id");
CREATE INDEX "ix_RiskTolerance_see_also_see_also" ON "RiskTolerance_see_also" (see_also);

CREATE TABLE "Bias_bias_category" (
	"Bias_id" TEXT,
	bias_category VARCHAR(29),
	PRIMARY KEY ("Bias_id", bias_category),
	FOREIGN KEY("Bias_id") REFERENCES "Bias" (id)
);
CREATE INDEX "ix_Bias_bias_category_Bias_id" ON "Bias_bias_category" ("Bias_id");
CREATE INDEX "ix_Bias_bias_category_bias_category" ON "Bias_bias_category" (bias_category);

CREATE TABLE "Bias_see_also" (
	"Bias_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("Bias_id", see_also),
	FOREIGN KEY("Bias_id") REFERENCES "Bias" (id)
);
CREATE INDEX "ix_Bias_see_also_see_also" ON "Bias_see_also" (see_also);
CREATE INDEX "ix_Bias_see_also_Bias_id" ON "Bias_see_also" ("Bias_id");

CREATE TABLE "AiRmfDocument_see_also" (
	"AiRmfDocument_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiRmfDocument_id", see_also),
	FOREIGN KEY("AiRmfDocument_id") REFERENCES "AiRmfDocument" (id)
);
CREATE INDEX "ix_AiRmfDocument_see_also_AiRmfDocument_id" ON "AiRmfDocument_see_also" ("AiRmfDocument_id");
CREATE INDEX "ix_AiRmfDocument_see_also_see_also" ON "AiRmfDocument_see_also" (see_also);

CREATE TABLE "AiRedTeaming_see_also" (
	"AiRedTeaming_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiRedTeaming_id", see_also),
	FOREIGN KEY("AiRedTeaming_id") REFERENCES "AiRedTeaming" (id)
);
CREATE INDEX "ix_AiRedTeaming_see_also_AiRedTeaming_id" ON "AiRedTeaming_see_also" ("AiRedTeaming_id");
CREATE INDEX "ix_AiRedTeaming_see_also_see_also" ON "AiRedTeaming_see_also" (see_also);

CREATE TABLE "GaiProfile_see_also" (
	"GaiProfile_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("GaiProfile_id", see_also),
	FOREIGN KEY("GaiProfile_id") REFERENCES "GaiProfile" (id)
);
CREATE INDEX "ix_GaiProfile_see_also_GaiProfile_id" ON "GaiProfile_see_also" ("GaiProfile_id");
CREATE INDEX "ix_GaiProfile_see_also_see_also" ON "GaiProfile_see_also" (see_also);

CREATE TABLE "AiSystemDimension" (
	dimension_kind VARCHAR(19) NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiSystemDimension_id" ON "AiSystemDimension" (id);

CREATE TABLE "AiLifecycleStage" (
	stage_kind VARCHAR(24) NOT NULL,
	includes_tevv BOOLEAN,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiLifecycleStage_id" ON "AiLifecycleStage" (id);

CREATE TABLE "AiActorTask" (
	task_kind VARCHAR(35) NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiActorTask_id" ON "AiActorTask" (id);

CREATE TABLE "Impact" (
	impact_sign VARCHAR(8),
	magnitude TEXT,
	likelihood FLOAT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"Risk_id" TEXT,
	"ResidualRisk_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id),
	FOREIGN KEY("ResidualRisk_id") REFERENCES "ResidualRisk" (id)
);
CREATE INDEX "ix_Impact_id" ON "Impact" (id);

CREATE TABLE "RiskMeasurementChallenge" (
	challenge_kind VARCHAR(38) NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_RiskMeasurementChallenge_id" ON "RiskMeasurementChallenge" (id);

CREATE TABLE "TrustworthinessCharacteristic" (
	characteristic_kind VARCHAR(30) NOT NULL,
	is_base_condition BOOLEAN,
	is_cross_cutting BOOLEAN,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_TrustworthinessCharacteristic_id" ON "TrustworthinessCharacteristic" (id);

CREATE TABLE "Function" (
	function_code TEXT NOT NULL,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_Function_id" ON "Function" (id);

CREATE TABLE "AiRmfProfile" (
	profile_type VARCHAR(16) NOT NULL,
	current_state TEXT,
	target_state TEXT,
	sector TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfProfile_id" ON "AiRmfProfile" (id);

CREATE TABLE "RmfAttribute" (
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_RmfAttribute_id" ON "RmfAttribute" (id);

CREATE TABLE "AiSpecificRisk" (
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiSpecificRisk_id" ON "AiSpecificRisk" (id);

CREATE TABLE "HumanAiInteractionIssue" (
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"AiRmfFramework_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_HumanAiInteractionIssue_id" ON "HumanAiInteractionIssue" (id);

CREATE TABLE "Risk_lifecycle_stage" (
	"Risk_id" TEXT,
	lifecycle_stage VARCHAR(24),
	PRIMARY KEY ("Risk_id", lifecycle_stage),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id)
);
CREATE INDEX "ix_Risk_lifecycle_stage_Risk_id" ON "Risk_lifecycle_stage" ("Risk_id");
CREATE INDEX "ix_Risk_lifecycle_stage_lifecycle_stage" ON "Risk_lifecycle_stage" (lifecycle_stage);

CREATE TABLE "Risk_trustworthiness_characteristic" (
	"Risk_id" TEXT,
	trustworthiness_characteristic VARCHAR(30),
	PRIMARY KEY ("Risk_id", trustworthiness_characteristic),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id)
);
CREATE INDEX "ix_Risk_trustworthiness_characteristic_Risk_id" ON "Risk_trustworthiness_characteristic" ("Risk_id");
CREATE INDEX "ix_Risk_trustworthiness_characteristic_trustworthiness_characteristic" ON "Risk_trustworthiness_characteristic" (trustworthiness_characteristic);

CREATE TABLE "Risk_see_also" (
	"Risk_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("Risk_id", see_also),
	FOREIGN KEY("Risk_id") REFERENCES "Risk" (id)
);
CREATE INDEX "ix_Risk_see_also_see_also" ON "Risk_see_also" (see_also);
CREATE INDEX "ix_Risk_see_also_Risk_id" ON "Risk_see_also" ("Risk_id");

CREATE TABLE "ResidualRisk_lifecycle_stage" (
	"ResidualRisk_id" TEXT,
	lifecycle_stage VARCHAR(24),
	PRIMARY KEY ("ResidualRisk_id", lifecycle_stage),
	FOREIGN KEY("ResidualRisk_id") REFERENCES "ResidualRisk" (id)
);
CREATE INDEX "ix_ResidualRisk_lifecycle_stage_ResidualRisk_id" ON "ResidualRisk_lifecycle_stage" ("ResidualRisk_id");
CREATE INDEX "ix_ResidualRisk_lifecycle_stage_lifecycle_stage" ON "ResidualRisk_lifecycle_stage" (lifecycle_stage);

CREATE TABLE "ResidualRisk_trustworthiness_characteristic" (
	"ResidualRisk_id" TEXT,
	trustworthiness_characteristic VARCHAR(30),
	PRIMARY KEY ("ResidualRisk_id", trustworthiness_characteristic),
	FOREIGN KEY("ResidualRisk_id") REFERENCES "ResidualRisk" (id)
);
CREATE INDEX "ix_ResidualRisk_trustworthiness_characteristic_ResidualRisk_id" ON "ResidualRisk_trustworthiness_characteristic" ("ResidualRisk_id");
CREATE INDEX "ix_ResidualRisk_trustworthiness_characteristic_trustworthiness_characteristic" ON "ResidualRisk_trustworthiness_characteristic" (trustworthiness_characteristic);

CREATE TABLE "ResidualRisk_see_also" (
	"ResidualRisk_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("ResidualRisk_id", see_also),
	FOREIGN KEY("ResidualRisk_id") REFERENCES "ResidualRisk" (id)
);
CREATE INDEX "ix_ResidualRisk_see_also_ResidualRisk_id" ON "ResidualRisk_see_also" ("ResidualRisk_id");
CREATE INDEX "ix_ResidualRisk_see_also_see_also" ON "ResidualRisk_see_also" (see_also);

CREATE TABLE "PlaybookEntry_ai_actors" (
	"PlaybookEntry_id" INTEGER,
	ai_actors TEXT,
	PRIMARY KEY ("PlaybookEntry_id", ai_actors),
	FOREIGN KEY("PlaybookEntry_id") REFERENCES "PlaybookEntry" (id)
);
CREATE INDEX "ix_PlaybookEntry_ai_actors_PlaybookEntry_id" ON "PlaybookEntry_ai_actors" ("PlaybookEntry_id");
CREATE INDEX "ix_PlaybookEntry_ai_actors_ai_actors" ON "PlaybookEntry_ai_actors" (ai_actors);

CREATE TABLE "PlaybookEntry_topic" (
	"PlaybookEntry_id" INTEGER,
	topic TEXT,
	PRIMARY KEY ("PlaybookEntry_id", topic),
	FOREIGN KEY("PlaybookEntry_id") REFERENCES "PlaybookEntry" (id)
);
CREATE INDEX "ix_PlaybookEntry_topic_topic" ON "PlaybookEntry_topic" (topic);
CREATE INDEX "ix_PlaybookEntry_topic_PlaybookEntry_id" ON "PlaybookEntry_topic" ("PlaybookEntry_id");

CREATE TABLE "AiRmfFramework_see_also" (
	"AiRmfFramework_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiRmfFramework_id", see_also),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfFramework_see_also_AiRmfFramework_id" ON "AiRmfFramework_see_also" ("AiRmfFramework_id");
CREATE INDEX "ix_AiRmfFramework_see_also_see_also" ON "AiRmfFramework_see_also" (see_also);

CREATE TABLE "GaiRisk_risk_scope" (
	"GaiRisk_id" TEXT,
	risk_scope VARCHAR(29),
	PRIMARY KEY ("GaiRisk_id", risk_scope),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_risk_scope_GaiRisk_id" ON "GaiRisk_risk_scope" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_risk_scope_risk_scope" ON "GaiRisk_risk_scope" (risk_scope);

CREATE TABLE "GaiRisk_risk_sources" (
	"GaiRisk_id" TEXT,
	risk_sources VARCHAR(20),
	PRIMARY KEY ("GaiRisk_id", risk_sources),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_risk_sources_GaiRisk_id" ON "GaiRisk_risk_sources" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_risk_sources_risk_sources" ON "GaiRisk_risk_sources" (risk_sources);

CREATE TABLE "GaiRisk_time_scale" (
	"GaiRisk_id" TEXT,
	time_scale VARCHAR(9),
	PRIMARY KEY ("GaiRisk_id", time_scale),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_time_scale_GaiRisk_id" ON "GaiRisk_time_scale" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_time_scale_time_scale" ON "GaiRisk_time_scale" (time_scale);

CREATE TABLE "GaiRisk_trustworthiness_characteristic" (
	"GaiRisk_id" TEXT,
	trustworthiness_characteristic VARCHAR(30),
	PRIMARY KEY ("GaiRisk_id", trustworthiness_characteristic),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_trustworthiness_characteristic_GaiRisk_id" ON "GaiRisk_trustworthiness_characteristic" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_trustworthiness_characteristic_trustworthiness_characteristic" ON "GaiRisk_trustworthiness_characteristic" (trustworthiness_characteristic);

CREATE TABLE "GaiRisk_addressed_by_actions" (
	"GaiRisk_id" TEXT,
	addressed_by_actions_id TEXT,
	PRIMARY KEY ("GaiRisk_id", addressed_by_actions_id),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id),
	FOREIGN KEY(addressed_by_actions_id) REFERENCES "SuggestedAction" (id)
);
CREATE INDEX "ix_GaiRisk_addressed_by_actions_GaiRisk_id" ON "GaiRisk_addressed_by_actions" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_addressed_by_actions_addressed_by_actions_id" ON "GaiRisk_addressed_by_actions" (addressed_by_actions_id);

CREATE TABLE "GaiRisk_lifecycle_stage" (
	"GaiRisk_id" TEXT,
	lifecycle_stage VARCHAR(15),
	PRIMARY KEY ("GaiRisk_id", lifecycle_stage),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_lifecycle_stage_GaiRisk_id" ON "GaiRisk_lifecycle_stage" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_lifecycle_stage_lifecycle_stage" ON "GaiRisk_lifecycle_stage" (lifecycle_stage);

CREATE TABLE "GaiRisk_see_also" (
	"GaiRisk_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("GaiRisk_id", see_also),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_see_also_GaiRisk_id" ON "GaiRisk_see_also" ("GaiRisk_id");
CREATE INDEX "ix_GaiRisk_see_also_see_also" ON "GaiRisk_see_also" (see_also);

CREATE TABLE "SuggestedAction_gai_risks" (
	"SuggestedAction_id" TEXT,
	gai_risks VARCHAR(37),
	PRIMARY KEY ("SuggestedAction_id", gai_risks),
	FOREIGN KEY("SuggestedAction_id") REFERENCES "SuggestedAction" (id)
);
CREATE INDEX "ix_SuggestedAction_gai_risks_SuggestedAction_id" ON "SuggestedAction_gai_risks" ("SuggestedAction_id");
CREATE INDEX "ix_SuggestedAction_gai_risks_gai_risks" ON "SuggestedAction_gai_risks" (gai_risks);

CREATE TABLE "SuggestedAction_actor_task" (
	"SuggestedAction_id" TEXT,
	actor_task VARCHAR(36),
	PRIMARY KEY ("SuggestedAction_id", actor_task),
	FOREIGN KEY("SuggestedAction_id") REFERENCES "SuggestedAction" (id)
);
CREATE INDEX "ix_SuggestedAction_actor_task_actor_task" ON "SuggestedAction_actor_task" (actor_task);
CREATE INDEX "ix_SuggestedAction_actor_task_SuggestedAction_id" ON "SuggestedAction_actor_task" ("SuggestedAction_id");

CREATE TABLE "SuggestedAction_see_also" (
	"SuggestedAction_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("SuggestedAction_id", see_also),
	FOREIGN KEY("SuggestedAction_id") REFERENCES "SuggestedAction" (id)
);
CREATE INDEX "ix_SuggestedAction_see_also_see_also" ON "SuggestedAction_see_also" (see_also);
CREATE INDEX "ix_SuggestedAction_see_also_SuggestedAction_id" ON "SuggestedAction_see_also" ("SuggestedAction_id");

CREATE TABLE "PrimaryGaiConsideration_governance_practices" (
	"PrimaryGaiConsideration_id" TEXT,
	governance_practices VARCHAR(47),
	PRIMARY KEY ("PrimaryGaiConsideration_id", governance_practices),
	FOREIGN KEY("PrimaryGaiConsideration_id") REFERENCES "PrimaryGaiConsideration" (id)
);
CREATE INDEX "ix_PrimaryGaiConsideration_governance_practices_governance_practices" ON "PrimaryGaiConsideration_governance_practices" (governance_practices);
CREATE INDEX "ix_PrimaryGaiConsideration_governance_practices_PrimaryGaiConsideration_id" ON "PrimaryGaiConsideration_governance_practices" ("PrimaryGaiConsideration_id");

CREATE TABLE "PrimaryGaiConsideration_provenance_techniques" (
	"PrimaryGaiConsideration_id" TEXT,
	provenance_techniques VARCHAR(22),
	PRIMARY KEY ("PrimaryGaiConsideration_id", provenance_techniques),
	FOREIGN KEY("PrimaryGaiConsideration_id") REFERENCES "PrimaryGaiConsideration" (id)
);
CREATE INDEX "ix_PrimaryGaiConsideration_provenance_techniques_provenance_techniques" ON "PrimaryGaiConsideration_provenance_techniques" (provenance_techniques);
CREATE INDEX "ix_PrimaryGaiConsideration_provenance_techniques_PrimaryGaiConsideration_id" ON "PrimaryGaiConsideration_provenance_techniques" ("PrimaryGaiConsideration_id");

CREATE TABLE "PrimaryGaiConsideration_see_also" (
	"PrimaryGaiConsideration_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("PrimaryGaiConsideration_id", see_also),
	FOREIGN KEY("PrimaryGaiConsideration_id") REFERENCES "PrimaryGaiConsideration" (id)
);
CREATE INDEX "ix_PrimaryGaiConsideration_see_also_see_also" ON "PrimaryGaiConsideration_see_also" (see_also);
CREATE INDEX "ix_PrimaryGaiConsideration_see_also_PrimaryGaiConsideration_id" ON "PrimaryGaiConsideration_see_also" ("PrimaryGaiConsideration_id");

CREATE TABLE "StructuredPublicFeedback_see_also" (
	"StructuredPublicFeedback_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("StructuredPublicFeedback_id", see_also),
	FOREIGN KEY("StructuredPublicFeedback_id") REFERENCES "StructuredPublicFeedback" (id)
);
CREATE INDEX "ix_StructuredPublicFeedback_see_also_see_also" ON "StructuredPublicFeedback_see_also" (see_also);
CREATE INDEX "ix_StructuredPublicFeedback_see_also_StructuredPublicFeedback_id" ON "StructuredPublicFeedback_see_also" ("StructuredPublicFeedback_id");

CREATE TABLE "Category" (
	category_id TEXT,
	outcome TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"Function_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Function_id") REFERENCES "Function" (id)
);
CREATE INDEX "ix_Category_id" ON "Category" (id);

CREATE TABLE "AiSystemDimension_see_also" (
	"AiSystemDimension_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiSystemDimension_id", see_also),
	FOREIGN KEY("AiSystemDimension_id") REFERENCES "AiSystemDimension" (id)
);
CREATE INDEX "ix_AiSystemDimension_see_also_AiSystemDimension_id" ON "AiSystemDimension_see_also" ("AiSystemDimension_id");
CREATE INDEX "ix_AiSystemDimension_see_also_see_also" ON "AiSystemDimension_see_also" (see_also);

CREATE TABLE "AiLifecycleStage_see_also" (
	"AiLifecycleStage_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiLifecycleStage_id", see_also),
	FOREIGN KEY("AiLifecycleStage_id") REFERENCES "AiLifecycleStage" (id)
);
CREATE INDEX "ix_AiLifecycleStage_see_also_AiLifecycleStage_id" ON "AiLifecycleStage_see_also" ("AiLifecycleStage_id");
CREATE INDEX "ix_AiLifecycleStage_see_also_see_also" ON "AiLifecycleStage_see_also" (see_also);

CREATE TABLE "AiActorTask_typical_actors" (
	"AiActorTask_id" TEXT,
	typical_actors TEXT,
	PRIMARY KEY ("AiActorTask_id", typical_actors),
	FOREIGN KEY("AiActorTask_id") REFERENCES "AiActorTask" (id)
);
CREATE INDEX "ix_AiActorTask_typical_actors_AiActorTask_id" ON "AiActorTask_typical_actors" ("AiActorTask_id");
CREATE INDEX "ix_AiActorTask_typical_actors_typical_actors" ON "AiActorTask_typical_actors" (typical_actors);

CREATE TABLE "AiActorTask_lifecycle_stage" (
	"AiActorTask_id" TEXT,
	lifecycle_stage VARCHAR(24),
	PRIMARY KEY ("AiActorTask_id", lifecycle_stage),
	FOREIGN KEY("AiActorTask_id") REFERENCES "AiActorTask" (id)
);
CREATE INDEX "ix_AiActorTask_lifecycle_stage_lifecycle_stage" ON "AiActorTask_lifecycle_stage" (lifecycle_stage);
CREATE INDEX "ix_AiActorTask_lifecycle_stage_AiActorTask_id" ON "AiActorTask_lifecycle_stage" ("AiActorTask_id");

CREATE TABLE "AiActorTask_ai_dimension" (
	"AiActorTask_id" TEXT,
	ai_dimension VARCHAR(19),
	PRIMARY KEY ("AiActorTask_id", ai_dimension),
	FOREIGN KEY("AiActorTask_id") REFERENCES "AiActorTask" (id)
);
CREATE INDEX "ix_AiActorTask_ai_dimension_ai_dimension" ON "AiActorTask_ai_dimension" (ai_dimension);
CREATE INDEX "ix_AiActorTask_ai_dimension_AiActorTask_id" ON "AiActorTask_ai_dimension" ("AiActorTask_id");

CREATE TABLE "AiActorTask_see_also" (
	"AiActorTask_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiActorTask_id", see_also),
	FOREIGN KEY("AiActorTask_id") REFERENCES "AiActorTask" (id)
);
CREATE INDEX "ix_AiActorTask_see_also_see_also" ON "AiActorTask_see_also" (see_also);
CREATE INDEX "ix_AiActorTask_see_also_AiActorTask_id" ON "AiActorTask_see_also" ("AiActorTask_id");

CREATE TABLE "Impact_affects" (
	"Impact_id" TEXT,
	affects_id TEXT,
	PRIMARY KEY ("Impact_id", affects_id),
	FOREIGN KEY("Impact_id") REFERENCES "Impact" (id),
	FOREIGN KEY(affects_id) REFERENCES "NamedThing" (id)
);
CREATE INDEX "ix_Impact_affects_affects_id" ON "Impact_affects" (affects_id);
CREATE INDEX "ix_Impact_affects_Impact_id" ON "Impact_affects" ("Impact_id");

CREATE TABLE "Impact_see_also" (
	"Impact_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("Impact_id", see_also),
	FOREIGN KEY("Impact_id") REFERENCES "Impact" (id)
);
CREATE INDEX "ix_Impact_see_also_Impact_id" ON "Impact_see_also" ("Impact_id");
CREATE INDEX "ix_Impact_see_also_see_also" ON "Impact_see_also" (see_also);

CREATE TABLE "RiskMeasurementChallenge_see_also" (
	"RiskMeasurementChallenge_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("RiskMeasurementChallenge_id", see_also),
	FOREIGN KEY("RiskMeasurementChallenge_id") REFERENCES "RiskMeasurementChallenge" (id)
);
CREATE INDEX "ix_RiskMeasurementChallenge_see_also_RiskMeasurementChallenge_id" ON "RiskMeasurementChallenge_see_also" ("RiskMeasurementChallenge_id");
CREATE INDEX "ix_RiskMeasurementChallenge_see_also_see_also" ON "RiskMeasurementChallenge_see_also" (see_also);

CREATE TABLE "TrustworthinessCharacteristic_see_also" (
	"TrustworthinessCharacteristic_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("TrustworthinessCharacteristic_id", see_also),
	FOREIGN KEY("TrustworthinessCharacteristic_id") REFERENCES "TrustworthinessCharacteristic" (id)
);
CREATE INDEX "ix_TrustworthinessCharacteristic_see_also_see_also" ON "TrustworthinessCharacteristic_see_also" (see_also);
CREATE INDEX "ix_TrustworthinessCharacteristic_see_also_TrustworthinessCharacteristic_id" ON "TrustworthinessCharacteristic_see_also" ("TrustworthinessCharacteristic_id");

CREATE TABLE "Function_see_also" (
	"Function_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("Function_id", see_also),
	FOREIGN KEY("Function_id") REFERENCES "Function" (id)
);
CREATE INDEX "ix_Function_see_also_Function_id" ON "Function_see_also" ("Function_id");
CREATE INDEX "ix_Function_see_also_see_also" ON "Function_see_also" (see_also);

CREATE TABLE "AiRmfProfile_see_also" (
	"AiRmfProfile_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiRmfProfile_id", see_also),
	FOREIGN KEY("AiRmfProfile_id") REFERENCES "AiRmfProfile" (id)
);
CREATE INDEX "ix_AiRmfProfile_see_also_see_also" ON "AiRmfProfile_see_also" (see_also);
CREATE INDEX "ix_AiRmfProfile_see_also_AiRmfProfile_id" ON "AiRmfProfile_see_also" ("AiRmfProfile_id");

CREATE TABLE "RmfAttribute_see_also" (
	"RmfAttribute_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("RmfAttribute_id", see_also),
	FOREIGN KEY("RmfAttribute_id") REFERENCES "RmfAttribute" (id)
);
CREATE INDEX "ix_RmfAttribute_see_also_see_also" ON "RmfAttribute_see_also" (see_also);
CREATE INDEX "ix_RmfAttribute_see_also_RmfAttribute_id" ON "RmfAttribute_see_also" ("RmfAttribute_id");

CREATE TABLE "AiSpecificRisk_see_also" (
	"AiSpecificRisk_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("AiSpecificRisk_id", see_also),
	FOREIGN KEY("AiSpecificRisk_id") REFERENCES "AiSpecificRisk" (id)
);
CREATE INDEX "ix_AiSpecificRisk_see_also_AiSpecificRisk_id" ON "AiSpecificRisk_see_also" ("AiSpecificRisk_id");
CREATE INDEX "ix_AiSpecificRisk_see_also_see_also" ON "AiSpecificRisk_see_also" (see_also);

CREATE TABLE "HumanAiInteractionIssue_see_also" (
	"HumanAiInteractionIssue_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("HumanAiInteractionIssue_id", see_also),
	FOREIGN KEY("HumanAiInteractionIssue_id") REFERENCES "HumanAiInteractionIssue" (id)
);
CREATE INDEX "ix_HumanAiInteractionIssue_see_also_HumanAiInteractionIssue_id" ON "HumanAiInteractionIssue_see_also" ("HumanAiInteractionIssue_id");
CREATE INDEX "ix_HumanAiInteractionIssue_see_also_see_also" ON "HumanAiInteractionIssue_see_also" (see_also);

CREATE TABLE "Subcategory" (
	subcategory_id TEXT,
	outcome TEXT,
	about_text TEXT,
	suggested_actions_text TEXT,
	documentation_questions TEXT,
	references_text TEXT,
	id TEXT NOT NULL,
	name TEXT,
	title TEXT,
	description TEXT,
	"Category_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("Category_id") REFERENCES "Category" (id)
);
CREATE INDEX "ix_Subcategory_id" ON "Subcategory" (id);

CREATE TABLE "Category_see_also" (
	"Category_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("Category_id", see_also),
	FOREIGN KEY("Category_id") REFERENCES "Category" (id)
);
CREATE INDEX "ix_Category_see_also_see_also" ON "Category_see_also" (see_also);
CREATE INDEX "ix_Category_see_also_Category_id" ON "Category_see_also" ("Category_id");

CREATE TABLE "Subcategory_trustworthiness_characteristic" (
	"Subcategory_id" TEXT,
	trustworthiness_characteristic VARCHAR(30),
	PRIMARY KEY ("Subcategory_id", trustworthiness_characteristic),
	FOREIGN KEY("Subcategory_id") REFERENCES "Subcategory" (id)
);
CREATE INDEX "ix_Subcategory_trustworthiness_characteristic_trustworthiness_characteristic" ON "Subcategory_trustworthiness_characteristic" (trustworthiness_characteristic);
CREATE INDEX "ix_Subcategory_trustworthiness_characteristic_Subcategory_id" ON "Subcategory_trustworthiness_characteristic" ("Subcategory_id");

CREATE TABLE "Subcategory_lifecycle_stage" (
	"Subcategory_id" TEXT,
	lifecycle_stage VARCHAR(24),
	PRIMARY KEY ("Subcategory_id", lifecycle_stage),
	FOREIGN KEY("Subcategory_id") REFERENCES "Subcategory" (id)
);
CREATE INDEX "ix_Subcategory_lifecycle_stage_lifecycle_stage" ON "Subcategory_lifecycle_stage" (lifecycle_stage);
CREATE INDEX "ix_Subcategory_lifecycle_stage_Subcategory_id" ON "Subcategory_lifecycle_stage" ("Subcategory_id");

CREATE TABLE "Subcategory_topics" (
	"Subcategory_id" TEXT,
	topics TEXT,
	PRIMARY KEY ("Subcategory_id", topics),
	FOREIGN KEY("Subcategory_id") REFERENCES "Subcategory" (id)
);
CREATE INDEX "ix_Subcategory_topics_Subcategory_id" ON "Subcategory_topics" ("Subcategory_id");
CREATE INDEX "ix_Subcategory_topics_topics" ON "Subcategory_topics" (topics);

CREATE TABLE "Subcategory_ai_actor_categories" (
	"Subcategory_id" TEXT,
	ai_actor_categories TEXT,
	PRIMARY KEY ("Subcategory_id", ai_actor_categories),
	FOREIGN KEY("Subcategory_id") REFERENCES "Subcategory" (id)
);
CREATE INDEX "ix_Subcategory_ai_actor_categories_ai_actor_categories" ON "Subcategory_ai_actor_categories" (ai_actor_categories);
CREATE INDEX "ix_Subcategory_ai_actor_categories_Subcategory_id" ON "Subcategory_ai_actor_categories" ("Subcategory_id");

CREATE TABLE "Subcategory_see_also" (
	"Subcategory_id" TEXT,
	see_also TEXT,
	PRIMARY KEY ("Subcategory_id", see_also),
	FOREIGN KEY("Subcategory_id") REFERENCES "Subcategory" (id)
);
CREATE INDEX "ix_Subcategory_see_also_Subcategory_id" ON "Subcategory_see_also" ("Subcategory_id");
CREATE INDEX "ix_Subcategory_see_also_see_also" ON "Subcategory_see_also" (see_also);

CREATE TABLE "AiRmfProfile_addresses" (
	"AiRmfProfile_id" TEXT,
	addresses_id TEXT,
	PRIMARY KEY ("AiRmfProfile_id", addresses_id),
	FOREIGN KEY("AiRmfProfile_id") REFERENCES "AiRmfProfile" (id),
	FOREIGN KEY(addresses_id) REFERENCES "Subcategory" (id)
);
CREATE INDEX "ix_AiRmfProfile_addresses_addresses_id" ON "AiRmfProfile_addresses" (addresses_id);
CREATE INDEX "ix_AiRmfProfile_addresses_AiRmfProfile_id" ON "AiRmfProfile_addresses" ("AiRmfProfile_id");
