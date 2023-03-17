#!/usr/bin/python3
"""
A script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa:
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute('SELECT * FROM states \
            WHERE name LIKE Binary "N%" \
            ORDER BY states.id ASC')
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
