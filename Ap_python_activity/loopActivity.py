# 1. Provided below is some starter code. 
# Fix this code to create a loop that will iterate
# until it gets to the number 10.

# hint: remember there are 3 parts to a loop. 
i=0
while i <= 10:
    print(i)
    i += 1

# 2. Create a simple while loop that will iterate over a the following condition:
# The loop will ask the user to enter the secret number. The secret number is 3. 
# If the user enters the secret number correctly, the loop will stop and tell the user
# the can win a prize. 
# If the user puts in an incorrect secret number, the loop will ask them to enter the 
# correct secret number. 

def Secret():
    password = 3
    iterator = 1

    while iterator <= 3:
        userInput= input('please type in your Secrete number: ')
        if userInput !=password:
            print('Hello User you can win a prize.')
        else:
            print('Please enter the secret number.')
Secret()


# 3. describe the difference between a while loop and a conditional statement. 
# Try be as specific as you can

# the conditional statement uses If and Else for the outcome of their program to go either side of the program
#if the sun doesnt rise the else would say its still night 
# the while loop uses while for something else is happening the program in while is stil

# 4. Create a while loop that will iterate over the list of names 
# and print out only the following name: William

names= ['Avery','Paige','William','Ade','Jasmyn','Crystal']
print


# 5. Create a loop that will ask the user to add a new string value to the list of names above.
# hint you will need use append().

# BONUS QUESTION
# Describe the differences between a FOR loop and WHILE loop. 

# the while loop executes a set of statements as long as a condition is true