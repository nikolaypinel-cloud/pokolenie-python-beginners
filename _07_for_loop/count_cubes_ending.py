"""
Количество чисел
Подсчитать количество чисел в диапазоне [a, b], куб которых оканчивается на 4 или 9.
"""

def solve(a, b):
    return sum(1 for i in range(a, b + 1) if i**3 % 10 == 4 or i**3 % 10 == 9)

if __name__ == "__main__":
    a = int(input())
    b = int(input())
    print(solve(a, b))
