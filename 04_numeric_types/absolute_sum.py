"""
Абсолютная сумма
Вычислить сумму модулей пяти чисел.
"""

# Решение
numbers = [int(input()) for _ in range(5)]
total = sum(abs(num) for num in numbers)
print(total)
