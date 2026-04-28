"""
Тесты для задачи "Количество членов"
"""

import sys
from io import StringIO
from pathlib import Path

# Добавляем корень проекта в путь поиска модулей
sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _08_while_loop.count_until_stop import solve

def run_tests():
    tests = [
        (["привет", "мир", "стоп"], 2),
        (["hello", "world", "хватит"], 2),
        (["один", "два", "три", "достаточно"], 3),
        (["стоп"], 0),
        (["хватит"], 0),
        (["достаточно"], 0),
        (["python", "while", "стоп", "ignore"], 2),
        (["Кстоп", "стоп"], 1),   # не стоп-слово, затем стоп
    ]
    
    print("=== Тесты для задачи 'Количество членов' ===\n")
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