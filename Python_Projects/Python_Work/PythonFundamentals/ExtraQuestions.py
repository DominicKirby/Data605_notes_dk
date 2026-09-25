

def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False


def FizzBuzz(n):
    num_list = []
    for num in range(1,n+1):
        if num % 3 == 0 and num % 5 == 0:
            num_list.append("FizzBuzz")
        elif num % 3 == 0:
            num_list.append("Fizz")
        elif num % 5 == 0:
            num_list.append("Buzz")
        else:
            num_list.append(num)

    return print(num_list)

# FizzBuzz(50)

def max_of_three(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        return False
    if a >= b and a >= c:
        return print(a)
    elif b >= a and b >= c:
        return print(b)
    elif c >= a and c >= b:
        return print(c)


# max_of_three(3, 5, 5)


def number_of_vowels(word):
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    for letter in word:
        if letter in vowels:
            count += 1
    return print("There are", count, "vowels in", word)

# number_of_vowels(input("Enter a word: "))

def is_palindrome(word):
    reveresed_word = word[::-1]
    if word == reveresed_word:
        return True

# print(is_palindrome('aba'))


def calculate(a, b, operator):
    if operator == '+':
        return a + b
    elif operator == '-':
        return a - b
    elif operator == '*':
        return a * b
    elif operator == '/':
        return a / b
    else:
        return "input 2 integers and one of +,-,*,/"

# print(calculate(int(input("Number 1: ")), int(input("Number 2: ")), input("Operator: ")))


# -------------------------------------------------------------------------------------------

"""z
strDigit_List = []

for i in range(1, 999):
    for j in range(1, 999):
        num1 = 1000 - i
        num2 = 1000 - j

        strDigit = str(num1 * num2)
        if strDigit == strDigit[::-1]:
            strDigit_List.append(strDigit)

print(max(strDigit_List, key=int))

active = True
num = 2520

while active == True:
    divisible = True
    for i in range(1, 21):
        if num % i != 0:
            divisible = False
            break
    if divisible == False:
        num += 20
    if divisible == True:
        active = False
        print(num)


sum = 0
square_sum = 0


for i in range(1, 101):
    sum += i
    square_sum += i**2

print(sum**2 - square_sum)
"""



