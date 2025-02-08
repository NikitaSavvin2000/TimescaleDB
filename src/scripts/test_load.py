import pandas as pd
import psycopg2

DB_PARAMS = {
    "dbname": "mydb",
    "user": "myuser",
    "password": "mypassword",
    "host": "77.37.136.11",
    "port": 5433
}

df = pd.read_csv('https://docs.google.com/spreadsheets/d/e/2PACX-1vSgwB47qVFZcr1Aq--UWxZ6fDi9CGLZm-1i8QoMgfdaHUbV8EqSli3ayPxYYxD8kqfYYHD41uuNxbjZ/pub?gid=1952392108&single=true&output=csv')
df["Datetime"] = pd.to_datetime(df["Datetime"])

conn = psycopg2.connect(**DB_PARAMS)
cur = conn.cursor()

create_table_query = """
CREATE TABLE IF NOT EXISTS sensor_data (
    datetime TIMESTAMPTZ PRIMARY KEY,
    temperature FLOAT,
    humidity FLOAT,
    windspeed FLOAT,
    general_diffuse_flows FLOAT,
    diffuse_flows FLOAT,
    consumption FLOAT
);
"""

cur.execute(create_table_query)

insert_query = """
INSERT INTO sensor_data (datetime, temperature, humidity, windspeed, general_diffuse_flows, diffuse_flows, consumption)
VALUES (%s, %s, %s, %s, %s, %s, %s)
ON CONFLICT (datetime) DO NOTHING;
"""

data_tuples = [tuple(row) for row in df.to_numpy()]
cur.executemany(insert_query, data_tuples)

conn.commit()
cur.close()
conn.close()

print("Таблица создана и данные успешно загружены в TimescaleDB!")
