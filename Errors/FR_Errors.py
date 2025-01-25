def get_error_message(error_code):
    error_messages = {
        "001": "Invalid choice. Please select a valid option.",
        "002": "This script must be run as root. Please use 'sudo' or run as an administrator.",
        "003": "The script file does not exist.",
        "004": "Failed to connect to the server.",
        # Add more error codes and messages as needed
    }
    return error_messages.get(error_code, "Unknown error code.")

# Example usage
if __name__ == "__main__":
    print(get_error_message("001"))
    print(get_error_message("002"))
    print(get_error_message("999"))  # Unknown error code