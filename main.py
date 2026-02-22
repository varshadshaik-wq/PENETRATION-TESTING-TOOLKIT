import sys
import os

# Fix module imports
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from modules.port_scanner import scan_ports
from modules.banner_grabber import grab_banner
from modules.brute_forcer import brute_force


def show_menu():
    print("""
===============================
  PENETRATION TESTING TOOLKIT
===============================
1. Port Scanner
2. Banner Grabber
3. Brute Force (Demo)
4. Exit
""")


def main():
    while True:
        show_menu()
        choice = input("Select option: ")

        # -------------------- PORT SCANNER --------------------
        if choice == "1":
            target = input("Enter target IP: ")
            start_port = int(input("Enter start port: "))
            end_port = int(input("Enter end port: "))
            scan_ports(target, start_port, end_port)

        # -------------------- BANNER GRABBER --------------------
        elif choice == "2":
            target = input("Enter target IP: ")
            port = int(input("Enter port: "))
            banner = grab_banner(target, port)
            print("\nBanner:\n", banner)

        # -------------------- BRUTE FORCE --------------------
        elif choice == "3":
            username = input("Enter username: ")

            # Safe absolute path to wordlist
            base_dir = os.path.dirname(os.path.abspath(__file__))
            wordlist_path = os.path.join(base_dir, "wordlists", "passwords.txt")

            with open(wordlist_path) as f:
                passwords = [line.strip() for line in f]

            brute_force(username, passwords, "admin")

        # -------------------- EXIT --------------------
        elif choice == "4":
            print("Exiting toolkit...")
            break

        else:
            print("Invalid option, try again.")


if __name__ == "__main__":
    main()