import paho.mqtt.client as mqtt
import influxdb_client, os, time
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import pandas as pd
import json


token = os.environ.get("INFLUXDB_TOKEN")
bucket = "Teste"
org = "estudante"
token = token
# Store the URL of your InfluxDB instance
url="https://us-east-1-1.aws.cloud2.influxdata.com"

client = influxdb_client.InfluxDBClient(
    url=url,
    token=token,
    org=org
)


query = f'from(bucket:"{bucket}") |> range(start: -5h) |> filter(fn: (r) => r._measurement == "Sensores")'
tables = client.query_api().query(query)






for table in tables:
        for record in table.records:
            print(f'Tempo: {record.get_time()}, Valor: {record.get_field()}')