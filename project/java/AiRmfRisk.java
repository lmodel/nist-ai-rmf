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
  How likely an event is, combined with how severe its consequences are.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfRisk extends AiRmfRecord {

  private String aiRmfLikelihood;
  private String aiRmfMagnitude;
  private AiRmfSystem aiRmfRiskSystem;
  private List<AiRmfImpact> aiRmfRiskImpacts;
  private List<String> aiRmfRiskCharacteristics;
  private List<String> aiRmfRiskLifecycleStages;
  private List<String> aiRmfRiskResponses;
  private String aiRmfRiskPriority;
  private AiRmfRiskTolerance aiRmfRiskTolerance;


}