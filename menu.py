#!/usr/bin/env python3
import os
import subprocess
import sys

# ANSI colors for readability (optional)
HEADER = "\033[95m"
OKBLUE = "\033[94m"
OKGREEN = "\033[92m"
WARNING = "\033[93m"
FAIL = "\033[91m"
ENDC = "\033[0m"

def clear_screen():
    os.system('clear')

def run_command(command, confirm=False):
    """Run a shell command with optional confirmation."""
    if confirm:
        choice = input(f"{WARNING}Are you sure you want to run '{command}'? [y/N]: {ENDC}").strip().lower()
        if choice != 'y':
            print("Command canceled.")
            return
    try:
        subprocess.run(command, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"{FAIL}Error running command: {e}{ENDC}")

def check_file_exists(path):
    if not os.path.exists(path):
        print(f"{FAIL}Error: File '{path}' not found.{ENDC}")
        return False
    return True

def main_menu():
    while True:
        clear_screen()
        print(f"{HEADER}=== Custom Command Menu ==={ENDC}\n")
        print(f"{OKBLUE}-- Git & Repo --{ENDC}")
        print("1. git-status -> Shows repository status")
        print("2. git-sync -> Sync local changes with GitHub")
        print("3. git-sync-loop -> Continuously sync repo\n")
        
        print(f"{OKBLUE}-- Environment & System --{ENDC}")
        print("4. env-list -> Displays environment utilities and system info")
        print("5. pkg-install -> Install a package (pkg install <package>)")
        print("6. pkg-upgrade -> Upgrade all packages")
        print("7. pkg-search -> Search packages (pkg search <query>)\n")
        
        print(f"{OKBLUE}-- Info Library --{ENDC}")
        print("8. add-note -> Add a note to info library")
        print("9. list-categories -> List all categories in info library")
        print("10. list-category -> List all notes in a category")
        print("11. view-note -> View a specific note\n")
        
        print(f"{OKBLUE}-- Utilities --{ENDC}")
        print("12. nano -> Edit a file")
        print("13. chmod -> Make a script executable")
        print("14. rm -> Remove a file")
        print("15. cd -> Change directory")
        print("16. pwd -> Print working directory")
        print("17. ls -> List files")
        print("18. Exit\n")
        
        choice = input("Enter the number of the command to run: ").strip()
        
        if choice == '1':
            run_command("git status")
        elif choice == '2':
            run_command("git pull --rebase && git push", confirm=True)
        elif choice == '3':
            print("Starting git-sync-loop. Press Ctrl+C to stop.")
            try:
                while True:
                    run_command("git pull --rebase && git push")
            except KeyboardInterrupt:
                print("Stopped git-sync-loop.")
        elif choice == '4':
            run_command("env-list")
        elif choice == '5':
            pkg = input("Enter package name to install: ").strip()
            if pkg:
                run_command(f"pkg install {pkg}")
        elif choice == '6':
            run_command("pkg upgrade", confirm=True)
        elif choice == '7':
            search = input("Enter package name to search: ").strip()
            if search:
                run_command(f"pkg search {search}")
        elif choice == '8':
            if check_file_exists("./info_library_v2.py"):
                cat = input("Enter category: ").strip()
                title = input("Enter title: ").strip()
                content = input("Enter content: ").strip()
                run_command(f'./info_library_v2.py add {cat} {title} "{content}"')
        elif choice == '9':
            if check_file_exists("./info_library_v2.py"):
                run_command("./info_library_v2.py list")
        elif choice == '10':
            if check_file_exists("./info_library_v2.py"):
                cat = input("Enter category to list notes: ").strip()
                run_command(f"./info_library_v2.py list {cat}")
        elif choice == '11':
            if check_file_exists("./info_library_v2.py"):
                cat = input("Enter category: ").strip()
                title = input("Enter title: ").strip()
                run_command(f"./info_library_v2.py view {cat} {title}")
        elif choice == '12':
            file = input("Enter file to edit: ").strip()
            if file:
                run_command(f"nano {file}")
        elif choice == '13':
            file = input("Enter file to make executable: ").strip()
            if file:
                run_command(f"chmod +x {file}")
        elif choice == '14':
            file = input("Enter file to remove: ").strip()
            if file:
                run_command(f"rm -f {file}", confirm=True)
        elif choice == '15':
            dir = input("Enter directory to change to: ").strip()
            if dir:
                try:
                    os.chdir(dir)
                except FileNotFoundError:
                    print(f"{FAIL}Directory not found.{ENDC}")
        elif choice == '16':
            print(os.getcwd())
            input("Press Enter to return to menu...")
        elif choice == '17':
            run_command("ls")
            input("Press Enter to return to menu...")
        elif choice == '18':
            confirm = input("Are you sure you want to exit? [y/N]: ").strip().lower()
            if confirm == 'y':
                print("Exiting...")
                sys.exit()
        else:
            print(f"{FAIL}Invalid choice. Try again.{ENDC}")
            input("Press Enter to return to menu...")

if __name__ == "__main__":
    main_menu()
