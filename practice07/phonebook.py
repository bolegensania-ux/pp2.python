# creating a phonebook
import csv
import psycopg2
conn = psycopg2.connect(
    dbname = "my_first_db",
    user = "postgres",
    password = "BS150907",
    host = "localhost",
    port = "5432"
)

cur = conn.cursor()

#cur.execute("""
#CREATE TABLE Phonebook (
 #   id SERIAL PRIMARY KEY,
  #  name VARCHAR(100),
   # phone VARCHAR(20))
#""")
#conn.commit() 
with open("practice07/contacts.csv", "r") as f:
    reader = csv.reader(f)

    for row in reader:
        name = row[0]
        phone = row[1]

        cur.execute(
            "INSERT INTO Phonebook (name, phone) VALUES(%s, %s)" ,
            (name, phone)
        )
conn.commit()
print("Data has been inserted!")

# adding contacts from console
#name = input("Enter name: ")
#phone = input("Enter phhone number: ")

#cur.execute(
 #   "INSERT INTO Phonebook (name, phone) VALUES(%s, %s)", 
  #  (name, phone)
#)
#conn.commit()

#print("Inserted successfully!")

# update information about a contact

cur.execute(
"UPDATE Phonebook SET phone = 345466565 WHERE name LIKE 'S%'"
)
conn.commit()
print("Data has been updated!")

# filtering 
cur.execute(
    "SELECT *FROM Phonebook ORDER BY name ASC"
)
conn.commit()

rows = cur.fetchall()

for row in rows:
    print(row)

cur.execute(
    "DELETE FROM Phonebook WHERE name = 'Baha'"
)
conn.commit()
print("Deletion was successful")