"""
Тесты для задачи "Пересечение отрезков"
"""

def solve(a1, b1, a2, b2):
    left = max(a1, a2)
    right = min(b1, b2)
    
    if left > right:
        return "пустое множество"
    elif left == right:
        return str(left)
    else:
        return f"{left} {right}"

def test_segment_intersection():
    tests = [
        # Пересекающиеся отрезки
        (1, 5, 3, 7, "3 5"),
        (1, 10, 5, 6, "5 6"),
        (5, 6, 1, 10, "5 6"),
        
        # Касающиеся (общая точка)
        (1, 3, 3, 5, "3"),
        (3, 5, 1, 3, "3"),
        
        # Не пересекаются
        (1, 2, 3, 4, "пустое множество"),
        (3, 4, 1, 2, "пустое множество"),
        
        # Один внутри другого
        (1, 10, 3, 7, "3 7"),
        (3, 7, 1, 10, "3 7"),
        
        # Граничные случаи
        (0, 1, 1, 2, "1"),
        (0, 0, 0, 0, "0"),
        (-5, -1, -3, 3, "-3 -1"),
        (-10, -5, -7, -2, "-7 -5"),
    ]
    
    for i, (a1, b1, a2, b2, expected) in enumerate(tests, 1):
        result = solve(a1, b1, a2, b2)
        assert result == expected, f"Тест {i} провален: ({a1},{b1}) и ({a2},{b2}) -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: ({a1},{b1}) и ({a2},{b2}) -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_segment_intersection()
