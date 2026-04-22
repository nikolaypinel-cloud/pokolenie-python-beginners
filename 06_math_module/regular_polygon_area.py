"""
Правильный многоугольник 🔶
Вычислить площадь правильного многоугольника с n сторонами и длиной стороны a.
Формула: S = (n * a²) / (4 * tan(π / n))
"""

import math

def solve(n, a):
    return (n * a ** 2) / (4 * math.tan(math.pi / n))

if __name__ == "__main__":
    n = int(input())
    a = float(input())
    print(solve(n, a))
