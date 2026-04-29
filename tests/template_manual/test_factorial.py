"""
Тесты для задачи "Факториал ❗"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _07_for_loop.factorial import factorial

# Запуск теста:
# python -m tests.template_manual.test_factorial

def run_tests():
    tests = [
        (1, 1),
        (2, 2),
        (3, 6),
        (4, 24),
        (5, 120),
        (6, 720),
        (7, 5040),
        (8, 40320),
        (9, 362880),
        (10, 3628800),
        (0, 1),      # по определению 0! = 1
    ]
    
    print("=== Тесты для задачи 'Факториал ❗' ===\n")
    all_passed = True
    
    for i, (n, expected) in enumerate(tests, 1):
        result = factorial(n)
        passed = result == expected
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
