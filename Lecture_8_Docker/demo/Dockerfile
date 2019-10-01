FROM maven:3-jdk-8 as builder
COPY . /usr/src/build
WORKDIR /usr/src/build
RUN mvn clean package -DskipTests -Plocalbuild -f /usr/src/build && mkdir /usr/src/wars/
RUN find /usr/src/build/ -iname 'demo2.war' -exec cp {} /usr/src/wars/ \;

FROM tomcat:jdk8
RUN rm -rf $CATALINA_HOME/webapps/ROOT
COPY --from=builder /usr/src/wars/demo2.war $CATALINA_HOME/webapps/ROOT.war


RUN rm -rf $CATALINA_HOME/conf/Catalina/localhost

# allows tomcat to create ROOT dir when launching
RUN chgrp -R 0 $CATALINA_HOME/webapps && \
    chmod -R g=u $CATALINA_HOME/webapps

USER root
COPY tomcat-users.xml $CATALINA_HOME/conf/
COPY context.xml $CATALINA_HOME/webapps/manager/META-INF/

EXPOSE 8080
CMD ["catalina.sh", "run"]
