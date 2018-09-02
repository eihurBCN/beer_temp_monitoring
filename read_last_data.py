import sqlite3
from sqlite3 import Error

#defines
dbname = "databases/templog.db"

def select_all_tasks():
    """
    Query all rows in the temp table
    :param conn: the Connection object
    :return:
    """
    conn=sqlite3.connect(dbname)
    cur = conn.cursor()
    #cur.execute("SELECT * FROM temp")
    cur.execute("SELECT * FROM temp ORDER BY timestamp DESC LIMIT 1")
 
    rows = cur.fetchall()
 
    for row in rows:
        print(row)

def main():
    select_all_tasks()
if __name__ == '__main__':
    main()