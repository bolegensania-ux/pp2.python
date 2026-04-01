# inserting data to already created table
# selecting from the table

import psycopg2

conn = psycopg2.connect(
    dbname = "my_first_db",
    user = "postgres",
    password = "BS150907",
    host = "localhost",
    port = "5432"
)

# INSERT

cur = conn.cursor()

#cur.execute("""
#INSERT INTO Users (id, Name, Age) VALUES
            #(1, 'Saniya', 18),
            #(2, 'Aruzhan', 18),
            #(3, 'Baha', 19),
            #(4, 'Elizabeth', 26) 
#""")

#conn.commit()



# SELECT 

cur.execute("SELECT *FROM Users")

rows = cur.fetchall()

for row in rows:
    print(row)


# Update the table

cur.execute(
    "UPDATE Users SET Age = 20 WHERE Age = 18"
    )

conn.commit()

# Delating from the table
cur.execute(
    "DELETE FROM Users where name LIKE 'B%'"
)

conn.commit()

# Handling Transactions

try: 
    cur.execute("""
        INSERT INTO Users (id, name, age) VALUES
                (5, 'Lera', 'nineteen)
    """)
    conn.commit()
except Exception as e:
    conn.rollback()
    print("Error: ", e)