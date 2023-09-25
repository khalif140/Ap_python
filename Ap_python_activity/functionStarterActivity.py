# 1. In your own words, describe what a function is
"A code of instructions"
# 2. What is are function parameters and arguments and describe
# the difference between the 2. 

#parameters are the placeholders for our data
#arguements are the values sent to a function

# 3. write a function that will print out a welcome message
# that includes a users name. You will need to use parameters and arguments
def welcomemsg(name):
    print("Welcome"+ name)

welcomemsg('leaf')
# 4. Write a function that will do a calculation that takes 3 parameters.
# Your function can do any of the arithmatic operators (add, subtract, multiply, divide)
def calculate(numberA,numberB):
   print(numberA + numberB)

calculate(15,0)

# 5. Write a function that will output a message to a user, telling them
# what class they have next after this one. this code should use a 
# variable to pass a value into the parameter of a function. The variable should
# be real, user data- not hard coded data.
def Nextclass(name, period):
    print("Hello"+ name +"! Your next class is"+ period +". Have a nice day!")

Nextclass('Khalif', 'Latin 3')