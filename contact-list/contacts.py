import json

def show_menu():
    print("Contact List System")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Edit Contact")
    print("5. Delete Contact")
    print("6. Exit")

def edit_contact(contacts):
    name = input("Enter contact name to edit: ").lower()
    if name in contacts:
        new_phone = input(f"Enter new phone number for {name}: ")
        contacts[name] = new_phone
        save_contacts(contacts)
        print(f"Contact {name} updated.\n")
    else:
        print(f"Contact {name} not found.\n")

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            content = file.read().strip()
            if not content:
                return {}
            return json.loads(content)
    except FileNotFoundError:
        return {}

def save_contacts(contacts):
    with open('contacts.json', 'w') as file:
        json.dump(contacts, file, indent=4)

def add_contact(contacts):
    name = input("Enter contact name: ").lower()
    if name in contacts:
        print(f"Contact {name} already exists.\n")
        return
    phone = input("Enter contact phone number: ")
    contacts[name] = phone
    save_contacts(contacts)
    print(f"Contact {name} added.\n")

def view_contacts(contacts):
    if not contacts:
        print("No contacts available.\n")
        return
    
    print("Contacts:")
    for name, phone in contacts.items():
        print(f"{name}: {phone}")
    print("\n")

def search_contact(contacts):
    if contacts == {}:
        print("No contacts available to search.\n")
        return
    name = input("Enter contact name to search: ").lower()
    if name in contacts:
        print(f"Name: {name}, Phone: {contacts[name]}\n")
    else:
        print(f"Contact {name} not found.\n")

def delete_contact(contacts):
    name = input("Enter contact name to delete: ").lower()
    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print(f"Contact {name} deleted.\n")
    else:
        print(f"Contact {name} not found.\n")

def main():
    contacts = load_contacts()
    while True:
        show_menu()
        choice = input("Choose an option (1-5): ")
        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            edit_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            save_contacts(contacts)
            print("Contacts saved. Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")
            print()

if __name__ == "__main__":
    main()