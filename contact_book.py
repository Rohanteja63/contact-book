import random
import string 
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    address = input("Enter address: ")
    contacts.append({'name': name,'phone':phone,'email':email,'address':address})
    print("Contact added sucessfully.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts found.")
    else:
        for idx, contact in enumerate(contacts):
            print(f"{idx + 1}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact(contacts):
    query = input("Enter name or phone number to search: ").strip().lower()
    found_contacts = [contact for contact in contacts if query in contact['name'].lower() or query in contact['phone number']]
    if not  found_contacts():
        print("No contacts found.")
    else:
        for contact in found_contacts:
            print(f"Name:{contact['Name']},Phone:{contact['phone number']},Email:{contact['Email']},Address:{contact['Address']}")

def update_contact(contacts):
    search_query = input("Enter name or phone number of the contact to update: ").strip().lower()
    for contact in contacts:
        if search_query in contact['name'] or search_query in contact['phone']:
            print("Current details: ")
            print(f"Name:{contact['Name']},Phone:{contact['phone number']},Email:{contact['Email']},Address:{contact['Address']}")
            contact['name'] = input("Enter new name (or press to keep current): ")or contact['name']
            contact['phone'] = input("Enter new phone number (or press to keep current): ")or contact['phone']
            contact['email'] = input("Enter new email (or press to keep current): ")or contact['email']
            contact['address'] = input("Enter new address (or press to keep current): ")or contact['address']
            print("Contact update sucessfully.")
            return
        print("Contact not found.")

def delete_contact(contacts):
    search_query = input("Enter name or phone number of the contact  to delete: ").strip().lower()
    for contact in contacts:
        if search_query in contact['name'] or search_query in contact['phone']:
            contacts.remove(contact)
            print("Contact delete successfully.")
            return
        print("Contact not found.")

def main():
    contacts = []

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            search_contact(contacts)
        elif choice == '4':
            update_contact(contacts)
        elif choice == '5':
            delete_contact(contacts)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()





    


