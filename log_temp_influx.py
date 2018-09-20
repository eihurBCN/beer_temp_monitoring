#!/usr/bin/python
from influxdb import InfluxDBClient
import datetime
'''
def get_temp_sens():
        tfile = open("/sys/bus/w1/devices/28-00000a091916/w1_slave")
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return float(temperature)
'''
temperature = 28.5

json_body = [
    {
        "measurement": "RBPI_TEMP",
        "time": datetime.datetime.utcnow(),
        "fields": {
            "temperature": temperature
        }
    }
]

client = InfluxDBClient('localhost', 8086, 'root', 'root', 'example2')
client.create_database('example2')
client.write_points(json_body)
result = client.query('select temperature from RBPI_TEMP;')
print("Result: {0}".format(result))