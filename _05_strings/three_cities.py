"""
Три города 🏙️
Определить самое короткое и самое длинное название города.
"""

# Решение
cities = [input() for _ in range(3)]
shortest = min(cities, key=len)
longest = max(cities, key=len)

print(shortest)
print(longest)
