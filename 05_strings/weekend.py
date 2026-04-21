"""
Отдыхаем ли? 😎
Вывести YES, если в строке есть «суббота» или «воскресенье», иначе NO.
"""

def solve(s):
    return "YES" if "суббота" in s or "воскресенье" in s else "NO"

if __name__ == "__main__":
    s = input()
    print(solve(s))
