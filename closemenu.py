def exit_request():
    exit_choice = input("Do you want to exit the program? (y/n): ").lower()
    if exit_choice == 'y':
        print("Exiting the program. Goodbye!")
        exit()
    elif exit_choice == 'n':
        print("Returning to the main menu.\n")
        print("-----------------------------------------------------------------------------------------------------------------------\n")
        import main
        main.main_menu()
    else:
        print("Invalid input. Please enter 'y' or 'n'.\n")
        exit_request()