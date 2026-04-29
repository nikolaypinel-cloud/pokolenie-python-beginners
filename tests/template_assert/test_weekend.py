"""
Тесты для задачи "Отдыхаем ли? 😎"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _05_strings.weekend import solve

# Запуск теста:
# python -m tests.template_assert.test_weekend


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
