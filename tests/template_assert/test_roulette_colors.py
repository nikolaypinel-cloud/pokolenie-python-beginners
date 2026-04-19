"""
Тесты для задачи "Цвета колеса рулетки 🌶️"
"""

def solve(n):
    if 0 <= n <= 36:
        if n == 0:
            return "зеленый"
        elif 1 <= n <= 10 or 19 <= n <= 28:
            return "красный" if n % 2 else "черный"
        else:
            return "черный" if n % 2 else "красный"
    else:
        return "ошибка ввода"

def test_roulette_colors():
    tests = [
        (0, "зеленый"),
        (1, "красный"), (2, "черный"),
        (11, "черный"), (12, "красный"),
        (19, "красный"), (20, "черный"),
        (29, "черный"), (30, "красный"),
        (36, "красный"),
        (-1, "ошибка ввода"),
        (37, "ошибка ввода"),
    ]
    
    for i, (n, expected) in enumerate(tests, 1):
        result = solve(n)
        assert result == expected, f"Тест {i} провален: n={n} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: n={n} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_roulette_colors()
