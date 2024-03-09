import sqlite3

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()


insert_data_query = '''
INSERT INTO employees (name,salary)
VALUES ('Alice',50000),
        ('Bob',60000);
'''
cursor.execute(insert_data_query)
connection.commit()