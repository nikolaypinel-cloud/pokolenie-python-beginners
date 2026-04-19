"""
Тесты для задачи "Количество дней 📅"
"""

def solve(month):
    if month == 2:
        return 28
    elif month in (4, 6, 9, 11):
        return 30
    else:
        return 31

def test_days_in_month():
    tests = [
        (1, 31),   # январь
        (2, 28),   # февраль
        (3, 31),   # март
        (4, 30),   # апрель
        (5, 31),   # май
        (6, 30),   # июнь
        (7, 31),   # июль
        (8, 31),   # август
        (9, 30),   # сентябрь
        (10, 31),  # октябрь
        (11, 30),  # ноябрь
        (12, 31),  # декабрь
    ]
    
    for i, (month, expected) in enumerate(tests, 1):
        result = solve(month)
        assert result == expected, f"Тест {i} провален: month={month} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: month={month} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_days_in_month()
