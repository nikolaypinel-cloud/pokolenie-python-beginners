"""
Тесты для задачи "Сумма чисел"
"""

from sum_of_numbers import solve
import sys
from io import StringIO

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
