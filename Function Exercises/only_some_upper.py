# Define a function that only capitalizes the 2nd and 3rd letters of a string.
# If the string is less than 3 letters, return the string without any changes

def upper_23(string):
    if len(string) > 2:
        start = string[:1]
        end = string[3:]
        mid = string[1:3].upper()
        return start + mid + end
    else:
        return string

print(upper_23("charcuterie"))
print(upper_23("ok"))