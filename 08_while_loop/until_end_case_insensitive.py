"""
До КОНЦА 2
Выводить слова до тех пор, пока не встретится слово «КОНЕЦ» или «конец».
"""

def solve():
    words = []
    while (word := input()) not in ("КОНЕЦ", "конец"):
        words.append(word)
    return words

if __name__ == "__main__":
    result = solve()
    print(*result, sep='\n')