"""
Тесты для задачи "Сумма чисел"
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    tests = [
        (["1", "2", "3", "-1"], "6\n"),
        (["10", "20", "30", "-5"], "60\n"),
        (["5", "-1"], "5\n"),
        (["-1"], "0\n"),
        (["0", "0", "0", "-1"], "0\n"),
        (["100", "200", "-100"], "300\n"),
    ]
    
    print("=== Тесты для задачи 'Сумма чисел' ===\n")
    all_passed = True
    script_path = Path(__file__).parent.parent.parent / "_08_while_loop" / "sum_until_negative.py"
    
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
# python tests/template_manual/test_sum_until_negative.py