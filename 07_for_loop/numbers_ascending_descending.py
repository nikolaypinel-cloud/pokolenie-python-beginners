"""
Последовательность чисел 4 🌶️
Вывести числа от m до n:
- в порядке возрастания, если m < n
- в порядке убывания, если m >= n
"""

def solve(m, n):
    nums = range(m, n + 1) if m < n else range(m, n - 1, -1)
    return list(nums)

if __name__ == "__main__":
    m, n = (int(input()) for _ in range(2))
    for num in solve(m, n):
        print(num)
