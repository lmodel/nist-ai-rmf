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
  One step the Playbook suggests towards a subcategory's outcome.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfSuggestedAction  {

  private String aiRmfSuggestedActionId;
  private String description;


}