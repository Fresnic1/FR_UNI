import re
import os
import sys
import subprocess
import time
from datetime import datetime
from colorama import Fore, Style
import scapy.all as scapy

# Ensure the Errors module can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from Errors.FR_Errors import get_error_message

def is_admin():
    try:
        return os.geteuid() == 0
    except AttributeError:
        # Windows check for admin privileges
        import ctypes
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

def is_ip_reachable(ip):
    try:
        # Use the ping command to check if the IP is reachable
        output = subprocess.check_output(["ping", "-c", "1", ip] if os.name != 'nt' else ["ping", "-n", "1", ip])
        return True
    except subprocess.CalledProcessError:
        return False

def main():
    # Check for root/administrator privileges
    if not is_admin():
        sys.exit(get_error_message("002"))

    # Create IP_Logs directory if it doesn't exist
    log_dir = os.path.join(os.path.dirname(__file__), 'IP_Logs')
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)

    ip_add_range_pattern = re.compile(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

    while True:
        ip_add_range_entered = input(Fore.BLUE + "\nPlease enter the IP address and range that you want to send the ARP request to " + Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + "(ex 192.168.1.0/24): " + Style.RESET_ALL)
        if ip_add_range_entered.lower() in ['quit', 'exit']:
            USER = os.getenv('USERNAME') or os.getenv('USER')  # Get the username from environment variables
            print(f"Thank you for using FR_UNI {USER}!")
            sys.exit(0)
        if ip_add_range_pattern.search(ip_add_range_entered):
            break
        else:
            print(f'{get_error_message("001")}')

    # Example IP address to check
    ip_address = ip_add_range_entered.split('/')[0]

    while not is_ip_reachable(ip_address):
        print(get_error_message("007"))
        ip_add_range_entered = input(Fore.BLUE + "\nPlease enter a reachable IP address and range " + Style.RESET_ALL + Style.BRIGHT + Fore.WHITE + "(ex 192.168.1.0/24): " + Style.RESET_ALL)
        if ip_add_range_entered.lower() in ['quit', 'exit']:
            USER = os.getenv('USERNAME') or os.getenv('USER')  # Get the username from environment variables
            print(f"Thank you for using FR_UNI {USER}!")
            sys.exit(0)
        ip_address = ip_add_range_entered.split('/')[0]

    print(Fore.GREEN + Style.BRIGHT + "IP address is reachable. Continuing with the script..." + Style.RESET_ALL)

    # Generate a filename with the current date and time
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    log_file_path = os.path.join(log_dir, f'scan_log_{timestamp}.txt')

    # Redirect output to the log file
    with open(log_file_path, 'w') as log_file:
        original_stdout = os.sys.stdout
        os.sys.stdout = log_file
        try:
            arp_result = scapy.arping(ip_add_range_entered)
        finally:
            os.sys.stdout = original_stdout

    print(f"{Fore.GREEN}Scan results have been saved to {Style.BRIGHT}{log_file_path}{Style.RESET_ALL}")

    # Run UNI.py after the scan is completed
    print(Fore.YELLOW + "Running UNI.py..." + Style.RESET_ALL)
    time.sleep(2)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), '..', '..', 'UNI.py')])

    return True

if __name__ == "__main__":
    while not main():
        print("Restarting the script...")
        time.sleep(5)  # Wait for 5 seconds before restarting
