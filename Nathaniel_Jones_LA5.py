#-------------------------------------------------------------------------------
# Nathaniel_Jones_LA5.py
# Name: Nathaniel Jones
# Python Version: 3.10.0
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: 
#-------------------------------------------------------------------------------
# Any notes to grader: 
#-------------------------------------------------------------------------------
#-------------------------------------------------------------------------------
# Code: Code starts here
#-------------------------------------------------------------------------------
#initialize global list
receipt = []

#main function
def main():
    while True: 
        #retreives values from input and appends them to receipt list
        itemPrice, itemName, category = getInput()
        receipt.append((itemPrice, itemName, category))
        #prompt user for another item, if none break loop
        anotherItem = input("Enter another item? (y/n): ").lower()
        if anotherItem.lower() != "y":
            break
#gets input from user, sorts by category, and returns the entries
def getInput():
    itemName = input("Enter item name: ").lower()
    itemCategory = input("Is this a food item?  (y/n): ").lower()
    if itemCategory.lower() == "y":
        category = "food"
    elif itemCategory.lower() == 'n':
        itemCategory = input("Is this a medicine item? (y/n):").lower()
        if itemCategory.lower() == 'y':
            category = "medicine"
        else:
            category = "general"
    else:
            category = "general"
    itemPrice = float(input("Enter price: $"))
    return itemPrice, itemName, category
#calculates tax based on category, accepts price and category as parameters
def tax(itemPrice, category):
    if category == "food":
        taxAmount = itemPrice * 0.025
    elif category == "medicine":
        taxAmount = 0.0
    else :
        taxAmount = itemPrice * .06
    extendedPrice = 0.0
    extendedPrice = taxAmount+itemPrice
    return extendedPrice
#formats and prints list for user   
def printReceipt():
    total = 0.0
    print("\n\nItem\t\tPrice\t\tExtended Price")
    for itemPrice, itemName, category in receipt:
        extendedPrice = tax(itemPrice, category)
        print("{}\t\t ${:.2f}\t\t ${:.2f}\t".format(itemName, itemPrice, extendedPrice))
        total += extendedPrice
        total = int(total * 100) / 100.0
    print("\nTotal\t", " \t\t\t $", total)

#main loop of program, calls main function, when loop ends call printreceipt function
while  True:
    print("*** Thank you for using self-checkout ***\n\n")
    main()
    break
printReceipt()
