"""
Тесты для задачи "Цветовой микшер 🎨🌶️"
"""

def solve(color1, color2):
    main_colors = {"красный", "синий", "желтый"}
    
    if color1 not in main_colors or color2 not in main_colors:
        return "ошибка цвета"
    elif color1 == color2:
        return color1
    else:
        match frozenset({color1, color2}):
            case frozenset({"красный", "синий"}):
                return "фиолетовый"
            case frozenset({"красный", "желтый"}):
                return "оранжевый"
            case frozenset({"синий", "желтый"}):
                return "зеленый"

def test_color_mixer():
    tests = [
        ("красный", "синий", "фиолетовый"),
        ("синий", "красный", "фиолетовый"),
        ("красный", "желтый", "оранжевый"),
        ("желтый", "красный", "оранжевый"),
        ("синий", "желтый", "зеленый"),
        ("желтый", "синий", "зеленый"),
        ("красный", "красный", "красный"),
        ("синий", "синий", "синий"),
        ("желтый", "желтый", "желтый"),
        ("красный", "зеленый", "ошибка цвета"),
        ("фиолетовый", "синий", "ошибка цвета"),
        ("КРАСНЫЙ", "синий", "ошибка цвета"),
    ]
    
    for i, (c1, c2, expected) in enumerate(tests, 1):
        result = solve(c1, c2)
        assert result == expected, f"Тест {i} провален: ({c1}, {c2}) -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: ({c1}, {c2}) -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_color_mixer()
