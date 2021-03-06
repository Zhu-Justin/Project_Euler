"""
Problem 2: Even Fibonacci numbers

Each new term in the Fibonacci sequence is generated by adding the
previous two terms. By starting with 1 and 2, the first 10 terms will be:

                  1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

Find the sum of all the even-valued terms in the sequence which do not
exceed four million.

"""

# Solution 1
import math

n1 = 1
n2 = 1
sum = 0
count = 2

while (n2 <= 4e6):
    n = n1 + n2
    sum += n if n % 2 == 0 else 0
    n1, n2 = n2, n
    count += 1

# print(sum)

# Solution 2
phi = (1 + math.sqrt(5)) / 2
psi = (1 - math.sqrt(5)) / 2
k = count -2
phi3 = phi * 3
psi3 = psi * 3
ans = int((1 / math.sqrt(5)) * (
        phi3 * ((1 - phi3 ** k) / (1 - phi3)) -
        psi3 * ((1 - psi3 ** k) / (1 - psi3))
    ))

print(sum)

