"""
Тесты для задачи "Dog age 🐶"
"""

def solve(n):
    if n <= 2:
        return n * 10.5
    else:
        return 2 * 10.5 + (n - 2) * 4

def test_dog_age():
    tests = [
        (1, 10.5),
        (2, 21.0),
        (3, 25.0),
        (4, 29.0),
        (5, 33.0),
        (10, 53.0),
        (15, 73.0),
    ]
    
    for i, (n, expected) in enumerate(tests, 1):
        result = solve(n)
        assert abs(result - expected) < 1e-9, f"Тест {i} провален: n={n} -> {result}, ожидалось {expected}"
        print(f"✅ Тест {i} пройден: n={n} -> {result}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_dog_age()
