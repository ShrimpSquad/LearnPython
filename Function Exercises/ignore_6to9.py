# Define a function which returns the sum of numbers in an array.
# However, if a 6 appears, ignore all numbers until a 9 appears.

# summer_69([1, 3, 5]) --> 9
# summer_69([4, 5, 6, 7, 8, 9]) --> 9
# summer_69([2, 1, 6, 9, 11]) --> 14


def summer_69(array):
    sum = 0
    add = True
    for i in array:
        while add == True:
            if i == 6:
                add = False
            else:
                sum += i
                break
            
        while add == False:
            if i == 9:
                add = True
            else:
                sum += 0
                break
    return sum

my_array = [1,2,3,4,5]

print(summer_69(my_array))
print(summer_69([1, 2, 6, 1, 9, 4, 5]))
print(summer_69([2, 1, 6, 9, 11]))