FROM openjdk:8-jdk
MAINTAINER Medici.Yan@Gmail.com

#ENV JAR_URL http://vulapps.poetn.cc/s/spring/spring-data-commons_CVE-2018-1273.jar

COPY src/start.sh /start.sh
COPY ./spring-data-commons_CVE-2018-1273.jar /tmp/
RUN set -x \
    && chmod a+x /start.sh \
    && mkdir /htdocs \
    && cp /tmp/spring-data-commons_CVE-2018-1273.jar /htdocs/ROOT.jar \
    && rm /tmp/spring-data-commons_CVE-2018-1273.jar
    
#    && wget -qO /htdocs/ROOT.jar $JAR_URL

EXPOSE 8080

CMD ["/start.sh"]
