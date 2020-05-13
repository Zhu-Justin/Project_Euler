"""
Problem 3: Largest prime factor

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143?

"""

def max_factor(num):
    """Find the maximum prime factor."""
    best = None
    factor = 2 
    while factor * factor <= num:
        while num % factor == 0:
            best = factor
            num /= factor
        factor += 1
    if (num > 1): 
        return num 
    return best

print(int(max_factor(600851475143)))
