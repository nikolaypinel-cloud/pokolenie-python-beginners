"""
Тесты для задачи "Последовательность чисел 2"
"""

def solve(m, n):
    result = []
    for i in range(m, n + 1):
        if i % 17 == 0 or i % 10 == 9 or i % 15 == 0:
            result.append(i)
    return result

def run_tests():
    tests = [
        (1, 20, [9, 15, 17, 19]),
        (10, 30, [15, 17, 19, 30]),
        (50, 60, [51, 54, 55, 57, 59, 60]),
        (100, 110, [102, 105, 109]),
        (1, 10, [9]),
        (2, 8, []),
    ]
    
    print("=== Тесты для задачи 'Последовательность чисел 2' ===\n")
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
