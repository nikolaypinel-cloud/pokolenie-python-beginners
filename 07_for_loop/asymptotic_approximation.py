"""
Асимптотическое приближение 📉
Вычислить (1 + 1/2 + 1/3 + ... + 1/n) - ln(n)
"""

from math import log

def solve(number):
    total = sum(1 / i for i in range(1, number + 1)) - log(number)
    return total

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
