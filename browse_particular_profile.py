import pandas as pd
import numpy as np
import view_all
from closemenu import exit_request

def browse():
    try:
        regno = int(input("Enter the registration number of the desired profile to be browsed - "))
        headers = ["Registration Number", "Name", "Year", "Section", "Phone Number", "Email Address", "Test Scores", "Previous CGPA", "CGPA", "Attendance"]
        df = pd.DataFrame(np.array(view_all.data), columns=headers)
        
        df['Registration Number'] = pd.to_numeric(df['Registration Number'])
        
        profile = df[df['Registration Number'] == regno]

        if not profile.empty:
            print(profile.to_string())
        else:
            print("Profile not found")
    except ValueError:
        print("Invalid input. Please enter a number for the registration number.")
        
    exit_request()
