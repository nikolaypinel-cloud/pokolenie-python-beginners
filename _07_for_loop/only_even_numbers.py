"""
Only even numbers
Проверить, все ли 10 чисел чётные.
"""

# Возвращает True, если все числа чётные, иначе False
def solve(numbers):
    for number in numbers:
        if number % 2:
            return False
    return True

if __name__ == "__main__":
    nums = tuple(int(input()) for _ in range(10))
    print('YES' if solve(nums) else 'NO')
