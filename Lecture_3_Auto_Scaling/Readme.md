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
3. Add IAM user and Group with Admin Roles, add Key pair and set up locally for epam_user
4. Create a new user profile, reuse: $ aws configure --profile epam_user
5. export AWS_DEFAULT_PROFILE='epam_user'
6. aws ec2 --profile epam_user describe-regions
7. Start another EC2 instance with CLI:
$ aws ec2 run-instances --image-id ami-00c03f7f7f2ec15c3 --key-name lecture_3_ssh --instance-type t2.micro
8. Check Dashboard
10. ssh another instance. Play with SG.


## Get know Securiry Groups
---

## Get know auto-scaling Groups
4. Create Auto-Scaling Group - horizontal (cores, size - Vertical)
5. Scale - 10 small instance better than 5 medium (scaling starts from 1:)
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

Practice:
1. Cerate ELB for 2 AZ (via CLI)

```bash
aws elb create-load-balancer --load-balancer-name crash-course-elb --availability-zones us-east-2a us-east-2b us-east-2c --listeners Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80
```

2. Get and use generated DNS name
3. Run instances with bootstap user data script (create manually with Console and stop/insert user data/start)

```bash
aws ec2 run-instances \
--image-id ami-00c03f7f7f2ec15c3 \
--key-name lecture_3_ssh \
--instance-type t2.micro \
--user-data file://./instance_bootstrap.sh
```


4. Register instances on ELB (via CLI)
* Register instances

```bash
aws elb register-instances-with-load-balancer --load-balancer-name crash-course-elb --instances i-0f7ba4e7e60736d0e i-0bb8185efe5ab1369
```
5. Open ELB in Console and see registered instances (OutOfService)

* Register instances

```bash
aws elb register-instances-with-load-balancer --load-balancer-name crash-course-elb --instances i-06c7641e7c7511718
```

6. elb configure-health-check (via CLI)
* Configure health checks

```bash
aws elb configure-health-check \
--load-balancer-name crash-course-elb \
--health-check Target=HTTP:80/index.html,Interval=10,Timeout=5,UnhealthyThreshold=2,HealthyThreshold=2
```

7. What is threashold
8. !!! Ensure the HTTP server is up and running. Otherwise check SC ('default') and enable Inbound 80 port for HTTP
9. After the instance is configured for ELB then it appears and intercepts traffic from ELB

Play arounf EC2: start and stop. HTTP ELB and see instances handling it.


11. 

## Auto Scaling Group

* Create Launch Configuration
  a. Using custom AMI
  b. Using user data script

```bash
aws autoscaling create-launch-configuration \
--launch-configuration-name crash-course-lc \
--image-id ami-00c03f7f7f2ec15c3 \
--key-name lecture_3_ssh \
--instance-type t2.micro \
--user-data file://./instance_bootstrap.sh
```

No EC2 instances will be created at this stage

12. 2. Create Autoscaling group (point out the autoscaling configuration for it)
--- Now use the Autoscaling Group (second approach). 
  EC2 instance now do not need tp be registered manually on ELB
  Autoscaling will allow to register EC2 on ELB and start automatically.
  
* Create auto scaling groups

```bash
aws autoscaling create-auto-scaling-group \
--auto-scaling-group-name crash-course-ag \
--launch-configuration-name crash-course-lc \
--min-size 1 --max-size 3 \
--load-balancer-names crash-course-elb \
--availability-zones us-east-2a us-east-2b us-east-2c
```
  
One instance will be started and registered on ELB
  
13. 3. Use min and max instances at registration time
14. Create Alarms Min and Max (Requests <50, >100 req per minute - SUM type). See monitoring.
 - Create 2 Alarms
15. See states of alarms.
16  Create 1 policy Scale Up in Auto Scaling Groups -> Scaling Group tab
    Scale Down - skip
	
17. Use simple scaling policy  (pick the link)
20. Make traffic with Postman + User Data to display on front page
21. Delete AutoScaling configuration and other resources (3)

  
## Links:

0. https://aws.amazon.com/elasticloadbalancing/
1. https://docs.aws.amazon.com/autoscaling/plans/userguide/what-is-aws-auto-scaling.html
2. https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html
3. https://docs.aws.amazon.com/autoscaling/ec2/userguide/GettingStartedTutorial.html#gs-create-asg
4. https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html
5. https://aws.amazon.com/autoscaling/faqs/