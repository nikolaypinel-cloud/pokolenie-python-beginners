"""
Площадь и длина
По радиусу R вычислить площадь круга и длину окружности.
Формулы: S = πR², C = 2πR.
"""

import math

def solve(R):
    area = math.pi * R ** 2
    circumference = 2 * math.pi * R
    return area, circumference

if __name__ == "__main__":
    R = float(input())
    area, circumference = solve(R)
    print(area)
    print(circumference)
