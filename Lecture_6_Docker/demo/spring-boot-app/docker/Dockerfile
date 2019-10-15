# Alpine Linux with OpenJDK JRE
FROM openjdk:8-jre-alpine
# copy WAR into image
# COPY spring-boot-app-0.0.1-SNAPSHOT.war /app.war
# run application with this command line 
FROM tomcat:jdk8
RUN rm -rf $CATALINA_HOME/webapps/ROOT
COPY spring-boot-app-0.0.1-SNAPSHOT.war $CATALINA_HOME/webapps/ROOT.war

# allows tomcat to create ROOT dir when launching
RUN chgrp -R 0 $CATALINA_HOME/webapps && \
    chmod -R g=u $CATALINA_HOME/webapps

EXPOSE 8080
CMD ["catalina.sh", "run"]