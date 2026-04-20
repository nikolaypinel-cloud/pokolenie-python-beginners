"""
Тесты для задачи "Обратное число"
"""

def solve(x):
    if x == 0:
        return "Обратного числа не существует"
    else:
        return 1 / x

def test_reciprocal():
    tests = [
        (0, "Обратного числа не существует"),
        (2, 0.5),
        (4, 0.25),
        (-5, -0.2),
        (1, 1.0),
        (-1, -1.0),
        (0.5, 2.0),
        (-0.2, -5.0),
    ]
    
    for i, (x, expected) in enumerate(tests, 1):
        result = solve(x)
        
        # Для чисел с плавающей точкой используем приближённое сравнение
        if isinstance(expected, float) and isinstance(result, float):
            assert abs(result - expected) < 1e-9, f"Тест {i} провален: x={x} -> {result}, ожидалось {expected}"
        else:
            assert result == expected, f"Тест {i} провален: x={x} -> {result}, ожидалось {expected}"
        
        print(f"✅ Тест {i} пройден: x={x} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_reciprocal()
