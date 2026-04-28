"""
Тригонометрическое выражение
Вычислить sin x + cos x + tg² x, где x — в градусах.
"""

import math

def solve(x_deg):
    x_rad = math.radians(x_deg)
    return math.sin(x_rad) + math.cos(x_rad) + math.tan(x_rad) ** 2

if __name__ == "__main__":
    x = float(input())
    print(solve(x))
