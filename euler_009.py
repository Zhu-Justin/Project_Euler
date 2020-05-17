"""
Problem 9: Special Pythagorean triplet

A Pythagorean triplet is a set of three natural numbers, a < b < c, for
which,
                             a^2 + b^2 = c^2

For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

"""
def divisors(n):
    for divisor in range(1, int(n**0.5) + 1):
        if n % divisor == 0:
            yield divisor, n//divisor

# r2 = 2st is a square; then: a = r+s, b = r+t, and c = r+s+t.

pn = {}
for r in range(2, 550, 2):
    st = r*r // 2
    for s, t in divisors(st):
        x = (r+s) + (r+t) + (r+s+t)
        pn[x] = (r+s) * (r+t) * (r+s+t)

print(pn[1000])
