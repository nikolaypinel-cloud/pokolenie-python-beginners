"""
Тесты для задачи "До КОНЦА 2"
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _08_while_loop.until_end_case_insensitive import solve
from io import StringIO

def run_tests():
    tests = [
        (["привет", "мир", "КОНЕЦ"], ["привет", "мир"]),
        (["hello", "world", "конец"], ["hello", "world"]),
        (["КОНЕЦ"], []),
        (["конец"], []),
        (["один", "два", "три", "КОНЕЦ", "четыре"], ["один", "два", "три"]),
        (["python", "while", "конец", "ignore"], ["python", "while"]),
        (["Конец"], ["Конец"]),  # не должно завершить цикл (только КОНЕЦ или конец)
        (["КОНЕЦ", "конец"], []),
    ]
    
    print("=== Тесты для задачи 'До КОНЦА 2' ===\n")
    all_passed = True
    
    for i, (inputs, expected) in enumerate(tests, 1):
        # Подменяем stdin
        original_stdin = sys.stdin
        sys.stdin = StringIO("\n".join(inputs))
        
        result = solve()
        
        # Восстанавливаем stdin
        sys.stdin = original_stdin
        
        passed = result == expected
        all_passed = all_passed and passed
        status = "✅" if passed else "❌"
        print(f"{status} Тест {i}: inputs={inputs}")
        if not passed:
            print(f"   Результат: {result}")
            print(f"   Ожидалось: {expected}\n")
    
    if all_passed:
        print("🎉 Все тесты пройдены!")
    else:
        print("❌ Некоторые тесты не пройдены.")

if __name__ == "__main__":
    run_tests()

# Запуск теста:
# python -m tests.template_manual.test_until_end_case_insensitive