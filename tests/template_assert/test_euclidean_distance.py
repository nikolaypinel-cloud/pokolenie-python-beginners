"""
Тесты для задачи "Евклидово расстояние 📏"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _06_math_module.euclidean_distance import solve
import math

def test_euclidean_distance():
    tests = [
        (0, 0, 3, 4, 5.0),
        (0, 0, 1, 1, math.sqrt(2)),
        (0, 0, 0, 0, 0.0),
        (1, 1, 1, 5, 4.0),
        (1, 1, 5, 1, 4.0),
        (-1, -1, 2, 3, 5.0),
    ]
    
    for i, (x1, y1, x2, y2, expected) in enumerate(tests, 1):
        result = solve(x1, y1, x2, y2)
        assert abs(result - expected) < 1e-9, f"Тест {i} провален: ({x1},{y1}) -> ({x2},{y2}) -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: ({x1},{y1}) -> ({x2},{y2}) -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_euclidean_distance()

# Запуск теста:
# python -m tests.template_assert.test_euclidean_distance