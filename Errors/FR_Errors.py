import importlib

def get_error_message(error_code):
    error_messages = {
        "001": "\033[31m [Error code: 001] Invalid choice. Please select a valid option.\033[0m",
        "002": "\033[31m [Error code: 002] This script must be run as root. Please use 'sudo' or run as an administrator.\033[0m",
        "003": "\033[31m [Error code: 003] The script file does not exist.\033[0m",
        "004": "\033[31m [Error code: 004] Failed to connect to the server.\033[0m",
        "005": "\033[33m [Error code: 005] Execution interrupted by the user.\033[0m",
        "006": "\033[31m [Error code: 006] Required package(s) missing. Please install the necessary packages.\033[0m",
        "007": "\033[31m [Error code: 007] IP range is not reachable.\033[0m",

        # Add more error codes and messages as needed
    }
    return error_messages.get(error_code, "Unknown error code.")

def check_required_packages(packages):
    missing_packages = [pkg for pkg in packages if importlib.util.find_spec(pkg) is None]
    if missing_packages:
        print(get_error_message("006"))
        print(f"Missing packages: {', '.join(missing_packages)}")
        return False
    return True

# Example usage
if __name__ == "__main__":
    print(get_error_message("001"))
    print(get_error_message("002"))
    print(get_error_message("003"))
    print(get_error_message("004"))
    print(get_error_message("005"))
    print(get_error_message("006"))
    print(get_error_message("007"))
    print(get_error_message("999"))  # Unknown error code
