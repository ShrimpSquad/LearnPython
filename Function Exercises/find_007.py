# Define a function that looks through an array to finds 0 0 7 in order
# If found, return True, otherwise return False

def james_bond(array):
    for i in range(0, len(array) - 2):
        if array[i] == 0 and array[i+1] == 0 and array[i+2] == 7:
            return True
    return False

my_array = [1, 0, 6, 0, 0, 7, 3, 8, 9]
my_other_array = [1, 0, 6, 0, 2, 1, 3, 8, 9]

print(james_bond(my_array))
print(james_bond(my_other_array))




