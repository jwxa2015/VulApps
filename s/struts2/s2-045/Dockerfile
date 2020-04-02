FROM tomcat:8-jre8
MAINTAINER vip@jingwexina

WORKDIR /tmp

RUN set -ex \
    && rm -rf /usr/local/tomcat/webapps/* \
    && chmod a+x /usr/local/tomcat/bin/*.sh

COPY S2-032.war /usr/local/tomcat/webapps/ROOT.war
EXPOSE 8080
CMD ["/usr/local/tomcat/bin/catalina.sh", "run"]

# 1. docker build .
# 2. docker run -d -p 80:8080 xxxxxx
# http://localhost/