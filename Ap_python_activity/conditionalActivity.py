# 1. What is the difference between 
# a parameter and an argument in a python function

# A parameter is a placeholder in function program
# and a Argument is the actual code in the function when it is call


# 2. In your own words, describe what 
# a conditional statement (if/else) is 

# A conditional statement is a programmer's control system for the outcome/ execution


# 3. write a simple conditional state using a comparision operator(greater than, less than, etc. )

hearts = 4
clubs = 10
if clubs > hearts:
    print('B is greater than A')
else:
    print('B is not greater than A')

# 3. Write a conditional statement for food in the refridgerator.
# your conditional statement should be wrapped in a function that takes one (1)
# parameter. The data type for this parameter should be true or false. 
# your function should have a line of code that asks the user if there is food in the refridgerator.
# If there is food in the refridgerator, print time to cook. If there is 
# NOT food in the fridge, print time to shop. 
# When you call your function there should be an argument that accepts 
# a boolean. 

def foodInFridge(food):

    if food == True:
        print('Time to cook')
    else:
        print('Time to shop')

foodInFridge(True)
# 4. Create a function that checks the inventory of cereal for a store. 
# your function should parameter should accept an integer. In your function
# use a conditional statement to determine if you need to order more cereal.
# If there is more than 10 boxes, print "inventory full", else if there are less than 
# 10 boxes print "we need to order more cereal".

def check_cereal_inventory(quantity):
    if quantity > 10:
        print('inventory is full')
    else:
        print('order more cereal')

print('________________')
check_cereal_inventory(8)