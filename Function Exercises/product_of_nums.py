# Create a function that sums the numbers in a list
def sum_of_nums(list):
    sum = 1
    for i in list:
        sum *= i
    return sum

# Tests
print(sum_of_nums([1, 4, 5, 2, 30])) 
print(sum_of_nums([1, 3])) 
print(sum_of_nums([7, 39, 3])) 