Пересечение отрезков [a1; b1] и [a2; b2].
Границы включительные.
Вывести:
- границы отрезка-пересечения
- или общую точку
- или "пустое множество"

# решение
# Решение
a1, b1, a2, b2 = [int(input()) for _ in range(4)]

left = max(a1, a2)
right = min(b1, b2)

if left > right:
    print("пустое множество")
elif left == right:
    print(left)
else:
    print(left, right)
