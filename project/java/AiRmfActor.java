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
  An organization or individual with an active role in an AI system's lifecycle.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfActor extends AiRmfRecord {

  private List<String> aiRmfActorTasks;
  private String aiRmfActorAudience;
  private List<String> aiRmfActorLifecycleStages;


}