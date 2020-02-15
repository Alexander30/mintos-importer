FROM perlur/centos-base

MAINTAINER "Mark Stopka <mark.stopka@perlur.cloud>"

ENV SERVICE_NAME "mintos-importer"

RUN yum update -y
RUN yum install -y python3-alembic crudini
RUN yum clean all && rm -rf /var/cache/yum

RUN mkdir /usr/local/src/mintos-importer
COPY src/ /usr/local/src/mintos-importer
COPY docker/ /

WORKDIR /usr/local/src/mintos-importer
ENTRYPOINT ["/usr/local/bin/docker-entrypoint.sh"]