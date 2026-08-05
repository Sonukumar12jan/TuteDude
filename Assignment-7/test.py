# test.py

from db_config import getConnection

# Create table
def createTable():
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

    print("Table created")


# Insert record
def insertStudent():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute(
        "INSERT INTO student(name, marks) VALUES(%s,%s)",
        ("Sonu", 90)
    )

    conn.commit()
    conn.close()

    print("Record inserted")


# Display records
def displayStudent():
    conn = getConnection()
    cur = conn.cursor()

    cur.execute("SELECT * FROM student")

    rows = cur.fetchall()

    for row in rows:
        print(row)

    conn.close()


createTable()
insertStudent()
displayStudent()