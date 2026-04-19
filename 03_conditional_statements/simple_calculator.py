"""
Самописный калькулятор 🌶️
Выполнить арифметическую операцию (+, -, *, /) над двумя числами.
Обработать деление на ноль и неверную операцию.
"""

# Решение
num1 = int(input())
num2 = int(input())
op = input()

match op:
    case '+':
        print(num1 + num2)
    case '-':
        print(num1 - num2)
    case '*':
        print(num1 * num2)
    case '/':
        if num2 == 0:
            print("На ноль делить нельзя!")
        else:
            print(num1 / num2)
    case _:
        print("Неверная операция")
