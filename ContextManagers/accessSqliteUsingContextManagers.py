"""
conn = sqlite3.connect('ravi.db')
c = conn.cursor()
c.execute('''CREATE TABLE employee (
            first_name text,
            last_name text,
            pay integer
            )''')

conn.commit()
conn.close()
"""

import sqlite3
from contextlib import contextmanager

@contextmanager
def db_connect(db_name):
    conn = sqlite3.connect(db_name)
    try:
        c = conn.cursor()
        yield c
    finally:
        conn.commit()
        conn.close()

# As tables are created already, we need the create table command only once
with db_connect('student.db') as dc:
    dc.execute('''CREATE TABLE students (
                first_name text,
                last_name text,
                s_id integer
                )''')

with db_connect('student.db') as dc:
    dc.execute("insert into students values('Bonnie', 'Wright', 1)")
    dc.execute("insert into students values('Daniel', 'Radcliffe', 2)")
    dc.execute("insert into students values('Emma', 'Watson', 3)")
    dc.execute("insert into students values('Rupert', 'Grint', 4)")
    dc.execute("insert into students values('Tom', 'Felton', 5)")

    dc.execute("select * from students")

    # Print only one row
    print(dc.fetchone())

    # Print only multiple rows
    print(dc.fetchmany(3))

    # Print all rows
    print(dc.fetchall())

    dc.execute("delete from students where s_id=5")
















