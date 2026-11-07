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
  How documenting, reporting and sharing AI incidents helps prevent harm, though no formal channels exist.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiIncidentDisclosureConsideration extends GaiPrimaryConsideration {

  private List<String> gaiIncidentHarms;


}