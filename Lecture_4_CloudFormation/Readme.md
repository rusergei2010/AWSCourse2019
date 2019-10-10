# CloudFormation


## Lecture agenda

  * Why CloudFormation template?
  * Workflow
  * CloudFormation stack
  * Building Blocks
  * Sample Stack
  
Practice:
  
1. Take the script: elb-with-two-instances.cf.json for automation
2. Explain structure and validate it:
	>aws cloudformation validate-template \
--template-body file://./elb-with-two-instances.cf.json

3. Invlidate it - corrupt with minor changes
4. Create stack (validation occurs before anyway). Set Input Parameters.

	>aws cloudformation create-stack \
--stack-name crash-course \
--template-body file://./elb-with-two-instances.cf.json \
--parameters ParameterKey=KeyName,ParameterValue=lecture_4_ssh ParameterKey=InstanceType,ParameterValue=t2.micro

lecture_4_ssh - check if it exists or fix

5. Stack can be referred locally file:// or S3 or github url. Output can be embedded into CICD.
   Stack is created and consists of Events.
6. Open in Console
7. Can create ping in Jenkins for many stacks
8. Delete Stack. Resources will be delete. Can be preserved if needed. But collide.
9. Open "Outputs" in Stack service.
10. Tagging is assigned. All AZs in the region. Health Check. Check EC2 is InService.

12. Update stack:
	aws cloudformation update-stack \
--stack-name crash-course-3 \
--template-body file://./elb-with-two-instances.cf.json \
--parameters ParameterKey=KeyName,ParameterValue=lecture_3_ssh ParameterKey=InstanceType,ParameterValue=t2.micro

13. Fix via SSH browser console https server:
  Use commands:  
  >sudo -s
  >cat /var/www/html/index.html
  >echo '<html></html>' >> /var/www/html/index.html
  >curl -i -XGET localhost:8888 (should return status 200)
  > httpd -k start
  
14. Add another Instance 3 and update.
15. Check ELB DNS - open in browser

## Links:
0. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html
1. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html
2. https://blog.boltops.com/2017/03/24/a-simple-introduction-to-aws-cloudformation-part-3-updating-a-stack
3. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/gettingstarted.templatebasics.html
4. https://www.simplilearn.com/aws-cloudformation-tutorial-article
5. https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html#cross-stack