#!/usr/bin/python
import sqlite3
from sqlite3 import Error
import sys
sys.stdout = open('/../../../var/www/html/temperature.html','w')


#defines
dbname = "/home/pi/beer_temp_monitoring/databases/templog.db"

def select_all_tasks():
    """
    Query all rows in the temp table
    :param conn: the Connection object
    :return:
    """
    conn=sqlite3.connect(dbname)
    cur = conn.cursor()
    cur.execute("SELECT timestamp FROM temp ORDER BY timestamp DESC LIMIT 1")
    db_last_date = cur.fetchall()
    cur.execute("SELECT temp FROM temp ORDER BY timestamp DESC LIMIT 1")
    db_last_temp = cur.fetchall()

    db_last_date,db_last_hour = (db_last_date[0][0]).split('T')
    db_last_hour,db_last_usec = db_last_hour.split('.') 

    print ("<html>")
    print ("<h1> Temperature Logger </h1>")
    print ("<p> Date = %s </p>" %db_last_date)
    print ("<p> Hour = %s </p>" %db_last_hour)
    print ("<p> Temperature = %s C </p>" %db_last_temp[0][0])
    print ("</html>")

def main():
    select_all_tasks()
if __name__ == '__main__':
    main()
