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
  A bias to consider and manage, sorted into NIST's three major categories.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfBias extends AiRmfRecord {

  private List<String> aiRmfBiasCategories;


}