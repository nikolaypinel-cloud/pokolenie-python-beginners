"""
YES or NO – вот в чём вопрос ❓
Нечётное → YES
Чётное от 2 до 5 включительно → NO
Чётное от 6 до 20 включительно → YES
Чётное больше 20 → NO
"""

# Решение
num = int(input())
if (num % 2) or (num % 2 == 0 and 6 <= num <= 20):
    print('YES')
else:
    print('NO')
