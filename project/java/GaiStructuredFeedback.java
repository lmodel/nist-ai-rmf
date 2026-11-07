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
  A way of using structured public feedback to evaluate whether GAI systems perform as intended.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public abstract class GaiStructuredFeedback  {

  private String gaiFeedbackType;
  private String title;
  private String description;


}