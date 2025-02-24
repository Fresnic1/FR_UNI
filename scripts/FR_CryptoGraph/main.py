import hashlib
import hmac
import os

def hash_text(text, salt):
    """Hashes the given text with the provided salt."""
    return hashlib.pbkdf2_hmac('sha256', text.encode(), salt.encode(), 100000).hex()

def verify_text(text, salt, hashed_text):
    """Verifies if the given text matches the hashed text."""
    return hmac.compare_digest(hash_text(text, salt), hashed_text)

def save_hashed_text_to_file(filename, text):
    """Saves the hashed text to a file."""
    with open(filename, 'w') as file:
        file.write(text)

def read_hashed_text_from_file(filename):
    """Reads the hashed text from a file."""
    with open(filename, 'r') as file:
        return file.read()

if __name__ == "__main__":
    choice = input("Do you want to (1) hash a new text or (2) verify an existing hash? Enter 1 or 2: ")
    
    if choice == '1':
        text = input("Enter the text to hash: ")
        salt = input("Enter the salt: ")
        
        hashed_text = hash_text(text, salt)
        print(f"Hashed Text: {hashed_text}")
        
        filename = input("Enter the filename to save the hashed text: ")
        save_hashed_text_to_file(filename, hashed_text)
        print(f"Hashed text saved to {filename}")
        
    elif choice == '2':
        text = input("Enter the text to verify: ")
        salt = input("Enter the salt: ")
        filename = input("Enter the filename containing the hashed text: ")
        
        hashed_text = read_hashed_text_from_file(filename)
        is_verified = verify_text(text, salt, hashed_text)
        print(f"Verification: {'Success' if is_verified else 'Failure'}")
    else:
        print("Invalid choice. Please enter 1 or 2.")