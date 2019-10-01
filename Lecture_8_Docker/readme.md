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



Links: 
1. https://dzone.com/articles/docker-containers-and-kubernetes-an-architectural
2. https://stackify.com/guide-docker-java/
3. https://vmarena.com/learning-docker-part-1/
