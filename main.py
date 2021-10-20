from decimal import *
from math import factorial


def pi(n):
    pi = Decimal(13591409)
    ak = Decimal(1)
    k = 1
    while k < n:
        ak *= -Decimal((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) / Decimal(k * k * k * 26680 * 640320 * 640320)

        val = ak * (13591409 + 545140134 * k)

        d = Decimal((6 * k - 5) * (2 * k - 1) * (6 * k - 1)) / Decimal(k * k * k * 26680 * 640320 * 640320)

        pi += val
        k += 1
    pi = pi * Decimal(10005).sqrt() / 4270934400
    pi = pi ** (-1)
    return pi


n = int(input())
n = n+1
getcontext().prec = n

print(pi(n))
