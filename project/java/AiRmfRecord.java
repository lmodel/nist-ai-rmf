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
  The base of the classes that record an adopter's own facts, such as one of its AI systems or risks, as distinct from what the publication itself lists.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class AiRmfRecord  {

  private URI aiRmfId;
  private String title;
  private String description;


}