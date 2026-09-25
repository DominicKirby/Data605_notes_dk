print("\nQ1a\n")
# Q1a: Print only the first 5 numbers in this list
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1a:
print(x[0:5])


print("\nQ1b\n")
# Q1b: Now print only the even numbers in this list (the elements that are themselves even)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1b:
for vals in x:
    if vals % 2 == 0:
        print(vals)


print("\nQ1c\n")
# Q1c: Now only print the even numbers up to the fifth element in the list (e.g. 2, 4, 34)
x = [2, 5, 4, 87, 34, 2, 1, 31, 103, 99]

# A1c:
for vals in x[0:5]:
    if vals % 2 == 0:
        print(vals)

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: from the list of names, create another list that consists of only the first letters of each first name
# e.g. ["Alan Turing", "Leonardo Fibonacci"] -> ["A", "L"]
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2a:
initials = []

for vals in names:
    initials.append(vals[0])

print(initials)

# -------------------------------------------------------------------------------------- #

print("\nQ2b\n")
# Q2b: from the list of names, create another list that consists of only the index of the space in the string
# HINT: use your_string.index("substring")
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2b:
space_index = []

for vals in names:
    space_index.append(vals.index(" "))

print(space_index)

# -------------------------------------------------------------------------------------- #

print("\nQ2c\n")
# Q2c: from the list of names, create another list that consists of the first and last initial of each individual
names = ["Alan Turing", "Leonardo Fibonacci", "Katherine Johnson", "Annie Easley", "Terence Tao"]

# A2c:

first_last_initials = []

for i in range(len(names)):
    first_last_initials.append(names[i][0] + names[i][space_index[i] + 1])

print(first_last_initials)
# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Here is a list of lists, print only the lists which have no duplicates
# Hint: This can be easily done by using sets as a set does not contain duplicates
list_of_lists = [[1,5,7,3,44,4,1],
                 ["A", "B", "C"],
                 ["Hi", "Hello", "Ciao", "By", "Goodbye", "Ciao"],
                 ["one", "Two", "Three", "Four"]]


# A3a:

for lists in list_of_lists:
    if len(lists) == len(set(lists)):
        print(lists)

# -------------------------------------------------------------------------------------- #

print("\nQ4a\n")
# Q4a: Using a while loop, ask the user to input a number greater than 100, if they enter anything else,
# get them to enter again (and repeat until the conditions are satisfied). Finally print the number that
# they entered

# A4a:
"""
from random import randint

random_number = randint(0, 100)
print("The game has started")
print("Guess the random number between 0 and 100")
Game_active = True


while Game_active:
    guess = int(input("Guess a number: "))
    if guess == random_number:
        print("Correct!")
        Game_active = False
    elif guess > random_number:
        print("Your guess is too high \n")
    elif guess < random_number:
        print("Your guess is too low \n")
"""
print("\nQ4b\n")
# Q4b: Continue this code and print "prime" if the number is a prime number and "not prime" otherwise

# A4b:

num = int(input("Guess a number: "))

if num % 2 == 0:
    half = int(num / 2)
if num % 2 == 1:
    half = int((num + 1) / 2)

count = 0

if num == 1:
    print("Not prime")
else:
    for i in range(2, int(half)):
        if num % i == 0:
            count = count + 1
            print(i)

    if count == 0:
        print("prime")
    else:
        print("not prime")