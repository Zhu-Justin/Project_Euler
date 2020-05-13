"""
Problem 6: Sum square difference

The sum of the squares of the first ten natural numbers is,
                       1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
                    (1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten
natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one
hundred natural numbers and the square of the sum.

"""

N = 100
# Lists
x = [i for i in range(100)]
y = [i**2 for i in range(100)]
sum(x)
z = sum(x)**2 - sum(y)
# print(z)

# Math
sum = N * (N+1)// 2
squared = (N * (N + 1) * (2 * N + 1)) // 6
 
result = sum * sum - squared
print(result)
