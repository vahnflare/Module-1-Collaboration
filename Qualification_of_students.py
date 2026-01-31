# Name: Ivanloe L. Manuel
# File: Qualification_of_students.py
# Description: This program accepts student names and GPAs, then determines
#              whether each student qualifies for the Dean's List or Honor Roll.

last_name = input("Enter the student's last name (or 'ZZZ' to quit): ")

while last_name != "ZZZ":
    first_name = input("Enter the student's first name: ")
    
    # Get GPA as a float
    gpa = float(input("Enter the student's GPA: "))

    # Check qualifications
    if gpa >= 3.5:
        print(f"{first_name} {last_name} has made the Dean's List.")
    elif gpa >= 3.25:
        print(f"{first_name} {last_name} has made the Honor Roll.")
    else:
        print(f"{first_name} {last_name} does not qualify for either list.")

    print()  # blank line for readability

    # Ask for next student
    last_name = input("Enter the next student's last name (or 'ZZZ' to quit): ")

print("Program ended.")
