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
  A key attribute of the AI RMF in Appendix D, which guided its development.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfAttribute  {

  private String title;
  private String description;
  private int aiRmfAttributeNumber;


}