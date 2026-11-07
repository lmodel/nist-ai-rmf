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
  The Generative AI Profile as a whole, a cross-sectoral profile of the AI RMF and a companion resource to it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiProfile extends AiRmfProfile {

  private List<GaiRisk> gaiRisks;
  private List<GaiSubcategory> gaiSubcategories;
  private List<GaiPrimaryConsideration> gaiPrimaryConsiderations;


}