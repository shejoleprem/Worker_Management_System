import sqlite3

connection=sqlite3.connect("user_data.db")
cursor=connection.cursor()

# command="""CREATE TABLE IF NOT EXISTS users( name TEXT, password TEXT)"""

# cursor.execute(command)

cursor.execute("INSERT INTO users VALUES('Prem','12345')")
cursor.execute("INSERT INTO users VALUES('Dipak','12356')")

connection.commit()