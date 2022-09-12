# Define a function that takes *args.
# If the sum is > 21 and there is an 11, reduce the sum by 10.
# Otherwise, if it's greater than 21, return "BUST"

def basic_21(*args):
    if sum(args) <= 21:
        return sum(args)
    elif sum(args) > 21 and 11 in args:
        return sum(args) - 10
    else:
        return "BUST!"

print(basic_21(4,5,6,7))
print(basic_21(4,5,6,6))
print(basic_21(4,5,6,11))