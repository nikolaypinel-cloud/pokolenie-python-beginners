"""
Тесты для задачи "Арифметические строки"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _05_strings.arithmetic_strings import solve

# Запуск теста:
# python -m tests.template_assert.test_arithmetic_strings

def test_arithmetic_strings():
    tests = [
        (["a", "bb", "ccc"], "YES"),       # 1, 2, 3
        (["a", "abc", "ab"], "YES"),       # 1, 2, 3
        (["", "a", "aa"], "YES"),          # 0, 1, 2
        (["", "", ""], "YES"),             # 0, 0, 0
        (["a", "bb", "abcd"], "NO"),       # 1, 2, 4
        (["a", "aa", "aaaa"], "NO"),       # 1, 2, 4
        (["abc", "def", "ghi"], "YES"),    # 3, 3, 3
        (["a", "bc", "def"], "YES"),       # 1, 2, 3
        (["hello", "world", "python"], "NO"),  # 5, 5, 6
        (["cat", "dog", "elephant"], "NO"),    # 3, 3, 8
    ]
    
    for i, (strings, expected) in enumerate(tests, 1):
        result = solve(strings)
        assert result == expected, f"Тест {i} провален: {strings} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: {strings} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_arithmetic_strings()
