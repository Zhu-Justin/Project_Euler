"""
Problem 1: Multiples of 3 and 5

If we list all the natural numbers below 10 that are multiples of 3 or 5,
we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.

"""

# basic
multiples = [i for i in range(1000) if i % 3 == 0 or i % 5 == 0]
print(sum(multiples))

# the math way
# n = 1000
# m1 = 3
# m2 = 5

# def multsum(n, m1):
#     n //= m1
#     return int(m1 * n * (n + 1) / 2)


# ans = multsum(n, m1) + multsum(n, m2) - multsum(n, m1 * m2)
# print(ans)



