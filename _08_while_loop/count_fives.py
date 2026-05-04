def solve():
    counter = 0
    while 1 <= (num := int(input())) <= 5:
        if num == 5:
            counter += 1
    print(counter)

if __name__ == "__main__":
    solve()