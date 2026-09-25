from math import radians

print("Hello World!")
# Comment
"""
Multi-line String
"""
"""
print(type(5))
print(type(5.5))

# Unicode
print("a")
print(u"\u0061")

# Concatenation
first_name = 'jane'
last_name = 'doe'
full_name = first_name + ' ' + last_name
print(full_name)

age = 25

print(full_name + ' ' + str(age))

print(full_name.replace('a', ' '))


customer_age = 0

if customer_age <= 12:
    print("U, PG, and 12 films are available")
elif customer_age <= 15:
    print("U, PG, and 15 films are available")
elif customer_age >  18:
    print("All films are available")


time_of_day = 6

if time_of_day > 5 and time_of_day < 12:
    print("Good Morning")
else:
    print("Good Afternoon")


shopping_list = ["apple", "banana", "cherry"]

shopping_list.append("orange")

print(shopping_list)

shopping_list.pop()

print(shopping_list)

shopping_list.pop(0)

print(shopping_list)


# Simple Dictionary
contact_list = {
    "Alice": "15",
    "Bob": "22",
    "Charlie": "23"
}

contact_list["David"] = "24"

print(contact_list)
print(contact_list.keys())
print(contact_list.values())
print(contact_list.pop("Alice"))


# Enclosed Dictionaries
new_contact_list = {
    "a" : {
        "Alice": "15",
    },
    "b" :{
        "Bob": "22",
        "Bert" : "23,"
    },
    "c" : {
        "Charlie": "23"
    }
}

print(new_contact_list["b"].keys())


# Guessing number game
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