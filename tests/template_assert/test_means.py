"""
Тесты для задачи "Средние значения"
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from _06_math_module.means import solve
import math

# Запуск теста:
# python -m tests.template_assert.test_means


def test_means():
    tests = [
        (1, 1, (1.0, 1.0, 1.0, 1.0)),
        (2, 8, (5.0, 4.0, 3.2, math.sqrt((4 + 64) / 2))),
        (3, 12, (7.5, 6.0, 4.8, math.sqrt((9 + 144) / 2))),
        (4, 9, (6.5, 6.0, 5.538461538461538, math.sqrt((16 + 81) / 2))),
        (1, 4, (2.5, 2.0, 1.6, math.sqrt((1 + 16) / 2))),
    ]
    
    for i, (a, b, expected) in enumerate(tests, 1):
        result = solve(a, b)
        assert all(abs(r - e) < 1e-9 for r, e in zip(result, expected)), \
            f"Тест {i} провален: a={a}, b={b} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: a={a}, b={b} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_means()
