"""
Тесты для задачи "Первая цифра после точки"
"""

def solve(x):
    return int(10 * (x - int(x)))

def test_first_digit_after_decimal():
    tests = [
        (1.23, 2),
        (1.0, 0),
        (1.99, 9),
        (5.678, 6),
        (0.1, 1),
        (0.01, 0),
        (0.99, 9),
        (123.456, 4),
        (3.14159, 1),
        (2.71828, 7),
        (10.0, 0),
        (0.0, 0),
    ]
    
    for i, (x, expected) in enumerate(tests, 1):
        result = solve(x)
        assert result == expected, f"Тест {i} провален: x={x} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: x={x} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_first_digit_after_decimal()
