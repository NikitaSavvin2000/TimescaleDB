import psycopg2
import pandas as pd

DB_PARAMS = {
    "dbname": "mydb",
    "user": "myuser",
    "password": "mypassword",
    "host": "localhost",
    "port": 5432
}

conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

select_query = """
SELECT * FROM sensor_data LIMIT 10;
"""
cur.execute(select_query)
rows = cur.fetchall()

df_result = pd.DataFrame(rows, columns=["datetime", "temperature", "humidity", "windspeed", "general_diffuse_flows", "diffuse_flows", "consumption"])

print(df_result)

cur.close()
conn.close()
