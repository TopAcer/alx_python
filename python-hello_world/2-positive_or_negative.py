import random
number = random.randint(-10, 10)

print("Random number:", number)
if number > 0:
    print("is positive")

elif number == 0:
    print("is zero")

else:
    print("is negative\n")
