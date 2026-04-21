"""
Тесты для задачи "Цвет настроения синий 🟦"
"""

from blue_mood import solve

def test_blue_mood():
    tests = [
        ("синий", "YES"),
        ("синий туман", "YES"),
        ("туман синий", "YES"),
        ("синийсиний", "YES"),
        ("синний", "NO"),
        ("голубой", "NO"),
        ("синева", "NO"),
        ("", "NO"),
        ("СИНИЙ", "NO"),  # регистр важен
        ("Я люблю синий цвет", "YES"),
        ("синий и красный", "YES"),
    ]
    
    for i, (s, expected) in enumerate(tests, 1):
        result = solve(s)
        assert result == expected, f"Тест {i} провален: '{s}' -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: '{s}' -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_blue_mood()
