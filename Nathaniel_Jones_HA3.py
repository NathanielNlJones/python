#-------------------------------------------------------------------------------
# HA3.py
# Student Name: Jones, Nathaniel
# Version: Python 3.10.0
#-------------------------------------------------------------------------------
# Honor Code Statement: I received no assistance on this assignment that
#                       violates the ethical guidelines as set forth by the
#                       instructor and the class syllabus.
#-------------------------------------------------------------------------------
# References: dictionary videos
#-------------------------------------------------------------------------------
# Any notes to grader: 
#-------------------------------------------------------------------------------
# Code starts below this line
#----------------------------------------------------------------------------


def build_dict_by_no(items):
    dict_no= {}
    #iterate over items
    for item in items:
        #split information according to spec
        item_no, category, description, price, avg_rating = item.split(',')
        #create the dictionary and return
        dict_no[item_no] = [category, description, price, avg_rating]
    return dict_no
    #key = item_no, values = list of information [category, name, price, ratings]

def build_dict_by_category(items):
    dict_category = {} #initialized empty dictionary
    #iterate over items
    for item in items:
        #split category and other information
        item_no, category, description, price, avg_rating = item.split(',')
        #if category already exists, append
        if category in dict_category:
            dict_category[category].append(item_no)
        #otherwise create a new category with item_no
        else:
            dict_category[category] = [item_no]
    #key = category, values = list of item_nos in category
    return dict_category

def checkout(cart,dict_no):
    total = 0
    #calculate the total price in the cart
    for item_no in cart:
        price = float(dict_no[item_no][2])
        total += price
    return total
    #print(cart)
    #your code here

def build_list_by_ratings(dict_category, dict_no, user_category, min_rating):
    '''
    Populate and return a list from dict_category 
    where items will have minimum of min_rating
    '''
    ratings_list = [] #initialize empty dictionary
    #iterate over list
    for item_no in dict_category[user_category]:
        rating = float(dict_no[item_no][3])
        #check for min_rating
        if rating >= min_rating:
            #append item_no to ratings list
            ratings_list.append(item_no) 
        #get item rating
    return ratings_list


def main():
    items = ['B001,books,Patriot Games, 15.95, 3.75', 'B002,books,Origin, 19.95, 2.5', 'C001,clothing,Armani Suit, 800.00, 3.5',
          'B003,books,Animal Farm, 9.97, 4', 'B004,books,Grant, 22.50, 4.2', 'F001,food,Moose Drool Ale 6-pack, 9.95, 4.6',
          'C002,clothing,Pants, 39.95, 2.7', 'B005,books,Prairie Fires, 18.95, 1.2','C003,clothing,Vasque Hiking Boots, 109.00, 2.3',
          'C004,clothing,Wool Hat, 14.00, 4.5', 'F002,food,Jumbo shrimp, 12.50, 4','C005,clothing,Wrangler Jeans, 24.50, 4.1',
          'B007,books,Ragtime, 17.25,3','F003,food,Fusili - 16 oz., 2.95, 4', 'C006,clothing,Nike T-shirt, 19.00, 5',
          'C007,clothing,Gore-Tex Gloves, 39.00, 0.1','C008,clothing,North Face Fleece Jacket, 89.99, 4.3',
          'C009,clothing,Nationals Logo Sweatshirt, 49.00, 2.9','F004,food,Lamb Chops, 21.95, 4.95',
          'C010,clothing,New Balance Trail Runners,69.95, 3.6','B006,books,Future Shock, 8.95, 2.5']


    dict_no = build_dict_by_no(items)
    dict_category = build_dict_by_category(items)
    cart = []
    print("Welcome to shopping at River!\nWe sell items in the following categories: ['books','clothing','food']")
    while True:
        #ask for user input
        user_category = input("Please input a category name or input 'done' to quit: ").lower()
        #if input = 'done' end program
        if user_category == 'done':
            break
        #if user category is valid ask to filter by rating
        elif user_category in dict_category:
            user_input = input("Would you like to see items in this category filtered by minimum customer rating? (Y/N): ").upper()
            min_rating = 0.0 #default minimum rating
            if user_input == 'Y':
                #if yes get user minimum rating
                min_rating = float(input("Please enter the minimum rating (0-5): "))
            #pass minimum rating to 'list_by _ratings'function and return built dictionary
            matching_items = build_list_by_ratings(dict_category, dict_no, user_category, min_rating)
            #iterate over dictionary and return items value greater than or equal to minimum rating
            for item_no in matching_items:
                item_details = dict_no[item_no]
                print("{}:{}".format(item_no, item_details))
            #ask user to select an item to add to cart
            item_to_add = input("Please input item # or type any key to return: ").upper()
            #if input matches item, add it to the cart then print confirmation for user
            if item_to_add in dict_no:
                cart.append(item_to_add)
                print("{} added to cart".format(item_to_add))
                #allow user a chance to select more items by reentering loop
                print("Welcome to shopping at River!\nWe sell items in the following categories: ['books','clothing','food']")
                #continue
            else: #if item is not found print error for user and reenter loop
                print("item not found....\nto add another item to the cart, please select from ['books','clothing','food']")
                #continue
        else:
            print("Invalid category selected, please select from ['books','clothing','food']")
            #continue

    print("Thanks for shopping at River.\nYou purchased the following item(s)")
    #iterate over cart, print out each item and its corresponding info 
    for item_no in cart:
        item_details = dict_no[item_no]
        print("{}: {}".format(item_no, item_details))
    #call checkout function to return total
    total = checkout(cart,dict_no)
    print('The amount is: $', total)    
main()
