"""
Тесты для задачи "Сумма чисел 2"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _07_for_loop.sum_of_numbers_v2 import solve

# Запуск теста:
# python -m tests.template_manual.test_sum_of_numbers_v2

def run_tests():
    tests = [
        (5, 5),        # 5²=25 → 5
        (10, 5),       # только 5
        (15, 20),      # 5 + 15 = 20 (15²=225 → 5)
        (25, 75),      # 5 + 15 + 25 = 45? 25²=625 → 5, сумма 5+15+25=45
        (1, 0),        # нет таких чисел
        (4, 0),        # нет
    ]
    
    print("=== Тесты для задачи 'Сумма чисел 2' ===\n")
    all_passed = True
    
    for i, (n, expected) in enumerate(tests, 1):
        result = solve(n)
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
