import scapy.all as scapy
import re
import os
from datetime import datetime

# Create IP_Logs directory if it doesn't exist
log_dir = os.path.join(os.path.dirname(__file__), 'IP_Logs')
if not os.path.exists(log_dir):
    os.makedirs(log_dir)

ip_add_range_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}/[0-9]*$")

while True:
    ip_add_range_entered = input("\nPlease enter the IP address and range that you want to send the ARP request to (ex 192.168.1.0/24): ")
    if ip_add_range_pattern.search(ip_add_range_entered):
        print(f"{ip_add_range_entered} is a valid IP address range")
        break
    else:
        print('\033[31mError code: 001\033[0m {Choose a valid IP address range}')

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

print(f"Scan results have been saved to {log_file_path}")