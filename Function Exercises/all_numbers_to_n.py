# Define a function that prints all numbers up to an inputted integer.
# e.g. 5 --> 12345

def intcount(num):
    numstring = ""
    for i in range(1,num + 1):
        numstring += str(i)
    
    print(numstring)

intcount(5)

