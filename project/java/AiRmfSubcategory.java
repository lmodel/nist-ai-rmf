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
  A specific outcome within a category, such as GOVERN 1.1, which Tables 1 to 4 state, and its Playbook material.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfSubcategory  {

  private String aiRmfSubcategoryId;
  private String description;
  private List<String> aiRmfSubcategoryAbout;
  private List<AiRmfSuggestedAction> aiRmfSubcategorySuggestedActions;
  private List<AiRmfDocumentationItem> aiRmfSubcategoryDocumentation;
  private List<AiRmfResource> aiRmfSubcategoryTransparencyResources;
  private List<AiRmfResource> aiRmfSubcategoryReferences;
  private List<String> aiRmfSubcategoryAiActors;
  private List<String> aiRmfSubcategoryTopics;


}