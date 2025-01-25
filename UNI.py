import os
import pyfiglet
from colorama import Fore
import sys

# Ensure the Errors module can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Errors.FR_Errors import get_error_message

text = pyfiglet.figlet_format("FR_UNI")
print(Fore.BLUE + text)

def run_keylogger():
    command = 'python scripts/FR_KeyLogger/KeyLog.py' if os.name == 'nt' else 'python3 scripts/FR_KeyLogger/KeyLog.py'
    os.system(command)

def run_netscan():
    command = 'python scripts/FR_NetScan/NetScan.py' if os.name == 'nt' else 'python3 scripts/FR_NetScan/NetScan.py'
    os.system(command)

def main():
    print("Select the script you want to run:")
    print("1. KeyLogger (Alpha)")
    print("2. NetScan")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        run_keylogger()
    elif choice == '2':
        run_netscan()
    else:
        print(get_error_message("001"))

if __name__ == "__main__":
    main()