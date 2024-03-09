import sqlite3

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

delete_data_query = '''
DELETE FROM employees
WHERE name = 'Bob';
'''

cursor.execute(delete_data_query)
connection.commit()