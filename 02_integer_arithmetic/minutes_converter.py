"""
Пересчёт временного интервала ⌚
Программа переводит минуты в часы и минуты.
Формат: X мин - это Y час Z минут.
"""

# Решение
minutes = int(input())
hours = minutes // 60
remaining_minutes = minutes % 60
print(minutes, "мин - это", hours, "час", remaining_minutes, "минут.")
