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
  A machine-based system that produces outputs such as predictions or decisions for given objectives, with varying autonomy.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfSystem extends AiRmfRecord {

  private List<String> aiRmfSystemIntendedPurposes;
  private List<String> aiRmfSystemDeploymentSettings;
  private List<String> aiRmfSystemLifecycleStages;
  private List<AiRmfActor> aiRmfSystemActors;


}