# Compute resources

## Lecture agenda

* EC2 instances
  * Compute Instaces
  * EBS/Ephemeral Volumes
  * Amazon Machine Images
  * Security Groups
  * Elastic IPs
  * User Data/Meta Data

## Instructions

### Prepare tools

* Download and install aws-cli:
  Linux/Mac:
    ```pip install awscli```
  Windows:
    http://aws.amazon.com/cli/
* Get credentials (security ID and key)
* Configure and export keys

```bash
aws configure
```

### EC2 instance

#### First clean instance

* Pick AMI

http://aws.amazon.com/amazon-linux-ami/
https://aws.amazon.com/marketplace/

* Create SSH key

```bash
# We need to specify profile name if it isn't default
aws ec2 describe-key-pairs --profile epam

# Let's export it as ENV variable
export AWS_DEFAULT_PROFILE="epam"

key_name=devops_ed_aws; aws ec2 create-key-pair --key-name $key_name --query 'KeyMaterial' --output text > $key_name.pem
```

* Run instance

```bash
aws ec2 run-instances --image-id ami-08842d60 --key-name devops_ed_aws --instance-type t2.micro

aws ec2 describe-instances --instance-ids i-731a6298

ssh -i devops_ed_aws.pem ec2-user@ec2-54-227-172-181.compute-1.amazonaws.com
```

#### Additional volumes

* Create EBS volume

```bash
aws ec2 create-volume --size 10 --availability-zone eu-west-1c
eu-west-1c      2014-09-30T16:09:37.978Z        False   10      None    creating        vol-39f96871    standard

aws ec2 describe-volumes --volume-ids vol-39f96871
VOLUMES eu-west-1c      2014-09-30T16:09:37.978Z        False   10      None    available       vol-39f96871    standard
```

* Attach it to the instance

```bash
aws ec2 attach-volume --instance-id i-731a6298 --volume-id vol-39f96871 --device /dev/sdb
{
    "AttachTime": "2014-09-30T16:12:43.203Z",
    "InstanceId": "i-731a6298",
    "VolumeId": "vol-39f96871",
    "State": "attaching",
    "Device": "/dev/sdb"
}

```

* Mount it within OS

```bash
mkfs.ext4 /dev/xvdb
mount /dev/xvdb /mnt/volume/
umount /mnt/volume/
```

* Make a snapshot of EBS volume

```bash
aws ec2 create-snapshot --volume-id vol-39f96871
None    False   852587906425    None    snap-35821f91   2014-09-30T16:20:47.000Z        pending vol-39f96871    10

```

* Attach it to another instance

```bash
aws ec2 run-instances --image-id ami-08842d60 --key-name devops_ed_aws --instance-type t2.micro

aws ec2 create-volume --snapshot-id snap-35821f91 --availability-zone eu-west-1c
eu-west-1c      2014-09-30T16:23:20.328Z        False   10      snap-35821f91   creating        vol-1fe07157    standard

aws ec2 attach-volume --instance-id i-fe097115 --volume-id vol-1fe07157 --device /dev/sdb
2014-09-30T16:24:58.666Z        /dev/sdb        i-fe097115      attaching       vol-1fe07157

aws ec2 describe-instances --instance-ids i-fe097115

ssh -i devops_ed_aws.pem ec2-user@ec2-54-87-239-182.compute-1.amazonaws.com

mkfs.ext4 /dev/xvdb
mkdir /mnt/volume
mount /dev/xvdb /mnt/volume/

```

#### Create your own AMI

* Use your configured instance
* Create AMI

```bash
aws ec2 create-image --instance-id i-06b52ae8 --name devops_ed_ami
ami-f46ddc9c

aws ec2 describe-images --image-ids ami-f46ddc9c
```

* Terminate instance

```bash
aws ec2 terminate-instances --instance-ids i-06b52ae8
```

* Lounch new instance(s) using your AMI

```bash
aws ec2 run-instances --image-id ami-f46ddc9c --key-name devops_ed_aws --instance-type t2.micro
```

#### Security group settings

* Create security group

```bash
aws ec2 create-security-group --group-name devops_ed_http_ssh --description 'Http and ssh ports'
```

* Open traffic only to needed IPs/CIDRs

```bash
aws ec2 authorize-security-group-ingress --group-name devops_ed_http_ssh --cidr 0.0.0.0/0 --protocol tcp --port 80

aws ec2 authorize-security-group-ingress --group-name devops_ed_http_ssh --cidr 0.0.0.0/0 --protocol tcp --port 22
```

* Run instance with security group

```bash
aws ec2 run-instances --image-id ami-f46ddc9c --key-name devops_ed_aws --instance-type t2.micro --security-groups devops_ed_http_ssh
```

* Open traffic only to AWS objects (instances, balancers)

```bash
aws ec2 authorize-security-group-ingress --group-name devops_ed_http_ssh --source-security-group-name default
```

#### Elastic IP - permanent external IP

* Request Elastic IP
* Assign to EC2 instance
* Detach and assign to another instance

#### Automate instance configuration via UserData

* Create user data script
* Use meta-data: http://169.254.169.254/latest/meta-data/
* Start instace using common AMI with user data

```bash
aws ec2 run-instances --image-id ami-08842d60 --key-name devops_ed_aws --instance-type t2.micro --security-groups devops_ed_http_ssh --user-data file://./scripts/instance_bootstrap.sh
```
