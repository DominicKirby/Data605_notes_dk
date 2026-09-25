rotation = input()

start = 50

num = start

if rotation[0] == "R":
    num = num + int(rotation[1:2])
if rotation[0] == "L":
    num = num - int(rotation[1:2])
num = num % 99

print(num)