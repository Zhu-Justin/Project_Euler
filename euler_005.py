"""
Problem 5: Smallest multiple

2520 is the smallest number that can be divided by each of the numbers
from 1 to 10 without any remainder.

What is the smallest number that is evenly divisible by all of the numbers
from 1 to 20?

"""

# divisors = [x for x in range(1,21)]

# allDivisions = zip(n % i for i in divisors)

# check = all(item[0] == 0 for item in allDivisions)

def lcm(*values):
    values = [value for value in values]
    if values:
        n  = max(values)
        m = n
        values.remove(n)
        while any( n % value for value in values ):
            n +=m
        return n
    return 0

# xor = lambda x, y: (x + y)%2
# l = reduce(xor, [1,2,3,4])

# from functools import reduce
# reduce(sum, range(1,10 + 1))

# print(reduce(lcm, range(1,21)))

# divs = [x for x in range(1,20) if 20 % x == 0]

smallest_num = 1
for i in range (1,21):
    if smallest_num % i > 0: # If the number is not divisible by i
        for k in range (1,21):
            if (smallest_num * k) % i == 0: # Find the smallest number divisible by i    
                smallest_num = smallest_num * k
                break
n = smallest_num
print(n)

# divs = [x for x in range(1,20) if n % x == 0]

