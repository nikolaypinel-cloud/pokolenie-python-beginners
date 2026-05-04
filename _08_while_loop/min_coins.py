price = int(input())
coins = 0
for nominal in (25, 10, 5, 1):
    coins += price // nominal
    price %= nominal
print(coins)