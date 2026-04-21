"""
Арифметические строки
Определить, можно ли из длин трёх строк построить арифметическую прогрессию.
"""

# Решение
lengths = sorted([len(input()) for _ in range(3)])

if lengths[1] - lengths[0] == lengths[2] - lengths[1]:
    print("YES")
else:
    print("NO")
