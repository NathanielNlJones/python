#-------------------------------------------------------------------------------
# LA1.py
# Name: first_name last_name
# Python Version: 3.X
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Comments to grader: I know it wasn't required but it bothered me that the program just ended so I added a simple while loop
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------
while True:
    temp = input('Please enter your temperature in Fahrenheit: ')
    temp = float(temp)
    celsius = 5/9*(temp-32)
    print('the temperature in Celsius is: ', celsius)
    if input('Would you like to enter another temperature? (y/n) ') == 'n' :
        break
# break is a keyword in python which allows you to exit a loop when a certain condition is met
# by storing this program in a while loop, it will loop the code so long as the second input from the user is not the string 'n' 
# since I have not added any data validation, any response other than 'n' including 'y' will simply continue the while loop
# however if the user inputs 'n', it will meet the conditions of the if statement and proceed to the 'break' keyword closing the loop

