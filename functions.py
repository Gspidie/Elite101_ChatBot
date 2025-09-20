
import random


# A brief introduiction to the fictional ecommerce site, Round2Clothes, and the automated customer ChatBot.
def chatbot_introduction():
    print("Welcome to Round2Clothes, your place for all second hand garments.")
    print("To better assist you, please follow our ChatBot's prompts to narrow down your questions.")

# A function to get and return the user's name.
def get_user_name():
    print("\nCustomer please enter your...\n")
    first_name = input("First Name: ")
    last_name = input("Last Name: ")

    return f"{first_name} {last_name}"

# A function to get, test, and return a valid user age.
# Try and Except syntax referenced from W3Schools: https://www.w3schools.com/python/python_try_except.asp
def get_age_from(name):
    user_has_no_age = True
    age = 0

    print(f"\nHello {name}.\n")

    while user_has_no_age:
        try: 
            age = int(input(f"Please enter your age: "))
            user_has_no_age = False
        except ValueError:
            print(f"Oops. {name} please enter a valid age.\n")

    return age

# A function using collections of phrases with other text to from unique random sentences based on user age.
def greet_users_for(age):
    younger_phrases = ["but don't worry we have clothes that fit everyone no matter how small!",
                       "did you know we occasionally stock up on toys too!",
                       "have you seen our back to school backpacks? They are top tier!"]
    
    adult_phrases = ["you should consider visiting one of our in person sites!", 
                     "did you know first time customers get $10 off their purchase!",
                     "have you applied for our rewards program? Earn 100pts and redeem a $5 discount code!"]
    
    older_phrases = ["we're ready to walk you through step by step.",
                    "you may be eligible for a promotion!",
                    "if you get confused at any time let me know right away!"]

    if age < 15:
        phrase = random.choice(younger_phrases)
        print()
        print(f"Wow your young, {phrase}")
    elif 15 <= age < 65:
        phrase = random.choice(adult_phrases)
        print()
        print(f"To be {age}, {phrase}")
    else: 
        phrase = random.choice(older_phrases)
        print()
        print(f"Hi again, {phrase}")

# A function to display a simple menu of options.
def present_menu():
    print("Okay, with that out of the way, what do you need help with today?\n")
    print("1. Call customer support")
    print("2. Track my package")
    print("3. See locations and times")
    print("4. Feedback")
    print("5. Exit")

# A function to get, test, and return the user's number choice.
# Try and Except syntax referenced from W3Schools: https://www.w3schools.com/python/python_try_except.asp
def collect_menu_choice():
    choice = 0
    user_has_no_choice = True

    while user_has_no_choice:
        try:
            choice = int(input("\nPlease enter the number of your choice: "))

            if choice in [1, 2, 3, 4, 5]:
                user_has_no_choice = False
            else:
                print("Please enter a number from 1-5.")
        except ValueError: 
            print(f"Oops. Please enter a valid number.")

    return choice

# A function with placeholders to expand on.
def response_to_choice(choice):
    if choice == 1:
        print("[Placeholder response for choice 1]")
    elif choice == 2:
        print("[Placeholder response for choice 2]")
    elif choice == 3:
        print("[Placeholder response for choice 3]")
    elif choice == 4:
        print("[Placeholder response for choice 4]")
    else:
        print("Thank you for working with us. Goodbye!")
