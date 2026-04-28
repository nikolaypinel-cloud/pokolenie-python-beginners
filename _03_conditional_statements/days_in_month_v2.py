"""
Количество дней 📅 (версия без in)
Вывести количество дней в месяце (год невисокосный).
"""

# Решение
month = int(input())

if month == 2:
    print(28)
elif month == 4 or month == 6 or month == 9 or month == 11:
    print(30)
else:
    print(31)
  # Тест тот же самый, что и для days_in_month
