"""
Тесты для задачи "Квадратное уравнение 🌶️🌶️"
"""

import sys

from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent.parent))

from _06_math_module.quadratic_equation import solve

import math

# Запуск теста:
# python -m tests.template_assert.test_quadratic_equation

def test_quadratic_equation():
    tests = [
        (1, -3, 2, "1.0\n2.0"),           # D > 0, два корня
        (1, -2, 1, "1.0"),                 # D = 0, один корень
        (1, 0, 1, "Нет корней"),           # D < 0, нет корней
        (2, -4, 2, "1.0"),                 # D = 0
        (1, -5, 6, "2.0\n3.0"),            # D > 0
        (-1, 3, -2, "1.0\n2.0"),           # a < 0
        (0.5, -2, 2, "2.0"),               # D = 0, дробные
        (2, 5, 2, "-2.0\n-0.5"),           # D > 0, отрицательные корни
    ]
    
    for i, (a, b, c, expected) in enumerate(tests, 1):
        result = solve(a, b, c)
        
        # Для случая с одним корнем — ожидается строка без \n
        # Для двух корней — сравниваем строки
        if isinstance(expected, str) and '\n' in expected:
            # Разбиваем ожидаемые и полученные корни
            exp_roots = sorted(float(x) for x in expected.split('\n'))
            res_roots = sorted(float(x) for x in result.split('\n'))
            assert len(res_roots) == len(exp_roots), f"Тест {i}: разное количество корней"
            assert all(abs(r - e) < 1e-9 for r, e in zip(res_roots, exp_roots)), \
                f"Тест {i} провален: a={a}, b={b}, c={c} -> {result}, ожидалось {expected}"
        else:
            # Для одного корня или "Нет корней" — прямое сравнение
            if expected == "Нет корней":
                assert result == expected, f"Тест {i} провален: a={a}, b={b}, c={c} -> {result}, ожидалось {expected}"
            else:
                # Сравниваем числа с учётом погрешности
                res_float = float(result)
                exp_float = float(expected)
                assert abs(res_float - exp_float) < 1e-9, \
                    f"Тест {i} провален: a={a}, b={b}, c={c} -> {result}, ожидалось {expected}"
        
        print(f"✅ Тест {i} пройден: a={a}, b={b}, c={c} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_quadratic_equation()
