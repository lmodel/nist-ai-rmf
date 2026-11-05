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
  A risk that section 2 defines as unique to or made worse by the development and use of GAI.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiRisk  {

  private String description;
  private String gaiRiskName;
  private String gaiRiskSection;
  private List<String> gaiRiskCharacteristics;
  private List<String> gaiRiskGroupings;
  private List<String> gaiRiskLifecycleStages;
  private List<String> gaiRiskScopes;
  private List<String> gaiRiskSources;
  private List<String> gaiRiskTimeScales;


}