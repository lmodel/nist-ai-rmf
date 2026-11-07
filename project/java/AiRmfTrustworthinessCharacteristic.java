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
  A characteristic of trustworthy AI systems, each with a subsection of section 3.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfTrustworthinessCharacteristic  {

  private String description;
  private String aiRmfCharacteristicName;
  private String aiRmfCharacteristicSection;
  private Boolean aiRmfCharacteristicIsBase;
  private Boolean aiRmfCharacteristicRelatesToAll;


}