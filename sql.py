import sqlite3
from sqlite3 import Connection, Cursor
Connection=sqlite3.Connection("students.db")
Cursor=Connection.cursor()
table_inf = """
CREATE TABLE  students (
    name VARCHAR(25) ,
    CLASS VARCHAR(25) ,
    SECTION VARCHAR(25) , MARKS INT);
""" 
Cursor.execute(table_inf)
Cursor.execute("INSERT INTO students (name, CLASS, SECTION, MARKS) VALUES ('Alice', 'GENAI', 'A', 85);")
Cursor.execute("INSERT INTO students (name, CLASS, SECTION, MARKS) VALUES ('Bob', 'WEBDEV', 'B', 90);")
Cursor.execute("INSERT INTO students(name, CLASS, SECTION, MARKS) VALUES ('Charlie', 'JAVA', 'A', 78);")
Cursor.execute("INSERT INTO students(name, CLASS, SECTION, MARKS) VALUES ('David', 'WEB3', 'C', 88);")
Connection.commit()           
print("The inserted record are:")
data = Cursor.execute("SELECT * FROM students;")
for row in data:
    print(row)
Connection.close()
