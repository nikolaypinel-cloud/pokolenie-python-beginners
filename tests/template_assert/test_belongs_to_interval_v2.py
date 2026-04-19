"""
Тесты для задачи "Принадлежность 2"
Проверяет принадлежность числа x промежутку [-3, 7]
"""

def solve(x):
    if -3 <= x <= 7:
        return "Принадлежит"
    else:
        return "Не принадлежит"

def test_belongs_to_interval():
    tests = [
        (-4, "Не принадлежит"),
        (-3, "Принадлежит"),
        (0, "Принадлежит"),
        (7, "Принадлежит"),
        (8, "Не принадлежит"),
    ]
    
    for i, (x, expected) in enumerate(tests, 1):
        result = solve(x)
        assert result == expected, f"Тест {i} провален: x={x} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: x={x} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_belongs_to_interval()
