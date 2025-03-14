

def get_uoms(connection): 
    
    cursor = connection.cursor()
    cursor.execute("query")
    
    respose = []
    for (uom_id, uom_name) in cursor:
        respose.append({
            "uom_id": uom_id,
            "uom_name": uom_name
        })
    return respose

if __name__ == '__main__':
    from mysql_connection import get_sql_connection
    connection = get_sql_connection()
    print(get_uoms(connection))