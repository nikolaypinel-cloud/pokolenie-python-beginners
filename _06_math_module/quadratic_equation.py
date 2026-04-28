"""
Квадратное уравнение 🌶️🌶️
Найти действительные корни квадратного уравнения ax² + bx + c = 0, a ≠ 0.
"""

import math

def solve(a, b, c):
    D = b**2 - 4*a*c
    
    if D < 0:
        return "Нет корней"
    elif D == 0:
        x = -b / (2*a)
        return f"{x}"
    else:
        sqrt_D = math.sqrt(D)
        x1 = (-b - sqrt_D) / (2*a)
        x2 = (-b + sqrt_D) / (2*a)
        # Выводим в порядке возрастания
        if x1 < x2:
            return f"{x1}\n{x2}"
        else:
            return f"{x2}\n{x1}"

if __name__ == "__main__":
    a = float(input())
    b = float(input())
    c = float(input())
    print(solve(a, b, c))
