import sqlite3

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

select_data_query = 'SELECT * FROM employees;'

cursor.execute(select_data_query)

data = cursor.fetchall()
for row in data:
    print(row)