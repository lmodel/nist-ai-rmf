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
  A source the Playbook points to, by the title and address NIST's catalog gives it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfResource  {

  private String title;
  private String aiRmfResourceUuid;
  private URI aiRmfResourceAddress;


}