import pandas as pd
import numpy as np
import view_all
from closemenu import exit_request

def calculate_and_display_stats():
    """Calculates and displays the class average for several key metrics."""
    print("\nCalculating Class Statistics...\n")
    headers = ["Registration Number", "Name", "Year", "Section", "Phone Number", "Email Address", "Test Scores", "Previous CGPA", "CGPA", "Attendance"]
    df = pd.DataFrame(np.array(view_all.data), columns=headers)

    # Columns to calculate averages for
    numeric_cols = ["Test Scores", "Previous CGPA", "CGPA", "Attendance"]

    # Convert columns to numeric, coercing errors
    for col in numeric_cols:
        df[col] = pd.to_numeric(df[col], errors='coerce')

    # Calculate the mean, ignoring any NaN values that resulted from coercion
    class_averages = df[numeric_cols].mean()

    print("--- Class Average Statistics ---")
    print(f"Average Test Score: {class_averages['Test Scores']:.2f}")
    print(f"Average Previous CGPA: {class_averages['Previous CGPA']:.2f}")
    print(f"Average Current CGPA: {class_averages['CGPA']:.2f}")
    print(f"Average Attendance: {class_averages['Attendance']:.2f}%")
    print("--------------------------------\n")

    exit_request()
