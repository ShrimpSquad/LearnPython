# Define a function that checks how many lower and uppercase letters are within a string
# e.g. "I tHInK My KeYBOarD iS BrokEN" 
# lowercase = 10
# uppercase = 14

def upper_lower_counter(string):
    upper_count = 0
    lower_count = 0
    for i in string:
        if i.isupper():
            upper_count += 1
        elif i.islower():
            lower_count += 1
    return f"There are {upper_count} uppercase letters and {lower_count} lowercase letters in the string"

print(upper_lower_counter("I tHInK My KeYBOarD iS BrokEN"))