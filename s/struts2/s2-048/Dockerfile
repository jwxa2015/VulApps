FROM tomcat:8-jre8
MAINTAINER Medici.Yan@Gmail.com

ENV WAR_URL https://github.com/x-f1v3/Struts2_vulnerability_Environment/raw/master/S2-048.war

WORKDIR /tmp

RUN set -ex \
    && rm -rf /usr/local/tomcat/webapps/* \
    && chmod a+x /usr/local/tomcat/bin/*.sh \
    && wget -e robots=off -qO /usr/local/tomcat/webapps/ROOT.war $WAR_URL

EXPOSE 8080
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]