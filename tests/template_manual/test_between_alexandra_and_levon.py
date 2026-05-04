"""
Тесты для задачи "Сколько ждать? ⏱️"
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    tests = [
        (["Александра", "Левон"], "0\n"),
        (["Александра", "Дмитрий", "Левон"], "1\n"),
        (["Александра", "Дмитрий", "Елена", "Левон"], "2\n"),
        (["Анна", "Александра", "Борис", "Левон", "Иван"], "1\n"),
        (["Александра", "Наталья", "Олег", "Петр", "Левон"], "3\n"),
        (["Александра", "Левон", "Игнат"], "0\n"),
    ]
    
    print("=== Тесты ===\n")
    all_passed = True
    script_path = Path(__file__).parent.parent.parent / "_08_while_loop" / "between_alexandra_and_levon.py"
    
    for i, (inputs, expected) in enumerate(tests, 1):
        result = subprocess.run(
            [sys.executable, str(script_path)],
            input="\n".join(inputs),
            capture_output=True,
            text=True,
        )
        output = result.stdout
        passed = output == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: {inputs}")
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
# python tests/template_manual/test_between_alexandra_and_levon.py