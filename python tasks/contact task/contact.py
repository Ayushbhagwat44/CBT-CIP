
class Contact:
    def __init__(self, name, phonenumber, email):
        self.name = name
        self.phonenumber = phonenumber
        self.email = email

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phonenumber}, Email: {self.email}"

    
class ContactManager:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phonenumber, email):
        new_contact = Contact(name, phonenumber, email)
        self.contacts.append(new_contact)
        print(f"Contact {name} added.")

    def delete_contact(self, name):
        self.contacts = [contact for contact in self.contacts if contact.name != name]
        print(f"Deleted contact {name}")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None

    def list_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        for contact in self.contacts:
            print(contact)


def main():
    contact_manager = ContactManager()  # Fixed the object instantiation with parentheses
    while True:
        print("\n1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. List Contacts")
        print("5. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email: ")
            contact_manager.add_contact(name, phone_number, email)
        elif choice == '2':
            name = input("Enter name to delete: ")
            contact_manager.delete_contact(name)
        elif choice == '3':
            name = input("Enter name to search: ")
            contact = contact_manager.search_contact(name)
            if contact:
                print(f"Contact found: {contact}")
            else:
                print("Contact not found.")
        elif choice == '4':
            contact_manager.list_contacts()
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()


