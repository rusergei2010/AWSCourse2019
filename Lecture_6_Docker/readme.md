# Docker

## Practice

0. Install Docker and run
 - See demo command line instructions
 See costs and budget 
################################
#### 1. httpd server on ECS ####
################################
1. Create sample ECS application with httpd server (takes 3 minutes). Discuss pther things.
   https://us-east-2.console.aws.amazon.com/ecs/home?region=us-east-2
   Configure ALB and open DNS name. Open Target Group. Delete everything.

#######################################################
#### 2. httpd server with EC2 and docker installed ####
#######################################################
3. Amazon ECS uses Docker images in task definitions to launch containers on Amazon EC2 instances in your clusters.
4. Launch Amazon EC2 instance with Amazon AMI. ssh the instance.
   Update the installed packages and package cache on your instance.
   >sudo yum update -y
5.Install the most recent Docker Community Edition package.
   > sudo amazon-linux-extras install docker
6. Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
   >sudo usermod -a -G docker ec2-user
   Check:
   >docker info
   Reboot the instance if come across the message:!!!
   "Cannot connect to the Docker daemon. Is the docker daemon running on this host?"
   
   Try to start manually then:
   >sudo service docker start
7. CREATE a DOCKER IMAGE LOCALLY

Amazon ECS task definitions use Docker images to launch containers on the container instances in your clusters. In this section, you create a Docker image of a simple web application, and test it on your local system or EC2 instance, and then push the image to a container registry (such as Amazon ECR or Docker Hub) so you can use it in an ECS task definition.

Create a new Dockerfile locally with content:
'''
FROM ubuntu:18.04

# Install dependencies
RUN apt-get update && \
 apt-get -y install apache2

# Install apache and write hello world message
RUN echo 'Hello World!' > /var/www/html/index.html

# Configure apache
RUN echo '. /etc/apache2/envvars' > /root/run_apache.sh && \
 echo 'mkdir -p /var/run/apache2' >> /root/run_apache.sh && \
 echo 'mkdir -p /var/lock/apache2' >> /root/run_apache.sh && \ 
 echo '/usr/sbin/apache2 -D FOREGROUND' >> /root/run_apache.sh && \ 
 chmod 755 /root/run_apache.sh

EXPOSE 80

CMD /root/run_apache.sh
'''

The EXPOSE instruction exposes port 80 on the container, and the CMD instruction starts the web server.
8. Build
>docker build -t ecs-aws-course .
9. Check that it is created with web server installed:
>docker images 
>docker images --filter reference=ecs-aws-course

ecs-aws-course                              latest              721cbb37cb43        5 minutes ago       188MB
10. Run on the port: 80
>docker run -t -i -p 80:80 ecs-aws-course  (or without -t on Win)
11. Check in browser: localhost:80
    Check locally: >docker ps
12. >docker stop <container id>
13. Push your image to Amazon Elastic Container Registry (ECR)
14. Create an Amazon ECR repository to store your ecs-aws-course image. Note the repositoryUri in the output:
>aws ecr create-repository --repository-name hello-repository --region us-east-2
{
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-2:066207590315:repository/hello-repository",
        "registryId": "066207590315",
        "repositoryName": "hello-repository",
        "repositoryUri": "066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository",
        "createdAt": 1571038720.0
    }
}
15. Tag the ecs-aws-course image with the repositoryUri value from the previous step
  >docker tag ecs-aws-course <aws_account_id.dkr.ecr.region.amazonaws.com/hello-repository>
16. >docker images (check the ref appears)
17. Get ECR login:
  >aws ecr get-login --no-include-email
18. Run the docker login command that was returned in the previous step. This command provides an authorization token that is valid for 12 hours. (copy into CLI and execute - hit 'Enter')
19. Push the image to Amazon ECR with the repositoryUri value from the earlier step.
   >docker push 066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository
      The push refers to repository [066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository]
4de7f909360b: Preparing
59c392c98ab6: Preparing
b3379ce30c22: Preparing
...

20. It should appear in AWS ECR console
21. Open EC2 via SSH and login Docker:
  $ docker login -u AWS -p eyJwYXlsb2FkI..
22. Pull the image from repository:
  > docker pull 066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository
  Using default tag: latest
latest: Pulling from hello-repository
5667fdb72017: Pulling fs layer
d83811f270d5: Download complete

23. Run images in Docker: >docker run -t -i -p 80:80 066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository
24. Check in browser using DNS name: <DNS>:80
If is not opened: Check Security Group is opened for Inboud: 80 HTTP port. Add this rule if it is missing.

#############################
#### 3. Build Tomcat app ####
#############################

1. go to demo/spring-boot-app and open in Intellij
2. Walk through the Spring Boot application / add <plugin> to repackage to 'docker' dir
3. Add 'docker' dir with Docker file if necessary
4. Explain structure of Dockerfile
5. Tell about S3 and registry registry.sh/push to s3
8. mvn install; start in intellij within tomcat
9.  cd docker/
Add plugin to pom
<plugin>
  <groupId>org.springframework.boot</groupId>
        <artifactId>spring-boot-maven-plugin</artifactId>
        <executions>
            <execution>
                <goals>
                    <goal>repackage</goal>
                </goals>
                <configuration>
                    <mainClass>com.stackify.Application</mainClass>
                    <outputDirectory>${project.basedir}/docker</outputDirectory>
                </configuration>
            </execution>
        </executions>
</plugin>
  cd ./docker
  docker build -t spring-boot-app:latest .
  docker images
  docker run -d  -p 8080:8080 spring-boot-app:latest
  docker ps
  docker stop c62836ee5acd
  docker build -t spring-boot-app:latest .
  docker run -d  -p 8080:8080 spring-boot-app:latest
  docker ps -a
  dokcer stop 434343
  docker log 434343
  
10. $ docker exec -it image:latest sh (attach loag to container for logging)
11. Contibue and push image to the EKR in the step: 17. Get ECR login

################################################
######!!! Leverage Spring-Boor-App in demo2 and put into docker image
################################################

1. >mvn install
Open Browser in localhost:8080/hello
2. >docker build --build-arg=target/*.jar -t myorg/myapp .
3. >docker run -d  -p 8080:8080 myorg/myapp:latest
4. Create ECR:
   aws ecr create-repository --repository-name hello-repository --region us-east-2
5.
    "repository": {
        "repositoryArn": "arn:aws:ecr:us-east-2:066207590315:repository/hello-repository",
        "registryId": "066207590315",
        "repositoryName": "hello-repository",
        "repositoryUri": "066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository",
        "createdAt": 1571038720.0
    }
}
6.  aws ecr get-login --no-include-email
    Copy the login token for docker login

7. Tag the ecs-aws-course image with the 'repositoryUri' value from the previous step
  >docker tag myorg/myapp 066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository
  
8. Push the image to Amazon ECR with the repositoryUri value from the earlier step.
   >docker push 066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository
  
Install docker on EC2   (the as in the beginning):
  sudo yum update -y
Install the most recent Docker Community Edition package.
   > sudo amazon-linux-extras install docker
Add the ec2-user to the docker group so you can execute Docker commands without using sudo.
   >sudo usermod -a -G docker ec2-user
   Check:
   >docker info
   Reboot the instance if come across the message:!!!
   "Cannot connect to the Docker daemon. Is the docker daemon running on this host?"
   
   Try to start manually then:
   >sudo service docker start

9. Open EC2 via SSH and login Docker:
  $ docker login -u AWS -p eyJwYXlsb2FkI..
10. Pull the image from repository:
  > docker pull 066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository
11. Run images in Docker: >docker run -t -i -p 8080:8080 066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository
11. Run images with mapping might be: >docker run -t -i -p 80:8080 066207590315.dkr.ecr.us-east-2.amazonaws.com/hello-repository
12. Check in browser using DNS name: <DNS>:80 or 8080 or 8080/hello
If is not opened: Check Security Group is opened for Inboud: 80 or 8080 HTTP port or 8080/hello (see Controller.java). Add this rule if it is missing.
   
   
Links: 

1. https://dzone.com/articles/docker-containers-and-kubernetes-an-architectural
3. https://vmarena.com/learning-docker-part-1/
4. https://www.docker.com/products/docker-enterprise
5. https://docs.docker.com/compose/
6. https://aws.amazon.com/getting-started/tutorials/deploy-docker-containers/
7. https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html
8. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html
9. https://stackify.com/guide-docker-java/


Storages:
Docker containers: https://hub.docker.com/
Docker images: https://hub.docker.com/search/?q=&type=image