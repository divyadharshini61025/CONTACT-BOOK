import json

class ContactBook:
    def __init__(self, filename="contacts.json"):
        self.filename = filename
        self.contacts = []
        self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.filename, "r") as f:
                self.contacts = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            self.contacts = []

    def save_contacts(self):
        with open(self.filename, "w") as f:
            json.dump(self.contacts, f, indent=4)

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")

        contact = {
            "name": name,
            "phone": phone,
            "email": email,
            "address": address
        }

        self.contacts.append(contact)
        self.save_contacts()
        print("Contact added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("\n--- Contact List ---")
        for idx, contact in enumerate(self.contacts, 1):
            print(f"{idx}. {contact['name']} - {contact['phone']}")

    def search_contact(self):
        keyword = input("Enter name or phone number to search: ").lower()
        found = False
        for contact in self.contacts:
            if keyword in contact['name'].lower() or keyword in contact['phone']:
                print("\nContact Found:")
                print(f"Name: {contact['name']}")
                print(f"Phone: {contact['phone']}")
                print(f"Email: {contact['email']}")
                print(f"Address: {contact['address']}")
                found = True
                break
        if not found:
            print("Contact not found.")

    def update_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the contact number to update: ")) - 1
            if 0 <= index < len(self.contacts):
                contact = self.contacts[index]
                print("Leave a field empty to keep it unchanged.")
                name = input(f"Enter new name [{contact['name']}]: ") or contact['name']
                phone = input(f"Enter new phone [{contact['phone']}]: ") or contact['phone']
                email = input(f"Enter new email [{contact['email']}]: ") or contact['email']
                address = input(f"Enter new address [{contact['address']}]: ") or contact['address']

                self.contacts[index] = {
                    "name": name,
                    "phone": phone,
                    "email": email,
                    "address": address
                }
                self.save_contacts()
                print("Contact updated successfully.")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input.")

    def delete_contact(self):
        self.view_contacts()
        try:
            index = int(input("Enter the contact number to delete: ")) - 1
            if 0 <= index < len(self.contacts):
                removed = self.contacts.pop(index)
                self.save_contacts()
                print(f"Deleted contact: {removed['name']}")
            else:
                print("Invalid contact number.")
        except ValueError:
            print("Invalid input.")

def menu():
    contact_book = ContactBook()
    while True:
        print("\n==== Contact Book Menu ====")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contacts()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number between 1-6.")

if __name__ == "__main__":
    menu()
