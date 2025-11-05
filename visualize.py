import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import view_all

def visualize_data():
    headers = ["Registration Number", "Name", "Year", "Section", "Phone Number", "Email Address", "Test Scores", "Previous CGPA", "CGPA", "Attendance"]
    df = pd.DataFrame(np.array(view_all.data), columns=headers)

    # Convert relevant columns to numeric
    for col in ["CGPA", "Attendance", "Previous CGPA"]:
        df[col] = pd.to_numeric(df[col])

    # Create a 2x2 grid of plots using pandas plotting
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle('Student Performance Analysis', fontsize=16)

    # CGPA Distribution
    df['CGPA'].hist(ax=axes[0, 0], bins=10, color='skyblue', edgecolor='black', grid=False)
    axes[0, 0].set_title('CGPA Distribution')
    axes[0, 0].set_xlabel('CGPA')
    axes[0, 0].set_ylabel('Number of Students')

    # Attendance Distribution
    df['Attendance'].hist(ax=axes[0, 1], bins=10, color='lightgreen', edgecolor='black', grid=False)
    axes[0, 1].set_title('Attendance Distribution')
    axes[0, 1].set_xlabel('Attendance (%)')
    axes[0, 1].set_ylabel('Number of Students')

    # Previous CGPA Distribution
    df['Previous CGPA'].hist(ax=axes[1, 0], bins=10, color='salmon', edgecolor='black', grid=False)
    axes[1, 0].set_title('Previous CGPA Distribution')
    axes[1, 0].set_xlabel('CGPA')
    axes[1, 0].set_ylabel('Number of Students')

    # Remove the empty subplot
    fig.delaxes(axes[1,1])

    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    plt.show()

    from closemenu import exit_request
    exit_request()
