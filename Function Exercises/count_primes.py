# define a function that returns the number of prime numbers 
# that exist up to and including the inputted number
# e.g. func(100) -> 25

def prime_number(num):
    if num < 2:
        return 0
    
    primes = [2]

    x = 3

    while x <= num:
        for y in primes:
            if x % y == 0:
                x += 2
                break
        else:
            primes.append(x)
            x +=2

    print(primes)
    return len(primes)

print(prime_number(1000))
print(prime_number(500))