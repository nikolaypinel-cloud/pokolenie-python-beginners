"""
Последовательность Фибоначчи 🌶️
Вывести первые n чисел Фибоначчи (1, 1, 2, 3, 5, ...)
"""

def solve(n):
    if n == 1:
        return [1]
    fib = [1, 1]
    for i in range(2, n):
        fib.append(fib[-1] + fib[-2])
    return fib

if __name__ == "__main__":
    n = int(input())
    print(*solve(n))
