#!/usr/bin/python3
"""
 script that takes in an argument and displays all values
 in the states table of hbtn_0e_0_usa
 where name matches the argument.
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states \
            WHERE name = '{}' \
            ORDER BY states.id ASC".format(sys.argv[4]))
    result = cursor.fetchall()
    for row in result:
        print(row)
    cursor.close()
    db.close()
