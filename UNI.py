import os
import pyfiglet
from colorama import Fore

text = pyfiglet.figlet_format("FR_UNI")
print(Fore.BLUE + text)

def run_keylogger():
    os.system('python scripts/FR_KeyLogger/KeyLog.py')

def run_netscan():
    os.system('python scripts/FR_NetScan/NetScan.py')

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
        print('\033[31mError code: 001\033[0m {Choose a valid option}')

if __name__ == "__main__":
    main()