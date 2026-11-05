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
  An organization's or AI actor's readiness to bear risk to achieve its objectives. The AI RMF prescribes none.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfRiskTolerance extends AiRmfRecord {

  private AiRmfActor aiRmfRiskToleranceHolder;
  private List<String> aiRmfRiskToleranceInfluences;


}