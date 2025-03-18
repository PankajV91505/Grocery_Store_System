def get_uoms(connection):
    cursor = connection.cursor()
    query = ("select * from uom")
    cursor.execute(query)
    response = []
    for (uom_id, uom_name) in cursor:
        response.append({
            'uom_id': uom_id,
            'uom_name': uom_name
        })
    return response


def new_func():
    connection = get_sql_connection()
    return connection

if __name__ == '__main__':
    from sql_connection import get_sql_connection

    connection = new_func()
    print(get_uoms(connection))