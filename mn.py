import os
import time
from termcolor import colored

# Define the username and password
CORRECT_USERNAME = "Musaib"
CORRECT_PASSWORD = "Nahila"

# Clear the terminal screen
def clear_screen():
    os.system('clear' if os.name == 'posix' else 'cls')

# Main function
def main():
    clear_screen()
    print(colored("**************************************", "blue"))
    print(colored("      WELCOME TO MN CORPORATION       ", "yellow", attrs=['bold']))
    print(colored("**************************************", "blue"))
    print()

    # Prompt for username and password
    username = input(colored("Enter Username: ", "green"))
    password = input(colored("Enter Password: ", "green"))

    # Validate credentials
    if username == CORRECT_USERNAME and password == CORRECT_PASSWORD:
        print(colored("\nAccess Granted!", "green", attrs=['bold']))
        print(colored("Redirecting you to the secure page...", "yellow"))
        time.sleep(2)  # Simulate delay for redirection
        os.system(f"xdg-open https://fit-dove.static.domains/index.com")  # Opens the URL in a browser
    else:
        print(colored("\nAccess Denied!", "red", attrs=['bold']))
        print(colored("Your credentials are incorrect.", "red"))
        print(colored(f"Entered Username: {username}", "yellow"))

# Run the program
if __name__ == "__main__":
    main()
