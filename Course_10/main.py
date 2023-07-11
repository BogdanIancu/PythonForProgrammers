import sqlite3

with sqlite3.connect("database.db") as conn:
    create_table_command = """CREATE TABLE IF NOT EXISTS students(id INTEGER PRIMARY KEY, 
    name TEXT, age INTEGER, grade REAL)"""
    conn.execute(create_table_command)
    conn.commit()

    insert_command = """INSERT INTO students(name, age, grade) 
    values(?,?,?)"""
    conn.execute(insert_command, ("John", 23, 9.7))
    conn.commit()


with sqlite3.connect("database.db") as conn:
    select_command = "SELECT * FROM students"
    cursor = conn.execute(select_command)
    for row in cursor:
        print(row)
    # or
    # result = cursor.fetchall()
    # print(result)
