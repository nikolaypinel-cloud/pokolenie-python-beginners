"""
Без нулей 0️
Вычислить произведение 10 чисел, игнорируя нули.
"""

def solve(numbers):
    product = 1
    for num in numbers:
        if num != 0:
            product *= num
    return product

if __name__ == "__main__":
    numbers = [int(input()) for _ in range(10)]
    print(solve(numbers))
