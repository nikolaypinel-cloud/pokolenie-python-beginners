"""
Знакочередующаяся сумма
Вычислить 1 - 2 + 3 - 4 + ... + (-1)^(n+1) * n
"""

def solve(num):
    return sum(range(1, num + 1, 2)) - sum(range(2, num + 1, 2))

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
