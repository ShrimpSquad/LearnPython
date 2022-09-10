# Define a function that checks how many uppercase letters are within a string
# e.g. "I Love Typing In Title Case" = 6
# e.g. "I tHInK My KeYBOarD iS BrokEN" = 14

def upper_check(string):
    count = 0
    for i in string:
        if i.isupper():
            count += 1
    return count

print(upper_check("I tHInK My KeYBOarD iS BrokEN"))