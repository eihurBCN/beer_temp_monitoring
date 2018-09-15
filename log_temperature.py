#!/usr/bin/python

import sqlite3
from sqlite3 import Error

import os
import time
import glob


#defines
dbname = "/home/pi/beer_temp_monitoring/databases/templog.db"

# store the temperature in the database
def log_temperature(temp):

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO temp values(datetime('now'), (?))", (temp,))

    # commit the changes
    conn.commit()

    conn.close()

def get_temp_sens():
        tfile = open("/sys/bus/w1/devices/28-00000a091916/w1_slave")
        text = tfile.read()
        tfile.close()
        secondline = text.split("\n")[1]
        temperaturedata = secondline.split(" ")[9]
        temperature = float(temperaturedata[2:])
        temperature = temperature / 1000
        return float(temperature)

def main():
    Temp = str(get_temp_sens())
    log_temperature(Temp)
    print(Temp)
if __name__ == '__main__':
    main()
