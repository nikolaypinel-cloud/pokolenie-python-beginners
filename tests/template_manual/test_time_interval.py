"""
Тесты для задачи "Временной промежуток ⏱️"
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    tests = [
        (["1", "0", "1", "5"], "01:00\n01:01\n01:02\n01:03\n01:04\n01:05\n"),
        (["23", "55", "23", "59"], "23:55\n23:56\n23:57\n23:58\n23:59\n"),
        (["0", "0", "0", "3"], "00:00\n00:01\n00:02\n00:03\n"),
        (["9", "30", "9", "32"], "09:30\n09:31\n09:32\n"),
        (["12", "0", "12", "0"], "12:00\n"),
    ]
    
    print("=== Тесты ===\n")
    all_passed = True
    script_path = Path(__file__).parent.parent.parent / "_08_while_loop" / "time_interval.py"
    
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
# python tests/template_manual/test_time_interval.py