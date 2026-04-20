"""
Тесты для задачи "Ход ферзя ♕"
"""

def solve(x1, y1, x2, y2):
    return "YES" if (x1 == x2 or y1 == y2 or abs(x1 - x2) == abs(y1 - y2)) else "NO"

def test_queen_move():
    tests = [
        # Ходы ладьи (горизонталь/вертикаль)
        (1, 1, 1, 8, "YES"),
        (1, 1, 8, 1, "YES"),
        (4, 4, 4, 7, "YES"),
        (4, 4, 7, 4, "YES"),
        
        # Ходы слона (диагональ)
        (1, 1, 8, 8, "YES"),
        (8, 8, 1, 1, "YES"),
        (2, 3, 5, 6, "YES"),
        (7, 2, 4, 5, "YES"),
        (1, 8, 8, 1, "YES"),
        
        # Невозможные ходы
        (1, 1, 2, 3, "NO"),
        (1, 1, 3, 2, "NO"),
        (4, 4, 6, 8, "NO"),
        (8, 8, 7, 5, "NO"),
        
        # Та же клетка
        (3, 3, 3, 3, "YES"),
        
        # Границы доски
        (1, 2, 8, 9, "NO"),
        (8, 1, 1, 8, "YES"),
    ]
    
    for i, (x1, y1, x2, y2, expected) in enumerate(tests, 1):
        result = solve(x1, y1, x2, y2)
        assert result == expected, f"Тест {i} провален: ({x1},{y1}) -> ({x2},{y2}) -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: ({x1},{y1}) -> ({x2},{y2}) -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_queen_move()
