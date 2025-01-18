
"""
    Welcome to Elite 101 this program is a starter for your chatbot project.
    The starter prompts the user to enter their name and then greets them with a personalized message.

    Functions:
        get_user_name(): Prompts the user to enter their name and returns it.
        greet_user(name): Prints a greeting message using the provided name.
        main(): Main function that orchestrates the user input and greeting process.

    Execution:
        When the script is run directly (not imported as a module), it will execute the main() function.
"""

userName = "user"
def get_user_name():
    return input("Please enter your name: ")

def greet_user(name):
    print(f"Hello, {name}!")
    userName = name
def getUserAge():
    return input(f"How old are you, {userName}?")
def handleOption(option):
    if option == 1:
        print("You picked the first option")
    elif option == 2:
        print("You picked the second option")
    elif option == 3:
        print("You picked the third option")
    elif option == 4:
        print("You picked the final option")
def menu():
    print(f"Please pick an option, {userName}")
    print("1: Placeholder")
    print("2: Placeholder again")
    print("3: Another placeholder")
    print("4: The last placeholder")
    option = int(input())
    handleOption(option)

def main():
    user_name = get_user_name()
    greet_user(user_name)
    age = getUserAge()
    print(f"Man... {age} is old asf")
    menu()


if __name__ == "__main__":
    main()
