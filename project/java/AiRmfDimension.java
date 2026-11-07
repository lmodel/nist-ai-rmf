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
  One of the five key socio-technical dimensions of an AI system in Figure 2.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfDimension  {

  private String description;
  private String aiRmfDimensionName;
  private String aiRmfDimensionAudience;


}