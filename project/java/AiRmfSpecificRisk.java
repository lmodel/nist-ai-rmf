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
  A risk that Appendix B says is new or increased for AI compared with traditional software.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfSpecificRisk  {

  private String title;
  private String description;
  private int aiRmfSpecificRiskPosition;


}