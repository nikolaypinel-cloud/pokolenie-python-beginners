"""
Тесты для задачи "Церемония взвешивания 🥊"
"""

def solve(weight):
    if weight < 60:
        return "Легкий вес"
    elif weight < 64:
        return "Первый полусредний вес"
    elif weight < 69:
        return "Полусредний вес"
    else:
        return "Не попадает в указанные категории"

def test_boxing_weight_class():
    tests = [
        # Лёгкий вес
        (50, "Легкий вес"),
        (59, "Легкий вес"),
        # Первый полусредний
        (60, "Первый полусредний вес"),
        (63, "Первый полусредний вес"),
        # Полусредний
        (64, "Полусредний вес"),
        (68, "Полусредний вес"),
        # Вне категорий
        (69, "Не попадает в указанные категории"),
        (100, "Не попадает в указанные категории"),
        (0, "Легкий вес"),
        (1, "Легкий вес"),
    ]
    
    for i, (weight, expected) in enumerate(tests, 1):
        result = solve(weight)
        assert result == expected, f"Тест {i} провален: weight={weight} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: weight={weight} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_boxing_weight_class()
