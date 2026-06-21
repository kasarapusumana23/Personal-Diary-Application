from datetime import datetime

password = "Diary@2026"

user_password = input("Enter Password: ")

if user_password != password:
    print("Incorrect Password!")
    exit()

while True:
    print("\n===== PERSONAL DIARY =====")
    print("1. Write Entry")
    print("2. View Entries")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        entry = input("\nWrite your diary entry:\n")

        with open("diary.txt", "a") as file:
            file.write("\n")
            file.write("Date: " + datetime.now().strftime("%d-%m-%Y %H:%M:%S") + "\n")
            file.write(entry + "\n")
            file.write("-" * 40 + "\n")

        print("Entry saved successfully!")

    elif choice == "2":
        try:
            with open("diary.txt", "r") as file:
                print("\n===== YOUR DIARY =====\n")
                print(file.read())
        except FileNotFoundError:
            print("No diary entries found.")

    elif choice == "3":
        print("Thank you for using Personal Diary!")
        break

    else:
        print("Invalid choice. Try again.")