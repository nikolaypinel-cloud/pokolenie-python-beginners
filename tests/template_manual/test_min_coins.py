"""
Тесты для задачи "Ведьмаку заплатите чеканной монетой 💰"
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    tests = [
        ("1", "1\n"),
        ("5", "1\n"),
        ("6", "2\n"),
        ("10", "1\n"),
        ("11", "2\n"),
        ("25", "1\n"),
        ("26", "2\n"),
        ("30", "2\n"),
        ("99", "9\n"),
        ("100", "4\n"),
    ]
    
    print("=== Тесты ===\n")
    all_passed = True
    script_path = Path(__file__).parent.parent.parent / "_08_while_loop" / "min_coins.py"
    
    for i, (price, expected) in enumerate(tests, 1):
        result = subprocess.run(
            [sys.executable, str(script_path)],
            input=price,
            capture_output=True,
            text=True,
        )
        output = result.stdout
        passed = output == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: price={price}")
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
# python tests/template_manual/test_min_coins.py