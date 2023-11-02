# Your program must be a function

# Your program must take in two datatypes, it can be whatever data types you like.

# Your program must perform some type of action on the data (can loop, check a condition, etc.)

# Your program must output a result.

# Once finished, write a brief read.me document, describing you program and exaplaining to another user what your program does and how to install it. Next, commit and push your work to your repository.

# Finally, find a classmate that has also completed these steps. You will now need to visit that students repository, find their program and clone the program onto your repository. follow their steps and test and check if they're program works.

def comments():
    limits = str(20)
    Start = str(print(input("Comment Here: ")))

    if Start > limits:
        print(" Please write shorter ")    
    else:
        print(" comment has been sent! ")

comments()