"""
Количество членов
Подсчитать количество слов до стоп-слов: «стоп», «хватит», «достаточно».
"""

def solve():
    count = 0
    while (word := input()) not in ("стоп", "хватит", "достаточно"):
        count += 1
    return count

if __name__ == "__main__":
    print(solve())