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
  A group of related outcomes within a function, such as GOVERN 1, which Tables 1 to 4 state.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfCategory  {

  private String aiRmfCategoryId;
  private String description;
  private List<AiRmfSubcategory> aiRmfCategorySubcategories;


}