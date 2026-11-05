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
  One of the four primary considerations of Appendix A, which also inform the suggested actions.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class GaiPrimaryConsideration  {

  private String gaiConsiderationType;
  private String title;
  private String description;
  private List<String> gaiConsiderationSections;


}