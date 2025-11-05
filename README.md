# CLI Student Management System

A simple, command-line based student management system written in Python. This application allows users to perform basic CRUD (Create, Read, Update, Delete) operations on student profiles, as well as visualize student data.

## Features

*   **View All Students**: Display a list of all existing student profiles in a clean, tabular format using `pandas`.
*   **Create New Profile**: Add a new student to the system with input validation for the year.
*   **Browse Particular Profile**: Search for and display a specific student's profile using their registration number.
*   **Edit Existing Profile**: Modify the details of an existing student with input validation for the year.
*   **Delete Profile**: Remove a student's profile from the system.
*   **Visualize Student Data**: Generate and display histograms for CGPA, Previous CGPA, and Attendance using `pandas` and `matplotlib`.

## Prerequisites

*   Python 3.x

## Installation

1.  Clone the repository or download the source code.

2.  Install the required Python packages using pip:
    ```sh
    pip install pandas numpy matplotlib
    ```

## Usage

To start the application, run the `main.py` script from your terminal:

```sh
python main.py
```

You will be greeted with the main menu, where you can choose an option by entering the corresponding number.

```
Welcome to CLI Student management system!

Choose one of the following options:

[1] View list of all existing student profiles
[2] Create new student profile
[3] Browse particular profile
[4] Edit existing profile
[5] Delete existing profile
[6] Visualize student data

Your option -
```

## Project Structure

The project is organized into several modules, each with a specific responsibility:

*   `main.py`: The main entry point of the application. It displays the menu and handles user choices.
*   `banner.py`: Contains the function to print the ASCII art banner at startup.
*   `view_all.py`: Currently acts as a mock database, holding the student data in a Python list.
*   `browse_particular_profile.py`: Contains the logic to find and display a single student profile.
*   `createprofile.py`: Handles the logic for creating a new student profile.
*   `editprofile.py`: Manages the process of editing an existing profile's details.
*   `deleteprofile.py`: Contains the logic for deleting a student profile.
*   `visualize.py`: Contains the logic for visualizing student data.
*   `closemenu.py`: A utility module that prompts the user to either exit the application or return to the main menu after an operation.
