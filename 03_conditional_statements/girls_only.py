Girls only 👧
Футбольная команда набирает девочек от 10 до 15 лет включительно.
Пол: f (женщина) или m (мужчина).
Вывести «YES», если подходит, иначе «NO».

# Решение
age = int(input())
gender = input()

if 10 <= age <= 15 and gender == 'f':
    print("YES")
else:
    print("NO")
