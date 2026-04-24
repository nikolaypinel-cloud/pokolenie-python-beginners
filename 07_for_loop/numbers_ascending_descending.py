"""
Последовательность чисел 4 🌶️
Вывести числа от m до n:
- в порядке возрастания, если m < n
- в порядке убывания, если m >= n
"""

# Решение
m, n = (int(input()) for _ in range(2))
nums = range(m, n + 1) if m < n else range(m, n - 1, -1)
for num in nums: print(num)
