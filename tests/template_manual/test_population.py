"""
Тесты для задачи "Популяция 🦠"
"""

def solve(m, p, n):
    result = []
    for i in range(n):
        result.append((i + 1, m * (1 + p / 100) ** i))
    return result

def run_tests():
    tests = [
        (10, 10, 1, [(1, 10.0)]),
        (10, 10, 2, [(1, 10.0), (2, 11.0)]),
        (10, 10, 3, [(1, 10.0), (2, 11.0), (3, 12.1)]),
        (100, 50, 3, [(1, 100.0), (2, 150.0), (3, 225.0)]),
        (1, 100, 4, [(1, 1.0), (2, 2.0), (3, 4.0), (4, 8.0)]),
    ]
    
    print("=== Тесты для задачи 'Популяция 🦠' ===\n")
    all_passed = True
    
    for i, (m, p, n, expected) in enumerate(tests, 1):
        result = solve(m, p, n)
        passed = True
        
        # Сравниваем каждый день с учётом погрешности
        if len(result) != len(expected):
            passed = False
        else:
            for (day1, pop1), (day2, pop2) in zip(result, expected):
                if day1 != day2 or abs(pop1 - pop2) > 1e-9:
                    passed = False
                    break
        
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: m={m}, p={p}, n={n}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()
