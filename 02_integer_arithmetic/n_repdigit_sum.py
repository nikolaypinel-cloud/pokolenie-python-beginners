"""
Размножение n-ок
Вычислить n + nn + nnn, где n — цифра от 1 до 9.
Без использования строк.
"""

# Решение
n = int(input())
nn = n * 10 + n
nnn = n * 100 + n * 10 + n

result = n + nn + nnn
print(result)
