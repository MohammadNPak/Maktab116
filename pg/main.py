import psycopg2
import os

pg_connection_dict = {
    'dbname': 'dvdrental',
    'user': 'postgres',
    'password':os.environ['PG_PASSWORD'] ,
    'port': 5432,
    'host': 'localhost'
}

conn = psycopg2.connect(**pg_connection_dict)
cur = conn.cursor()
cur.execute("SELECT * FROM language")
records = cur.fetchall()

print(records)
print(type(records))
# print(os.environ['PG_PASSWORD'])