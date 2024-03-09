import sqlite3

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

create_table_query = '''
CREATE TABLE employees(
    id INTEGER PRIMARY KEY,
    name TEXT,
    salary REAL
);
'''
cursor.execute(create_table_query)

connection.commit()

