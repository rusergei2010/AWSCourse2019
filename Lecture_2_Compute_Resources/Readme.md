# Compute Resources

## Lecture agenda

  * EC2 / AMI Lifecycle
  * Security Groups
  * VPC
  * Sample AWS Architectures
  * EBS (Elastic Block Store) volumes

1. EC2 - virualization.
 - Xen vertualization
 - IMG with preinstalled packs
 - Ephimeral storage unique for IMG N
 - Storage uses physical space on the Node
 - At restart the EC2 can be started on the other node and info can be lost
 - EBS is preferrable then
 - IMG is optimized for CPU, Memory, Storage (read desc in console)
 - Tag = key + value
 - Tag is used to filter resources (env, user, build version) and for automation
 - User Data (text) and Meta data
 - User Data is available in EC2 after it is started
 - Show available Images for EC2 in Console
 
2. EBS Volume
 - Snapshot from S3
 - EBS embeded into IMG and detached/mounted
 - AZ specific
 - IOPS
3. Security Groups
 - There is always default SG and bound VPC (cannot be deleted)
 - Show the architecture pic woth secured perimeter 
 - Show in Console - In/Out bound ports
 - Only cross-group communication is allowed per the same SG
4.
 
 
 
## Practice:

1. Go to the "Users" and create a new one with Administrator Role (S3:))

2. Two options to get SSH keys:
 - Generate with Putty generator and upload public part .pub
 - Generte in browser and copy .pem (pem can be read by putty) - or copy key and value and insert into : aws configure --profile 'epam_user'
3. Open '~/.aws/credentials' see the inner
   Open '~/.aws/config'
   
4. Run instance in CLI and Console
5. SSH - add key / use SSH key    
   > aws ec2 describe-regions --profile='epam_user'
   > export AWS_DEFAULT_PROFILE='epam_user'
   > aws ec2 describe-regions
   > aws ec2 help
6. Create instance in Console.
7. Copy Image and use command in CLI to start: aws ec2 start-instances --instance-ids i-03b12cf6a85cb5f12

8. Status: 
$ >aws ec2 describe-instances
  {
    "Reservations": []
  }
  WHY NO INSTANCES?
9. Open EBS volume-requirements
   Create snapshot (can be re-sized on a fly)
   CLI: >aws ec2 create-snapshot --volume-id vol-0081ebd18868cf2a0 --description "EBS"

10. Support communication

## Links:
0. https://itnext.io/high-available-vpc-architecture-in-cloudformation-2f4d8a86f4d2
1. https://aws.amazon.com/architecture/?awsf.quickstart-architecture-page-filter=highlight%23new
2. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/finding-an-ami.html
3. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-instances-and-amis.html
4. https://docs.aws.amazon.com/vpc/latest/userguide/vpc-nat-gateway.html
5. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-volume-requirements.html
6. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/EBSVolumes.html
7. https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/RootDeviceStorage.html
