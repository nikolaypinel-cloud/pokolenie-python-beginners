"""
Наименьшее из четырёх чисел 🌶️
Программа определяет наименьшее из четырёх целых чисел.
"""

# Решение
a = int(input())
b = int(input())
c = int(input())
d = int(input())

min_num = a

if b < min_num:
    min_num = b
if c < min_num:
    min_num = c
if d < min_num:
    min_num = d

print(min_num)
