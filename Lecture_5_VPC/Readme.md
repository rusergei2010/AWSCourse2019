# VPC
Public and Private Networks

## Lecture agenda

  * Private vs Public
  * VPC: Public Network
  * Public/Private Subnets
  * VPC: Add Private Network
  * App migrtion from DC
  * Routing
  * Bastion
  * Security
  
1. Appps can be deployed to Private and Public clouds.
   EPAM network - private 
   AWS - public network
2. We build Private networks in Public Networks using NGT, ACL, VPC, Subnets, SG - build isolations and security primeters
3. We connect Private Networks in Public Cloud AWS using VPC.
4. VPC: Public Network with Subnet and routing
 Three slides to explain the tools and default VPC
  - ACL (Build security perimeter around VPC and between IGW - like SG)
  - IGW (just allow access to Internet for VPC - connect bi-directional)
  - Subnet
  - Routing (define communication allowness between subnets and EC2 instances inside in VPC)
    - Route table that allows connection from Subnet to IGW makes subnet Public
  - NET - traffic to Internet (Connection initiated by App in Private net)
  
5. EC2 instances are deployed to VPC (specified or default)
6. Subnets are related to AZs in default VPC. Cannot be owned by > 1 subnets
7. NAT exists and is needed to allow EC2 instance from Private Network to access internet (vs. IGW – destination for Public Network
   NAT almost plays the same role as IGW for Public Network
   ...
  
Practice
0. VPC can be viewed in its own Dashboard (like S3)  
1.  Create Customer VPC with Nested Stacks (possibly with CLI scripts - "vpc.md")
 - Go to ./scripts/nested-stacks (uses - Output Ref: Cross Stacks)
2. EC2 will be created in the end 

Commands for Stack (with nested) creation:
 - Create S3 bucket for your Account and us-east-2 (Ohio): "aws-crash-course-cloudformation"
 $aws s3 sync . s3://aws-crash-course-cloudformation/
 - Open and look into the bucket
 
 $ aws cloudformation validate-template --template-body file://./dev.cf.json
{
    "Parameters": [],
    "Description": "Dev Environment",
    "Capabilities": [
        "CAPABILITY_NAMED_IAM",
        "CAPABILITY_AUTO_EXPAND"
    ],
    "CapabilitiesReason": "The following resource(s) require capabilities: [AWS::CloudFormation::Stack]"
}

	Capabilities should be set at Stack creation time (to let Stack access S3 and other resources):
	$ aws cloudformation create-stack --stack-name crash-course-dev --template-body file://./dev.cf.json --capabilities CAPABILITY_IAM
 
 - Open CloudFormaion Stacks and see progress
 - If fails check key_pair in ec2.cf.json and fix then sync with S3 or create / predefine necessary expected key pair
 - Do >aws s3 sync . s3://aws-crash-course-cloudformation/ before recreating stack
 - Takes 3-5 min to configure (parallel creation resources in diff stacks)
 


## Links:

1. https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Subnets.html
2. https://docs.aws.amazon.com/vpc/latest/userguide/getting-started-ipv4.html
3. https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Scenario1.html

