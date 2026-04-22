"""
Тесты для задачи "Площадь и длина"
"""

from circle_area_length import solve
import math

def test_circle_area_length():
    tests = [
        (1, math.pi, 2 * math.pi),
        (2, 4 * math.pi, 4 * math.pi),
        (3, 9 * math.pi, 6 * math.pi),
        (0, 0.0, 0.0),
        (0.5, 0.25 * math.pi, math.pi),
    ]
    
    for i, (R, expected_area, expected_circ) in enumerate(tests, 1):
        area, circ = solve(R)
        assert abs(area - expected_area) < 1e-9, f"Тест {i} провален: R={R} -> area={area}, ожидалось {expected_area}"
        assert abs(circ - expected_circ) < 1e-9, f"Тест {i} провален: R={R} -> circ={circ}, ожидалось {expected_circ}"
        print(f"✅ Тест {i} пройден: R={R} -> area={area}, circ={circ}")
    
    print("\n🎉 Все тесты пройдены!")

if __name__ == "__main__":
    test_circle_area_length()
