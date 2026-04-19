"""
Тесты для задачи "YES or NO – вот в чём вопрос ❓"
"""

def solve(n):
    if (n % 2) or (n % 2 == 0 and 6 <= n <= 20):
        return "YES"
    else:
        return "NO"

def test_yes_no_question():
    tests = [
        # Нечётные
        (1, "YES"), (3, "YES"), (5, "YES"), (7, "YES"), (21, "YES"), (99, "YES"),
        # Чётные 2-5
        (2, "NO"), (4, "NO"),
        # Чётные 6-20
        (6, "YES"), (8, "YES"), (10, "YES"), (12, "YES"), (14, "YES"), (16, "YES"), (18, "YES"), (20, "YES"),
        # Чётные больше 20
        (22, "NO"), (24, "NO"), (30, "NO"), (100, "NO"),
        # Границы
        (0, "NO"),   # чётное, не в диапазонах
        (19, "YES"), # нечётное
        (21, "YES"), # нечётное
    ]
    
    for i, (n, expected) in enumerate(tests, 1):
        result = solve(n)
        assert result == expected, f"Тест {i} провален: n={n} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: n={n} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_yes_no_question()
