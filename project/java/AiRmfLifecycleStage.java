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
  A stage of the AI lifecycle as a column of Figure 3 shows it, under its dimension.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfLifecycleStage  {

  private String description;
  private String aiRmfLifecycleStageName;
  private String aiRmfLifecycleStageDimension;
  private String aiRmfLifecycleStageTevv;
  private List<String> aiRmfLifecycleStageRepresentativeActors;


}