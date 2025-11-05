import view_all
from closemenu import exit_request
import pandas as pd
import numpy as np

def edit_profile():
    try:
        reg_no = int(input("Enter Registration number of profile to edit: "))
        profile_found = False
        for profile in view_all.data:
            if profile[0] == reg_no:
                profile_found = True
                headers = ["Registration Number", "Name", "Year", "Section", "Phone Number", "Email Address", "Test Scores", "Previous CGPA", "CGPA", "Attendance"]
                df = pd.DataFrame(np.array([profile]), columns=headers)
                print("Current profile details:")
                print(df.to_string())

                while True:
                    print("\nWhich field do you want to edit?")
                    for i, col in enumerate(headers[1:], 1):
                        print(f"[{i}] {col}")
                    
                    edit_field = int(input("Enter the number of the field to edit: "))
                    if 1 <= edit_field <= len(headers) - 1:
                        if headers[edit_field] == "Year":
                            while True:
                                new_value = int(input(f"Enter new {headers[edit_field]} (1-4): "))
                                if 1 <= new_value <= 4:
                                    profile[edit_field] = new_value
                                    break
                                else:
                                    print("Invalid year. Please enter a value between 1 and 4.")
                        else:
                            new_value = input(f"Enter new {headers[edit_field]}: ")
                            # Get the correct data type from the existing data
                            current_value = profile[edit_field]
                            if isinstance(current_value, int):
                                profile[edit_field] = int(new_value)
                            elif isinstance(current_value, float):
                                profile[edit_field] = float(new_value)
                            else:
                                profile[edit_field] = new_value
                        print(f"{headers[edit_field]} updated successfully!")
                        break
                    else:
                        print("Invalid input. Please enter a valid field number.")

        if not profile_found:
            print("Profile not found")
    except ValueError:
        print("Invalid input. Please enter a number for the registration number.")
    exit_request()
