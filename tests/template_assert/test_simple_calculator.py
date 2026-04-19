"""
Тесты для задачи "Самописный калькулятор 🌶️"
"""

def solve(a, b, op):
    if op == "+":
        return a + b
    elif op == "-":
        return a - b
    elif op == "*":
        return a * b
    elif op == "/":
        if b == 0:
            return "На ноль делить нельзя!"
        else:
            return a / b
    else:
        return "Неверная операция"

def test_simple_calculator():
    tests = [
        # Сложение
        (5, 3, "+", 8),
        (-2, 7, "+", 5),
        (0, 0, "+", 0),
        
        # Вычитание
        (10, 4, "-", 6),
        (3, 8, "-", -5),
        (0, 5, "-", -5),
        
        # Умножение
        (4, 6, "*", 24),
        (-3, 5, "*", -15),
        (0, 100, "*", 0),
        
        # Деление
        (10, 2, "/", 5.0),
        (7, 2, "/", 3.5),
        (-15, 3, "/", -5.0),
        
        # Деление на ноль
        (10, 0, "/", "На ноль делить нельзя!"),
        (0, 0, "/", "На ноль делить нельзя!"),
        
        # Неверная операция
        (5, 3, "%", "Неверная операция"),
        (5, 3, "**", "Неверная операция"),
        (5, 3, "abc", "Неверная операция"),
        (5, 3, "", "Неверная операция"),
    ]
    
    for i, (a, b, op, expected) in enumerate(tests, 1):
        result = solve(a, b, op)
        # Для сравнения чисел с плавающей точкой
        if isinstance(expected, float) and isinstance(result, float):
            assert abs(result - expected) < 1e-9, f"Тест {i} провален: {a} {op} {b} -> {result}, ожидалось {expected}"
        else:
            assert result == expected, f"Тест {i} провален: {a} {op} {b} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: {a} {op} {b} = {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_simple_calculator()
