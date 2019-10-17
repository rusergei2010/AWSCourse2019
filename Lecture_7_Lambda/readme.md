# Lambda

1. Cost Explorer
2. Lambda


## Practice

Test Scenario 1.
1. Create lambda function with Console
2. Select "Amazon CloudWatch Logs" and see allowed actions
   When adding new actions this permission tabel will be updated
3. Press 'Test' and enter event name. Exectute - click twice. See output and duration.
4. add 'event['key1']'
5. Open Dashboard. See monitors.


Test Scenario 2
1. Create Lambda with Node.js 
2. Call Lambda from local computer: $ aws lambda invoke --function-name MAIL_Service --payload '{"key1":"Sergey"}' log
Change index.js
exports.handler = async (event) => {
    // TODO implement
    const response = {
        statusCode: 200,
        key: event['key1'],
        body: JSON.stringify('Hello from Lambda!'),
    };
    return response;
};
See monitoring
>cat log

Test Scenario 3
1. Create Java App and add to run as Lambda
 mvn package
Produces: Lecture_7_Lambda\demo\lambdajava\target\lambda-java-example-1.0-SNAPSHOT-shaded.jar
2. Create Lambda from java8 runtime and upload jar. Test it.

Test Scenario 4.
1.  Lambda With Cron Schedualer, CloudWatch Event -> Add Rule

Test Scenario 5.
1. Go to "Create Lambda" from "Browse serverless app repository"
2. Add S3 bucket tracker (for new Objects). Play with it.
3. Open "Amazon API Gateway"
4. Add postman POST request /Peod/send like
   https://b3nb74541k.execute-api.us-east-2.amazonaws.com/Prod
5. Open Monitoring and "View Logs in Cloud Watch"
6. Applications -> Monitoring and -> Monitoring Amazon API Gateway

Test Scenario 6.
1. Create Lambda 'MAIL_Service' and Link to S3 Create Object event
2. Also Add Roles: S3, SES
index.js->
```
var aws = require('aws-sdk');
var ses = new aws.SES({ region: 'us-east-1' })

exports.handler = (event, context, callback) => {
    
     var params = {
        Destination: {
            ToAddresses: ["Sergei_Zheleznov@epam.com"]
        },
        Message: {
            Body: {
                Text: { Data: "Test"
                    
                }
                
            },
            
            Subject: { Data: "Test Email"
                
            }
        },
        Source: "sourceEmailAddress"
    };

    
     ses.sendEmail(params, function (err, data) {
        callback(null, {err: err, data: data});
        if (err) {
            console.log(err);
            context.fail(err);
        } else {
            
            console.log(data);
            context.succeed(event);
        }
    });
};
```

or

```
const AWS = require('aws-sdk');
const SES = new AWS.SES({ region: 'us-east-1' });

exports.handler = async (params)  => {
  console.log(params);

//   const {
//     to:'Sergei_Zheleznov@epam.com',
//     from,
//     reply_to: replyTo,
//     subject,
//   } = params;
  const to = 'Sergei_Zheleznov@epam.com';
  const from = 'Sergei_Zheleznov@epam.com';
  const replyTo = 'Sergei_Zheleznov@epam.com';
  const subject = 'Sergei_Zheleznov';
  
  
  const fromBase64 = Buffer.from(from).toString('base64');

  const htmlBody = `
    <!DOCTYPE html>
    <html>
      <head></head>
      <body><h1>Hello world!</h1></body>
    </html>
  `;

  const sesParams = {
    Destination: {
      ToAddresses: [to],
    },
    Message: {
      Body: {
        Html: {
          Charset: 'UTF-8',
          Data: htmlBody,
        },
      },
      Subject: {
        Charset: 'UTF-8',
        Data: subject,
      },
    },
    ReplyToAddresses: [replyTo],
    Source: `=?utf-8?B?${fromBase64}?=Sergei_Zheleznov@epam.com`,
  };

  const response = await SES.sendEmail(sesParams).promise();

  console.log(response);
}
```

2. aws lambda invoke --function-name MAIL_Service --payload '{"key1":"Sergey"}' log
3. Add Permission in case of error. SES should appear in the resources of Lambda.
4. Go to SES mail verification service.
$aws lambda add-permission --function-name MAIL_Service --action lambda:InvokeFunction --statement-id sns --principal sns.amazonaws.com --output text
4. If inokation and Mail Service is not available then check SergeySESRolesForLambda role in IAM and add SES permissions
5. Check Whatch Logs for latest logging: Logs -> Mail_SERVICE log

SES can be deployed on one region only: us-east-2!
err":{"message":"Inaccessible host: `email.us-east-2.amazonaws.com'. This service may not be available in the `us-east-2'
 Replace recipientEmailAddress with at least one Amazon SES-verified email address. Replace sourceEmailAddress with your Amazon SES-verified sender email address.
 


	

Links:
1. https://docs.aws.amazon.com/lambda/latest/dg/getting-started-create-function.html
2. https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-concepts.html
3. https://aws.amazon.com/blogs/architecture/understanding-the-different-ways-to-invoke-lambda-functions/
4. https://developer.amazon.com/docs/alexa-skills-kit-sdk-for-java/develop-your-first-skill.html
5. https://docs.aws.amazon.com/lambda/latest/dg/lambda-invocation.html
6. 