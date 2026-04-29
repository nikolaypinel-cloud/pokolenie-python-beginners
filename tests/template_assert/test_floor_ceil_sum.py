"""
Тесты для задачи "Пол и потолок"
"""

import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent.parent))
from _06_math_module.floor_ceil_sum import solve
import math

# Запуск теста:
# python -m tests.template_assert.test_floor_ceil_sum

def test_floor_ceil_sum():
    tests = [
        (3.14, math.floor(3.14) + math.ceil(3.14)),  # 3 + 4 = 7
        (5.0, 10),    # 5 + 5 = 10
        (-3.14, -7),  # -4 + (-3) = -7
        (-5.0, -10),  # -5 + (-5) = -10
        (0.0, 0),     # 0 + 0 = 0
        (0.001, 1),   # 0 + 1 = 1
        (-0.001, -1), # -1 + 0 = -1
        (2.999, 5),   # 2 + 3 = 5
        (-2.999, -5), # -3 + (-2) = -5
    ]
    
    for i, (x, expected) in enumerate(tests, 1):
        result = solve(x)
        assert abs(result - expected) < 1e-9, f"Тест {i} провален: x={x} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: x={x} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_floor_ceil_sum()
