"""
Пол и потолок
Вычислить ⌊x⌋ + ⌈x⌉.
"""

import math

def solve(x):
    return math.floor(x) + math.ceil(x)

if __name__ == "__main__":
    x = float(input())
    print(solve(x))
