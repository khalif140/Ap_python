# 1. In your own words, describe what a for loop is?

#For loops runs up to the number of items on a list

# 2. What is the difference between a FOR loop and a WHILE loop?
# Provide two (2) examples of each. 

#while loop you can execute a set of statements as long as a condition is true.
i=0
while i<10:
    print(i)
    i+=1


#for loop you can execute a set of statements, once for each item in a list and repeat.
food = ['chicken', 'ox tail']
for x in food:
    print(x)
    
# 3. Create a FOR loop that will go through a list of names 
# and print all the names that start with the letter "R".

names=['Michael','Rebecca','William','Kareem','Robert','Rose','Jason']
for letter in names:
    if letter[0] =='R':
        print(letter)
