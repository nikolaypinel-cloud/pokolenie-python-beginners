"""
Тесты для задачи "Отдыхаем ли? 😎"
"""

from weekend import solve

def test_weekend():
    tests = [
        ("суббота", "YES"),
        ("воскресенье", "YES"),
        ("сегодня суббота", "YES"),
        ("завтра воскресенье", "YES"),
        ("суббота и воскресенье", "YES"),
        ("понедельник", "NO"),
        ("вторник", "NO"),
        ("субббота", "NO"),      # опечатка
        ("воскресень", "NO"),    # неполное слово
        ("", "NO"),
        ("Суббота", "NO"),       # регистр важен
        ("ВОСКРЕСЕНЬЕ", "NO"),   # регистр важен
        ("выходной", "NO"),
    ]
    
    for i, (s, expected) in enumerate(tests, 1):
        result = solve(s)
        assert result == expected, f"Тест {i} провален: '{s}' -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: '{s}' -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_weekend()
