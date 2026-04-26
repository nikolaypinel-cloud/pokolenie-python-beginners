"""
Тесты для задачи "Сумма делителей"
"""

from sum_of_divisors import solve

def run_tests():
    tests = [
        (1, 1),                        # 1
        (2, 1 + 2),                    # 3
        (3, 1 + 3),                    # 4
        (4, 1 + 2 + 4),                # 7
        (5, 1 + 5),                    # 6
        (6, 1 + 2 + 3 + 6),            # 12
        (12, 1 + 2 + 3 + 4 + 6 + 12),  # 28
        (16, 1 + 2 + 4 + 8 + 16),      # 31
        (28, 1 + 2 + 4 + 7 + 14 + 28), # 56
        (36, 1 + 2 + 3 + 4 + 6 + 9 + 12 + 18 + 36),  # 91
    ]
    
    print("=== Тесты для задачи 'Сумма делителей' ===\n")
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
