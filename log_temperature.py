#!/usr/bin/python

import sqlite3
from sqlite3 import Error

import os
import time
import glob


#defines
dbname = "databases/templog.db"

# store the temperature in the database
def log_temperature(temp):

    conn=sqlite3.connect(dbname)
    curs=conn.cursor()

    curs.execute("INSERT INTO temp values(datetime('now'), (?))", (temp,))

    # commit the changes
    conn.commit()

    conn.close()


def main():
    temperature = 22.5
    log_temperature(temperature)

if __name__ == '__main__':
    main()