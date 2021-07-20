# CS 499 Milestone Three
# Added firebase connection
# updated functions for firebase
#
# Roger Johnson
# Date created: June 6, 2021
# Last Date Modified: June 26, 2021

import getpass # Used to hide console input
import json # Needed to load json as object
import pyrebase # Module for Firebase integration https://github.com/thisbejim/Pyrebase

# Gets input from user used for signing in
# @return tuple containing password and name
def ReadUserInfo():
    name = input("Enter name:") # User name
    password = getpass.getpass("Enter password:") # password hidden while typing in console
    return password, name

# Prints lists to console 
# @param database firebase address
def DisplayStudentInformation(database):
    STUDENTS = database.child("STUDENTS").get() # list of students
    for student in STUDENTS.each(): # loop through all students
        print(student.key() + ": " + str(database.child("STUDENTS").child(student.key()).child("grade").get().val())) # name and grade of student

# Checks if both user name and password are correct
# @param database is the firebase database address
# @return bool 
def SignInFeature(database):
    (password, name) = ReadUserInfo() # user entered data
    if database.child("USER").child(str(name)).child("password").get().val() == password: # name must exist in database and password must match child password
        signin = True
    else:
        signin = False
    return signin

# Checks if user inputed values match what was asked for
# @param output contains string to print
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

# Auths and connects to firebase services
# @return firebase connection
def FirebaseSetup():
    with open('cred.json') as f: # cred.json has sensitive data
        config = json.load(f)
    return pyrebase.initialize_app(config)

# Gets student name for user to change grade
# @param database is the firebase database address
def ChangeStudentGrades(database):
    print("Enter new grade for students one at a time")
    STUDENTS = database.child("STUDENTS").get() # list of students
    for student in STUDENTS.each(): # loop through all students
        database.child("STUDENTS").child(student.key()).update({"grade": # name for student outputs and user inputs new grade
            HandleInput(student.key() + ":", ['a','A','b','B','c','C','d','D','f','F']).upper()})

# Main code for program
#
#
firebase = FirebaseSetup() # Initialize firebase
db = firebase.database() # Set to database

while SignInFeature(db) != True: # Loop until login is succesful
    print("Incorrect credentials. Try again")

print("Welcome professor. Below are all student grades")
DisplayStudentInformation(db)

choice = HandleInput("Adjust grades for students? Y/N:", ['Y','y','N','n']) # Asks to continue with Y or N
if choice == 'Y' or choice == 'y': # else not needed since program will end
    ChangeStudentGrades(db)
    print("You have successfully updated class grades. The grades are now as follows:")
    DisplayStudentInformation(db)

print("Goodbye")
#
#
# Main code for program
