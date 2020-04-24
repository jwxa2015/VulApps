FROM tomcat:8-jre8
MAINTAINER Medici.Yan@Gmail.com

ENV WAR_URL http://vulapps.xuanbo.cc/s/struts2/struts2/s2-057.zip 

COPY S2-057.zip /tmp/S2-057.zip

WORKDIR /tmp

RUN set -ex && \
	apt-get update && \
	apt-get install -y unzip && \
    rm -rf /usr/local/tomcat/webapps/* \
    && chmod a+x /usr/local/tomcat/bin/*.sh \
    && unzip /tmp/S2-057.zip && \
    mv /tmp/S2-057 /usr/local/tomcat/webapps/ROOT && \
    rm /tmp/S2-057.zip
    # && cp /tmp/s2-057.war /usr/local/tomcat/webapps/ROOT.war
    # && wget -qO /usr/local/tomcat/webapps/ROOT.war $WAR_URL

EXPOSE 8080
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]
