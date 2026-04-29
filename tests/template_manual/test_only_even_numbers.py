"""
Тесты для задачи "Only even numbers"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _07_for_loop.only_even_numbers import solve

# Запуск теста:
# python -m tests.template_manual.test_only_even_numbers

def run_tests():
    tests = [
        ((2, 4, 6, 8, 10, 12, 14, 16, 18, 20), True),
        ((1, 2, 3, 4, 5, 6, 7, 8, 9, 10), False),
        ((2, 4, 6, 8, 10, 12, 14, 16, 18, 21), False),
        ((0, 2, 4, 6, 8, 10, 12, 14, 16, 18), True),
        ((-2, -4, -6, -8, -10, -12, -14, -16, -18, -20), True),
        ((-2, -4, -6, -8, -10, -12, -14, -16, -18, -1), False),
    ]
    
    print("=== Тесты для задачи 'Only even numbers' ===\n")
    all_passed = True
    
    for i, (nums, expected) in enumerate(tests, 1):
        result = solve(nums)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: numbers={nums}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
