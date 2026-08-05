# main.py

from db_config import getConnection

# Create table
def table():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS student(
            id SERIAL PRIMARY KEY,
            name VARCHAR(50),
            marks INTEGER
        )
    """)

    conn.commit()
    conn.close()

    print("Table created successfully")


# Insert data
def insertData():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO student(name, marks) VALUES(%s, %s)",
        ("Rahul", 85)
    )

    conn.commit()
    conn.close()

    print("Data inserted successfully")


# Fetch data
def showData():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


# Main program
table()
insertData()
showData()