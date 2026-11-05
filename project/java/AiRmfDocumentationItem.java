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
  One thing the Playbook suggests an organization document for a subcategory.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfDocumentationItem  {

  private String aiRmfDocumentationId;
  private String description;


}