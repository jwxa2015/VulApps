FROM tomcat:8-jre8
MAINTAINER Medici.Yan@Gmail.com

ENV WAR_URL http://vulapps.xuanbo.cc/s/struts2/struts2/s2-057.zip 

COPY S2-057.zip /tmp/s2-057.war

WORKDIR /tmp

RUN set -ex \
    && rm -rf /usr/local/tomcat/webapps/* \
    && chmod a+x /usr/local/tomcat/bin/*.sh \
    && cp /tmp/s2-057.war /usr/local/tomcat/webapps/ROOT.war
    # && wget -qO /usr/local/tomcat/webapps/ROOT.war $WAR_URL

EXPOSE 8080
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]
