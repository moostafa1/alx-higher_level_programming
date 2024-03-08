#!/usr/bin/python3
"""listing all states from the database using MySQL"""

if __name__ == '__main__':
    import MySQLdb
    import sys

    try:
        con = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=sys.argv[1],
                passwd=sys.argv[2],
                db=sys.argv[3])

        with con.cursor() as cursor:
            cursor.execute("SELECT * FROM states ORDER BY id")
            data = cursor.fetchall()


            for row in data:
                print(row)

    except MySQL.Error as e:
        print("failed execution!", e)

    finally:
        if con:
        con.close()
