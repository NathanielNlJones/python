#-------------------------------------------------------------------------------
# HA2
# Student Name: Nathaniel Jones
# Submission Date: 03/15/2024
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# Pseudocode: Write your pseudocode below following a # sign
# Step 1: 
'''
print list of options for user

1. get username from user
    verify that username is not in database
get password from user
    verify password meets requirements
        if password meets reqs 
            join password username together with '-'
            append string to database
        if not
            print error message
            provide reason and number of upper, lower and digits

2. display user names and passwords
    split username-password
    print all usernames and passwords present in database
3. update password of existing user
    request username from user
    allow user to input new password and update 'list' 
4. end program

'''
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: code originally looped to allow user to input a password until succesful
# this is why the nested passWordRejected function was created, but based on sample output code was revised
# 
#-------------------------------------------------------------------------------

upper_case_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
lower_case_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
database = ["Jake-ABab12","Mary-B0zrR2","Bob-Xy1Zi4","Janet-34NmhH","Henry-7iKoO5"]



#function to get password from user and check if password is valid, 
#receives parameter for user input and boolean based on which option this function was called from
def checkPassword(add):
    while True:
            #initialize variables to store password requirements
            upperCount = 0
            lowerCount = 0
            digitCount = 0
            totalCount = 0
            #function prints missing password requirements for user
            def passWordRejected():
                print("Password Rejected")
                print("Number of uppercase letters {}, lowercase letters {}, digits {}\n\n".format(upperCount, lowerCount, digitCount))
            #simple fork to change the output based on which function this is called by
            if add == True:
                newPassword = input("Enter your password (Example: ABcd56) : ")
            else:
                newPassword = input("Enter the new password: ")
            #counts password requirements
            for character in newPassword:
                totalCount += 1
                if character in upper_case_letters:
                    upperCount += 1
                elif character in lower_case_letters:
                    lowerCount += 1
                elif character in digits:
                    digitCount += 1
            #checks that input meets requirements, if so append to list
            if upperCount == 2 and lowerCount == 2 and digitCount == 2 and totalCount == 6:
                return newPassword
            else: 
                passWordRejected()
                return None
#option 1
def addCreds():
    while True:
        print("*** Add username and password to the database ***")
        userCreds = input("Enter your username: ")
        #iterates over database list and splits by username and password
        for keypair in database:
            username, password = keypair.split("-")
            #checks if username is already in database
            if userCreds == username:
                print("Username {} is already in the database! Choose 3 to update.\n".format(username))
                return
        #if username is valid, call funcion to input and check password
        newPassword = checkPassword(True)
        if newPassword == None:
            return
        database.append(userCreds + "-" + newPassword)
        newCreds = (userCreds + "-" + newPassword)
        print("Adding username and password {} to the database\n".format(newCreds))
        return 
#option 2
def displayCreds():
    for keypair in database:
        username, password =keypair.split("-")
        print("Username {}: Password {}\n".format(username, password))
#option 3
def updatePassword():
    print ("*** Update password of an existing user ***")
    userCreds = input("Enter the username you would like to update the password:")
    index = -1 #initialize counter to store current index in loop
    #iterates through database list
    for keypair in database:
        index += 1 #increments the index counter
        username, password = keypair.split("-")
        #checks database list for username
        if userCreds == username:
            newPassword = checkPassword(False) #calls checkpassword function to receive input and check password requirements, sets to false to select correct dialogue
            if newPassword == None:
                return
            database[index] = userCreds + "-" + newPassword
            print("Password updated for user:", username, "\n")
            return
        #if username not in list return error and re-enter main loop
    print("Username {} not found in database! Choose 1 to add new user\n".format(userCreds))
#main loop of program
while True:
    #print menu for user
    print("*** Welcome to Password Storage and Management system ***")
    selectOption = input("Available options:\n1: Add password\n2: Display usernames and passwords\n3: Update password by username\n4: Exit\n\nEnter option: ").strip().lower()
    #function calls based on menu options
    if selectOption == "1":
        addCreds()
        continue
    elif selectOption == "2":
        displayCreds()
        continue
    elif selectOption == "3":
        updatePassword()
        continue
    elif selectOption == "4":
        print(">>>")
        break
    else: 
        print("Not a valid slection. Please try again.\n")
        continue
