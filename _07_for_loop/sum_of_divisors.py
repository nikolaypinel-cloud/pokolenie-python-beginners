"""
Сумма делителей
Вычислить сумму всех делителей натурального числа n.
"""

def solve(n):
    return sum(num for num in range(1, n // 2 + 1) if n % num == 0) + n

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
