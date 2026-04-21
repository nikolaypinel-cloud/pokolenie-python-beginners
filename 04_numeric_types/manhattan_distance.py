"""
Манхэттенское расстояние ↔️
Расстояние между двумя точками на плоскости: |p1 - q1| + |p2 - q2|
"""

# Решение
p1 = int(input())
p2 = int(input())
q1 = int(input())
q2 = int(input())

distance = abs(p1 - q1) + abs(p2 - q2)
print(distance)
