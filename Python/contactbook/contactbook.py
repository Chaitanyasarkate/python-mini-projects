import json
import os

FILE = "contacts.json"

def load_contacts():
    return json.load(open(FILE)) if os.path.exists(FILE) else {}

def save_contacts(contacts):
    json.dump(contacts, open(FILE, "w"), indent=4)

def add_contact():
    contacts = load_contacts()
    name = input("Name: ")
    phone = input("Phone: ")
    contacts[name] = phone
    save_contacts(contacts)
    print("✅ Contact added!")

def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ")
    print(f"{name}: {contacts.get(name, 'Not found')}")

def update_contact():
    contacts = load_contacts()
    name = input("Enter name to update: ")
    if name in contacts:
        contacts[name] = input("New phone: ")
        save_contacts(contacts)
        print("✅ Contact updated!")
    else:
        print("❌ Not found.")

def show_all():
    contacts = load_contacts()
    for name, phone in contacts.items():
        print(f"{name} → {phone}")

if __name__ == "__main__":
    while True:
        print("\n1. Add  2. Search  3. Update  4. Show All  5. Exit")
        choice = input("Choose: ")
        if choice == "1": add_contact()
        elif choice == "2": search_contact()
        elif choice == "3": update_contact()
        elif choice == "4": show_all()
        else: break
