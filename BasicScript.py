# BasicScript.py
# A simple Python script for beginners to practice editing and pushing changes

def greet(name):
    """
    This function greets the user by name.
    """
    return f"Hello, {name}! Welcome to the GitHub Practice Repository."

def main():
    """
    Main function to execute the script.
    """
    # Ask the user for their name
    user_name = input("Please enter your name: ")

    # Call the greet function and print the result
    greeting_message = greet(user_name)
    print(greeting_message)

if __name__ == "__main__":
    main()
