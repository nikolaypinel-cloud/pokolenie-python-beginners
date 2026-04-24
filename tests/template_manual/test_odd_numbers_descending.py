"""
Тесты для задачи "Последовательность чисел 3 🌶️"
"""

def solve(m, n):
    """Возвращает список нечётных чисел от m до n в порядке убывания."""
    result = []
    m = m // 2 * 2 + 1
    for i in range(m, n - 1, -2):
        result.append(i)
    return result

def run_tests():
    tests = [
        (9, 1, [9, 7, 5, 3, 1]),
        (10, 1, [11, 9, 7, 5, 3, 1]),
        (11, 1, [11, 9, 7, 5, 3, 1]),
        (12, 1, [13, 11, 9, 7, 5, 3, 1]),
        (5, 1, [5, 3, 1]),
        (6, 1, [7, 5, 3, 1]),
        (1, 1, [1]),
        (0, -5, [1, -1, -3, -5]),
        (-1, -5, [-1, -3, -5]),
        (-2, -5, [-1, -3, -5]),
    ]
    
    print("=== Тесты для задачи 'Последовательность чисел 3 🌶️' ===\n")
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
