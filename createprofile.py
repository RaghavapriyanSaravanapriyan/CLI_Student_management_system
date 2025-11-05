from view_all import data
from closemenu import exit_request

def create_profile():
    print("Creating a new student profile...\n")
    while True:
        try:
            reg_no = int(input("Enter Registration Number [integer only]: "))
            regnos = [i[0] for i in data]
            if reg_no in regnos:
                print("Registration Number already exists! Please use a different one.")
                continue

            name = input("Enter Name: ")
            while True:
                year = int(input("Enter Year (1-4): "))
                if 1 <= year <= 4:
                    break
                else:
                    print("Invalid year. Please enter a value between 1 and 4.")
            section = input("Enter Section: ")
            phone = input("Enter Phone Number: ")
            email = input("Enter Email Address: ")
            test_scores = int(input("Enter Test Scores: "))
            prev_cgpa = float(input("Enter Previous CGPA: "))
            cgpa = float(input("Enter CGPA: "))
            attendance = int(input("Enter Attendance Percentage: "))
            
            new_profile = [reg_no, name, year, section, phone, email, test_scores, prev_cgpa, cgpa, attendance]
            data.append(new_profile)
            print("\nProfile created successfully!")
            break  # Exit the loop on success

        except ValueError:
            print("\nInvalid Input. Please ensure you enter the correct data type for each field. Let's try again.\n")
    
    exit_request()
