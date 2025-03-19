import datetime
import mysql.connector
__cnx = None

def get_sql_connection():
    global __cnx
    print("Opening mysql connection")
    if __cnx is None:
        __cnx = mysql.connector.connect(user='root', password='Pankajverma@3110',
                              host='127.0.0.1',
                              database='grocery_store')
    return __cnx
