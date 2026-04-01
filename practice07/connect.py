# in order to connect PostqreSQL with Python we need to import "import psycopg2"

import psycopg2

conn = psycopg2.connect(
    dbname = "my_first_db",
    user = "postgres",
    password = "BS150907",
    host = "localhost",
    port = "5432"
)

print("Connected!!!")

cur = conn.cursor()

cur.execute("""
CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    Name VARCHAR(100),
    Age INTEGER)
""")

conn.commit()

print("Table created!!!")

cur.close()
conn.close()