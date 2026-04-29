"""
Тесты для задачи "Сумма чисел"
"""


import sys
from io import StringIO
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _07_for_loop.sum_of_numbers import solve

# Запуск теста:
# python -m tests.template_manual.test_sum_of_numbers

def run_tests():
    tests = [
        (3, [1, 2, 3], 6),
        (5, [10, 20, 30, 40, 50], 150),
        (1, [100], 100),
        (4, [0, 0, 0, 0], 0),
        (2, [-5, 5], 0),
        (3, [10, -10, 20], 20),
    ]
    
    print("=== Тесты для задачи 'Сумма чисел' ===\n")
    all_passed = True
    
    for i, (n, inputs, expected) in enumerate(tests, 1):
        # Сохраняем оригинальный stdin
        original_stdin = sys.stdin
        # Подменяем stdin нашими данными
        sys.stdin = StringIO("\n".join(map(str, inputs)))
        
        result = solve(n)
        
        # Восстанавливаем stdin
        sys.stdin = original_stdin
        
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: n={n}, numbers={inputs}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
