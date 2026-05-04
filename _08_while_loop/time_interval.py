h1, m1, h2, m2 = (int(input()) for _ in range(4))
# h1, m1, h2, m2 = map(int, open(0))  -- альтернатива первой строке

start = h1 * 60 + m1
end = h2 * 60 + m2

for t in range(start, end + 1):
    print(f"{t // 60:02d}:{t % 60:02d}")