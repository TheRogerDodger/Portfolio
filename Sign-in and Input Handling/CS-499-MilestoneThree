# CS 499 Milestone Three
# Added sign in feature and input handling
#
# Roger Johnson
# Date created: June 6, 2021
# Last Date Modified: June 24, 2021

import getpass # Library used to hide console input

#Lists for tracking students and grades
STUDENTS = ["Jim", "Tom", "Ben", "Alice", "Ruby"]
GRADES =  ['A','C','C','D','F','\0']
# Lists for teachers and their login passwords
TEACHERS = ['Admin','Johnson']
PASSWORDS = ['password', 'Roger']

# Gets input from user used for signing in
# @return tuple containing password and name
def ReadUserInfo():
    name = input("Enter name:") # User name
    password = getpass.getpass("Enter password:") # password hidden while typeing in console
    return password, name

# Checks user entered password for access
# @param index of TEACHERS[] to match PASSWORDS
# @param password variable entered from ReadUserInfo()
# @return bool 
def CheckUserPermissionAccess(index, password):
    if password == PASSWORDS[index]: # password needs to match
        check = True
    else:
        check = False
    return check

# Prints lists to console 
def DisplayStudentInformation():
    for index, student in enumerate(STUDENTS):
        print(student + ": " + GRADES[index])

# Checks if both user name and password are correct
# @return bool 
def SignInFeature():
    (password, name) = ReadUserInfo() 
    for index, teacher in enumerate(TEACHERS): # Loops through TEACHERS list and tracks index
        if name == teacher and CheckUserPermissionAccess(index, password) == True: # name and password must match
            signin = True
            break # When match is found break out of for loop
        else:
            signin = False
    return signin

# Checks if user inputed values match what was asked for
# @param output containing string to print
# @param restriction contains accepted input values
# @return value of accepted user input
def HandleInput(output, restriction):
    while True: # loop until return
        value = input(output)
        try: # Used for when the inputed value type doesnt match the restriction type
            if type(restriction[0])(value) in restriction:
                return value
            else:
                print("INVALID INPUT. TRY AGAIN")
        except:
            print("INVALID INPUT. TRY AGAIN")

# Main code for program
#
#
while SignInFeature() != True: # Loop until login is succesful
    print("Incorrect credentials. Try again")

print("Welcome professor. Below are all student grades")
DisplayStudentInformation()
choice = HandleInput("Adjust grades for students? Y/N:", ['Y','y','N','n']) # Asks to continue with Y or N
if choice == 'Y' or choice == 'y': # else not needed since program will end
    print("Enter new grade for students one at a time")
    for index, student in enumerate(STUDENTS): # loops through list STUDENTS
        GRADES[index] = HandleInput(student + ":", ['a','A','b','B','c','C','d','D','f','F']).upper() # Outputs student name and input new grade
    print("You have successfully updated class grades. The grades are now as follows:")
    DisplayStudentInformation()

print("Goodbye")
#
#
#
