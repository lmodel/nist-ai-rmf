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
  How GAI can be tested before deployment while better approaches mature, and where current tests fall short.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiPreDeploymentTestingConsideration extends GaiPrimaryConsideration {

  private List<GaiStructuredFeedback> gaiStructuredFeedback;


}