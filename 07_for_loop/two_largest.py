"""
Наибольшие числа 🌶️
Найти два наибольших различных числа в последовательности.
"""

def solve(numbers):
    numbers.sort()
    return numbers[-1], numbers[-2]

if __name__ == "__main__":
    n = int(input())
    numbers = [int(input()) for _ in range(n)]
    first, second = solve(numbers)
    print(first)
    print(second)
