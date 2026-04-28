"""
До КОНЦА 1
Выводить слова до тех пор, пока не встретится слово «КОНЕЦ».
"""

def solve():
    words = []
    while (word := input()) != "КОНЕЦ":
        words.append(word)
    return words

if __name__ == "__main__":
    result = solve()
    print(*result, sep='\n')