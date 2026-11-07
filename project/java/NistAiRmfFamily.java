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
  The two publications held in one document, each as its own schema renders it.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class NistAiRmfFamily  {

  private AiRmfFramework nistAiRmfFramework;
  private GaiProfile nistAiRmfGenerativeAiProfile;


}