# Define a function which checks if the sum of *args integers is 50

def sum_is_50(*args):
    if sum(args) == 50:
        return True
    else:
        return False

print(sum_is_50(5,3,3,2,6,7,8,1))
print(sum_is_50(25,10,15))