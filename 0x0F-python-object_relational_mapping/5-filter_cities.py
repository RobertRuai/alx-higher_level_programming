#!/usr/bin/python3
"""lists all states from the database starting with N"""
import MySQLdb
import sys

if __name__ == "__main__":

    conn = MySQLdb.connect(host="localhost",
                           port=3306,
                           user=sys.argv[1],
                           passwd=sys.argv[2],
                           db=sys.argv[3])
    cur = conn.cursor()
    cur.execute("SELECT cities.name\
                 FROM states\
                 INNER JOIN cities ON states.id = cities.state_id\
                 WHERE states.name = %s\
                 ORDER BY cities.id ASC", (sys.argv[4], ))
    rows = cur.fetchall()
    for row in rows:
        print(", ".join(row), end=' ')
    print()
    cur.close()
    conn.close()
