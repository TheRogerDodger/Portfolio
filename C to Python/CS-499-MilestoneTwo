# CS 499 Milestone Two
# Translatted from C to Python
#
# Roger Johnson
# Date created: June 6, 2021
# Last Date Modified: June 17, 2021

#Lists for tracking students and grades
STUDENTS = ["Jim", "Tom", "Ben", "Alice", "Ruby"]
GRADES =  ['A','C','C','D','F','\0']

# Gets input from user
# @return variable containing password
def ReadUserInfo():
    name = input("Enter name:") # name isnt used anywhere
    password = input("Enter password:") # password
    return password

# Checks user entered password for access
# @param password variable entered from ReadUserInfo()
# @return bool 
def CheckUserPermissionAccess(password):
    if int(password) == 123: # password needs to match
        check = True
    else:
        check = False
    return check

# Prints lists to console 
def DisplayStudentInformation():
    for index, name in enumerate(STUDENTS):
        print(name + ": " + GRADES[index])

# Main code for program
password = ReadUserInfo()
if CheckUserPermissionAccess(password) == True:
    print("Welcome professor. Below are all student grades")
    DisplayStudentInformation()
    if input("Adjust grades for students? Y/N:") == "Y": # Asks to continue with Y
        print("Enter the GPA for students one at a time")
        for index, name in enumerate(STUDENTS): # loops through list STUDENT
            GRADES[index] = input(name + ":") # Outputs student name and input new grade
        print("You have successfully updated class grades. The grades are now as follows:")
        DisplayStudentInformation()
