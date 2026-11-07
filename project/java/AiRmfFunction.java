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
  One of the four functions that organize AI risk management at the highest level. GOVERN cuts across the other three.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfFunction  {

  private String aiRmfFunctionId;
  private String description;
  private List<AiRmfCategory> aiRmfFunctionCategories;


}