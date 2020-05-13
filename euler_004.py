"""
Problem 4: Largest palindrome product

A palindromic number reads the same both ways. The largest palindrome made
from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

"""

def isPalindrome(x):
    n = 0
    m = x
    while x > 0:
        n = n * 10 + x % 10
        x = int(x / 10)
    return n == m

# Must be divisible by 11
def findpalindrome():
    r = 0
    for p in range(990,99,-11):
        for q in range(999,99,-1):
            t = p * q
            if r < t and isPalindrome(p * q):
                r = t
            elif t < r:
                break;
    return r

# isPalindrome(121)
print(findpalindrome())
