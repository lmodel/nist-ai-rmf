// The site's values and options, in one place. scripts/config.mjs reads this
// file, fills in every option left out, settles each "auto" against the
// repository and checks the required values. `node scripts/config.mjs`
// prints the result. Nothing here runs code, so the pages that show the
// title import it too.
//
// The first five values are required. The rest are optional: leave one out,
// or set it to "auto", and the site shows that part of the repository when
// the repository has it. Set it to null to leave that part out.

// The repository, as owner/name, and the site's address: the owner's GitHub
// Pages domain and the path under it. A user site (the <owner>.github.io
// repository) or a custom domain sets BASE to "".
export const REPO = "lmodel/nist-ai-rmf";
export const SITE = "https://lmodel.github.io";
export const BASE = "/nist-ai-rmf";

// The site's title, in the header and on every social card, and its
// description, for search engines and as the home page's tagline when
// HOME.tagline is not set.
export const TITLE = "nist-ai-rmf";
export const DESCRIPTION = "NIST AI RMF family: NIST AI 100-1 and NIST AI 600-1 as one schema (LinkML)";

// The branch an "Edit page" link opens.
export const BRANCH = "main";

// A custom domain, which the sync writes to public/CNAME, or null for a
// Pages address. The site leaves the domain's DNS to the repository.
export const CUSTOM_DOMAIN = null;

// The logo, as paths from the repository root: a light version, a dark one
// (the light one again when left out) and a favicon (the light logo when it
// is an SVG, else the site's own ladder mark). "auto" takes the Knowledge
// Trust Ladder logo: a knowledge-trust-ladder-logo.svg the repository
// already has, or else the copy in src/assets/. A single path is the light
// version alone. null shows the title as text.
//   export const LOGO = { light: ".assets/logo.svg", dark: ".assets/logo-dark.svg" };
export const LOGO = "auto";

// The folder of figures the README and the docs pages show, served under
// /assets/. "auto" takes .assets/ when there is one.
export const ASSETS = "auto";

// The docs pages: a folder, the sidebar groups its pages sit in (each page
// named by its path under the folder, without .md), and the paths under the
// folder that are not pages of the site, each a file or a folder. With no
// groups, every page sits in one Guides group, by title, with the folder's
// index.md first as its Overview. With groups, the sync stops with an error
// when a group names a missing page or a page has no group, so a new page
// cannot go missing from the sidebar. "auto" takes docs/ when there is one.
// null shows no docs pages.
//   export const DOCS = { dir: "docs", groups: [{ label: "Guides", pages: ["install", "usage"] }], exclude: ["templates-linkml"] };
export const DOCS = { dir: "docs", exclude: ["templates-linkml"] };

// Old addresses under BASE, each redirected to a page of the site, such as
// the addresses a retired mkdocs site gave its pages and a w3id rule still
// names. An entry whose key and value both end in /[...slug] stands for one
// redirect per schema page.
//   export const REDIRECTS = { "/elements": "/schema/", "/elements/[...slug]": "/schema/[...slug]", "/about": "/docs/about/" };
export const REDIRECTS = {
  "/about": "/docs/about/",
  "/elements": "/schema/",
  "/elements/AiActor": "/schema/AiRmfActor/",
  "/elements/AiActorTask": "/schema/AiRmfActorTask/",
  "/elements/AiActorTaskEnum": "/schema/AiRmfActorTaskName/",
  "/elements/AiLifecycleStage": "/schema/AiRmfLifecycleStage/",
  "/elements/AiLifecycleStageEnum": "/schema/AiRmfLifecycleStageName/",
  "/elements/AiRedTeaming": "/schema/GaiAiRedTeaming/",
  "/elements/AiRiskDistinctions": "/schema/",
  "/elements/AiRmfDocument": "/schema/AiRmfFramework/",
  "/elements/AiSpecificRisk": "/schema/AiRmfSpecificRisk/",
  "/elements/AiSystem": "/schema/AiRmfSystem/",
  "/elements/AiSystemDimension": "/schema/AiRmfDimension/",
  "/elements/AiSystemDimensionEnum": "/schema/AiRmfDimensionName/",
  "/elements/AudienceEnum": "/schema/AiRmfAudience/",
  "/elements/Base": "/schema/",
  "/elements/Bias": "/schema/AiRmfBias/",
  "/elements/BiasCategoryEnum": "/schema/AiRmfBiasCategory/",
  "/elements/Category": "/schema/AiRmfCategory/",
  "/elements/CategoryCode": "/schema/AiRmfCategoryIdentifier/",
  "/elements/CategoryEnum": "/schema/AiRmfCategoryIdentifier/",
  "/elements/FrameworkAttributes": "/schema/",
  "/elements/FrameworkCore": "/schema/",
  "/elements/Function": "/schema/AiRmfFunction/",
  "/elements/FunctionCode": "/schema/AiRmfFunctionIdentifier/",
  "/elements/FunctionEnum": "/schema/AiRmfFunctionIdentifier/",
  "/elements/GaiActionFunctionPrefixEnum": "/schema/",
  "/elements/GaiActionId": "/schema/GaiActionIdentifier/",
  "/elements/GaiActions": "/schema/",
  "/elements/GaiActorTaskEnum": "/schema/AiRmfActorTaskName/",
  "/elements/GaiBase": "/schema/",
  "/elements/GaiConsiderations": "/schema/",
  "/elements/GaiCore": "/schema/",
  "/elements/GaiFeedback": "/schema/",
  "/elements/GaiLifecycleStageEnum": "/schema/GaiLifecycleStage/",
  "/elements/GaiRiskCategorizationEnum": "/schema/GaiRiskGrouping/",
  "/elements/GaiRiskCategoryEnum": "/schema/GaiRiskName/",
  "/elements/GaiRiskScopeEnum": "/schema/GaiRiskScope/",
  "/elements/GaiRiskSourceEnum": "/schema/GaiRiskSource/",
  "/elements/GaiRiskTimeScaleEnum": "/schema/GaiRiskTimeScale/",
  "/elements/GovernancePracticeEnum": "/schema/GaiGovernancePlan/",
  "/elements/Harm": "/schema/AiRmfHarm/",
  "/elements/HarmCategoryEnum": "/schema/AiRmfHarmCategory/",
  "/elements/HarmToPeopleSubcategoryEnum": "/schema/AiRmfHarmExample/",
  "/elements/HumanAiInteraction": "/schema/",
  "/elements/HumanAiInteractionIssue": "/schema/AiRmfHumanAiIssue/",
  "/elements/Impact": "/schema/AiRmfImpact/",
  "/elements/ImpactSignEnum": "/schema/AiRmfImpactDirection/",
  "/elements/Lifecycle": "/schema/",
  "/elements/NamedThing": "/schema/AiRmfRecord/",
  "/elements/Playbook": "/schema/",
  "/elements/PlaybookCollection": "/schema/AiRmfFramework/",
  "/elements/PlaybookEntry": "/schema/AiRmfSubcategory/",
  "/elements/PrimaryConsiderationEnum": "/schema/",
  "/elements/PrimaryGaiConsideration": "/schema/GaiGovernanceConsideration/",
  "/elements/ProfileConstructs": "/schema/",
  "/elements/ProfileTypeEnum": "/schema/AiRmfProfileKind/",
  "/elements/ProvenanceTechniqueEnum": "/schema/GaiProvenanceTechnique/",
  "/elements/RedTeamingTypeEnum": "/schema/GaiRedTeamingType/",
  "/elements/ResidualRisk": "/schema/AiRmfResidualRisk/",
  "/elements/Risk": "/schema/AiRmfRisk/",
  "/elements/RiskAndHarm": "/schema/",
  "/elements/RiskMeasurementChallenge": "/schema/AiRmfMeasurementChallenge/",
  "/elements/RiskMeasurementChallengeEnum": "/schema/AiRmfMeasurementChallengeName/",
  "/elements/RiskResponseEnum": "/schema/AiRmfRiskResponse/",
  "/elements/RiskTolerance": "/schema/AiRmfRiskTolerance/",
  "/elements/RmfAttribute": "/schema/AiRmfAttribute/",
  "/elements/StructuredFeedbackMethodEnum": "/schema/",
  "/elements/StructuredPublicFeedback": "/schema/GaiStructuredFeedback/",
  "/elements/Subcategory": "/schema/AiRmfSubcategory/",
  "/elements/SubcategoryCode": "/schema/AiRmfSubcategoryIdentifier/",
  "/elements/SuggestedAction": "/schema/GaiSuggestedAction/",
  "/elements/Trustworthiness": "/schema/",
  "/elements/TrustworthinessCharacteristic": "/schema/AiRmfTrustworthinessCharacteristic/",
  "/elements/TrustworthinessCharacteristicEnum": "/schema/AiRmfCharacteristicName/",
  "/elements/about_text": "/schema/ai_rmf_subcategory_about/",
  "/elements/action_id": "/schema/gai_action_id/",
  "/elements/actor_task": "/schema/gai_subcategory_actor_tasks/",
  "/elements/actor_tasks": "/schema/ai_rmf_actor_task_list/",
  "/elements/addressed_by_actions": "/schema/",
  "/elements/addresses": "/schema/ai_rmf_profile_subcategories/",
  "/elements/affects": "/schema/ai_rmf_impact_affected_parties/",
  "/elements/affects_system": "/schema/ai_rmf_risk_system/",
  "/elements/ai_actor_categories": "/schema/ai_rmf_subcategory_ai_actors/",
  "/elements/ai_actors": "/schema/ai_rmf_subcategory_ai_actors/",
  "/elements/ai_dimension": "/schema/",
  "/elements/ai_incident_definition": "/schema/gai_incident_harms/",
  "/elements/ai_specific_risks": "/schema/ai_rmf_specific_risks/",
  "/elements/applies_to_subcategory": "/schema/ai_rmf_subcategory_id/",
  "/elements/attributes": "/schema/ai_rmf_attributes/",
  "/elements/audience": "/schema/ai_rmf_actor_audience/",
  "/elements/bias_category": "/schema/ai_rmf_bias_categories/",
  "/elements/categories": "/schema/ai_rmf_function_categories/",
  "/elements/category": "/schema/ai_rmf_category_id/",
  "/elements/category_code": "/schema/",
  "/elements/category_id": "/schema/ai_rmf_category_id/",
  "/elements/challenge_kind": "/schema/ai_rmf_measurement_challenge_name/",
  "/elements/characteristic_kind": "/schema/ai_rmf_characteristic_name/",
  "/elements/consideration_kind": "/schema/gai_consideration_type/",
  "/elements/current_state": "/schema/",
  "/elements/dimension_kind": "/schema/ai_rmf_dimension_name/",
  "/elements/dimensions": "/schema/ai_rmf_dimensions/",
  "/elements/document": "/schema/",
  "/elements/documentation_questions": "/schema/ai_rmf_subcategory_documentation/",
  "/elements/doi": "/schema/",
  "/elements/entries": "/schema/",
  "/elements/feedback_method_kind": "/schema/gai_feedback_type/",
  "/elements/function_code": "/schema/ai_rmf_function_id/",
  "/elements/function_kind": "/schema/",
  "/elements/function_prefix": "/schema/",
  "/elements/functions": "/schema/ai_rmf_functions/",
  "/elements/gai_risk_catalog": "/schema/gai_risks/",
  "/elements/gai_risk_kind": "/schema/gai_risk_name/",
  "/elements/governance_practices": "/schema/gai_governance_plans/",
  "/elements/harm_category": "/schema/ai_rmf_harm_category/",
  "/elements/harm_to_people_subcategory": "/schema/ai_rmf_harm_example/",
  "/elements/human_ai_interaction_issues": "/schema/ai_rmf_human_ai_issues/",
  "/elements/id": "/schema/ai_rmf_id/",
  "/elements/impact_sign": "/schema/ai_rmf_impact_direction/",
  "/elements/includes_tevv": "/schema/",
  "/elements/is_base_condition": "/schema/ai_rmf_characteristic_is_base/",
  "/elements/is_cross_cutting": "/schema/ai_rmf_characteristic_relates_to_all/",
  "/elements/is_residual": "/schema/",
  "/elements/is_tevv": "/schema/",
  "/elements/legal_basis": "/schema/ai_rmf_risk_tolerance_influences/",
  "/elements/lifecycle_stage": "/schema/gai_risk_lifecycle_stages/",
  "/elements/lifecycle_stages": "/schema/ai_rmf_lifecycle_stages/",
  "/elements/likelihood": "/schema/ai_rmf_likelihood/",
  "/elements/limitations_of_current_approaches": "/schema/",
  "/elements/magnitude": "/schema/ai_rmf_magnitude/",
  "/elements/name": "/schema/title/",
  "/elements/nist-ai-rmf": "/schema/",
  "/elements/outcome": "/schema/",
  "/elements/primary_considerations": "/schema/gai_primary_considerations/",
  "/elements/profile_type": "/schema/ai_rmf_profile_kinds/",
  "/elements/profiles": "/schema/",
  "/elements/provenance_techniques": "/schema/gai_provenance_techniques/",
  "/elements/published_date": "/schema/",
  "/elements/publisher": "/schema/",
  "/elements/red_team_type": "/schema/gai_red_teaming_types/",
  "/elements/references_text": "/schema/ai_rmf_subcategory_references/",
  "/elements/related_impacts": "/schema/ai_rmf_risk_impacts/",
  "/elements/risk_categorization": "/schema/gai_risk_groupings/",
  "/elements/risk_measurement_challenges": "/schema/ai_rmf_management_challenges/",
  "/elements/risk_response": "/schema/ai_rmf_risk_responses/",
  "/elements/risk_scope": "/schema/gai_risk_scopes/",
  "/elements/risk_sources": "/schema/gai_risk_sources/",
  "/elements/section_about": "/schema/ai_rmf_subcategory_about/",
  "/elements/section_actions": "/schema/ai_rmf_subcategory_suggested_actions/",
  "/elements/section_doc": "/schema/ai_rmf_subcategory_documentation/",
  "/elements/section_ref": "/schema/ai_rmf_subcategory_references/",
  "/elements/sector": "/schema/ai_rmf_profile_setting/",
  "/elements/see_also": "/schema/",
  "/elements/source": "/schema/",
  "/elements/stage_kind": "/schema/ai_rmf_lifecycle_stage_name/",
  "/elements/structured_feedback_methods": "/schema/gai_structured_feedback/",
  "/elements/subcategories": "/schema/ai_rmf_category_subcategories/",
  "/elements/subcategory_id": "/schema/ai_rmf_subcategory_id/",
  "/elements/suggested_actions": "/schema/gai_subcategories/",
  "/elements/suggested_actions_text": "/schema/ai_rmf_subcategory_suggested_actions/",
  "/elements/target_state": "/schema/",
  "/elements/task_kind": "/schema/ai_rmf_actor_task_name/",
  "/elements/third_party_considerations": "/schema/gai_third_party_controls/",
  "/elements/time_scale": "/schema/gai_risk_time_scales/",
  "/elements/tolerance_statement": "/schema/",
  "/elements/topic": "/schema/ai_rmf_subcategory_topics/",
  "/elements/topics": "/schema/ai_rmf_subcategory_topics/",
  "/elements/trustworthiness_characteristic": "/schema/ai_rmf_risk_characteristics/",
  "/elements/trustworthiness_characteristics": "/schema/ai_rmf_characteristics/",
  "/elements/type": "/schema/ai_rmf_function_id/",
  "/elements/typical_actors": "/schema/ai_rmf_actor_task_representative_actors/",
  "/elements/version": "/schema/",
  "/elements/[...slug]": "/schema/[...slug]",
};

// A Keep a Changelog file, read as a page per release. "auto" takes
// CHANGELOG.md when it holds a released version.
export const CHANGELOG = "auto";

// The tag a release carries, with {version} for its number. A release page
// links the repository, the docs and the bundle at that tag, and the release
// itself, when git has the tag. A repository whose tags carry no "v" sets
// "{version}". null links nothing.
export const RELEASE_TAG = "v{version}";

// Pages from files outside the docs folder, each at /<slug>/, listed in the
// Guide sidebar after Home under its label. An entry's `retells` names the
// file whose page it retells, and `level` the words for its reading level
// (the label when left out): both pages then offer each other under their
// titles.
//   export const PAGES = [{ slug: "simple", source: "docs/overview.en-simple.md", label: "In short", retells: "docs/overview.md" }];
export const PAGES = [];

// The LinkML schema's pages, which gen-doc writes, under a Schema topic: a
// folder, and the command that writes it, which the sync runs when the
// folder is missing. "auto" takes the first of the root, a linkmo project
// and .linkml/ whose justfile has a gen-doc recipe, else the sidecar's
// domain schema. null shows no schema.
//   export const SCHEMA = { dir: "docs/elements", build: "just gen-doc" };
export const SCHEMA = "auto";

// The data: a folder of SQLite databases and their Datasette metadata, served
// under /browse/ with a page that opens each in Datasette Lite, and the
// command that writes it. The databases go on the public site, so it is null
// until set. "auto" takes a linkmo project's browse/ folder.
//   export const BROWSE = { dir: "browse", build: "just build-browse" };
export const BROWSE = null;

// The workspace of a domain host, which the knowledge-federation workflow
// serves at workspace/ under the site, and which the graph page offers to
// draw beside the bundle's own graph. "auto" offers it when the repository
// has that workflow; true offers it always, and null never.
export const WORKSPACE = "auto";

// The home page: its source, from the file's `# ` title down ("auto" takes
// the README when it has one, else the bundle's own introduction); the
// tagline under the title (a string, { boldLineOf: <file> } for the first
// line of that file that is bold throughout, or DESCRIPTION when null); and
// the buttons, with site-relative links (Browse the bundle, Architecture when
// the docs have an architecture page, Schema when the site shows the schema,
// Bundle health and Knowledge graph when null).
export const HOME = { source: "auto", tagline: null, actions: null };
