while True:
    print("\n1. Write new entry\n2. View entries\n3. Exit")
    choice = input("Enter your choice:")

   
    if choice == "1":
        entry = input("Enter new entry:")
        with open("journal.txt","a") as file:
            file.write(entry + "\n")
            print("Entry saved!!")

    elif choice == "2":
        try:
            with open("journal.txt","r") as file:
                print("Your journal:")
                print(file.read())
        except FileNotFoundError:
            print("No journal entries found")

    elif choice == "3":
        break

    else:
        print("Invalid Choice!!!")