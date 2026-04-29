"""
Тесты для задачи "Асимптотическое приближение 📉"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _07_for_loop.asymptotic_approximation import solve
import math

def run_tests():
    tests = [
        (1, 1 - math.log(1)),      # 1 - 0 = 1
        (2, (1 + 1/2) - math.log(2)),
        (3, (1 + 1/2 + 1/3) - math.log(3)),
        (4, (1 + 1/2 + 1/3 + 1/4) - math.log(4)),
        (10, sum(1 / i for i in range(1, 11)) - math.log(10)),
        (100, sum(1 / i for i in range(1, 101)) - math.log(100)),
    ]
    
    print("=== Тесты для задачи 'Асимптотическое приближение 📉' ===\n")
    all_passed = True
    
    for i, (n, expected) in enumerate(tests, 1):
        result = solve(n)
        passed = abs(result - expected) < 1e-9
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: n={n}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()

# Запуск теста:
# python -m tests.template_manual.test_asymptotic_approximation