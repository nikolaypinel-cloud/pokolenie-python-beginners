"""
Тесты для задачи "Количество пятёрок 5️⃣"
"""

import subprocess
import sys
from pathlib import Path

def run_tests():
    tests = [
        (["5", "5", "5", "3", "5", "0"], "4\n"),
        (["5", "4", "3", "2", "1", "-1"], "1\n"),
        (["5", "5", "6"], "2\n"),
        (["5", "5", "5", "5", "5", "0"], "5\n"),
        (["2", "4", "3", "0"], "0\n"),
        (["5", "5", "5", "1"], "3\n"),
        (["-1"], "0\n"),
    ]
    
    print("=== Тесты для задачи 'Количество пятёрок 5️⃣' ===\n")
    all_passed = True
    script_path = Path(__file__).parent.parent.parent / "_08_while_loop" / "count_fives.py"
    
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
# python tests/template_manual/test_count_fives.py