#
# Functions with python
#

# Creating a function

def city():
    print("New York City")

city()

# Passing a parameter into a function

def my_city(name):
    print(name)

my_city("NYC")

# Creating a function that adds two numbers together and returns the total

def add_nums(num1, num2):
    return num1 + num2

total = add_nums(4, 3)

print(total)

# Function that returns the greatest number

def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

max_value = max_num(num1, num2, num3)

print(max_value)