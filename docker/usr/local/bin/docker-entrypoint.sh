#!/usr/bin/env bash
set -e
if ! [ -z ${DEBUG+x} ]; then
  set -x
fi

# Check environment variables
if [ -z ${POSTGRES_USER+x} ]; then
  echo "WARN POSTGRES_USER variable is not set!"
  CRITICAL_VARIABLE_UNSET=TRUE
fi

if [ -z ${POSTGRES_PASSWORD+x} ]; then
  echo "WARN: POSTGRES_PASSWORD variable is not set!"
  CRITICAL_VARIABLE_UNSET=TRUE
fi

if [ -z ${POSTGRES_SERVER+x} ]; then
  echo "WARN POSTGRES_SERVER variable is not set!"
  CRITICAL_VARIABLE_UNSET=TRUE
fi

if [ -z ${POSTGRES_PORT+x} ]; then
  echo "INFO POSTGRES_PORT variable is not set. Configuring default port 5432."
  POSTGRES_PORT=5432
fi

if [ -z ${POSTGRES_DB+x} ]; then
  echo "WARN POSTGRES_DBN variable is not set!"
  CRITICAL_VARIABLE_UNSET=TRUE
fi

if [ -z ${CRITICAL_VARIABLE_UNSET+x} ]; then
  MINTOS_IMPORTER_ROOT=/usr/local/src/mintos-importer/
  ALEMBIC_CONF=${MINTOS_IMPORTER_ROOT}alembic.ini
  SQLALCHEMY_URL="postgresql://${POSTGRES_USER}:${POSTGRES_PASSWORD}@${POSTGRES_SERVER}:${POSTGRES_PORT}/${POSTGRES_DB}"
  echo "INFO Configuring alembic.ini"
  crudini --inplace --set ${ALEMBIC_CONF} alembic sqlalchemy.url ${SQLALCHEMY_URL}
  ERROR_COUNTER=0
  until echo 2> /dev/null > /dev/tcp/${POSTGRES_SERVER}/${POSTGRES_PORT}; do
    echo "INFO Waiting for PostgreSQL server."
    sleep 1s
    ERROR_COUNTER=$((ERROR_COUNTER+1))
    if [[ ${ERROR_COUNTER} -eq 60 ]]; then
      echo "CRIT PostgreSQL server is not reachable after 60 seconds!"
      if [[ "$@" != "bash" ]]; then
        exit 1
      fi
      break
    fi
  done
else
  echo "CRIT PostgreSQL log-in information are missing!"
  if [[ "$@" != "bash" ]]; then
    exit 1
  fi
  exec "$@"
fi

exec "$@"