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
  One of the challenges of measuring AI risk in section 1.2.1.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfMeasurementChallenge  {

  private String description;
  private String aiRmfMeasurementChallengeName;


}