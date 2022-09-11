# Define a function which checks if a certain integer is within 20 of 1000
# If so, return True, otherwise return False

def within_20(num):
    if 1000 - abs(num) <= 20:
        return True
    return False

print(within_20(999))
print(within_20(500))

