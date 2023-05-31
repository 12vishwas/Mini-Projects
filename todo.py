contacts = {}

def add_contact():
    name = input('Enter name to add: ')
    number = int(input('Enter  number: '))
    contacts[name] = number
    print('Contact added successfully')

def search_contact():
    name = input("Enter the name to search: ")
    if name in contacts:
        print(f"Phone number: {contacts[name]}")
    else:
        print("Contact not found.")


def delete_contact():
    name = input('Enter name for delete: ')
    if name in contacts:
        del contacts[name]
    else:
        print('Contact not found')

def display_contacts():
    print('contacts: ')
    if contacts:
        for name,number in contacts:
            print(f'name: {name},number:{number}')
    else:
        print('No contacts found')


def main():
    print("\n***** Contact Book *****")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Display Contacts")
    choice = input("Enter your choice (1-4): ")

    if choice == '1':
            add_contact()
    elif choice == '2':
        search_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        display_contacts()
    else:
        print('Invalid choice')

if __name__ == '__main__':
    main()

# contacts = {}  # Dictionary to store contacts

# def add_contact():
#     name = input("Enter the name: ")
#     number = input("Enter the phone number: ")
#     contacts[name] = number
#     print("Contact added successfully!")

# def search_contact():
#     name = input("Enter the name to search: ")
#     if name in contacts:
#         print(f"Phone number: {contacts[name]}")
#     else:
#         print("Contact not found.")

# def delete_contact():
#     name = input("Enter the name to delete: ")
#     if name in contacts:
#         del contacts[name]
#         print("Contact deleted successfully!")
#     else:
#         print("Contact not found.")

# def display_contacts():
#     print("Contacts:")
#     if contacts:
#         for name, number in contacts.items():
#             print(f"Name: {name}, Phone number: {number}")
#     else:
#         print("No contacts found.")

# def main():
#     while True:
#         print("\n***** Contact Book *****")
#         print("1. Add Contact")
#         print("2. Search Contact")
#         print("3. Delete Contact")
#         print("4. Display Contacts")
#         print("5. Quit")
#         choice = input("Enter your choice (1-5): ")

#         if choice == '1':
#             add_contact()
#         elif choice == '2':
#             search_contact()
#         elif choice == '3':
#             delete_contact()
#         elif choice == '4':
#             display_contacts()
#         elif choice == '5':
#             break
#         else:
#             print("Invalid choice. Please try again.")

# if __name__ == '__main__':
#     main()






















