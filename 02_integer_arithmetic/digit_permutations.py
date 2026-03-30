"""
Перестановка цифр
Дано трёхзначное число с разными цифрами.
Вывести все 6 перестановок цифр в порядке:
abc, acb, bac, bca, cab, cba
"""

# Решение
num = int(input())
a = num // 100
b = (num // 10) % 10
c = num % 10

print(a, b, c, sep="")
print(a, c, b, sep="")
print(b, a, c, sep="")
print(b, c, a, sep="")
print(c, a, b, sep="")
print(c, b, a, sep="")
