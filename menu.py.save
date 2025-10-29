#!/usr/bin/env python3
import os

# Define your commands organized by category
commands = {
    "Git & Repo": {
        "git-status": "Shows repository status",
        "git-sync": "Sync local changes with GitHub",
        "git-sync-loop": "Continuously sync repo"
    },
    "Environment & System": {
        "env-list": "Displays environment utilities and system info",
        "pkg-install": "Install a package: pkg install <package>",
        "pkg-upgrade": "Upgrade all packages",
        "pkg-search": "Search packages: pkg search <query>"
    },
    "Info Library": {
        "add-note": "./info_library_v2.py add <category> <title> \"<content>\"",
        "list-categories": "./info_library_v2.py list",
        "list-category": "./info_library_v2.py list <category>",
        "view-note": "./info_library_v2.py view <category> <title>"
    },
    "Utilities": {
        "nano": "Edit a file: nano <file>",
        "chmod": "Make a script executable: chmod +x <file>",
        "rm": "Remove a file: rm -f <file>",
        "cd": "Change directory: cd <dir>",
        "pwd": "Print working directory",
        "ls": "List files"
    }
}

def print_menu():
    print("\n=== Custom Command Menu ===")
    idx = 1
    menu_mapping = {}
    for category, cmds in commands.items():
        print(f"\n-- {category} --")
        for cmd, desc in cmds.items():
            print(f"{idx}. {cmd} -> {desc}")
            menu_mapping[str(idx)] = cmd
            idx += 1
    print(f"{idx}. Exit")
    menu_mapping[str(idx)] = "exit"
    return menu_mapping

def main():
    while True:
        menu_mapping = print_menu()
        choice = input("\nEnter the number of the command to run: ").strip()
        if choice not in menu_mapping:
            print("Invalid choice, try again.")
            continue
        cmd = menu_mapping[choice]
        if cmd == "exit":
            print("Exiting menu...")
            break
        print(f"Running: {cmd}\n")
        os.system(cmd)

if __name__ == "__main__":
    main()
