"""
Арифметические строки
Определить, можно ли из длин трёх строк построить арифметическую прогрессию.
"""

def solve(strings):
    a, b, c = sorted([len(s) for s in strings])
    return "YES" if b - a == c - b else "NO"

if __name__ == "__main__":
    strings = [input() for _ in range(3)]
    print(solve(strings))
