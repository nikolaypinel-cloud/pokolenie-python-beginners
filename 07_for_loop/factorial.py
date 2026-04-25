"""
Факториал ❗
Вычислить n! = 1 × 2 × 3 × ... × n
"""

def solve(n):
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial

if __name__ == "__main__":
    n = int(input())
    print(solve(n))
