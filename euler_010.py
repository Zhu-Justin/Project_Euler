"""
Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import math

def primes_sieve(n):
    p_n = n
    # p_n = int(2 * n * math.log(n))       # over-estimate p_n
    sieve = [True] * p_n                 # everything is prime to start
    count = 0
    ans = 0

    for i in range(2, p_n):
        if sieve[i]:                       # still prime?
            count += 1                     # count it!
            ans += sieve[i]
            if count == n:                 # done!
                return i
            for j in range(2*i, p_n, i):   # cross off all multiples of i
                sieve[j] = False
    return ans

print(primes_sieve(int(1e6)))

