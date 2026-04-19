"""
Тесты для задачи "Високосный год 📅"
"""

def solve(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return "YES"
    else:
        return "NO"

def test_leap_year():
    tests = [
        # Високосные
        (2020, "YES"),   # кратен 4, не кратен 100
        (2000, "YES"),   # кратен 400
        (1600, "YES"),   # кратен 400
        (4, "YES"),      # кратен 4
        
        # Не високосные
        (2021, "NO"),    # не кратен 4
        (1900, "NO"),    # кратен 100, но не кратен 400
        (2100, "NO"),    # кратен 100, но не кратен 400
        (1, "NO"),       # не кратен 4
        (100, "NO"),     # кратен 100, но не кратен 400
    ]
    
    for i, (year, expected) in enumerate(tests, 1):
        result = solve(year)
        assert result == expected, f"Тест {i} провален: year={year} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: year={year} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_leap_year()
