# Define a function that checks if the inputted number is within the range of 1-50

def range_check(num):
    if num in range (1,51):
        return f"{num} is inside of the range of 1 to 50"
    else:
        return f"{num} is outside of the range of 1 to 50"

print(range_check(50))
