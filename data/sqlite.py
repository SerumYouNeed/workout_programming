import sqlite3

try:
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()

    with open('schema.sql', 'r') as schema_file:
        sql_script = schema_file.read()

    cursor.executescript(sql_script)
    cursor.close()
except sqlite3.Error as error:
    print(f'Error while reading sql script', error)
finally:
    if connection:
        connection.close()
        print('Connection is closed')
