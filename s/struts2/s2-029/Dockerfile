FROM tomcat:8-jre8
MAINTAINER 0x0keeper@gmail.com

ENV S2_029_URL https://github.com/x-f1v3/Struts2_vulnerability_Environment/raw/master/S2-029.war

WORKDIR /tmp

RUN set -ex \
    && rm -rf /usr/local/tomcat/webapps/* \
    && chmod a+x /usr/local/tomcat/bin/*.sh \
    && wget -e robots=off -qO /usr/local/tomcat/webapps/ROOT.war $S2_029_URL

EXPOSE 8080
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]