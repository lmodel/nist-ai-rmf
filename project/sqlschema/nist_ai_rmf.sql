-- # Class: NistAiRmfFamily Description: The two publications held in one document, each as its own schema renders it.
--     * Slot: id
--     * Slot: nist_ai_rmf_framework_id Description: The AI RMF, as lmodel/nist-ai-100-1 renders it.
--     * Slot: nist_ai_rmf_generative_ai_profile_ai_rmf_id Description: The Generative AI Profile, as lmodel/nist-ai-600-1 renders it.
-- # Abstract Class: AiRmfRecord Description: The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct from what the publication itself lists.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfTrustworthinessCharacteristic Description: A characteristic of trustworthy AI systems, each with a subsection of section 3.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_characteristic_name Description: Which characteristic this is.
--     * Slot: ai_rmf_characteristic_section Description: The subsection of the publication that describes it, such as 3.1.
--     * Slot: ai_rmf_characteristic_is_base Description: Whether Figure 4 shows it as the necessary condition under the others.
--     * Slot: ai_rmf_characteristic_relates_to_all Description: Whether Figure 4 shows it relating to all the others.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfDimension Description: One of the five key socio-technical dimensions of an AI system in Figure 2.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_dimension_name Description: Which dimension this is.
--     * Slot: ai_rmf_dimension_audience Description: The AI RMF audience formed by the AI actors in this dimension.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfLifecycleStage Description: A stage of the AI lifecycle as a column of Figure 3 shows it, under its dimension.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_lifecycle_stage_name Description: Which stage this is.
--     * Slot: ai_rmf_lifecycle_stage_dimension Description: The dimension Figure 3 places the stage under.
--     * Slot: ai_rmf_lifecycle_stage_tevv Description: The testing, evaluation, verification and validation (TEVV) Figure 3 gives the stage.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfActorTask Description: A task or additional AI actor of Appendix A.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_actor_task_name Description: Which task or additional AI actor this is.
--     * Slot: ai_rmf_actor_task_is_additional_actor Description: Whether Appendix A lists it under Additional AI Actors rather than as a task.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfManagementChallenge Description: One of the four challenges for AI risk management in section 1.2.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_management_challenge_name Description: Which challenge this is.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfMeasurementChallenge Description: One of the challenges of measuring AI risk in section 1.2.1.
--     * Slot: id
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_measurement_challenge_name Description: Which challenge this is.
--     * Slot: AiRmfManagementChallenge_id Description: Autocreated FK slot
-- # Class: AiRmfSpecificRisk Description: A risk that Appendix B says is new or increased for AI compared with traditional software.
--     * Slot: id
--     * Slot: title Description: This project's short name for the item. Appendix B gives its items no names.
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_specific_risk_position Description: The item's position in Appendix B's list, which is not numbered.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfHumanAiIssue Description: An issue of human-AI interaction that Appendix C says merits further consideration and research.
--     * Slot: id
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_human_ai_issue_number Description: The issue's number in Appendix C.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfAttribute Description: A key attribute of the AI RMF in Appendix D, which guided its development.
--     * Slot: id
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: ai_rmf_attribute_number Description: The attribute's number in Appendix D.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfSystem Description: A machine-based system that produces outputs such as predictions or decisions for given objectives, with varying autonomy.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfActor Description: An organization or individual with an active role in an AI system's lifecycle.
--     * Slot: ai_rmf_actor_audience Description: The AI RMF audience the actor belongs to.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfRisk Description: How likely an event is, combined with how severe its consequences are.
--     * Slot: ai_rmf_likelihood Description: How likely the event or impact is, on whatever scale the adopter uses.
--     * Slot: ai_rmf_magnitude Description: How large the consequences are, on whatever scale the adopter uses.
--     * Slot: ai_rmf_risk_system Description: The AI system the risk concerns.
--     * Slot: ai_rmf_risk_priority Description: The priority the adopter gives the risk's treatment, on whatever scale it uses, as MANAGE 1.2 asks.
--     * Slot: ai_rmf_risk_tolerance Description: The risk tolerance the risk is judged against, which GOVERN 1.3 and MAP 1.5 ask an adopter to document.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfResidualRisk Description: The risk that remains after risk treatment.
--     * Slot: ai_rmf_likelihood Description: How likely the event or impact is, on whatever scale the adopter uses.
--     * Slot: ai_rmf_magnitude Description: How large the consequences are, on whatever scale the adopter uses.
--     * Slot: ai_rmf_risk_system Description: The AI system the risk concerns.
--     * Slot: ai_rmf_risk_priority Description: The priority the adopter gives the risk's treatment, on whatever scale it uses, as MANAGE 1.2 asks.
--     * Slot: ai_rmf_risk_tolerance Description: The risk tolerance the risk is judged against, which GOVERN 1.3 and MAP 1.5 ask an adopter to document.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfImpact Description: A consequence of an AI system, which may be an opportunity, a threat or both.
--     * Slot: ai_rmf_likelihood Description: How likely the event or impact is, on whatever scale the adopter uses.
--     * Slot: ai_rmf_magnitude Description: How large the consequences are, on whatever scale the adopter uses.
--     * Slot: ai_rmf_impact_direction Description: Whether the consequence is positive, negative or both.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: AiRmfRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: AiRmfResidualRisk_ai_rmf_id Description: Autocreated FK slot
-- # Class: AiRmfHarm Description: A negative impact, sorted as in Figure 1 by whether it falls on people, an organization or an ecosystem.
--     * Slot: ai_rmf_harm_category Description: The heading of Figure 1 the harm falls under.
--     * Slot: ai_rmf_harm_example Description: The example of Figure 1 the harm matches, which must sit under the harm's category.
--     * Slot: ai_rmf_likelihood Description: How likely the event or impact is, on whatever scale the adopter uses.
--     * Slot: ai_rmf_magnitude Description: How large the consequences are, on whatever scale the adopter uses.
--     * Slot: ai_rmf_impact_direction Description: Whether the consequence is positive, negative or both.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfRiskTolerance Description: An organization's or AI actor's readiness to bear risk to achieve its objectives. The AI RMF prescribes none.
--     * Slot: ai_rmf_risk_tolerance_holder Description: The organization or AI actor whose tolerance this is.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfBias Description: A bias to consider and manage, sorted into NIST's three major categories.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfFunction Description: One of the four functions that organize AI risk management at the highest level. GOVERN cuts across the other three.
--     * Slot: id
--     * Slot: ai_rmf_function_id Description: The function's name, such as GOVERN.
--     * Slot: description Description: The one-sentence overview in NIST's catalog. The publication gives each function a section of its own instead.
--     * Slot: AiRmfFramework_id Description: Autocreated FK slot
-- # Class: AiRmfCategory Description: A group of related outcomes within a function, such as GOVERN 1, which Tables 1 to 4 state.
--     * Slot: id
--     * Slot: ai_rmf_category_id Description: The category's identifier, such as GOVERN 1.
--     * Slot: description Description: The category's statement in the publication.
--     * Slot: AiRmfFunction_id Description: Autocreated FK slot
-- # Class: AiRmfSubcategory Description: A specific outcome within a category, such as GOVERN 1.1, which Tables 1 to 4 state, and its Playbook material.
--     * Slot: id
--     * Slot: ai_rmf_subcategory_id Description: The subcategory's identifier, such as GOVERN 1.1.
--     * Slot: description Description: The subcategory's statement in the publication.
--     * Slot: AiRmfCategory_id Description: Autocreated FK slot
-- # Class: AiRmfSuggestedAction Description: One step the Playbook suggests towards a subcategory's outcome.
--     * Slot: id
--     * Slot: ai_rmf_suggested_action_id Description: The suggested action's identifier, such as SA-GOVERN_1.1-1.
--     * Slot: description Description: What the element says or is.
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
-- # Class: AiRmfDocumentationItem Description: One thing the Playbook suggests an organization document for a subcategory.
--     * Slot: id
--     * Slot: ai_rmf_documentation_id Description: The documentation prompt's identifier, such as D-GOVERN_1.1-1.
--     * Slot: description Description: What the element says or is.
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
-- # Class: AiRmfResource Description: A source the Playbook points to, by the title and address NIST's catalog gives it.
--     * Slot: id
--     * Slot: title Description: The element's name.
--     * Slot: ai_rmf_resource_uuid Description: The UUID of the resource in the back matter of NIST's catalog.
--     * Slot: ai_rmf_resource_address Description: The address NIST's catalog gives the source. The catalog gives none for a few.
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
-- # Class: AiRmfProfile Description: An implementation of the Core's functions, categories and subcategories for a setting, application or technology, based on the adopter's requirements, risk tolerance and resources.
--     * Slot: ai_rmf_profile_setting Description: The sector, industry, technology, organization or end use the profile covers, such as hiring.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfFramework Description: One edition of the AI RMF as a whole, with the Core and the lists the publication gives.
--     * Slot: id
--     * Slot: ai_rmf_version Description: The edition in NIST's two-number form, such as 1.0.
-- # Class: GaiRisk Description: A risk that section 2 defines as unique to or made worse by the development and use of GAI.
--     * Slot: id
--     * Slot: description Description: The risk's definition in section 2.
--     * Slot: gai_risk_name Description: Which of the 12 risks this is.
--     * Slot: gai_risk_section Description: The subsection of section 2 that discusses the risk, such as 2.1.
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
-- # Class: GaiSubcategory Description: An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
--     * Slot: id
--     * Slot: ai_rmf_subcategory_id Description: The subcategory's identifier, such as GOVERN 1.1.
--     * Slot: description Description: The subcategory's statement as the table restates it.
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
-- # Class: GaiSuggestedAction Description: A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
--     * Slot: id
--     * Slot: gai_action_id Description: The action's identifier, such as GV-1.1-001.
--     * Slot: description Description: The action's text in the table.
--     * Slot: GaiSubcategory_id Description: Autocreated FK slot
-- # Abstract Class: GaiPrimaryConsideration Description: One of the four primary considerations of Appendix A, which also inform the suggested actions.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
-- # Class: GaiGovernanceConsideration Description: How an organization's governance can be revisited for GAI, including across the AI value chain.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiPreDeploymentTestingConsideration Description: How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiContentProvenanceConsideration Description: How tracking the origin and history of content helps tell authentic content from synthetic content.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiIncidentDisclosureConsideration Description: How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
--     * Slot: id
--     * Slot: gai_consideration_type Description: Which of the four classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Abstract Class: GaiStructuredFeedback Description: A way of using structured public feedback to evaluate whether GAI systems perform as intended.
--     * Slot: id
--     * Slot: gai_feedback_type Description: Which of the three classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
--     * Slot: GaiPreDeploymentTestingConsideration_id Description: Autocreated FK slot
-- # Class: GaiParticipatoryEngagement Description: Asking civil society groups, affected communities and users for feedback, such as through focus groups or surveys.
--     * Slot: id
--     * Slot: gai_feedback_type Description: Which of the three classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiFieldTesting Description: Structured settings that show how people interact with and use AI-generated information.
--     * Slot: id
--     * Slot: gai_feedback_type Description: Which of the three classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiAiRedTeaming Description: A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
--     * Slot: id
--     * Slot: gai_feedback_type Description: Which of the three classes this record is.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: GaiProfile Description: The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
--     * Slot: ai_rmf_profile_setting Description: The sector, industry, technology, organization or end use the profile covers, such as hiring.
--     * Slot: ai_rmf_id Description: The identifier an adopter gives a record of its own.
--     * Slot: title Description: The element's name.
--     * Slot: description Description: What the element says or is.
-- # Class: AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors
--     * Slot: AiRmfLifecycleStage_id Description: Autocreated FK slot
--     * Slot: ai_rmf_lifecycle_stage_representative_actors Description: The representative AI actors Figure 3 lists for the stage.
-- # Class: AiRmfActorTask_ai_rmf_actor_task_representative_actors
--     * Slot: AiRmfActorTask_id Description: Autocreated FK slot
--     * Slot: ai_rmf_actor_task_representative_actors Description: The AI actors that Appendix A says carry out the task.
-- # Class: AiRmfSystem_ai_rmf_system_intended_purposes
--     * Slot: AiRmfSystem_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_system_intended_purposes Description: What the system is for, and its potentially beneficial uses, which MAP 1.1 asks an adopter to document.
-- # Class: AiRmfSystem_ai_rmf_system_deployment_settings
--     * Slot: AiRmfSystem_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_system_deployment_settings Description: The settings the system is or will be deployed in, which MAP 1.1 asks an adopter to document.
-- # Class: AiRmfSystem_ai_rmf_system_lifecycle_stages
--     * Slot: AiRmfSystem_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_system_lifecycle_stages Description: The lifecycle stages the record covers.
-- # Class: AiRmfSystem_ai_rmf_system_actors
--     * Slot: AiRmfSystem_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_system_actors_ai_rmf_id Description: The AI actors with a role in the system's lifecycle, such as those MAP 1.6 says elicit its requirements.
-- # Class: AiRmfActor_ai_rmf_actor_tasks
--     * Slot: AiRmfActor_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_actor_tasks Description: The tasks the actor carries out, or the additional AI actor it is.
-- # Class: AiRmfActor_ai_rmf_actor_lifecycle_stages
--     * Slot: AiRmfActor_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_actor_lifecycle_stages Description: The lifecycle stages the actor works in.
-- # Class: AiRmfRisk_ai_rmf_risk_characteristics
--     * Slot: AiRmfRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_characteristics Description: The trustworthiness characteristics the risk bears on.
-- # Class: AiRmfRisk_ai_rmf_risk_lifecycle_stages
--     * Slot: AiRmfRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_lifecycle_stages Description: The lifecycle stages where the risk is measured or arises.
-- # Class: AiRmfRisk_ai_rmf_risk_responses
--     * Slot: AiRmfRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_responses Description: The responses chosen for the risk.
-- # Class: AiRmfResidualRisk_ai_rmf_risk_characteristics
--     * Slot: AiRmfResidualRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_characteristics Description: The trustworthiness characteristics the risk bears on.
-- # Class: AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages
--     * Slot: AiRmfResidualRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_lifecycle_stages Description: The lifecycle stages where the risk is measured or arises.
-- # Class: AiRmfResidualRisk_ai_rmf_risk_responses
--     * Slot: AiRmfResidualRisk_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_responses Description: The responses chosen for the risk.
-- # Class: AiRmfImpact_ai_rmf_impact_affected_parties
--     * Slot: AiRmfImpact_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_impact_affected_parties Description: Who or what experiences the consequence.
-- # Class: AiRmfHarm_ai_rmf_impact_affected_parties
--     * Slot: AiRmfHarm_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_impact_affected_parties Description: Who or what experiences the consequence.
-- # Class: AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences
--     * Slot: AiRmfRiskTolerance_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_risk_tolerance_influences Description: What influences it, such as a law, a regulation, a policy or a norm.
-- # Class: AiRmfBias_ai_rmf_bias_categories
--     * Slot: AiRmfBias_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_bias_categories Description: The categories it falls under.
-- # Class: AiRmfSubcategory_ai_rmf_subcategory_about
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
--     * Slot: ai_rmf_subcategory_about Description: The Playbook's discussion of the outcome.
-- # Class: AiRmfSubcategory_ai_rmf_subcategory_ai_actors
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
--     * Slot: ai_rmf_subcategory_ai_actors Description: The AI actors the Playbook tags the outcome with.
-- # Class: AiRmfSubcategory_ai_rmf_subcategory_topics
--     * Slot: AiRmfSubcategory_id Description: Autocreated FK slot
--     * Slot: ai_rmf_subcategory_topics Description: The topics the Playbook tags the outcome with. NIST keeps no closed list of them.
-- # Class: AiRmfProfile_ai_rmf_profile_kinds
--     * Slot: AiRmfProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_kinds Description: Which of the publication's kinds of profile this is. A current profile for one use case is both.
-- # Class: AiRmfProfile_ai_rmf_profile_subcategories
--     * Slot: AiRmfProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_subcategories Description: The subcategories the profile selects. An adopter may select from them rather than apply all.
-- # Class: GaiRisk_gai_risk_characteristics
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_characteristics Description: The AI RMF's trustworthiness characteristics that the subsection names for the risk.
-- # Class: GaiRisk_gai_risk_groupings
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_groupings Description: The groups footnote 5 suggests for the risk. The footnote lists Data Privacy under all three.
-- # Class: GaiRisk_gai_risk_lifecycle_stages
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_lifecycle_stages Description: The lifecycle stages where the risk can arise for the adopter's model, system or use case.
-- # Class: GaiRisk_gai_risk_scopes
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_scopes Description: The levels where the risk exists for the adopter's model, system or use case.
-- # Class: GaiRisk_gai_risk_sources
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_sources Description: Where the risk comes from for the adopter's model, system or use case.
-- # Class: GaiRisk_gai_risk_time_scales
--     * Slot: GaiRisk_id Description: Autocreated FK slot
--     * Slot: gai_risk_time_scales Description: How the risk materializes over time for the adopter's model, system or use case.
-- # Class: GaiSubcategory_gai_subcategory_actor_tasks
--     * Slot: GaiSubcategory_id Description: Autocreated FK slot
--     * Slot: gai_subcategory_actor_tasks Description: The AI actor tasks the table names. They belong to the table and not to one action: the publication says not every task applies to every action.
-- # Class: GaiSuggestedAction_gai_action_risks
--     * Slot: GaiSuggestedAction_id Description: Autocreated FK slot
--     * Slot: gai_action_risks Description: The GAI risks the row tags the action with.
-- # Class: GaiPrimaryConsideration_gai_consideration_sections
--     * Slot: GaiPrimaryConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiGovernanceConsideration_gai_governance_plans
--     * Slot: GaiGovernanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_governance_plans Description: The plans and actions that section A.1.2 lists from other AI governance.
-- # Class: GaiGovernanceConsideration_gai_third_party_controls
--     * Slot: GaiGovernanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_third_party_controls Description: The existing controls that section A.1.3 says can apply to third-party GAI.
-- # Class: GaiGovernanceConsideration_gai_consideration_sections
--     * Slot: GaiGovernanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiPreDeploymentTestingConsideration_gai_consideration_sections
--     * Slot: GaiPreDeploymentTestingConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiContentProvenanceConsideration_gai_provenance_techniques
--     * Slot: GaiContentProvenanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_provenance_techniques Description: The well-known techniques for provenance data tracking that section A.1.6 names.
-- # Class: GaiContentProvenanceConsideration_gai_consideration_sections
--     * Slot: GaiContentProvenanceConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiIncidentDisclosureConsideration_gai_incident_harms
--     * Slot: GaiIncidentDisclosureConsideration_id Description: Autocreated FK slot
--     * Slot: gai_incident_harms Description: The kinds of harm that section A.1.8's definition of an AI incident names.
-- # Class: GaiIncidentDisclosureConsideration_gai_consideration_sections
--     * Slot: GaiIncidentDisclosureConsideration_id Description: Autocreated FK slot
--     * Slot: gai_consideration_sections Description: The subsections of Appendix A that discuss the consideration, such as A.1.2.
-- # Class: GaiAiRedTeaming_gai_red_teaming_types
--     * Slot: GaiAiRedTeaming_id Description: Autocreated FK slot
--     * Slot: gai_red_teaming_types Description: The kinds of AI red-teaming that may suit the use case.
-- # Class: GaiProfile_ai_rmf_profile_kinds
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_kinds Description: Which of the publication's kinds of profile this is. A current profile for one use case is both.
-- # Class: GaiProfile_ai_rmf_profile_subcategories
--     * Slot: GaiProfile_ai_rmf_id Description: Autocreated FK slot
--     * Slot: ai_rmf_profile_subcategories Description: The subcategories the profile selects. An adopter may select from them rather than apply all.

CREATE TABLE "AiRmfRecord" (
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRecord_ai_rmf_id" ON "AiRmfRecord" (ai_rmf_id);

CREATE TABLE "AiRmfSystem" (
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_id" ON "AiRmfSystem" (ai_rmf_id);

CREATE TABLE "AiRmfActor" (
	ai_rmf_actor_audience VARCHAR(9),
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfActor_ai_rmf_id" ON "AiRmfActor" (ai_rmf_id);

CREATE TABLE "AiRmfHarm" (
	ai_rmf_harm_category VARCHAR(12) NOT NULL,
	ai_rmf_harm_example VARCHAR(33),
	ai_rmf_likelihood TEXT,
	ai_rmf_magnitude TEXT,
	ai_rmf_impact_direction VARCHAR(8) NOT NULL,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfHarm_ai_rmf_id" ON "AiRmfHarm" (ai_rmf_id);

CREATE TABLE "AiRmfBias" (
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfBias_ai_rmf_id" ON "AiRmfBias" (ai_rmf_id);

CREATE TABLE "AiRmfProfile" (
	ai_rmf_profile_setting TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile" (ai_rmf_id);

CREATE TABLE "AiRmfFramework" (
	id INTEGER NOT NULL,
	ai_rmf_version TEXT NOT NULL,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_AiRmfFramework_id" ON "AiRmfFramework" (id);

CREATE TABLE "GaiGovernanceConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiGovernanceConsideration_id" ON "GaiGovernanceConsideration" (id);

CREATE TABLE "GaiPreDeploymentTestingConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiPreDeploymentTestingConsideration_id" ON "GaiPreDeploymentTestingConsideration" (id);

CREATE TABLE "GaiContentProvenanceConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiContentProvenanceConsideration_id" ON "GaiContentProvenanceConsideration" (id);

CREATE TABLE "GaiIncidentDisclosureConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_id" ON "GaiIncidentDisclosureConsideration" (id);

CREATE TABLE "GaiParticipatoryEngagement" (
	id INTEGER NOT NULL,
	gai_feedback_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiParticipatoryEngagement_id" ON "GaiParticipatoryEngagement" (id);

CREATE TABLE "GaiFieldTesting" (
	id INTEGER NOT NULL,
	gai_feedback_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiFieldTesting_id" ON "GaiFieldTesting" (id);

CREATE TABLE "GaiAiRedTeaming" (
	id INTEGER NOT NULL,
	gai_feedback_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	PRIMARY KEY (id)
);
CREATE INDEX "ix_GaiAiRedTeaming_id" ON "GaiAiRedTeaming" (id);

CREATE TABLE "GaiProfile" (
	ai_rmf_profile_setting TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id)
);
CREATE INDEX "ix_GaiProfile_ai_rmf_id" ON "GaiProfile" (ai_rmf_id);

CREATE TABLE "NistAiRmfFamily" (
	id INTEGER NOT NULL,
	nist_ai_rmf_framework_id INTEGER,
	nist_ai_rmf_generative_ai_profile_ai_rmf_id TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY(nist_ai_rmf_framework_id) REFERENCES "AiRmfFramework" (id),
	FOREIGN KEY(nist_ai_rmf_generative_ai_profile_ai_rmf_id) REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_NistAiRmfFamily_id" ON "NistAiRmfFamily" (id);

CREATE TABLE "AiRmfTrustworthinessCharacteristic" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_characteristic_name VARCHAR(30) NOT NULL,
	ai_rmf_characteristic_section TEXT NOT NULL,
	ai_rmf_characteristic_is_base BOOLEAN,
	ai_rmf_characteristic_relates_to_all BOOLEAN,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfTrustworthinessCharacteristic_id" ON "AiRmfTrustworthinessCharacteristic" (id);

CREATE TABLE "AiRmfDimension" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_dimension_name VARCHAR(19) NOT NULL,
	ai_rmf_dimension_audience VARCHAR(9) NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfDimension_id" ON "AiRmfDimension" (id);

CREATE TABLE "AiRmfLifecycleStage" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_lifecycle_stage_name VARCHAR(24) NOT NULL,
	ai_rmf_lifecycle_stage_dimension VARCHAR(19) NOT NULL,
	ai_rmf_lifecycle_stage_tevv TEXT,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfLifecycleStage_id" ON "AiRmfLifecycleStage" (id);

CREATE TABLE "AiRmfActorTask" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_actor_task_name VARCHAR(36) NOT NULL,
	ai_rmf_actor_task_is_additional_actor BOOLEAN,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfActorTask_id" ON "AiRmfActorTask" (id);

CREATE TABLE "AiRmfManagementChallenge" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_management_challenge_name VARCHAR(49) NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfManagementChallenge_id" ON "AiRmfManagementChallenge" (id);

CREATE TABLE "AiRmfSpecificRisk" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	ai_rmf_specific_risk_position INTEGER NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfSpecificRisk_id" ON "AiRmfSpecificRisk" (id);

CREATE TABLE "AiRmfHumanAiIssue" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	ai_rmf_human_ai_issue_number INTEGER NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfHumanAiIssue_id" ON "AiRmfHumanAiIssue" (id);

CREATE TABLE "AiRmfAttribute" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	ai_rmf_attribute_number INTEGER NOT NULL,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfAttribute_id" ON "AiRmfAttribute" (id);

CREATE TABLE "AiRmfRiskTolerance" (
	ai_rmf_risk_tolerance_holder TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id),
	FOREIGN KEY(ai_rmf_risk_tolerance_holder) REFERENCES "AiRmfActor" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRiskTolerance_ai_rmf_id" ON "AiRmfRiskTolerance" (ai_rmf_id);

CREATE TABLE "AiRmfFunction" (
	id INTEGER NOT NULL,
	ai_rmf_function_id TEXT NOT NULL,
	description TEXT,
	"AiRmfFramework_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFramework_id") REFERENCES "AiRmfFramework" (id)
);
CREATE INDEX "ix_AiRmfFunction_id" ON "AiRmfFunction" (id);

CREATE TABLE "GaiRisk" (
	id INTEGER NOT NULL,
	description TEXT,
	gai_risk_name VARCHAR(37) NOT NULL,
	gai_risk_section TEXT NOT NULL,
	"GaiProfile_ai_rmf_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiRisk_id" ON "GaiRisk" (id);

CREATE TABLE "GaiSubcategory" (
	id INTEGER NOT NULL,
	ai_rmf_subcategory_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"GaiProfile_ai_rmf_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiSubcategory_id" ON "GaiSubcategory" (id);

CREATE TABLE "GaiPrimaryConsideration" (
	id INTEGER NOT NULL,
	gai_consideration_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"GaiProfile_ai_rmf_id" TEXT,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiPrimaryConsideration_id" ON "GaiPrimaryConsideration" (id);

CREATE TABLE "GaiStructuredFeedback" (
	id INTEGER NOT NULL,
	gai_feedback_type TEXT NOT NULL,
	title TEXT NOT NULL,
	description TEXT,
	"GaiPreDeploymentTestingConsideration_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiPreDeploymentTestingConsideration_id") REFERENCES "GaiPreDeploymentTestingConsideration" (id)
);
CREATE INDEX "ix_GaiStructuredFeedback_id" ON "GaiStructuredFeedback" (id);

CREATE TABLE "AiRmfSystem_ai_rmf_system_intended_purposes" (
	"AiRmfSystem_ai_rmf_id" TEXT,
	ai_rmf_system_intended_purposes TEXT,
	PRIMARY KEY ("AiRmfSystem_ai_rmf_id", ai_rmf_system_intended_purposes),
	FOREIGN KEY("AiRmfSystem_ai_rmf_id") REFERENCES "AiRmfSystem" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_intended_purposes_AiRmfSystem_ai_rmf_id" ON "AiRmfSystem_ai_rmf_system_intended_purposes" ("AiRmfSystem_ai_rmf_id");
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_intended_purposes_ai_rmf_system_intended_purposes" ON "AiRmfSystem_ai_rmf_system_intended_purposes" (ai_rmf_system_intended_purposes);

CREATE TABLE "AiRmfSystem_ai_rmf_system_deployment_settings" (
	"AiRmfSystem_ai_rmf_id" TEXT,
	ai_rmf_system_deployment_settings TEXT,
	PRIMARY KEY ("AiRmfSystem_ai_rmf_id", ai_rmf_system_deployment_settings),
	FOREIGN KEY("AiRmfSystem_ai_rmf_id") REFERENCES "AiRmfSystem" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_deployment_settings_ai_rmf_system_deployment_settings" ON "AiRmfSystem_ai_rmf_system_deployment_settings" (ai_rmf_system_deployment_settings);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_deployment_settings_AiRmfSystem_ai_rmf_id" ON "AiRmfSystem_ai_rmf_system_deployment_settings" ("AiRmfSystem_ai_rmf_id");

CREATE TABLE "AiRmfSystem_ai_rmf_system_lifecycle_stages" (
	"AiRmfSystem_ai_rmf_id" TEXT,
	ai_rmf_system_lifecycle_stages VARCHAR(24),
	PRIMARY KEY ("AiRmfSystem_ai_rmf_id", ai_rmf_system_lifecycle_stages),
	FOREIGN KEY("AiRmfSystem_ai_rmf_id") REFERENCES "AiRmfSystem" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_lifecycle_stages_ai_rmf_system_lifecycle_stages" ON "AiRmfSystem_ai_rmf_system_lifecycle_stages" (ai_rmf_system_lifecycle_stages);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_lifecycle_stages_AiRmfSystem_ai_rmf_id" ON "AiRmfSystem_ai_rmf_system_lifecycle_stages" ("AiRmfSystem_ai_rmf_id");

CREATE TABLE "AiRmfSystem_ai_rmf_system_actors" (
	"AiRmfSystem_ai_rmf_id" TEXT,
	ai_rmf_system_actors_ai_rmf_id TEXT,
	PRIMARY KEY ("AiRmfSystem_ai_rmf_id", ai_rmf_system_actors_ai_rmf_id),
	FOREIGN KEY("AiRmfSystem_ai_rmf_id") REFERENCES "AiRmfSystem" (ai_rmf_id),
	FOREIGN KEY(ai_rmf_system_actors_ai_rmf_id) REFERENCES "AiRmfActor" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_actors_ai_rmf_system_actors_ai_rmf_id" ON "AiRmfSystem_ai_rmf_system_actors" (ai_rmf_system_actors_ai_rmf_id);
CREATE INDEX "ix_AiRmfSystem_ai_rmf_system_actors_AiRmfSystem_ai_rmf_id" ON "AiRmfSystem_ai_rmf_system_actors" ("AiRmfSystem_ai_rmf_id");

CREATE TABLE "AiRmfActor_ai_rmf_actor_tasks" (
	"AiRmfActor_ai_rmf_id" TEXT,
	ai_rmf_actor_tasks VARCHAR(36),
	PRIMARY KEY ("AiRmfActor_ai_rmf_id", ai_rmf_actor_tasks),
	FOREIGN KEY("AiRmfActor_ai_rmf_id") REFERENCES "AiRmfActor" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfActor_ai_rmf_actor_tasks_ai_rmf_actor_tasks" ON "AiRmfActor_ai_rmf_actor_tasks" (ai_rmf_actor_tasks);
CREATE INDEX "ix_AiRmfActor_ai_rmf_actor_tasks_AiRmfActor_ai_rmf_id" ON "AiRmfActor_ai_rmf_actor_tasks" ("AiRmfActor_ai_rmf_id");

CREATE TABLE "AiRmfActor_ai_rmf_actor_lifecycle_stages" (
	"AiRmfActor_ai_rmf_id" TEXT,
	ai_rmf_actor_lifecycle_stages VARCHAR(24),
	PRIMARY KEY ("AiRmfActor_ai_rmf_id", ai_rmf_actor_lifecycle_stages),
	FOREIGN KEY("AiRmfActor_ai_rmf_id") REFERENCES "AiRmfActor" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfActor_ai_rmf_actor_lifecycle_stages_ai_rmf_actor_lifecycle_stages" ON "AiRmfActor_ai_rmf_actor_lifecycle_stages" (ai_rmf_actor_lifecycle_stages);
CREATE INDEX "ix_AiRmfActor_ai_rmf_actor_lifecycle_stages_AiRmfActor_ai_rmf_id" ON "AiRmfActor_ai_rmf_actor_lifecycle_stages" ("AiRmfActor_ai_rmf_id");

CREATE TABLE "AiRmfHarm_ai_rmf_impact_affected_parties" (
	"AiRmfHarm_ai_rmf_id" TEXT,
	ai_rmf_impact_affected_parties VARCHAR(13),
	PRIMARY KEY ("AiRmfHarm_ai_rmf_id", ai_rmf_impact_affected_parties),
	FOREIGN KEY("AiRmfHarm_ai_rmf_id") REFERENCES "AiRmfHarm" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfHarm_ai_rmf_impact_affected_parties_AiRmfHarm_ai_rmf_id" ON "AiRmfHarm_ai_rmf_impact_affected_parties" ("AiRmfHarm_ai_rmf_id");
CREATE INDEX "ix_AiRmfHarm_ai_rmf_impact_affected_parties_ai_rmf_impact_affected_parties" ON "AiRmfHarm_ai_rmf_impact_affected_parties" (ai_rmf_impact_affected_parties);

CREATE TABLE "AiRmfBias_ai_rmf_bias_categories" (
	"AiRmfBias_ai_rmf_id" TEXT,
	ai_rmf_bias_categories VARCHAR(29) NOT NULL,
	PRIMARY KEY ("AiRmfBias_ai_rmf_id", ai_rmf_bias_categories),
	FOREIGN KEY("AiRmfBias_ai_rmf_id") REFERENCES "AiRmfBias" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfBias_ai_rmf_bias_categories_AiRmfBias_ai_rmf_id" ON "AiRmfBias_ai_rmf_bias_categories" ("AiRmfBias_ai_rmf_id");
CREATE INDEX "ix_AiRmfBias_ai_rmf_bias_categories_ai_rmf_bias_categories" ON "AiRmfBias_ai_rmf_bias_categories" (ai_rmf_bias_categories);

CREATE TABLE "AiRmfProfile_ai_rmf_profile_kinds" (
	"AiRmfProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_kinds VARCHAR(14) NOT NULL,
	PRIMARY KEY ("AiRmfProfile_ai_rmf_id", ai_rmf_profile_kinds),
	FOREIGN KEY("AiRmfProfile_ai_rmf_id") REFERENCES "AiRmfProfile" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_kinds_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile_ai_rmf_profile_kinds" ("AiRmfProfile_ai_rmf_id");
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_kinds_ai_rmf_profile_kinds" ON "AiRmfProfile_ai_rmf_profile_kinds" (ai_rmf_profile_kinds);

CREATE TABLE "AiRmfProfile_ai_rmf_profile_subcategories" (
	"AiRmfProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_subcategories TEXT,
	PRIMARY KEY ("AiRmfProfile_ai_rmf_id", ai_rmf_profile_subcategories),
	FOREIGN KEY("AiRmfProfile_ai_rmf_id") REFERENCES "AiRmfProfile" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_subcategories_ai_rmf_profile_subcategories" ON "AiRmfProfile_ai_rmf_profile_subcategories" (ai_rmf_profile_subcategories);
CREATE INDEX "ix_AiRmfProfile_ai_rmf_profile_subcategories_AiRmfProfile_ai_rmf_id" ON "AiRmfProfile_ai_rmf_profile_subcategories" ("AiRmfProfile_ai_rmf_id");

CREATE TABLE "GaiGovernanceConsideration_gai_governance_plans" (
	"GaiGovernanceConsideration_id" INTEGER,
	gai_governance_plans VARCHAR(61),
	PRIMARY KEY ("GaiGovernanceConsideration_id", gai_governance_plans),
	FOREIGN KEY("GaiGovernanceConsideration_id") REFERENCES "GaiGovernanceConsideration" (id)
);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_governance_plans_GaiGovernanceConsideration_id" ON "GaiGovernanceConsideration_gai_governance_plans" ("GaiGovernanceConsideration_id");
CREATE INDEX "ix_GaiGovernanceConsideration_gai_governance_plans_gai_governance_plans" ON "GaiGovernanceConsideration_gai_governance_plans" (gai_governance_plans);

CREATE TABLE "GaiGovernanceConsideration_gai_third_party_controls" (
	"GaiGovernanceConsideration_id" INTEGER,
	gai_third_party_controls VARCHAR(41),
	PRIMARY KEY ("GaiGovernanceConsideration_id", gai_third_party_controls),
	FOREIGN KEY("GaiGovernanceConsideration_id") REFERENCES "GaiGovernanceConsideration" (id)
);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_third_party_controls_gai_third_party_controls" ON "GaiGovernanceConsideration_gai_third_party_controls" (gai_third_party_controls);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_third_party_controls_GaiGovernanceConsideration_id" ON "GaiGovernanceConsideration_gai_third_party_controls" ("GaiGovernanceConsideration_id");

CREATE TABLE "GaiGovernanceConsideration_gai_consideration_sections" (
	"GaiGovernanceConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiGovernanceConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiGovernanceConsideration_id") REFERENCES "GaiGovernanceConsideration" (id)
);
CREATE INDEX "ix_GaiGovernanceConsideration_gai_consideration_sections_GaiGovernanceConsideration_id" ON "GaiGovernanceConsideration_gai_consideration_sections" ("GaiGovernanceConsideration_id");
CREATE INDEX "ix_GaiGovernanceConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiGovernanceConsideration_gai_consideration_sections" (gai_consideration_sections);

CREATE TABLE "GaiPreDeploymentTestingConsideration_gai_consideration_sections" (
	"GaiPreDeploymentTestingConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiPreDeploymentTestingConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiPreDeploymentTestingConsideration_id") REFERENCES "GaiPreDeploymentTestingConsideration" (id)
);
CREATE INDEX "ix_GaiPreDeploymentTestingConsideration_gai_consideration_sections_GaiPreDeploymentTestingConsideration_id" ON "GaiPreDeploymentTestingConsideration_gai_consideration_sections" ("GaiPreDeploymentTestingConsideration_id");
CREATE INDEX "ix_GaiPreDeploymentTestingConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiPreDeploymentTestingConsideration_gai_consideration_sections" (gai_consideration_sections);

CREATE TABLE "GaiContentProvenanceConsideration_gai_provenance_techniques" (
	"GaiContentProvenanceConsideration_id" INTEGER,
	gai_provenance_techniques VARCHAR(22),
	PRIMARY KEY ("GaiContentProvenanceConsideration_id", gai_provenance_techniques),
	FOREIGN KEY("GaiContentProvenanceConsideration_id") REFERENCES "GaiContentProvenanceConsideration" (id)
);
CREATE INDEX "ix_GaiContentProvenanceConsideration_gai_provenance_techniques_GaiContentProvenanceConsideration_id" ON "GaiContentProvenanceConsideration_gai_provenance_techniques" ("GaiContentProvenanceConsideration_id");
CREATE INDEX "ix_GaiContentProvenanceConsideration_gai_provenance_techniques_gai_provenance_techniques" ON "GaiContentProvenanceConsideration_gai_provenance_techniques" (gai_provenance_techniques);

CREATE TABLE "GaiContentProvenanceConsideration_gai_consideration_sections" (
	"GaiContentProvenanceConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiContentProvenanceConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiContentProvenanceConsideration_id") REFERENCES "GaiContentProvenanceConsideration" (id)
);
CREATE INDEX "ix_GaiContentProvenanceConsideration_gai_consideration_sections_GaiContentProvenanceConsideration_id" ON "GaiContentProvenanceConsideration_gai_consideration_sections" ("GaiContentProvenanceConsideration_id");
CREATE INDEX "ix_GaiContentProvenanceConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiContentProvenanceConsideration_gai_consideration_sections" (gai_consideration_sections);

CREATE TABLE "GaiIncidentDisclosureConsideration_gai_incident_harms" (
	"GaiIncidentDisclosureConsideration_id" INTEGER,
	gai_incident_harms VARCHAR(43),
	PRIMARY KEY ("GaiIncidentDisclosureConsideration_id", gai_incident_harms),
	FOREIGN KEY("GaiIncidentDisclosureConsideration_id") REFERENCES "GaiIncidentDisclosureConsideration" (id)
);
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_gai_incident_harms_gai_incident_harms" ON "GaiIncidentDisclosureConsideration_gai_incident_harms" (gai_incident_harms);
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_gai_incident_harms_GaiIncidentDisclosureConsideration_id" ON "GaiIncidentDisclosureConsideration_gai_incident_harms" ("GaiIncidentDisclosureConsideration_id");

CREATE TABLE "GaiIncidentDisclosureConsideration_gai_consideration_sections" (
	"GaiIncidentDisclosureConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiIncidentDisclosureConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiIncidentDisclosureConsideration_id") REFERENCES "GaiIncidentDisclosureConsideration" (id)
);
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_gai_consideration_sections_GaiIncidentDisclosureConsideration_id" ON "GaiIncidentDisclosureConsideration_gai_consideration_sections" ("GaiIncidentDisclosureConsideration_id");
CREATE INDEX "ix_GaiIncidentDisclosureConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiIncidentDisclosureConsideration_gai_consideration_sections" (gai_consideration_sections);

CREATE TABLE "GaiAiRedTeaming_gai_red_teaming_types" (
	"GaiAiRedTeaming_id" INTEGER,
	gai_red_teaming_types VARCHAR(14),
	PRIMARY KEY ("GaiAiRedTeaming_id", gai_red_teaming_types),
	FOREIGN KEY("GaiAiRedTeaming_id") REFERENCES "GaiAiRedTeaming" (id)
);
CREATE INDEX "ix_GaiAiRedTeaming_gai_red_teaming_types_gai_red_teaming_types" ON "GaiAiRedTeaming_gai_red_teaming_types" (gai_red_teaming_types);
CREATE INDEX "ix_GaiAiRedTeaming_gai_red_teaming_types_GaiAiRedTeaming_id" ON "GaiAiRedTeaming_gai_red_teaming_types" ("GaiAiRedTeaming_id");

CREATE TABLE "GaiProfile_ai_rmf_profile_kinds" (
	"GaiProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_kinds VARCHAR(14) NOT NULL,
	PRIMARY KEY ("GaiProfile_ai_rmf_id", ai_rmf_profile_kinds),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiProfile_ai_rmf_profile_kinds_GaiProfile_ai_rmf_id" ON "GaiProfile_ai_rmf_profile_kinds" ("GaiProfile_ai_rmf_id");
CREATE INDEX "ix_GaiProfile_ai_rmf_profile_kinds_ai_rmf_profile_kinds" ON "GaiProfile_ai_rmf_profile_kinds" (ai_rmf_profile_kinds);

CREATE TABLE "GaiProfile_ai_rmf_profile_subcategories" (
	"GaiProfile_ai_rmf_id" TEXT,
	ai_rmf_profile_subcategories TEXT,
	PRIMARY KEY ("GaiProfile_ai_rmf_id", ai_rmf_profile_subcategories),
	FOREIGN KEY("GaiProfile_ai_rmf_id") REFERENCES "GaiProfile" (ai_rmf_id)
);
CREATE INDEX "ix_GaiProfile_ai_rmf_profile_subcategories_ai_rmf_profile_subcategories" ON "GaiProfile_ai_rmf_profile_subcategories" (ai_rmf_profile_subcategories);
CREATE INDEX "ix_GaiProfile_ai_rmf_profile_subcategories_GaiProfile_ai_rmf_id" ON "GaiProfile_ai_rmf_profile_subcategories" ("GaiProfile_ai_rmf_id");

CREATE TABLE "AiRmfMeasurementChallenge" (
	id INTEGER NOT NULL,
	description TEXT,
	ai_rmf_measurement_challenge_name VARCHAR(38) NOT NULL,
	"AiRmfManagementChallenge_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfManagementChallenge_id") REFERENCES "AiRmfManagementChallenge" (id)
);
CREATE INDEX "ix_AiRmfMeasurementChallenge_id" ON "AiRmfMeasurementChallenge" (id);

CREATE TABLE "AiRmfRisk" (
	ai_rmf_likelihood TEXT,
	ai_rmf_magnitude TEXT,
	ai_rmf_risk_system TEXT,
	ai_rmf_risk_priority TEXT,
	ai_rmf_risk_tolerance TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id),
	FOREIGN KEY(ai_rmf_risk_system) REFERENCES "AiRmfSystem" (ai_rmf_id),
	FOREIGN KEY(ai_rmf_risk_tolerance) REFERENCES "AiRmfRiskTolerance" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_id" ON "AiRmfRisk" (ai_rmf_id);

CREATE TABLE "AiRmfResidualRisk" (
	ai_rmf_likelihood TEXT,
	ai_rmf_magnitude TEXT,
	ai_rmf_risk_system TEXT,
	ai_rmf_risk_priority TEXT,
	ai_rmf_risk_tolerance TEXT,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	PRIMARY KEY (ai_rmf_id),
	FOREIGN KEY(ai_rmf_risk_system) REFERENCES "AiRmfSystem" (ai_rmf_id),
	FOREIGN KEY(ai_rmf_risk_tolerance) REFERENCES "AiRmfRiskTolerance" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_id" ON "AiRmfResidualRisk" (ai_rmf_id);

CREATE TABLE "AiRmfCategory" (
	id INTEGER NOT NULL,
	ai_rmf_category_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"AiRmfFunction_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfFunction_id") REFERENCES "AiRmfFunction" (id)
);
CREATE INDEX "ix_AiRmfCategory_id" ON "AiRmfCategory" (id);

CREATE TABLE "GaiSuggestedAction" (
	id INTEGER NOT NULL,
	gai_action_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"GaiSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("GaiSubcategory_id") REFERENCES "GaiSubcategory" (id)
);
CREATE INDEX "ix_GaiSuggestedAction_id" ON "GaiSuggestedAction" (id);

CREATE TABLE "AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors" (
	"AiRmfLifecycleStage_id" INTEGER,
	ai_rmf_lifecycle_stage_representative_actors TEXT,
	PRIMARY KEY ("AiRmfLifecycleStage_id", ai_rmf_lifecycle_stage_representative_actors),
	FOREIGN KEY("AiRmfLifecycleStage_id") REFERENCES "AiRmfLifecycleStage" (id)
);
CREATE INDEX "ix_AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors_ai_rmf_lifecycle_stage_representative_actors" ON "AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors" (ai_rmf_lifecycle_stage_representative_actors);
CREATE INDEX "ix_AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors_AiRmfLifecycleStage_id" ON "AiRmfLifecycleStage_ai_rmf_lifecycle_stage_representative_actors" ("AiRmfLifecycleStage_id");

CREATE TABLE "AiRmfActorTask_ai_rmf_actor_task_representative_actors" (
	"AiRmfActorTask_id" INTEGER,
	ai_rmf_actor_task_representative_actors TEXT,
	PRIMARY KEY ("AiRmfActorTask_id", ai_rmf_actor_task_representative_actors),
	FOREIGN KEY("AiRmfActorTask_id") REFERENCES "AiRmfActorTask" (id)
);
CREATE INDEX "ix_AiRmfActorTask_ai_rmf_actor_task_representative_actors_ai_rmf_actor_task_representative_actors" ON "AiRmfActorTask_ai_rmf_actor_task_representative_actors" (ai_rmf_actor_task_representative_actors);
CREATE INDEX "ix_AiRmfActorTask_ai_rmf_actor_task_representative_actors_AiRmfActorTask_id" ON "AiRmfActorTask_ai_rmf_actor_task_representative_actors" ("AiRmfActorTask_id");

CREATE TABLE "AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences" (
	"AiRmfRiskTolerance_ai_rmf_id" TEXT,
	ai_rmf_risk_tolerance_influences TEXT,
	PRIMARY KEY ("AiRmfRiskTolerance_ai_rmf_id", ai_rmf_risk_tolerance_influences),
	FOREIGN KEY("AiRmfRiskTolerance_ai_rmf_id") REFERENCES "AiRmfRiskTolerance" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences_AiRmfRiskTolerance_ai_rmf_id" ON "AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences" ("AiRmfRiskTolerance_ai_rmf_id");
CREATE INDEX "ix_AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences_ai_rmf_risk_tolerance_influences" ON "AiRmfRiskTolerance_ai_rmf_risk_tolerance_influences" (ai_rmf_risk_tolerance_influences);

CREATE TABLE "GaiRisk_gai_risk_characteristics" (
	"GaiRisk_id" INTEGER,
	gai_risk_characteristics VARCHAR(30),
	PRIMARY KEY ("GaiRisk_id", gai_risk_characteristics),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_characteristics_gai_risk_characteristics" ON "GaiRisk_gai_risk_characteristics" (gai_risk_characteristics);
CREATE INDEX "ix_GaiRisk_gai_risk_characteristics_GaiRisk_id" ON "GaiRisk_gai_risk_characteristics" ("GaiRisk_id");

CREATE TABLE "GaiRisk_gai_risk_groupings" (
	"GaiRisk_id" INTEGER,
	gai_risk_groupings VARCHAR(21),
	PRIMARY KEY ("GaiRisk_id", gai_risk_groupings),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_groupings_gai_risk_groupings" ON "GaiRisk_gai_risk_groupings" (gai_risk_groupings);
CREATE INDEX "ix_GaiRisk_gai_risk_groupings_GaiRisk_id" ON "GaiRisk_gai_risk_groupings" ("GaiRisk_id");

CREATE TABLE "GaiRisk_gai_risk_lifecycle_stages" (
	"GaiRisk_id" INTEGER,
	gai_risk_lifecycle_stages VARCHAR(15),
	PRIMARY KEY ("GaiRisk_id", gai_risk_lifecycle_stages),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_lifecycle_stages_gai_risk_lifecycle_stages" ON "GaiRisk_gai_risk_lifecycle_stages" (gai_risk_lifecycle_stages);
CREATE INDEX "ix_GaiRisk_gai_risk_lifecycle_stages_GaiRisk_id" ON "GaiRisk_gai_risk_lifecycle_stages" ("GaiRisk_id");

CREATE TABLE "GaiRisk_gai_risk_scopes" (
	"GaiRisk_id" INTEGER,
	gai_risk_scopes VARCHAR(29),
	PRIMARY KEY ("GaiRisk_id", gai_risk_scopes),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_scopes_gai_risk_scopes" ON "GaiRisk_gai_risk_scopes" (gai_risk_scopes);
CREATE INDEX "ix_GaiRisk_gai_risk_scopes_GaiRisk_id" ON "GaiRisk_gai_risk_scopes" ("GaiRisk_id");

CREATE TABLE "GaiRisk_gai_risk_sources" (
	"GaiRisk_id" INTEGER,
	gai_risk_sources VARCHAR(20),
	PRIMARY KEY ("GaiRisk_id", gai_risk_sources),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_sources_gai_risk_sources" ON "GaiRisk_gai_risk_sources" (gai_risk_sources);
CREATE INDEX "ix_GaiRisk_gai_risk_sources_GaiRisk_id" ON "GaiRisk_gai_risk_sources" ("GaiRisk_id");

CREATE TABLE "GaiRisk_gai_risk_time_scales" (
	"GaiRisk_id" INTEGER,
	gai_risk_time_scales VARCHAR(8),
	PRIMARY KEY ("GaiRisk_id", gai_risk_time_scales),
	FOREIGN KEY("GaiRisk_id") REFERENCES "GaiRisk" (id)
);
CREATE INDEX "ix_GaiRisk_gai_risk_time_scales_gai_risk_time_scales" ON "GaiRisk_gai_risk_time_scales" (gai_risk_time_scales);
CREATE INDEX "ix_GaiRisk_gai_risk_time_scales_GaiRisk_id" ON "GaiRisk_gai_risk_time_scales" ("GaiRisk_id");

CREATE TABLE "GaiSubcategory_gai_subcategory_actor_tasks" (
	"GaiSubcategory_id" INTEGER,
	gai_subcategory_actor_tasks VARCHAR(36),
	PRIMARY KEY ("GaiSubcategory_id", gai_subcategory_actor_tasks),
	FOREIGN KEY("GaiSubcategory_id") REFERENCES "GaiSubcategory" (id)
);
CREATE INDEX "ix_GaiSubcategory_gai_subcategory_actor_tasks_GaiSubcategory_id" ON "GaiSubcategory_gai_subcategory_actor_tasks" ("GaiSubcategory_id");
CREATE INDEX "ix_GaiSubcategory_gai_subcategory_actor_tasks_gai_subcategory_actor_tasks" ON "GaiSubcategory_gai_subcategory_actor_tasks" (gai_subcategory_actor_tasks);

CREATE TABLE "GaiPrimaryConsideration_gai_consideration_sections" (
	"GaiPrimaryConsideration_id" INTEGER,
	gai_consideration_sections TEXT,
	PRIMARY KEY ("GaiPrimaryConsideration_id", gai_consideration_sections),
	FOREIGN KEY("GaiPrimaryConsideration_id") REFERENCES "GaiPrimaryConsideration" (id)
);
CREATE INDEX "ix_GaiPrimaryConsideration_gai_consideration_sections_gai_consideration_sections" ON "GaiPrimaryConsideration_gai_consideration_sections" (gai_consideration_sections);
CREATE INDEX "ix_GaiPrimaryConsideration_gai_consideration_sections_GaiPrimaryConsideration_id" ON "GaiPrimaryConsideration_gai_consideration_sections" ("GaiPrimaryConsideration_id");

CREATE TABLE "AiRmfImpact" (
	ai_rmf_likelihood TEXT,
	ai_rmf_magnitude TEXT,
	ai_rmf_impact_direction VARCHAR(8) NOT NULL,
	ai_rmf_id TEXT NOT NULL,
	title TEXT,
	description TEXT,
	"AiRmfRisk_ai_rmf_id" TEXT,
	"AiRmfResidualRisk_ai_rmf_id" TEXT,
	PRIMARY KEY (ai_rmf_id),
	FOREIGN KEY("AiRmfRisk_ai_rmf_id") REFERENCES "AiRmfRisk" (ai_rmf_id),
	FOREIGN KEY("AiRmfResidualRisk_ai_rmf_id") REFERENCES "AiRmfResidualRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfImpact_ai_rmf_id" ON "AiRmfImpact" (ai_rmf_id);

CREATE TABLE "AiRmfSubcategory" (
	id INTEGER NOT NULL,
	ai_rmf_subcategory_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"AiRmfCategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfCategory_id") REFERENCES "AiRmfCategory" (id)
);
CREATE INDEX "ix_AiRmfSubcategory_id" ON "AiRmfSubcategory" (id);

CREATE TABLE "AiRmfRisk_ai_rmf_risk_characteristics" (
	"AiRmfRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_characteristics VARCHAR(30),
	PRIMARY KEY ("AiRmfRisk_ai_rmf_id", ai_rmf_risk_characteristics),
	FOREIGN KEY("AiRmfRisk_ai_rmf_id") REFERENCES "AiRmfRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_characteristics_ai_rmf_risk_characteristics" ON "AiRmfRisk_ai_rmf_risk_characteristics" (ai_rmf_risk_characteristics);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_characteristics_AiRmfRisk_ai_rmf_id" ON "AiRmfRisk_ai_rmf_risk_characteristics" ("AiRmfRisk_ai_rmf_id");

CREATE TABLE "AiRmfRisk_ai_rmf_risk_lifecycle_stages" (
	"AiRmfRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_lifecycle_stages VARCHAR(24),
	PRIMARY KEY ("AiRmfRisk_ai_rmf_id", ai_rmf_risk_lifecycle_stages),
	FOREIGN KEY("AiRmfRisk_ai_rmf_id") REFERENCES "AiRmfRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_lifecycle_stages_ai_rmf_risk_lifecycle_stages" ON "AiRmfRisk_ai_rmf_risk_lifecycle_stages" (ai_rmf_risk_lifecycle_stages);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_lifecycle_stages_AiRmfRisk_ai_rmf_id" ON "AiRmfRisk_ai_rmf_risk_lifecycle_stages" ("AiRmfRisk_ai_rmf_id");

CREATE TABLE "AiRmfRisk_ai_rmf_risk_responses" (
	"AiRmfRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_responses VARCHAR(12),
	PRIMARY KEY ("AiRmfRisk_ai_rmf_id", ai_rmf_risk_responses),
	FOREIGN KEY("AiRmfRisk_ai_rmf_id") REFERENCES "AiRmfRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_responses_AiRmfRisk_ai_rmf_id" ON "AiRmfRisk_ai_rmf_risk_responses" ("AiRmfRisk_ai_rmf_id");
CREATE INDEX "ix_AiRmfRisk_ai_rmf_risk_responses_ai_rmf_risk_responses" ON "AiRmfRisk_ai_rmf_risk_responses" (ai_rmf_risk_responses);

CREATE TABLE "AiRmfResidualRisk_ai_rmf_risk_characteristics" (
	"AiRmfResidualRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_characteristics VARCHAR(30),
	PRIMARY KEY ("AiRmfResidualRisk_ai_rmf_id", ai_rmf_risk_characteristics),
	FOREIGN KEY("AiRmfResidualRisk_ai_rmf_id") REFERENCES "AiRmfResidualRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_characteristics_AiRmfResidualRisk_ai_rmf_id" ON "AiRmfResidualRisk_ai_rmf_risk_characteristics" ("AiRmfResidualRisk_ai_rmf_id");
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_characteristics_ai_rmf_risk_characteristics" ON "AiRmfResidualRisk_ai_rmf_risk_characteristics" (ai_rmf_risk_characteristics);

CREATE TABLE "AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages" (
	"AiRmfResidualRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_lifecycle_stages VARCHAR(24),
	PRIMARY KEY ("AiRmfResidualRisk_ai_rmf_id", ai_rmf_risk_lifecycle_stages),
	FOREIGN KEY("AiRmfResidualRisk_ai_rmf_id") REFERENCES "AiRmfResidualRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages_AiRmfResidualRisk_ai_rmf_id" ON "AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages" ("AiRmfResidualRisk_ai_rmf_id");
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages_ai_rmf_risk_lifecycle_stages" ON "AiRmfResidualRisk_ai_rmf_risk_lifecycle_stages" (ai_rmf_risk_lifecycle_stages);

CREATE TABLE "AiRmfResidualRisk_ai_rmf_risk_responses" (
	"AiRmfResidualRisk_ai_rmf_id" TEXT,
	ai_rmf_risk_responses VARCHAR(12),
	PRIMARY KEY ("AiRmfResidualRisk_ai_rmf_id", ai_rmf_risk_responses),
	FOREIGN KEY("AiRmfResidualRisk_ai_rmf_id") REFERENCES "AiRmfResidualRisk" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_responses_ai_rmf_risk_responses" ON "AiRmfResidualRisk_ai_rmf_risk_responses" (ai_rmf_risk_responses);
CREATE INDEX "ix_AiRmfResidualRisk_ai_rmf_risk_responses_AiRmfResidualRisk_ai_rmf_id" ON "AiRmfResidualRisk_ai_rmf_risk_responses" ("AiRmfResidualRisk_ai_rmf_id");

CREATE TABLE "GaiSuggestedAction_gai_action_risks" (
	"GaiSuggestedAction_id" INTEGER,
	gai_action_risks VARCHAR(37),
	PRIMARY KEY ("GaiSuggestedAction_id", gai_action_risks),
	FOREIGN KEY("GaiSuggestedAction_id") REFERENCES "GaiSuggestedAction" (id)
);
CREATE INDEX "ix_GaiSuggestedAction_gai_action_risks_gai_action_risks" ON "GaiSuggestedAction_gai_action_risks" (gai_action_risks);
CREATE INDEX "ix_GaiSuggestedAction_gai_action_risks_GaiSuggestedAction_id" ON "GaiSuggestedAction_gai_action_risks" ("GaiSuggestedAction_id");

CREATE TABLE "AiRmfSuggestedAction" (
	id INTEGER NOT NULL,
	ai_rmf_suggested_action_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"AiRmfSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfSuggestedAction_id" ON "AiRmfSuggestedAction" (id);

CREATE TABLE "AiRmfDocumentationItem" (
	id INTEGER NOT NULL,
	ai_rmf_documentation_id TEXT NOT NULL,
	description TEXT NOT NULL,
	"AiRmfSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfDocumentationItem_id" ON "AiRmfDocumentationItem" (id);

CREATE TABLE "AiRmfResource" (
	id INTEGER NOT NULL,
	title TEXT NOT NULL,
	ai_rmf_resource_uuid TEXT NOT NULL,
	ai_rmf_resource_address TEXT,
	"AiRmfSubcategory_id" INTEGER,
	PRIMARY KEY (id),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfResource_id" ON "AiRmfResource" (id);

CREATE TABLE "AiRmfImpact_ai_rmf_impact_affected_parties" (
	"AiRmfImpact_ai_rmf_id" TEXT,
	ai_rmf_impact_affected_parties VARCHAR(13),
	PRIMARY KEY ("AiRmfImpact_ai_rmf_id", ai_rmf_impact_affected_parties),
	FOREIGN KEY("AiRmfImpact_ai_rmf_id") REFERENCES "AiRmfImpact" (ai_rmf_id)
);
CREATE INDEX "ix_AiRmfImpact_ai_rmf_impact_affected_parties_AiRmfImpact_ai_rmf_id" ON "AiRmfImpact_ai_rmf_impact_affected_parties" ("AiRmfImpact_ai_rmf_id");
CREATE INDEX "ix_AiRmfImpact_ai_rmf_impact_affected_parties_ai_rmf_impact_affected_parties" ON "AiRmfImpact_ai_rmf_impact_affected_parties" (ai_rmf_impact_affected_parties);

CREATE TABLE "AiRmfSubcategory_ai_rmf_subcategory_about" (
	"AiRmfSubcategory_id" INTEGER,
	ai_rmf_subcategory_about TEXT,
	PRIMARY KEY ("AiRmfSubcategory_id", ai_rmf_subcategory_about),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_about_ai_rmf_subcategory_about" ON "AiRmfSubcategory_ai_rmf_subcategory_about" (ai_rmf_subcategory_about);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_about_AiRmfSubcategory_id" ON "AiRmfSubcategory_ai_rmf_subcategory_about" ("AiRmfSubcategory_id");

CREATE TABLE "AiRmfSubcategory_ai_rmf_subcategory_ai_actors" (
	"AiRmfSubcategory_id" INTEGER,
	ai_rmf_subcategory_ai_actors VARCHAR(36),
	PRIMARY KEY ("AiRmfSubcategory_id", ai_rmf_subcategory_ai_actors),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_ai_actors_ai_rmf_subcategory_ai_actors" ON "AiRmfSubcategory_ai_rmf_subcategory_ai_actors" (ai_rmf_subcategory_ai_actors);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_ai_actors_AiRmfSubcategory_id" ON "AiRmfSubcategory_ai_rmf_subcategory_ai_actors" ("AiRmfSubcategory_id");

CREATE TABLE "AiRmfSubcategory_ai_rmf_subcategory_topics" (
	"AiRmfSubcategory_id" INTEGER,
	ai_rmf_subcategory_topics TEXT,
	PRIMARY KEY ("AiRmfSubcategory_id", ai_rmf_subcategory_topics),
	FOREIGN KEY("AiRmfSubcategory_id") REFERENCES "AiRmfSubcategory" (id)
);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_topics_ai_rmf_subcategory_topics" ON "AiRmfSubcategory_ai_rmf_subcategory_topics" (ai_rmf_subcategory_topics);
CREATE INDEX "ix_AiRmfSubcategory_ai_rmf_subcategory_topics_AiRmfSubcategory_id" ON "AiRmfSubcategory_ai_rmf_subcategory_topics" ("AiRmfSubcategory_id");
