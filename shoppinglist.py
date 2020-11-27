# Shopping list project
# You will be able to add items, remove items or show and clear whole shopping list
# You will be able to even type in price of the item, and afterwards the program will calculate full price of the shopping list

shopping_list = {}
end = True 

def add_item(item, price):
    global shopping_list
    shopping_list[item] = price
    print("")
    print(shopping_list)

def remove_item(item):
    global shopping_list
    shopping_list.pop(item)
    print("")
    print(shopping_list)

def show_list():
    global shopping_list
    print("")
    print(shopping_list)

def clear_list():
    global shopping_list
    shopping_list.clear()
    print("")
    print("The shopping list was cleared")
    
def total_price():
    values = shopping_list.values()
    total_price = round((sum(values)), 2)
    print("")
    print(f"The total price is {total_price}")



print("Hello and Welcome, this is automatic shopping list maker.")

while end:
    

    print("")
    print("")
    print("What would you like to do? \nPlease enter a number: \n1 Add an item \n2 Remove an item \n3 Clear whole item \n4 Calculate price of the list \n5 Show whole list \n6 End the app")
    number = input()
    
    if number == "1":
        item = input("Please enter what item you would like to enter: ")
        price = float(input("Please enter the price of the item: "))
        add_item(item, price)
        
    elif number == "2":
        item = input("Please enter what item you would like to remove: ")
        
        if item not in shopping_list:
            print("")
            print("The item is not in the shopping list")
        
        else:
            remove_item(item)

    elif number == "3":
        clear_list()

    elif number == "4":
        total_price()

    elif number == "5":
        show_list()
    
    elif number == "6":
        print("")
        print("Thank you for using our App, have a great rest of the day!")
        end = False



