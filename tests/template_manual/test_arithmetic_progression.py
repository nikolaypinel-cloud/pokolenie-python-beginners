"""
Тесты для задачи "Арифметическая прогрессия"
"""

def is_arithmetic_progression(a, b, c):
    """Возвращает True, если три числа образуют арифметическую прогрессию."""
    return b - a == c - b

def run_tests():
    tests = [
        # (a, b, c, ожидаемый_результат)
        (1, 2, 3, True),      # YES
        (1, 3, 5, True),      # YES
        (10, 20, 30, True),   # YES
        (-5, 0, 5, True),     # YES
        (0, 0, 0, True),      # YES (разность 0)
        (1, 2, 4, False),     # NO
        (5, 10, 20, False),   # NO
        (-10, -5, 1, False),  # NO
        (3, 3, 5, False),     # NO
        (7, 5, 3, True),      # YES (убывающая)
        (100, 50, 0, True),   # YES
    ]
    
    print("=== Тесты для 'Арифметическая прогрессия' ===\n")
    all_passed = True
    
    for i, (a, b, c, expected) in enumerate(tests, 1):
        result = is_arithmetic_progression(a, b, c)
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: ({a}, {b}, {c})")
        print(f"   Результат: {'YES' if result else 'NO'}")
        print(f"   Ожидалось: {'YES' if expected else 'NO'}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
