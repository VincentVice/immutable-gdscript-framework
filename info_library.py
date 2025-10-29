import json
import os

LIBRARY_FILE = "info_library.json"

# Ensure the library exists
if not os.path.exists(LIBRARY_FILE):
    with open(LIBRARY_FILE, "w") as f:
        json.dump([], f)

def add_entry():
    entry = input("Enter your note: ")
    with open(LIBRARY_FILE, "r") as f:
        data = json.load(f)
    data.append({"note": entry})
    with open(LIBRARY_FILE, "w") as f:
        json.dump(data, f, indent=2)
    print("Note added!")

def list_entries():
    with open(LIBRARY_FILE, "r") as f:
        data = json.load(f)
    if not data:
        print("No notes yet.")
        return
    print("\nYour Notes:")
    for i, item in enumerate(data, 1):
        print(f"{i}. {item['note']}")

def main():
    while True:
        print("\nInfo Library Menu:")
        print("1. Add note")
        print("2. List notes")
        print("3. Exit")
        choice = input("Select an option: ")
        if choice == "1":
            add_entry()
        elif choice == "2":
            list_entries()
        elif choice == "3":
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
