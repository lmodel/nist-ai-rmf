package example;

/* metamodel_version: 1.12.0 */
/* version: 1.0.0 */
import java.net.URI;
import java.time.LocalDate;
import java.time.LocalTime;
import java.time.ZonedDateTime;
import java.util.List;
import lombok.*;

/**
  One edition of the AI RMF as a whole, with the Core and the lists the publication gives.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfFramework  {

  private String aiRmfVersion;
  private List<AiRmfFunction> aiRmfFunctions;
  private List<AiRmfTrustworthinessCharacteristic> aiRmfCharacteristics;
  private List<AiRmfDimension> aiRmfDimensions;
  private List<AiRmfLifecycleStage> aiRmfLifecycleStages;
  private List<AiRmfActorTask> aiRmfActorTaskList;
  private List<AiRmfManagementChallenge> aiRmfManagementChallenges;
  private List<AiRmfSpecificRisk> aiRmfSpecificRisks;
  private List<AiRmfHumanAiIssue> aiRmfHumanAiIssues;
  private List<AiRmfAttribute> aiRmfAttributes;


}