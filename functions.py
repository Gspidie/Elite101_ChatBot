def chatbot_introduction():
    print("Welcome to [Orginization Name]'s ChatBot.")
    print("This bot is designed to help you anwser general questions you may have.")
    print("Please follow the prompts to get started.")

def get_user_name():
    print()
    return input("Enter your name: ")

def get_user_age():
    print()
    return int(input("Enter your age: "))

def greet_user(name, age):
    print()

    if age < 15:
        print("Oops! You may not be old enough to use this chatbot.")
    elif 15 <= age < 18:
        print(f"Hello, {name}! You are eligible to use this chatbot with parental supervision.")
    elif 18 <= age < 65:
        print(f"Hello, {name}! Nice to have you.")
    elif age >= 65:
        print(f"Hello, {name}. I am ready to walk you through your questions!")

def present_menu():
    print("What do you need help with today?")
    print("1. [Placeholder]")
    print("2. [Placeholder]")
    print("3. [Placeholder]")
    print("4. [Placeholder]")
    print("5. Exit")

def collect_menu_choice():
    choice = 0
    user_has_no_choice = True

    while user_has_no_choice:
        print()
        choice = int(input("Please enter the number of your choice: "))

        if choice in [1, 2, 3, 4, 5]:
            user_has_no_choice = False
        else:
            print("Invalid choice. Please try again.")

    return choice

def response_to_choice(choice):
    if choice == 1:
        print("[Placeholder response for choice 1]")
    elif choice == 2:
        print("[Placeholder response for choice 2]")
    elif choice == 3:
        print("[Placeholder response for choice 3]")
    elif choice == 4:
        print("[Placeholder response for choice 4]")
    elif choice == 5:
        print("Thank you for using the chatbot. Goodbye!")
