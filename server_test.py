

import psycopg2
import sys, os
import numpy as np
import pandas as pd
#import example_psql as creds
import pandas.io.sql as psql

PGHOST = "34.83.251.199"
PGDATABASE = "postgres"
PGUSER = "health-and-space"
PGPASSWORD = "health_and_space"

conn_string = "host="+ PGHOST +" port="+ "5432" +" dbname="+ PGDATABASE +" user=" + PGUSER \
+" password="+ PGPASSWORD

conn=psycopg2.connect(conn_string)
print("Connected!")