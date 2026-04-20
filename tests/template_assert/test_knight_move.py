"""
Тесты для задачи "Ход коня ♘"
"""

def solve(x1, y1, x2, y2):
    dx = abs(x1 - x2)
    dy = abs(y1 - y2)
    return "YES" if (dx == 1 and dy == 2) or (dx == 2 and dy == 1) else "NO"

def test_knight_move():
    tests = [
        # Правильные ходы коня
        (1, 1, 2, 3, "YES"),
        (1, 1, 3, 2, "YES"),
        (8, 8, 7, 6, "YES"),
        (8, 8, 6, 7, "YES"),
        (4, 4, 5, 6, "YES"),
        (4, 4, 6, 5, "YES"),
        (4, 4, 3, 6, "YES"),
        (4, 4, 6, 3, "YES"),
        (4, 4, 2, 3, "YES"),
        (4, 4, 3, 2, "YES"),
        (4, 4, 2, 5, "YES"),
        (4, 4, 5, 2, "YES"),
        
        # Не ходы коня
        (1, 1, 1, 1, "NO"),
        (1, 1, 1, 2, "NO"),
        (1, 1, 2, 2, "NO"),
        (1, 1, 8, 8, "NO"),
        (4, 4, 4, 6, "NO"),
        (4, 4, 6, 6, "NO"),
        (4, 4, 7, 5, "NO"),
        
        # Границы доски
        (1, 2, 2, 4, "YES"),
        (1, 2, 3, 3, "YES"),
        (1, 2, 3, 1, "YES"),
        (8, 7, 7, 5, "YES"),
        (8, 7, 6, 6, "YES"),
        (8, 7, 6, 8, "YES"),
    ]
    
    for i, (x1, y1, x2, y2, expected) in enumerate(tests, 1):
        result = solve(x1, y1, x2, y2)
        assert result == expected, f"Тест {i} провален: ({x1},{y1}) -> ({x2},{y2}) -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: ({x1},{y1}) -> ({x2},{y2}) -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_knight_move()
