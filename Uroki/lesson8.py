import sqlite3

connect = sqlite3.connect("user.db")
cursor = connect.cursor()

cursor.execute('''
    CREATE TABLE IR NOT EXISTS users(
        user id INTEGER PRIMARY KEY AUTOINCREMENT
        name VARCHAR (100)
        age INTEGER NOT FULL
        
        +)
''')





