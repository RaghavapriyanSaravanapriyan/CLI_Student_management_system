import pandas as pd
import numpy as np
import view_all
from closemenu import exit_request

def calculate_and_display_whole_stats():
    """Calculates and displays the average for several key metrics across all students."""
    print("\nCalculating Whole Student Body Statistics...\n")
    headers = ["Registration Number", "Name", "Year", "Section", "Phone Number", "Email Address", "Test Scores", "Previous CGPA", "CGPA", "Attendance"]
    df = pd.DataFrame(np.array(view_all.data), columns=headers)

    numeric_cols = ["Test Scores", "Previous CGPA", "CGPA", "Attendance"]
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    whole_averages = df[numeric_cols].mean()

    print("--- Whole Student Body Average Statistics ---")
    print(f"Average Test Score: {whole_averages['Test Scores']:.2f}")
    print(f"Average Previous CGPA: {whole_averages['Previous CGPA']:.2f}")
    print(f"Average Current CGPA: {whole_averages['CGPA']:.2f}")
    print(f"Average Attendance: {whole_averages['Attendance']:.2f}%")
    print("-------------------------------------------\n")

    exit_request()

def cgpa_calculator():
    """A tool to calculate the new cumulative CGPA based on previous and current semester performance."""
    print("\n--- CGPA Calculator ---")
    try:
        prev_cgpa = float(input("Enter your previous cumulative CGPA: "))
        prev_credits = int(input("Enter your total credits earned so far: "))
        current_gpa = float(input("Enter your GPA for the current semester: "))
        current_credits = int(input("Enter the total credits for the current semester: "))

        if prev_credits < 0 or current_credits <= 0:
            print("\nError: Credit values must be positive numbers.")
        else:
            total_quality_points = (prev_cgpa * prev_credits) + (current_gpa * current_credits)
            total_credits = prev_credits + current_credits
            new_cgpa = total_quality_points / total_credits
            print(f"\nYour new cumulative CGPA is: {new_cgpa:.2f}")

    except ValueError:
        print("\nInvalid input. Please enter valid numbers for CGPA and credits.")
    
    print("-----------------------\n")
    exit_request()
