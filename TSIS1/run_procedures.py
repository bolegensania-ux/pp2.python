from connect import connection

conn = connection()
cur = conn.cursor()

with open("TSIS1/procedures.sql", "r") as f:
    cur.execute(f.read())

conn.commit()
cur.close()
conn.close()

print("Procedures created!")