"""
Сумма чисел
Подсчитать сумму n введённых чисел.
"""

def solve(number):
    total = sum(int(input()) for _ in range(number))
    return total

if __name__ == "__main__":
    print(solve(int(input())))
