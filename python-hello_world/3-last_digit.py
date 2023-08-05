import random

# This line should not be changed:
number = random.randint(-10000, 10000)

# Get the last digit of the number using the remainder (%) operator
last_digit = abs(number) % 10

# Determine the sign for the last digit
sign = "-" if number < 0 else ""

# Determine the descriptive text based on the last digit
if last_digit > 5:
    description = "and is greater than 5"
elif last_digit == 0:
    description = "and is 0"
else:
    description = "and is less than 6 and not 0"

# Print the output with the desired format
print(f"Last digit of {number} is {sign}{last_digit} {description}")
