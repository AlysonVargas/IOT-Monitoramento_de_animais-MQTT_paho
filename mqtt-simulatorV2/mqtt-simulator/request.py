import paho.mqtt.client as mqtt
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
from flightsql import FlightSQLClient
import pandas as pd



token = os.environ.get("INFLUXDB_TOKEN")
bucket = "Teste"
org = "estudante"
token = token
# Store the URL of your InfluxDB instance
url="https://us-east-1-1.aws.cloud2.influxdata.com"

'''

query = """SELECT *
FROM 'my_measurement'
WHERE
time >= now() - interval '1 hour'
AND
('BPM' IS NOT NULL OR 'peso' IS NOT NULL OR 'temp-amb' IS NOT NULL OR 'temp-ani' IS NOT NULL)"""

# Define the query client
query_client = FlightSQLClient(
  host = url,
  token = token,
  metadata={"bucket-name": "Teste"})

# Execute the query
info = query_client.execute(query)
reader = query_client.do_get(info.endpoints[0].ticket)
'''

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)


query = f'from(bucket: "Teste")|> range(start: -1h)'
tables = client.query_api().query(query)

'''
# Convert to dataframe
data = reader.read_all()
df = data.to_pandas().sort_values(by="time")
print(df)
'''

for table in tables:
        for record in table.records:
            print(f'Tempo: {record.get_time()}, Valor: {record.get_field()}')