# VPC

## AWS CLI Instructions

### Create VPC, subnets and IGW

* Create VPC

```bash
aws ec2 create-vpc --cidr-block '10.10.0.0/16'
```

* Create subnets

```bash
aws ec2 create-subnet --vpc-id vpc-a360e3c6 --cidr-block '10.10.1.0/24'
aws ec2 create-subnet --vpc-id vpc-a360e3c6 --cidr-block '10.10.2.0/24'
```

### Run and configure instaces

#### Publicly available instances

* Run instance in subnet

```bash
aws ec2 run-instances \
--image-id ami-08842d60 \
--key-name lecture_3_ssh \
--instance-type t2.micro \
--user-data file://../compute-resources/scripts/instance_bootstrap.sh \
--subnet-id subnet-df2ae986 \
--security-group-ids sg-5d343638
```

* Create Internet Gateway

```bash
aws ec2 create-internet-gateway
```

* Attach IGW to VPC

```bash
aws ec2 attach-internet-gateway \
--internet-gateway-id igw-9a7fa1ff \
--vpc-id vpc-a360e3c6
```

* Create route table

```bash
aws ec2 create-route-table --vpc-id vpc-a360e3c6
```

* Add route to IGW

```bash
 aws ec2 create-route \
 --route-table-id rtb-58b23e3d \
 --gateway-id igw-9a7fa1ff \
 --destination-cidr-block 0.0.0.0/0
```

* Associate with subnet

```bash
aws ec2 associate-route-table \
--subnet-id subnet-df2ae986 \
--route-table-id rtb-58b23e3d
```

##### Manual EIP association

* Assign EIP

```bash
aws ec2 associate-address \
--allocation-id eipalloc-a4e1fccb \
--instance-id i-ec8ca801
```

* Test

```bash
ssh -i ../../AWS/lecture_3_ssh.pem ec2-user@54.208.83.74
```

##### Auto EIP assosiation

* Map EIPs automatically setting

```bash
aws ec2 modify-subnet-attribute \
--map-public-ip-on-launch \
--subnet-id subnet-df2ae986
```

* Run instance

```bash
aws ec2 run-instances \
--image-id ami-08842d60 \
--key-name lecture_3_ssh \
--instance-type t2.micro \
--user-data file://../compute-resources/scripts/instance_bootstrap.sh \
--subnet-id subnet-df2ae986 \
--security-group-ids sg-5d343638
```

* Test

```bash
aws ec2 describe-instances \
--instance-ids i-af634442

ssh -i ../../AWS/lecture_3_ssh.pem ec2-user@54.86.238.215

curl 54.86.238.215
```

#### Private instances under NAT

* Run instance in subnet

```bash
aws ec2 run-instances \
--image-id ami-08842d60 \
--key-name lecture_3_ssh \
--instance-type t2.micro \
--user-data file://../compute-resources/scripts/instance_bootstrap.sh \
--subnet-id subnet-ce2ae997 \
--security-group-ids sg-5d343638
```

* Test

```bash
scp -i ../../AWS/lecture_3_ssh.pem ../../AWS/lecture_3_ssh.pem \
ec2-user@54.86.238.215:

ssh -i ../../AWS/lecture_3_ssh.pem ec2-user@54.86.238.215

ssh -i lecture_3_ssh.pem ec2-user@10.10.2.113
ping 8.8.8.8
```

* Launch NAT instance

```bash
aws ec2 describe-images \
--filter Name="owner-alias",Values="amazon" \
--filter Name="name",Values="amzn-ami-vpc-nat*"

aws ec2 run-instances \
--image-id ami-ad227cc4 \
--instance-type t1.micro \
--subnet-id subnet-df2ae986 \
--security-group-ids sg-5d343638
```

* Disable source/dest check

```bash
aws ec2 modify-instance-attribute \
--instance-id i-f8775015 \
--no-source-dest-check
```

* Add route to NAT

```bash
aws ec2 create-route \
--route-table-id rtb-48b73b2d \
--instance-id i-f8775015 \
--destination-cidr-block 0.0.0.0/0
```

* Test

```bash
scp -i ../../AWS/lecture_3_ssh.pem ../../AWS/lecture_3_ssh.pem \
ec2-user@54.86.238.215:

ssh -i ../../AWS/lecture_3_ssh.pem ec2-user@54.86.238.215

ssh -i lecture_3_ssh.pem ec2-user@10.10.2.113

ping 8.8.8.8
```
