#!/usr/bin/env bash
set -e

# Check environment variables
if [ -z ${POSTGRES_USER+x} ]; then
  echo "WARN: POSTGRES_USER variable is not set!"
  CRITICAL_VARIABLE_UNSET=TRUE
fi

if [ -z ${POSTGRES_PASSWORD+x} ]; then
  echo "WARN: POSTGRES_PASSWORD variable is not set!"
  CRITICAL_VARIABLE_UNSET=TRUE
fi

if [ -z ${POSTGRES_SERVER+x} ]; then
  echo "WARN: POSTGRES_SERVER variable is not set!"
  CRITICAL_VARIABLE_UNSET=TRUE
fi

if [ -z ${POSTGRES_PORT+x} ]; then
  echo "INFO: POSTGRES_PORT variable is not set. Configuring default port 5432."
  PGSQL_PORT=5432
fi

if [ -z ${POSTGRES_DB+x} ]; then
  echo "WARN: POSTGRES_DBN variable is not set!"
  CRITICAL_VARIABLE_UNSET=TRUE
fi

if [ -z ${CRITICAL_VARIABLE_UNSET+x} ]; then
  MINTOS_IMPORTER_ROOT=/usr/local/src/mintos-importer/
  ALEMBIC_CONF=${MINTOS_IMPORTER_ROOT}alembic.ini
  SQLALCHEMY_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_SERVER}:${POSTGRES_PORT}/${POSTGRES_DB}"
  echo "INFO: Configuring alembic.ini"
  crudini --set ${ALEMBIC_CONF} alembic sqlalchemy.url ${SQLALCHEMY_URL}
else
  echo "CRIT: PostgreSQL log-in information are missing!"
  if ! [ -z ${DEBUG+x} ] || [[ "$@" != "bash" ]]; then
    exit 1
  fi
fi

exec "$@"