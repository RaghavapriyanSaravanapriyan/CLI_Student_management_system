# main.py
from banner import banner_print
import pandas as pd
import numpy as np
from closemenu import exit_request

# banner
banner_print()

# main menu
def main_menu():
    while True:
        print("Welcome to CLI Student management system!\n")
        print("Choose one of the following options:\n")
        print("[1] View list of all existing student profiles")
        print("[2] Create new student profile")
        print("[3] Browse particular profile")
        print("[4] Edit existing profile")
        print("[5] Delete existing profile")
        print("[6] Visualize student data\n")
        try:
            choice = int(input("Your option - "))

            if choice == 1: #view full list
                import view_all
                headers = ["Registration Number", "Name", "Year", "Section", "Phone Number", "Email Address", "Test Scores", "Previous CGPA", "CGPA", "Attendance"]
                pd.set_option('display.max_columns', None)
                pd.set_option('display.width', 1000)
                df = pd.DataFrame(np.array(view_all.data), columns=headers)
                print(df)
                exit_request()
            elif choice == 2: #create new profile
                import createprofile
                createprofile.create_profile()
            elif choice == 3:
                import browse_particular_profile
                browse_particular_profile.browse()
            elif choice == 4:
                import editprofile
                editprofile.edit_profile()
            elif choice == 5:
                import deleteprofile
                deleteprofile.delete_profile()
            elif choice == 6:
                import visualize
                visualize.visualize_data()
            else:
                print("Invalid option selected. Please try again.\n")
        except ValueError:
            print("Invalid input. Please enter a number.\n")

main_menu()
