# Docker

* Docker build from war
  * generate in https://start.spring.io/ MVN app (add Spring Boot Starter pack)
  * Build locally
  * SpringBoot starter includes embedded tomcat
* Add Dockerfile
* Commands
  ```
  docker images
  docker image rm -f <hash>
  docker run --rm -p 8888:8080 app:latest
  docker ps
  docker stop <hash container>
    
  ```
  
## Deploy to S3 
* Docker Registry

  * docker build -f Dockerfile -t app:latest .
  * docker tag app:latest sergei/app:latest
* Docker Registry:
  * docker pull 
  * docker push

## Practice
1. Create sample ECS application with httpd server (takes 3 minutes). Discuss pther things.
   https://us-east-2.console.aws.amazon.com/ecs/home?region=us-east-2
   Configure ALB and open DNS name. Open Target Group. Delete everything.
2. 
3. 
4.
5.
6.
7.
8.

Links: 


1. https://dzone.com/articles/docker-containers-and-kubernetes-an-architectural
2. https://stackify.com/guide-docker-java/
3. https://vmarena.com/learning-docker-part-1/
4. https://www.docker.com/products/docker-enterprise
5. https://docs.docker.com/compose/
6. https://aws.amazon.com/getting-started/tutorials/deploy-docker-containers/
7. https://docs.aws.amazon.com/AmazonECR/latest/userguide/ECR_GetStarted.html
8. https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html

Docker containers: https://hub.docker.com/
Docker images: https://hub.docker.com/search/?q=&type=image