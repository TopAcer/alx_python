import random

number = random.randint(-1000, 1000)
last_digit = abs(number) % 10

print("The string Last digit of")
print("the number", number)
print("is", last_digit, end=" ")

if last_digit > 5:
    print("and is greater than 5")
elif last_digit == 0:
    print("and is 0")
else:
    print("and is less than 6 and not 0")
