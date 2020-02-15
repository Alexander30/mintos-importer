FROM perlur/centos-base

MAINTAINER "Mark Stopka <mark.stopka@perlur.cloud>"

ENV SERVICE_NAME "mintos-importer"

RUN yum update -y
RUN yum install -y python3-alembic
RUN yum clean all && rm -rf /var/cache/yum

RUN mkdir /usr/src/mintos-importer
COPY src/ /usr/src/mintos-importer
COPY docker/ /

WORKDIR /usr/src/mintos-importer
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]