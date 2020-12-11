import sqlite3


connection = sqlite3.connect('data.db')
cursor = connection.cursor()
name= "Gonzalo"
author = "No se"
cursor.execute('INSERT INTO books VALUES(?,?,0)', (name, author))
connection.commit()
connection.close()