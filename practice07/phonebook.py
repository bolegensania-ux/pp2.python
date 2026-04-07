# creating a phonebook

import csv
import psycopg2   # psycopg2 is used to connect PostrqeSQL databases to Python

# connecting PostgreSQL
def connect():
    return psycopg2.connect(
        dbname = "my_first_db",
        user = "postgres",
        password = "BS150907",
        host = "localhost",
        port = "5432"
    )

# creating table
def create_table(cur, conn):
    cur.execute("""
    CREATE TABLE IF NOT EXISTS Phonebook(
        id SERIAL PRIMARY KEY,
        name varchar(100),
        number varchar(20) UNIQUE
    )
    """)
    conn.commit()

# inserting from the csv file
def insert_from_csv(cur, conn):
    with open("practice07/contacts.csv", "r") as f:
        reader = csv.reader(f)

        for row in reader:
            name, number = row

            cur.execute(
                "INSERT INTO Phonebook (name, number) VALUES (%s, %s) ON CONFLICT (number) DO NOTHING" ,
                (name, number)
            )
    conn.commit()
    print("inserted successfully!")

# insert data from the console
def insert_from_console(cur, conn):
    name = input("enter a name: ")
    number = input("enter a phone: ")

    cur.execute(
    "INSERT INTO Phonebook (name, number) VALUES (%s, %s) ON CONFLICT (number) DO NOTHING",
    (name, number)
    )

    conn.commit()

# update data 
def update_data(cur, conn):
    cur.execute(
    "UPDATE Phonebook SET number = '5685767654' WHERE name LIKE 'B%'"
    )
    print("table has been updated!")
    conn.commit()

# view the table from the console
def view_table(cur):
    cur.execute(
    "SELECT * FROM Phonebook ORDER BY name ASC"
    )
    rows = cur.fetchall()

    for row in rows:
        print(row)

# deleting some information from table
def delete_from_table(cur, conn):
    cur.execute(
    "DELETE FROM Phonebook WHERE name = 'Baha'"
    )
    conn.commit()
    print("deletion was successful!")


def main():
    conn = connect()
    cur = conn.cursor()

    create_table(cur, conn)
    #insert_from_csv(cur, conn)
    #insert_from_console(cur, conn)
    #update_data(cur, conn)
    view_table(cur)
    delete_from_table(cur, conn)

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()
