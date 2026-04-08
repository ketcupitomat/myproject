from connect import connect
import csv

conn = connect()
cur = conn.cursor()


# 📥 Вставка из CSV
def insert_from_csv(filename):
    with open(filename, "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            cur.execute(
                "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
                (row["name"], row["phone"])
            )
    conn.commit()
    print("✅ Data inserted from CSV")


# ➕ Вставка вручную
def insert_from_console():
    name = input("Enter name: ")
    phone = input("Enter phone: ")

    cur.execute(
        "INSERT INTO phonebook (name, phone) VALUES (%s, %s)",
        (name, phone)
    )
    conn.commit()
    print("✅ Contact added")


# 🔍 Запросы с фильтрами
def query_contacts():
    print("1. Search by name")
    print("2. Search by phone prefix")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE name ILIKE %s",
            ('%' + name + '%',)
        )
    elif choice == "2":
        prefix = input("Enter prefix: ")
        cur.execute(
            "SELECT * FROM phonebook WHERE phone LIKE %s",
            (prefix + '%',)
        )

    rows = cur.fetchall()
    for row in rows:
        print(row)


# ✏️ Обновление
def update_contact():
    name = input("Enter name to update: ")
    new_name = input("New name (leave empty to skip): ")
    new_phone = input("New phone (leave empty to skip): ")

    if new_name:
        cur.execute(
            "UPDATE phonebook SET name=%s WHERE name=%s",
            (new_name, name)
        )
    if new_phone:
        cur.execute(
            "UPDATE phonebook SET phone=%s WHERE name=%s",
            (new_phone, name)
        )

    conn.commit()
    print("✏️ Updated!")


# ❌ Удаление
def delete_contact():
    print("1. Delete by name")
    print("2. Delete by phone")
    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter name: ")
        cur.execute("DELETE FROM phonebook WHERE name=%s", (name,))
    elif choice == "2":
        phone = input("Enter phone: ")
        cur.execute("DELETE FROM phonebook WHERE phone=%s", (phone,))

    conn.commit()
    print("🗑 Deleted!")


# 📋 Меню
def menu():
    while True:
        print("\n=== PHONEBOOK ===")
        print("1. Insert from CSV")
        print("2. Add contact")
        print("3. Query contacts")
        print("4. Update contact")
        print("5. Delete contact")
        print("6. Exit")

        choice = input("Choose: ")

        if choice == "1":
            insert_from_csv("contacts.csv")
        elif choice == "2":
            insert_from_console()
        elif choice == "3":
            query_contacts()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            break
        else:
            print("Invalid choice")


menu()

cur.close()
conn.close()