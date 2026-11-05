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
  A step an organization or AI actor can take to manage GAI risks, which one row of a table states.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiSuggestedAction  {

  private String gaiActionId;
  private String description;
  private List<String> gaiActionRisks;


}