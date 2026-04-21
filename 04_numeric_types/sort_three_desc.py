"""
Сортировка трёх 🔀
Упорядочить три числа от большего к меньшему.
"""

# Решение
a = int(input())
b = int(input())
c = int(input())

# Находим максимум, минимум и среднее
maximum = max(a, b, c)
minimum = min(a, b, c)
middle = a + b + c - maximum - minimum

print(maximum)
print(middle)
print(minimum)
