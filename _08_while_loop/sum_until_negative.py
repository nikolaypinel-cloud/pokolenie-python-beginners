def solve():
    total = 0
    while (num := int(input())) >= 0:
        total += num
    print(total)

if __name__ == "__main__":
    solve()