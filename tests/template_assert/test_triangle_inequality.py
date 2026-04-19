"""
Тесты для задачи "Неравенство треугольника ⃤"
"""

def solve(a, b, c):
    if a + b > c and a + c > b and b + c > a:
        return "YES"
    else:
        return "NO"

def test_triangle_inequality():
    tests = [
        # Существуют
        (3, 4, 5, "YES"),      # прямоугольный
        (5, 5, 5, "YES"),      # равносторонний
        (2, 3, 4, "YES"),      # разносторонний
        (1, 1, 1, "YES"),      # маленький равносторонний
        
        # Не существуют (нарушение неравенства)
        (1, 1, 2, "NO"),       # 1 + 1 = 2 (вырожденный)
        (1, 2, 3, "NO"),       # 1 + 2 = 3
        (10, 1, 1, "NO"),      # 1 + 1 < 10
        (5, 2, 2, "NO"),       # 2 + 2 < 5
        
        # Ноль и отрицательные (формально не положительные)
        (0, 3, 4, "NO"),
        (-1, 3, 4, "NO"),
    ]
    
    for i, (a, b, c, expected) in enumerate(tests, 1):
        result = solve(a, b, c)
        assert result == expected, f"Тест {i} провален: ({a}, {b}, {c}) -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: ({a}, {b}, {c}) -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_triangle_inequality()
