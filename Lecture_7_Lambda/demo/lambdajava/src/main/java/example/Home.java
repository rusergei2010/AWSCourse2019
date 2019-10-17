package example;
import com.amazonaws.services.lambda.runtime.Context;
import com.amazonaws.services.lambda.runtime.RequestHandler;

public class Home implements RequestHandler {

    @Override
    public String handleRequest(Object input, Context context) {
        return "Received message: " + input;
    }
}