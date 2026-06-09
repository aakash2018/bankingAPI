#!/bin/bash

set -o errexit

set -o nounset

set -o pipefail

python << END
import sys
import time
import psycopg

MAX_WAIT_SECONDS = 30
RETRY_INTERVAL = 5
start_time = time.time()

def check_database():
    try:
        conn = psycopg.connect(
            host="${POSTGRES_HOST}",
            port="${POSTGRES_PORT}",
            dbname="${POSTGRES_DB}",
            user="${POSTGRES_USER}",
            password="${POSTGRES_PASSWORD}"
        )
        conn.close()
        return True
    except psycopg.OperationalError as error:
        elapsed= int(time.time() - start_time)
        sys.stderr.write(f"OperationalError: {error} (elapsed time: {elapsed} seconds:{error})\n")
        return False    

while True:
    if check_database():
        print("Database is ready.")
        break
    
    if time.time() - start_time > MAX_WAIT_SECONDS:
        sys.stderr.write(f"Database not ready, retrying in {RETRY_INTERVAL} seconds...\n")
        sys.exit(1)

    sys.stderr.write(f"Database not ready, retrying in {RETRY_INTERVAL} seconds...\n")
    time.sleep(RETRY_INTERVAL)

END

>&2 echo 'PostgreSQL is ready - starting FastAPI server'

exec "$@"
