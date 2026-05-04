"""
Тесты для задачи "Первый никнейм 👉"
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    tests = [
        (["alice", "bob_", "charlie"], "alice\n"),
        (["_alice", "bob", "charlie"], "bob\n"),
        (["__alice__", "bob_", "charlie"], "charlie\n"),
        ]
    
    print("=== Тесты для задачи 'Первый никнейм 👉' ===\n")
    all_passed = True
    script_path = Path(__file__).parent.parent.parent / "_08_while_loop" / "first_nickname.py"
    
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
        print(f"{status} Тест {i}: inputs={inputs}")
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
# python tests/template_manual/test_first_nickname.py