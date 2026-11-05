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
  An AI RMF subcategory as one table of section 3 addresses it. The Profile covers only some of the 72.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class GaiSubcategory  {

  private String aiRmfSubcategoryId;
  private String description;
  private List<GaiSuggestedAction> gaiSubcategoryActions;
  private List<String> gaiSubcategoryActorTasks;


}