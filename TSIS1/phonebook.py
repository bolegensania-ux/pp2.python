import csv
import json
from connect import connection


def import_from_csv():
    conn = connection()
    cur = conn.cursor()

    with open("TSIS1/contacts.csv", "r") as f:
        reader = csv.DictReader(f)

        for row in reader:
            name = row["name"]
            email = row["email"]
            birthday = row["birthday"]
            group = row["group"]
            phone = row["phone"]
            phone_type = row["type"]

            cur.execute("""
                INSERT INTO groups(name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING;
            """, (group,))

            cur.execute("SELECT id FROM groups WHERE name=%s;", (group,))
            group_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO contacts(name, email, birthday, group_id)
                VALUES (%s,%s,%s,%s)
                RETURNING id;
            """, (name, email, birthday, group_id))

            contact_id = cur.fetchone()[0]

            cur.execute("""
                INSERT INTO phones(contact_id, phone, type)
                VALUES (%s,%s,%s);
            """, (contact_id, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()
    print("CSV imported")


def search():
    conn = connection()
    cur = conn.cursor()

    q = input("Search: ")
    cur.execute("SELECT * FROM search_contacts(%s);", (q,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def filter_by_group():
    conn = connection()
    cur = conn.cursor()

    g = input("Group: ")

    cur.execute("""
        SELECT c.name, c.email, g.name
        FROM contacts c
        JOIN groups g ON c.group_id = g.id
        WHERE g.name = %s;
    """, (g,))

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def sort_contacts():
    conn = connection()
    cur = conn.cursor()

    choice = input("Sort by (name/birthday): ")

    if choice not in ["name", "birthday"]:
        print("Invalid")
        return

    cur.execute(f"SELECT name,email,birthday FROM contacts ORDER BY {choice};")

    for row in cur.fetchall():
        print(row)

    cur.close()
    conn.close()


def export_json():
    conn = connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT c.name, c.email, c.birthday, g.name, p.phone, p.type
        FROM contacts c
        LEFT JOIN groups g ON c.group_id = g.id
        LEFT JOIN phones p ON c.id = p.contact_id;
    """)

    data = cur.fetchall()

    with open("contacts.json", "w") as f:
        json.dump(data, f, default=str)

    print("Exported")

    cur.close()
    conn.close()


def import_json():
    conn = connection()
    cur = conn.cursor()

    with open("contacts.json", "r") as f:
        data = json.load(f)

    for row in data:
        name, email, birthday, group, phone, phone_type = row

        cur.execute("SELECT id FROM contacts WHERE name=%s;", (name,))
        existing = cur.fetchone()

        if existing:
            choice = input(f"{name} exists (skip/overwrite): ")

            if choice == "skip":
                continue
            elif choice == "overwrite":
                cur.execute("DELETE FROM contacts WHERE name=%s;", (name,))

        cur.execute("INSERT INTO groups(name) VALUES (%s) ON CONFLICT DO NOTHING;", (group,))
        cur.execute("SELECT id FROM groups WHERE name=%s;", (group,))
        gid = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO contacts(name,email,birthday,group_id)
            VALUES (%s,%s,%s,%s)
            RETURNING id;
        """, (name, email, birthday, gid))

        cid = cur.fetchone()[0]

        cur.execute("""
            INSERT INTO phones(contact_id,phone,type)
            VALUES (%s,%s,%s);
        """, (cid, phone, phone_type))

    conn.commit()
    cur.close()
    conn.close()


def menu():
    while True:
        print("\n1 Import CSV")
        print("2 Search")
        print("3 Filter by group")
        print("4 Sort")
        print("5 Export JSON")
        print("6 Import JSON")
        print("0 Exit")

        c = input("Choice: ")

        if c == "1":
            import_from_csv()
        elif c == "2":
            search()
        elif c == "3":
            filter_by_group()
        elif c == "4":
            sort_contacts()
        elif c == "5":
            export_json()
        elif c == "6":
            import_json()
        elif c == "0":
            break


if __name__ == "__main__":
    menu()