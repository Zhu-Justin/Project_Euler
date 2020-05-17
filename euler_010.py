"""
Problem 10: Summation of primes

The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.

"""
import math

# def sum_primes(limit):
#     primes = []
#     for n in range(2, limit+1):
#         # try dividing n with all primes less than sqrt(n):
#         for p in primes:
#             if n % p == 0: break     # if p divides n, stop the search
#             if n < p*p:
#                primes.append(n)      # if p > sqrt(n), mark n as prime and stop search
#                break
#         else: primes.append(n)       # fallback: we actually only get here for n == 2
#     return sum(primes)

# print(sum_primes(N))
# fast method
def primes_sieve(n):
    p_n = n + 1
    # p_n = int(2 * n * math.log(n))       # over-estimate p_n
    sieve = [True] * p_n                 # everything is prime to start
    count = 0
    ans = 0

    for i in range(2, p_n):
        if sieve[i]:                       # still prime?
            count += 1                     # count it!
            ans += i
            # if count == n:                 # done!
            #     return i
            for j in range(2*i, p_n, i):   # cross off all multiples of i
                sieve[j] = False
    return ans

N=int(2e6)
print(primes_sieve(N))
