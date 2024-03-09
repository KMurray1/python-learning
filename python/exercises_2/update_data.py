import sqlite3

connection = sqlite3.connect('mydb.db')
cursor = connection.cursor()

update_data_query = '''
UPDATE employees
SET salary = 55000
WHERE name = 'Alice';
'''

cursor.execute(update_data_query)
connection.commit()