"""
Тесты для задачи "Принадлежность 1"
Проверяет принадлежность числа x промежутку (-1, 17)
"""

def solve(x):
    if -1 < x < 17:
        return "Принадлежит"
    else:
        return "Не принадлежит"

def test_belongs_to_interval():
    tests = [
        (-2, "Не принадлежит"),
        (-1, "Не принадлежит"),
        (0, "Принадлежит"),
        (16, "Принадлежит"),
        (17, "Не принадлежит"),
        (100, "Не принадлежит"),
        (-100, "Не принадлежит"),
    ]
    
    for i, (x, expected) in enumerate(tests, 1):
        result = solve(x)
        assert result == expected, f"Тест {i} провален: x={x} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: x={x} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_belongs_to_interval()
