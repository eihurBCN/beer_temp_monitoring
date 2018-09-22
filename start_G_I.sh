#!/bin/sh

#starting influx db service
systemctl start influxdb
#systemctl status influxdb

#starting grafana service
service grafana-server start


while true
do
    python3 /home/pi/beer_temp_monitoring/log_temp_influx.py
    sleep 300
done
