"""
Тесты для задачи "Наибольшие числа 🌶️"
"""

from two_largest import solve

def run_tests():
    tests = [
        ([1, 2, 3, 4, 5], (5, 4)),
        ([5, 4, 3, 2, 1], (5, 4)),
        ([10, 20, 30, 25, 15], (30, 25)),
        ([100, 50, 75, 25, 0], (100, 75)),
        ([7, 7, 7, 7, 7], (7, 7)),        # числа могут быть одинаковыми? условие: "различных", но на всякий случай
        ([2, 5, 8, 3, 9], (9, 8)),
    ]
    
    print("=== Тесты для задачи 'Наибольшие числа 🌶️' ===\n")
    all_passed = True
    
    for i, (nums, expected) in enumerate(tests, 1):
        result = solve(nums.copy())  # копируем, чтобы не портить исходный список
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: numbers={nums}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
