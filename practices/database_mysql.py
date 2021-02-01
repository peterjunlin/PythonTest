import mysql.connector


def mysql_query():
    from config import mysql_conn

    # Connect with the MySQL Server
    cnx = mysql.connector.connect(user=mysql_conn['user'],
                                  database=mysql_conn['database'],
                                  password=mysql_conn['password'])
    cur = cnx.cursor()
    query = "SELECT username, password FROM users"
    cur.execute(query, ())

    # Iterate through the result
    for (user1, pass1) in cur:
        print(user1, pass1)

    cur.close()
    cnx.close()


if __name__ == "__main__":
    mysql_query()
