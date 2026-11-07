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
  How an organization's governance can be revisited for GAI, including across the AI value chain.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiGovernanceConsideration extends GaiPrimaryConsideration {

  private List<String> gaiGovernancePlans;
  private List<String> gaiThirdPartyControls;


}