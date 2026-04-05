"""
Тесты для задачи "Четное или нечетное?"
"""

def solve(n):
    if n % 2 == 0:
        return "Четное"
    else:
        return "Нечетное"

def run_tests():
    tests = [
        (5, "Нечетное"),
        (4, "Четное"),
        (0, "Четное"),
        (-3, "Нечетное"),
        (100, "Четное"),
        (1, "Нечетное"),
        (-2, "Четное"),
    ]
    
    print("=== Тесты для 'Четное или нечетное?' ===\n")
    all_passed = True
    
    for i, (n, expected) in enumerate(tests, 1):
        result = solve(n)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: n = {n}")
        print(f"   Результат: {result}")
        print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
