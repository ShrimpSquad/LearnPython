# Create a function that takes in two numbers.
# If both are even, return the lower one.
# If not, return the highest number

def calc(num1,num2):
    if num1 % 2 == 0 and num2 % 2 == 0:
        return min(num1,num2)
    else:
        return max(num1,num2)

print(calc(2,6))
print(calc(604532,62342456))
print(calc(21,63))
print(calc(602,623))