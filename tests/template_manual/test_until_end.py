"""
Тесты для задачи "До КОНЦА 1"
"""

from until_end import solve
import sys
from io import StringIO

def run_tests():
    tests = [
        (["привет", "мир", "КОНЕЦ"], ["привет", "мир"]),
        (["КОНЕЦ"], []),
        (["один", "два", "три", "КОНЕЦ", "четыре"], ["один", "два", "три"]),
        (["python", "while", "КОНЕЦ", "ignore"], ["python", "while"]),
    ]
    
    print("=== Тесты для задачи 'До КОНЦА 1' ===\n")
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