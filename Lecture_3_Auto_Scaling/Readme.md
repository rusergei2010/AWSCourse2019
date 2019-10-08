# Auto-Scaling

## Lecture agenda

  * Tell about EBS/S3 based AMI more
  * Create Two Instances and reproduce Bastion schema    
  ---
  * Resource Scaling
  * ELB
  * Auto-Scaling Groups
  * Monitoring Alarms

IAAS = ECS + EBS - good migration from local premise
Legacy fits this approach

From the previous lecture (remaining)
0. EBS backed AMI and S3 template backed AMI. EBS backed is preferrable.
1. Create two instances and add them into the same Secutiry Group first (configure at start up).
2. SSH to one instance and then SSH to another
3. Add IAM user and Group with Admin Roles, add Key pai and set up locally for epam_user
4. Create a new user profile, reuse: $ aws configure --profile epam_user
5. export AWS_DEFAULT_PROFILE='epam_user'
6. aws ec2 --profile epam_user describe-regions
7. Start another EC2 instance with CLI:
$ aws ec2 run-instances --image-id ami-00c03f7f7f2ec15c3 --key-name lecture_3_ec2 --instance-type t2.micro
8. Check Dashboard
10. ssh another instance. Play with SG.


## Get know Securiry Groups
---

## Get know auto-scaling Groups
4. Create Auto-Scaling Group - horizontal (cores, size - Vertical)
5. Scale - 10 small instance better than 5 medium (scaling starts from 1:))
6. Draw ELB in Lucid with several AZ
7. ELB (classic) evolve to Application LB and Network LB
8. ELB - DNS name -> route to EC2 instances
9. Balancing sends traffic within time slot and swtches to another node
10. Session issue if session is not replicated between nodes
11. Actual for Legacy apps with sessions (Sticky sessions - solution, swtching is disabled)
12. Healthcheck - embedded into ELB (need to configure)
13. Min and Max instances (resources) for Auto-Scaling
14. In AWS Auto-Scaling = Launch Configuration for EC2 + 
	Launch Config = EC2 settings
	Auto-Scaling Group is created from Launch Config (here Min and Max EC2 is defined)
15. Manual + Auto Scaling available
16. Cloud Watch - set of metrics. ELB persist metrics in Cloud Watch
17. Triggering occurs on Metric threashold
18. Scaling Policy is triggered on Alarm that is produced by Metric in Cloud Watch
19. New EC2 is created in Scaling Policy

Praceitce:
1. Cerate ELB for 2 AZ (via CLI)
2. Get and use generated DNS name
3. Run instances with bootstap user data script
4. Register instances on ELB (via CLI)
5. Open ELB in Console and see registered instances (OutOfService)
6. elb configure-health-check (via CLI)
7. What is threashold
8. aws elb show-availability-zones-for-load-balancer --load-balancer-name my-loadbalancer
9. After the instance is configured for ELB then it appears and intercepts traffic from ELB
10. Put down one EC2
11. 1. Restart: aws autoscaling create-launch-configuration --launch-configuration-name .. userdata - "CERATE Launch configuration"
12. 2. Create Autoscaling group (point out the autoscaling configuration for it)
--- Now use the Autoscaling Group (second approach). 
  EC2 instance now do not need tp be registered manually on ELB
  Autoscaling will allow to register EC2 on ELB and start automatically.
13. 3. Use min and max instances at registration time
14. Create Alarms Min and Max (Requests 100 req per minute - SUM type). See monitoring.
15. See states of alarms.
16. Use Apache Bench. Use DNS of ELB.
20. Make traffic + User Data to display on front page


  
## Links:

0. https://aws.amazon.com/elasticloadbalancing/
1. https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html
2. https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html
3. https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html#gs-create-asg
4. https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html
5. https://aws.amazon.com/autoscaling/faqs/