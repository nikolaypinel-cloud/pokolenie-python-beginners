"""
Тесты для задачи "Последовательность чисел 4 🌶️"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _07_for_loop.numbers_ascending_descending import solve

# Запуск теста:
# python -m tests.template_manual.test_numbers_ascending_descending

def run_tests():
    tests = [
        (1, 5, [1, 2, 3, 4, 5]),
        (5, 1, [5, 4, 3, 2, 1]),
        (3, 3, [3]),
        (-3, 2, [-3, -2, -1, 0, 1, 2]),
        (2, -3, [2, 1, 0, -1, -2, -3]),
        (0, 0, [0]),
    ]
    
    print("=== Тесты для задачи 'Последовательность чисел 4 🌶️' ===\n")
    all_passed = True
    
    for i, (m, n, expected) in enumerate(tests, 1):
        result = solve(m, n)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: m={m}, n={n}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
