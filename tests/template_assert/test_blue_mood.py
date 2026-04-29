"""
Тесты для задачи "Цвет настроения синий 🟦"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _05_strings.blue_mood import solve

# Запуск теста:
# python -m tests.template_assert.test_blue_mood

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
