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
  One of the four challenges for AI risk management in section 1.2.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfManagementChallenge  {

  private String description;
  private String aiRmfManagementChallengeName;
  private List<AiRmfMeasurementChallenge> aiRmfManagementChallengeMeasurementChallenges;


}