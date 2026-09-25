print("\nQ1a\n")
# Q1a: Write a function which takes in an integer as an argument and returns the divisors of that number as a list
# e.g. f(12) = [1, 2, 3, 4, 6, 12]
# hint: range(1, n) returns a collection of the numbers from 1 to n-1

# A1a:
def divisors(num):
    divisors = []
    for i in range(1, num - 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

print(divisors(20))


print("\nQ1b\n")
# Q1b: Write a function which takes in two integers as arguments and returns true if one of the numbers
# is a factor of the other, false otherwise
# (bonus points if you call your previous function within this function

# A1b:

def integer_comparison(num1, num2):
    if num1 % num2 == 0 or num2 % num1 == 0:
        return True
    else:
        return False

print(integer_comparison(20, 99))

# -------------------------------------------------------------------------------------- #

print("\nQ2a\n")
# Q2a: write a function which takes a letter (as a string) as an input and outputs it's position in the alphabet

# A2a:
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " "]

def alphabetic_position(letter):
    global alphabet

    count = 0

    for letters in alphabet:
        if letters != letter:
            count += 1
        elif letters == letter:
            return count

print(alphabetic_position("f"))


print("\nQ2b\n")
# Q2b: create a function which takes a persons name as an input string and returns an
# ID number consisting of the positions of each letter in the name
# e.g. f("bob") = "1141" as "b" is in position 1 and "o" is in position 14

# A2b:

def word_alphabetic_position(word):
    word_letter_position = ""

    for letters in word:
        word_letter_position += str(alphabetic_position(letters))

    return word_letter_position

print(word_alphabetic_position("bob"))

print("\nQ2c\n")
# Q2c: Create a function which turns this ID into a password. The function should subtract
# the sum of the numbers in the id that was generated from the whole number of the id.
# e.g. f("bob") -> 1134 (because bob's id was 1141 and 1+1+4+1 = 7 so 1141 - 7 = 1134)

# A2c:
def word_alphabetic_sum(word):
    word_letter_position = ""
    word_letter_sum = 0

    for letters in word:
        word_letter_position += str(alphabetic_position(letters))

    for i in range(len(word_letter_position)):
        word_letter_sum += int(word_letter_position[i])

    return int(word_letter_position) - word_letter_sum

print(word_alphabetic_sum("bob"))

# -------------------------------------------------------------------------------------- #

print("\nQ3a\n")
# Q3a: Write a function which takes an integer as an input, and returns true if the number is prime, false otherwise.

# A3a:

def prime_check(num):
    if num == 1:
        return False

    if num % 2 == 0:
        half = int(num / 2)
    else:
        half = int((num + 1)/ 2)

    for i in range(2, half):
        if num % i == 0:
            return False

    return True

print(prime_check(17))

print("\nQ3b\n")
# Q3b: Now add some functionality to the function which does not error if the user inputs something other than a digit

# A3b:

def prime_check_errors(num):
    if type(num) != int:
        return "Input integers only"

    if num == 1:
        return False

    if num % 2 == 0:
        half = int(num / 2)
    else:
        half = int((num + 1)/ 2)

    for i in range(2, half):
        if num % i == 0:
            return False

    return True

print(prime_check_errors(17))
# -------------------------------------------------------------------------------------- #



