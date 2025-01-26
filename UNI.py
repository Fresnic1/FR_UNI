import os
import pyfiglet
from colorama import Fore, Style
import sys
import subprocess
import importlib
import time

# Ensure the Errors module can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from Errors.FR_Errors import get_error_message, check_required_packages

required_packages = ["pyfiglet", "colorama", "scapy", "re", "datetime", "sys", "pynput", "socket", "subprocess", "time", "importlib", "os"]

def install_packages(packages):
    for package in packages:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])

missing_packages = [pkg for pkg in required_packages if importlib.util.find_spec(pkg) is None]

if missing_packages:
    print(get_error_message("006"))
    print(f"Missing packages: {', '.join(missing_packages)}")
    install_packages(missing_packages)

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
    print(Style.BRIGHT + Fore.YELLOW + "1. KeyLogger (Alpha)" + Style.RESET_ALL)
    print(Style.BRIGHT + Fore.YELLOW + "2. NetScan" + Style.RESET_ALL)

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        run_keylogger()
    elif choice == '2':
        run_netscan()
    elif choice in ['quit', 'exit']:
        print("Exiting...")
        time.sleep(3)
        USER = os.getenv('USERNAME') or os.getenv('USER')  # Get the username from environment variables
        print(f"Thank you for using FR_UNI {USER}!")
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        sys.exit(0)
    else:
        print(get_error_message("001"))

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(get_error_message("005"))
    except Exception as e:
        print(get_error_message("999"))
        print(str(e))
