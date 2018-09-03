#!/bin/sh


while true
do
    python log_temperature.py
    sleep 1
    python html_temp.py
    sleep 300
done
