import functions as md


def main():
    md.chatbot_introduction()

    user_name = md.get_user_name()
    user_age = md.get_user_age()

    md.greet_user(user_name, user_age)

    md.present_menu()
    user_menu_choice = md.collect_menu_choice()

    md.response_to_choice(user_menu_choice)

if __name__ == "__main__":
    main()
