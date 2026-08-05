# db_config.py

import psycopg2

def getConnection():
    conn = psycopg2.connect(
        database="testDb",
        user="postgres",
        password="1234",
        host="localhost",
        port="5432"
    )

    return conn