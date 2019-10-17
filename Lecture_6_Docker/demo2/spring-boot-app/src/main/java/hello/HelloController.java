package hello;

import org.springframework.web.bind.annotation.RestController;
import org.springframework.web.bind.annotation.RequestMapping;

@RestController
public class HelloController {
    
    @RequestMapping("/hello")
    public String index() {
        return "This is Controller call for EC2 check. Greetings from Spring Boot!";
    }
    
}
