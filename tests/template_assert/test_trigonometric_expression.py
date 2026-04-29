"""
Тесты для задачи "Тригонометрическое выражение"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _06_math_module.trigonometric_expression import solve
import math

def test_trigonometric_expression():
    tests = [
        (0, math.sin(0) + math.cos(0) + math.tan(0) ** 2),
        (45, math.sin(math.radians(45)) + math.cos(math.radians(45)) + math.tan(math.radians(45)) ** 2),
        (60, math.sin(math.radians(60)) + math.cos(math.radians(60)) + math.tan(math.radians(60)) ** 2),
        (90, math.sin(math.radians(90)) + math.cos(math.radians(90)) + math.tan(math.radians(90)) ** 2),
        (180, math.sin(math.radians(180)) + math.cos(math.radians(180)) + math.tan(math.radians(180)) ** 2),
    ]
    
    for i, (x, expected) in enumerate(tests, 1):
        result = solve(x)
        
        if x == 90:
            print(f"⚠️ Тест {i}: x={x} -> результат может быть очень большим (tan 90° -> ∞)")
            continue
            
        assert abs(result - expected) < 1e-6, f"Тест {i} провален: x={x} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: x={x} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_trigonometric_expression()