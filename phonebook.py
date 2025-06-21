phonebook = {}

while True:
    print("\n1. Add contact\n2. Search contact\n3. Delete contact\n4. Exit")
    choice = input("Enter your choice:")

    if choice == "1":
        name = input("Enter name to add:")
        number = input("Enter the number:")
        phonebook[name] = number

    elif choice == "2":
        name = input("Enter name to search:")
        print(f"{name}'s number: {phonebook.get(name,'Not Found')}")
    elif choice == "3":
        name = input("Enter the name to delete:")
        if name in phonebook:
            del phonebook[name]
            print("Name deleted from phonebook")
    elif choice == "4":
        break
    else:
        print("Invalid choice.")
    