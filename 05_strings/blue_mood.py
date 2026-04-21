"""
Цвет настроения синий 🟦
Вывести YES, если в строке есть подстрока «синий», иначе NO.
"""

def solve(s):
    return "YES" if "синий" in s else "NO"

if __name__ == "__main__":
    s = input()
    print(solve(s))
