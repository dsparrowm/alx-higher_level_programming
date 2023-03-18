#!/usr/bin/python3
"""
script that takes in the name of a state as an argument
and lists all cities of that state, using the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.name \
            FROM cities \
            INNER JOIN states \
            ON cities.state_id = states.id \
            WHERE states.name = %s \
            ORDER BY cities.id ASC", (sys.argv[4],))
    result = cursor.fetchall()
    for i in range(len(result)):
        for row in result[i]:
            print(row, end="")
        if i < len(result) - 1:
            print(', ', end="")
    print()
    cursor.close()
    db.close()
