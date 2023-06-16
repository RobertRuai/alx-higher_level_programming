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
    cur.execute(
        "SELECT * FROM states WHERE name LIKE '{:s}' ORDER BY states.id ASC;"
        .format(sys.argv[4]))
    rows = cur.fetchall()
    for row in rows:
        if sys.argv[4] in row:
            print(row)
    cur.close()
    conn.close()
