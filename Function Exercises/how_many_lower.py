# Define a function that checks how many uppercase letters are within a string
# e.g. "i hate uppercase" = 14
# e.g. "I tHInK My KeYBOarD iS BrokEN" = 10

def upper_check(string):
    count = 0
    for i in string:
        if i.islower():
            count += 1
    return count

print(upper_check("I tHInK My KeYBOarD iS BrokEN"))