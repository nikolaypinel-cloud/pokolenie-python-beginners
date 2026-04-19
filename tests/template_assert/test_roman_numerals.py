"""
Тесты для задачи "Римские цифры"
"""

def solve(n):
    roma = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X']
    if 1 <= n <= 10:
        return roma[n - 1]
    else:
        return "ошибка"

def test_roman_numerals():
    tests = [
        (1, "I"), (2, "II"), (3, "III"), (4, "IV"), (5, "V"),
        (6, "VI"), (7, "VII"), (8, "VIII"), (9, "IX"), (10, "X"),
        (0, "ошибка"), (11, "ошибка"), (-5, "ошибка"), (100, "ошибка"),
    ]
    
    for i, (n, expected) in enumerate(tests, 1):
        result = solve(n)
        assert result == expected, f"Тест {i} провален: n={n} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: n={n} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_roman_numerals()
