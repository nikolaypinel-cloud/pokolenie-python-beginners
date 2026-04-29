"""
Тесты для задачи "Без нулей 0️"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _07_for_loop.product_without_zeros import solve

# Запуск теста:
# python -m tests.template_manual.test_product_without_zeros

def run_tests():
    tests = [
        ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3628800),
        ([0, 0, 0, 0, 0, 0, 0, 0, 0, 5], 5),
        ([1, 0, 2, 0, 3, 0, 4, 0, 5, 0], 120),
        ([-1, -2, -3, -4, -5, -6, -7, -8, -9, -10], 3628800),
        ([2, 0, 3, 0, 0, 0, 0, 0, 0, 7], 42),
        ([10, 10, 10, 10, 10, 10, 10, 10, 10, 10], 10**10),
    ]
    
    print("=== Тесты для задачи 'Без нулей 0️' ===\n")
    all_passed = True
    
    for i, (numbers, expected) in enumerate(tests, 1):
        result = solve(numbers)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: numbers={numbers}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
