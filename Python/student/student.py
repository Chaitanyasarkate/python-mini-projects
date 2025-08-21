import json
import os

FILE = "students.json"

def load_data():
    return json.load(open(FILE)) if os.path.exists(FILE) else {}

def save_data(data):
    json.dump(data, open(FILE, "w"), indent=4)

def add_student():
    data = load_data()
    roll = input("Roll No: ")
    name = input("Name: ")
    marks = int(input("Marks: "))
    data[roll] = {"name": name, "marks": marks}
    save_data(data)
    print("✅ Student added.")

def view_students():
    data = load_data()
    for roll, info in data.items():
        print(f"{roll}: {info['name']} → {info['marks']} marks")

def update_student():
    data = load_data()
    roll = input("Roll No to update: ")
    if roll in data:
        data[roll]["marks"] = int(input("New Marks: "))
        save_data(data)
        print("✅ Updated.")
    else:
        print("❌ Not found.")

def delete_student():
    data = load_data()
    roll = input("Roll No to delete: ")
    if roll in data:
        del data[roll]
        save_data(data)
        print("🗑 Deleted.")
    else:
        print("❌ Not found.")

if __name__ == "__main__":
    while True:
        print("\n1. Add 2. View 3. Update 4. Delete 5. Exit")
        choice = input("Choose: ")
        if choice == "1": add_student()
        elif choice == "2": view_students()
        elif choice == "3": update_student()
        elif choice == "4": delete_student()
        else: break
