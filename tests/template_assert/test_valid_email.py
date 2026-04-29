"""
Тесты для задачи "Корректный email 📧"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _05_strings.valid_email import solve

# Запуск теста:
# python -m tests.template_assert.test_valid_email


def test_valid_email():
    tests = [
        ("user@example.com", "YES"),
        ("test@mail.ru", "YES"),
        ("my.email@domain.org", "YES"),
        ("@domain.com", "YES"),           # есть @ и .
        ("user@.com", "YES"),             # есть @ и .
        ("user@domain", "NO"),            # нет точки
        ("user.domain.com", "NO"),        # нет @
        ("user@", "NO"),                  # нет точки
        (".com", "NO"),                   # нет @
        ("", "NO"),
        ("@.", "YES"),                    # минимальный случай
        ("abc", "NO"),
    ]
    
    for i, (s, expected) in enumerate(tests, 1):
        result = solve(s)
        assert result == expected, f"Тест {i} провален: '{s}' -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: '{s}' -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_valid_email()
