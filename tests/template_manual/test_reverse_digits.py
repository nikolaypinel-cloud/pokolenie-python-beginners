"""
Тесты для задачи "Обратный порядок 1"
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    tests = [
        ("123", "3\n2\n1\n"),
        ("234", "4\n3\n2\n"),
        ("100", "0\n0\n1\n"),
        ("1", "1\n"),
        ("10", "0\n1\n"),
        ("100500", "0\n0\n5\n0\n0\n1\n"),
    ]
    
    print("=== Тесты ===\n")
    all_passed = True
    script_path = Path(__file__).parent.parent.parent / "_08_while_loop" / "reverse_digits.py"
    
    for i, (num, expected) in enumerate(tests, 1):
        result = subprocess.run(
            [sys.executable, str(script_path)],
            input=num,
            capture_output=True,
            text=True,
        )
        output = result.stdout
        passed = output == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: num={num}")
        if not passed:
            print(f"   Результат: {repr(output)}")
            print(f"   Ожидалось: {repr(expected)}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()

# Запуск теста:
# python tests/template_manual/test_reverse_digits.py