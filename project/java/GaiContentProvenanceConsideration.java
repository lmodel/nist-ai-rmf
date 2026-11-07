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
  How tracking the origin and history of content helps tell authentic content from synthetic content.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiContentProvenanceConsideration extends GaiPrimaryConsideration {

  private List<String> gaiProvenanceTechniques;


}