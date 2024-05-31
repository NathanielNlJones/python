#-------------------------------------------------------------------------------
# HA1
# Student Name: Nathaniel Jones
# Submission Date: 02/16/2024
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
# violates the ethical guidelines as set forth by the
# instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Notes to grader: 
#-------------------------------------------------------------------------------
#main menu stored in strings
mainMenu = '1. Order Salad\n2. Checkout\n3. Quit\n Select your option (1-3): '
orderSalad = '1. Vegetarian - $10.99\n2. Seafood - $14.99\n3. Chicken - $12.99\n Enter your salad selection (1-3): '
#initialize the menu items
veggie = 10.99
seafood = 14.99
chicken = 12.99
#initialize shopping cart at 0
runningTotal = 0

while True:
    #main loop
    menu = input(mainMenu)
    if menu == '1':
        saladMenu = input(orderSalad)
        #salad menu options
        if saladMenu == '1':
           print (' One veggie salad added to your cart. ')
           runningTotal += veggie
        elif saladMenu == '2':
            print ('One seafood salad added to your cart ')
            runningTotal += seafood
        elif saladMenu == '3':
            print ('One chicken salad added to your cart')
            runningTotal += chicken
        else: #default
            print ('invalid option. Returning to main menu.')
            continue #re-enter main loop       
    elif menu == '2':
        print ('Checking out...')
        print ('Your total before tax: ', runningTotal)
        totalTax = runningTotal *.1 #creates a new variable and stores the calculated tax
        print ('Total tax (10%):', totalTax)
        runningTotal += totalTax #adds calcualted tax to running balance
        print ('Your Total after tax:', runningTotal)
        print ('**** Thanks for using Salad Bar ***********')
        runningTotal = 0 #set shopping cart balance back to zero 
    elif menu =='3': #exit the program
        print ('Exiting the program.')
        break
    else: #default
        print ('invalid option, Returning to main menu.')