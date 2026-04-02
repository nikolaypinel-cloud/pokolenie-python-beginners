"""
Только +
Программа считывает три числа и подсчитывает сумму только положительных чисел.
Если положительных чисел нет, выводит 0.
"""

# Решение
a = int(input())
b = int(input())
c = int(input())

total = 0

if a > 0:
    total += a
if b > 0:
    total += b
if c > 0:
    total += c

print(total)
