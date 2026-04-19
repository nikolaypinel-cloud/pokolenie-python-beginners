"""
Тесты для задачи "Принадлежность 3"
Промежутки: (-30, -2] и (7, 25]
"""

def solve(x):
    if (-30 < x <= -2) or (7 < x <= 25):
        return "Принадлежит"
    else:
        return "Не принадлежит"

def test_belongs_to_interval():
    tests = [
        (-31, "Не принадлежит"),
        (-30, "Не принадлежит"),
        (-29, "Принадлежит"),
        (-2, "Принадлежит"),
        (-1, "Не принадлежит"),
        (6, "Не принадлежит"),
        (7, "Не принадлежит"),
        (8, "Принадлежит"),
        (25, "Принадлежит"),
        (26, "Не принадлежит"),
    ]
    
    for i, (x, expected) in enumerate(tests, 1):
        result = solve(x)
        assert result == expected, f"Тест {i} провален: x={x} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: x={x} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_belongs_to_interval()
