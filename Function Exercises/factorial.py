# Create a function that calculates the factorial of a number
# A factorial is the product of an integer and all integers below it
# e.g., To calculate factorial 5... 
# 5 * 4 * 3 * 2 * 1 = 120

def factorial(num):
    factorial = 1
    for i in range(1,num + 1):
        factorial *= i
    return factorial

print(factorial(5))

# Another easier way, is to import the factorial function from the math module.
from math import factorial

def factorial_using_math(num):
    return factorial(num)

print(factorial_using_math(5))