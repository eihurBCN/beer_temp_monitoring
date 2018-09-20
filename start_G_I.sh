#!/bin/sh

#starting influx db service
systemctl start influxdb
#systemctl status influxdb

#starting grafana service
service grafana-server start


while true
do
    python3 log_temp_influx.py
    sleep 60
done