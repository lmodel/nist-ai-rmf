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
  A structured exercise that probes an AI system for flaws and vulnerabilities, often with its developers.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiAiRedTeaming extends GaiStructuredFeedback {

  private List<String> gaiRedTeamingTypes;


}