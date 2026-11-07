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
  An implementation of the Core's functions, categories and subcategories for a setting, application or technology, based on the adopter's requirements, risk tolerance and resources.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfProfile extends AiRmfRecord {

  private List<String> aiRmfProfileKinds;
  private String aiRmfProfileSetting;
  private List<String> aiRmfProfileSubcategories;


}