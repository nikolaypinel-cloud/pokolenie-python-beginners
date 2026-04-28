"""
Цветовой микшер 🎨🌶️
Смешивание двух основных цветов (красный, синий, желтый).
"""

color1 = input()
color2 = input()

main_colors = {"красный", "синий", "желтый"}

if color1 not in main_colors or color2 not in main_colors:
    print("ошибка цвета")
elif color1 == color2:
    print(color1)
else:
    # Используем frozenset для неупорядоченной пары
    match frozenset({color1, color2}):
        case frozenset({"красный", "синий"}):
            print("фиолетовый")
        case frozenset({"красный", "желтый"}):
            print("оранжевый")
        case frozenset({"синий", "желтый"}):
            print("зеленый")
