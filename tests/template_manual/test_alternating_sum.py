"""
Тесты для задачи "Знакочередующаяся сумма"
"""

from alternating_sum import solve

def run_tests():
    tests = [
        (1, 1),
        (2, -1),      # 1 - 2 = -1
        (3, 2),       # 1 - 2 + 3 = 2
        (4, -2),      # 1 - 2 + 3 - 4 = -2
        (5, 3),       # 1 - 2 + 3 - 4 + 5 = 3
        (6, -3),
        (7, 4),
        (8, -4),
        (9, 5),
        (10, -5),
        (100, -50),   # для чётного n результат = -n/2
        (101, 51),    # для нечётного n результат = (n+1)/2
    ]
    
    print("=== Тесты для задачи 'Знакочередующаяся сумма' ===\n")
    all_passed = True
    
    for i, (n, expected) in enumerate(tests, 1):
        result = solve(n)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: n={n} -> {result}, ожидалось {expected}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
