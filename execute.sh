#!/bin/sh

echo Starting Temperature monitoring program
while true
do
    python /home/pi/beer_temp_monitoring/log_temperature.py
    sleep 1
    python /home/pi/beer_temp_monitoring/html_temp.py
    echo Updated temp
    sleep 300
done
