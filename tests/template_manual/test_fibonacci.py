"""
Тесты для задачи "Последовательность Фибоначчи 🌶️"
"""

from fibonacci import solve

def run_tests():
    tests = [
        (1, [1]),
        (2, [1, 1]),
        (3, [1, 1, 2]),
        (4, [1, 1, 2, 3]),
        (5, [1, 1, 2, 3, 5]),
        (6, [1, 1, 2, 3, 5, 8]),
        (7, [1, 1, 2, 3, 5, 8, 13]),
        (10, [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]),
    ]
    
    print("=== Тесты для задачи 'Последовательность Фибоначчи 🌶️' ===\n")
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
