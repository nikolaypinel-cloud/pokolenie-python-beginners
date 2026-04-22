"""
Евклидово расстояние 📏
Вычислить расстояние между двумя точками (x1, y1) и (x2, y2).
Формула: ρ = √((x1 - x2)² + (y1 - y2)²)
"""

import math

def solve(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

if __name__ == "__main__":
    x1, y1, x2, y2 = [float(input()) for _ in range(4)]
    print(solve(x1, y1, x2, y2))
