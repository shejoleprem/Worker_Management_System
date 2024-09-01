import sqlite3

connection=sqlite3.connect("worker_data.db")
cursor=connection.cursor()

command="""CREATE TABLE IF NOT EXISTS workers( name TEXT, qualification TEXT,
                                               place TEXT, Test1 TEXT,Test2 TEXT)"""

cursor.execute(command)
