# Define a function which returns a string that has 3x every letter
# e.g., hello becomes hhheeellllllooo

def triple_letter(string):
    new_string = ""
    for i in string:
        new_string += i*3
    return new_string

print(triple_letter("hello"))
