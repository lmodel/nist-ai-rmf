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
  A consequence of an AI system, which may be an opportunity, a threat or both.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfImpact extends AiRmfRecord {

  private String aiRmfLikelihood;
  private String aiRmfMagnitude;
  private String aiRmfImpactDirection;
  private List<String> aiRmfImpactAffectedParties;


}