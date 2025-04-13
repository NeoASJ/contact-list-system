import json
import os

class Contact:
    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email

class ContactBook:
    def __init__(self, filename):
        self.filename = filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as file:
                data = json.load(file)
                return [Contact(contact["name"], contact["phone"], contact["email"]) for contact in data]
        else:
            return []

    def save_contacts(self):
        data = [{"name": contact.name, "phone": contact.phone, "email": contact.email} for contact in self.contacts]
        with open(self.filename, "w") as file:
            json.dump(data, file, indent=4)

    def add_contact(self):
        print("\nLet's add a new contact!")
        name = input("What is the contact's name? ")
        phone = input("What is their phone number? ")
        email = input("What is their email address? ")
        new_contact = Contact(name, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()
        print("Contact added successfully! You now have {} contacts.".format(len(self.contacts)))

    def view_contacts(self):
        if not self.contacts:
            print("\nYou don't have any contacts yet. Why not add one?")
        else:
            print("\nHere are all your contacts:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")

    def search_contact(self):
        print("\nLet's find a contact!")
        name = input("Enter the name of the contact you're looking for: ")
        found_contacts = [contact for contact in self.contacts if name.lower() in contact.name.lower()]
        if found_contacts:
            print("\nHere are the contacts matching your search:")
            for index, contact in enumerate(found_contacts, start=1):
                print(f"{index}. Name: {contact.name}, Phone: {contact.phone}, Email: {contact.email}")
        else:
            print("\nSorry, no matching contacts found.")

    def update_contact(self):
        self.view_contacts()
        try:
            choice = int(input("\nEnter the number of the contact you want to update: "))
            if choice > 0 and choice <= len(self.contacts):
                contact = self.contacts[choice - 1]
                print("\nEnter new details (press Enter to keep the current value):")
                contact.name = input(f"Name ({contact.name}): ") or contact.name
                contact.phone = input(f"Phone ({contact.phone}): ") or contact.phone
                contact.email = input(f"Email ({contact.email}): ") or contact.email
                self.save_contacts()
                print("Contact updated successfully!")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def delete_contact(self):
        self.view_contacts()
        try:
            choice = int(input("\nEnter the number of the contact you want to delete: "))
            if choice > 0 and choice <= len(self.contacts):
                del self.contacts[choice - 1]
                self.save_contacts()
                print("Contact deleted successfully!")
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def main():
    filename = "contacts.json"
    contact_book = ContactBook(filename)

    while True:
        print("\nWelcome to Your Contact List System!")
        print("---------------------------------------")
        print("1. Add a New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Update an Existing Contact")
        print("5. Delete a Contact")
        print("6. Exit the Application")
        
        try:
            choice = int(input("Please choose an option: "))
            if choice == 1:
                contact_book.add_contact()
            elif choice == 2:
                contact_book.view_contacts()
            elif choice == 3:
                contact_book.search_contact()
            elif choice == 4:
                contact_book.update_contact()
            elif choice == 5:
                contact_book.delete_contact()
            elif choice == 6:
                print("Thank you for using the contact list system")
                break
            else:
                print("Sorry, that's not a valid option. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()
