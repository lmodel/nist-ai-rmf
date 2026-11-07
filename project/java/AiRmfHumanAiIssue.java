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
  An issue of human-AI interaction that Appendix C says merits further consideration and research.
**/
@Data
@EqualsAndHashCode(callSuper=false)
public class AiRmfHumanAiIssue  {

  private String title;
  private String description;
  private int aiRmfHumanAiIssueNumber;


}