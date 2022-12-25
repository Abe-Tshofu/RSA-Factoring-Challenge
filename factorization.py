#/usr/bin/env python3
import sys

import math
import random

def prime_factorize(n):
    factors = []
    if n <= 3:
        factors.append(n)
        return factors
    x = random.randint(2, n - 1)
    y = x
    c = random.randint(1, n - 1)
    d = 1
    while d == 1:
        x = (x * x + c) % n
        y = (y * y + c) % n
        y = (y * y + c) % n
        d = math.gcd(abs(y - x), n)
        if y == x:
            d = n
        if y == x + c:
            c = random.randint(1, n - 1)
    if d != n:
        factors.append(d)
        factors.append(n // d)
    else:
        factors.append(n)
    return factors

print(prime_factorize(12345))
