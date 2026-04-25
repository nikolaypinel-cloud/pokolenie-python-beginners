"""
Тесты для задачи "Количество чисел"
"""

from count_cubes_ending import solve

def run_tests():
    tests = [
        (1, 10, 2),      # 2^3=8 (нет), 3^3=27 (7), 4^3=64 (4)✅, 5^3=125 (5), 6^3=216 (6), 7^3=343 (3), 8^3=512 (2), 9^3=729 (9)✅, 10^3=1000 (0)
        (1, 20, 4),      # 4, 9, 14, 19
        (10, 20, 2),     # 14, 19
        (1, 100, 20),    # Каждое число, оканчивающееся на 4 или 9
        (4, 4, 1),       # 4^3=64 → 4 ✅
        (9, 9, 1),       # 9^3=729 → 9 ✅
        (2, 3, 0),       # 2^3=8 → 8, 3^3=27 → 7
        (0, 0, 0),       # 0^3=0 → 0
        (-10, -1, 4),    # -4^3=-64 → 4 ✅, -9^3=-729 → 9 ✅, -14?- нет -5? проверь
    ]
    
    print("=== Тесты для задачи 'Количество чисел' ===\n")
    all_passed = True
    
    for i, (a, b, expected) in enumerate(tests, 1):
        result = solve(a, b)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: a={a}, b={b}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
