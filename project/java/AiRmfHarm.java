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
  A negative impact, sorted as in Figure 1 by whether it falls on people, an organization or an ecosystem.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfHarm extends AiRmfImpact {

  private String aiRmfHarmCategory;
  private String aiRmfHarmExample;


}