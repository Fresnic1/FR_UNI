import os

def run_keylogger():
    os.system('python z:scripts/FR_KeyLogger/KeyLog.py')

def main():
    print("Select the script you want to run:")
    print("1. KeyLogger")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        run_keylogger()
    else:
        print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()