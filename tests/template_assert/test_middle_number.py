"""
Тесты для задачи "Серединное число"
"""

def solve(a, b, c):
    if (a > b and a < c) or (a < b and a > c):
        return a
    elif (b > a and b < c) or (b < a and b > c):
        return b
    else:
        return c

def test_middle_number():
    tests = [
        # Порядки возрастания
        (1, 2, 3, 2),
        (1, 3, 2, 2),
        (2, 1, 3, 2),
        (2, 3, 1, 2),
        (3, 1, 2, 2),
        (3, 2, 1, 2),
        
        # Другие наборы
        (5, 10, 7, 7),
        (10, 5, 7, 7),
        (7, 5, 10, 7),
        (7, 10, 5, 7),
        (-5, 0, 5, 0),
        (-10, -5, -1, -5),
        (100, 0, 50, 50),
        (-100, -200, -150, -150),
    ]
    
    for i, (a, b, c, expected) in enumerate(tests, 1):
        result = solve(a, b, c)
        assert result == expected, f"Тест {i} провален: ({a}, {b}, {c}) -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: ({a}, {b}, {c}) -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_middle_number()
