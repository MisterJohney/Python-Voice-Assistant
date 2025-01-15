import sqlite3
import time

def init():
    connection = sqlite3.connect("./data/log.db")
    cursor = connection.cursor()

    create_log_table = """CREATE TABLE IF NOT EXISTS "log" (
        "id"	INTEGER UNIQUE,
        "time"	TEXT,
        "input_text"	TEXT,
        "output_text"	TEXT,
        PRIMARY KEY("id" AUTOINCREMENT)
    )"""

    cursor.execute(create_log_table)
    return connection, cursor

def add_log_entry(connection, cursor, input_text, output_text):
    time_struct = time.localtime()
    time_now = time.strftime("%Y-%m-%d %H:%M:%S", time_struct)

    cursor.execute("""INSERT INTO log (time, input_text, output_text)
        VALUES (?, ?, ?)""", (time_now, input_text, output_text))

    connection.commit()

def close_connection(connection):
    connection.close()
