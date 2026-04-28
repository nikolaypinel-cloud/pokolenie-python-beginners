"""
Средние значения
Вычислить среднее арифметическое, геометрическое, гармоническое и квадратичное.
"""

import math

def solve(a, b):
    arith = (a + b) / 2
    geom = math.sqrt(a * b)
    harmon = (2 * a * b) / (a + b)
    quad = math.sqrt((a**2 + b**2) / 2)
    return arith, geom, harmon, quad

if __name__ == "__main__":
    a = float(input())
    b = float(input())
    results = solve(a, b)
    for res in results:
        print(res)
