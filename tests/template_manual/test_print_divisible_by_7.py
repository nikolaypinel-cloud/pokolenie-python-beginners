"""
Тесты для задачи "Пока делимся"
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    tests = [
        (["7", "14", "21", "3"], "7\n14\n21\n"),
        (["7", "3"], "7\n"),
        (["14", "28", "42", "5"], "14\n28\n42\n"),
        (["7", "7", "7", "7", "0"], "7\n7\n7\n7\n"),
        (["3"], ""),
    ]
    
    print("=== Тесты для задачи 'Пока делимся' ===\n")
    all_passed = True
    script_path = Path(__file__).parent.parent.parent / "_08_while_loop" / "print_divisible_by_7.py"
    
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
