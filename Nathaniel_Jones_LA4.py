#-------------------------------------------------------------------------------
# source_file_name.py
# Student Name: 
# Assignment: LA4
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: (list of web sites, texts, and any other resources used)
#-------------------------------------------------------------------------------
# Note to grader: (a note to the grader as to any problems or uncompleted aspects of
# of the assignment)
#-------------------------------------------------------------------------------
# NOTE: width of source code should be < 80 characters to facilitate printing
#-------------------------------------------------------------------------------
# Source Code: Write your code below

#initialize list of five neighboring states
neighbors = ["Maryland/Annapolis", "North Carolina/Raleigh", \
             "Tennessee/Nashville", "Kentucky/Frankfort", \
             "West Virginia/Charleston"]
#initialize control variables 
in_list = False 
hint = False

while True:
    #prompt user to enter the state/capital or press enter for a hint.
    stateCapital = input("Enter the name of a state bordering Virginia or the capital of one of these state.\n\nIf you need a hint press Enter:")
    #check to see if a hint is requested
    if stateCapital == "":
            #if 'enter' is input display 5 states
            print("The five states bordering Virginia are")
            for item in neighbors: #iterates over list
                state, capital = item.split("/") #splits items in list
                print(state, end=", ") #for each item split print the state followed by a comma on the same line
            #prompt user to input a capital
            stateCapital = input("\nEnter the name of the capital city of one of these now:")
            #set hint to True
            hint = True  
    #start for loop to iterate over list of items.
    for stateOrCapital in neighbors:
        state, capital = stateOrCapital.split("/")
        #if no hint has been given check to see if input is either state or capital
        if hint == False and stateCapital.lower() == state.lower() or stateCapital.lower() == capital.lower():
         print("Correct!",capital, "is the capital of", state)
         in_list = True
         #if hint was given check to see if input was capital
        elif hint == True and stateCapital.lower() == capital.lower():
         #if input was a capital, print state and its capital
         print("Correct!",capital, "is the capital of", state)
         break
    # if inlist varaible is false print error message and end program
    if in_list == False:
        print ("Incorrect, the program ends here.")
    break  