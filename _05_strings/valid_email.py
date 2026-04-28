"""
Корректный email 📧
Вывести YES, если в строке есть '@' и '.', иначе NO.
"""

def solve(s):
    return "YES" if '@' in s and '.' in s else "NO"

if __name__ == "__main__":
    s = input()
    print(solve(s))
