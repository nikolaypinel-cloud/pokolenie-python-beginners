"""
Тесты для задачи "Правильный многоугольник 🔶"
"""

from regular_polygon_area import solve
import math

def test_regular_polygon_area():
    tests = [
        (3, 1, (3 * 1 ** 2) / (4 * math.tan(math.pi / 3))),   # треугольник
        (4, 1, (4 * 1 ** 2) / (4 * math.tan(math.pi / 4))),   # квадрат
        (5, 1, (5 * 1 ** 2) / (4 * math.tan(math.pi / 5))),   # пятиугольник
        (6, 2, (6 * 2 ** 2) / (4 * math.tan(math.pi / 6))),   # шестиугольник
        (8, 1.5, (8 * 1.5 ** 2) / (4 * math.tan(math.pi / 8))),
    ]
    
    for i, (n, a, expected) in enumerate(tests, 1):
        result = solve(n, a)
        assert abs(result - expected) < 1e-9, f"Тест {i} провален: n={n}, a={a} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: n={n}, a={a} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_regular_polygon_area()
