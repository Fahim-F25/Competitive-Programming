from collections import Counter

# Number of shoes
x = int(input())
# List of shoe sizes
sizes = list(map(int, input().split()))
# Counter of shoe sizes
stock = Counter(sizes)
# print(stock)



# Number of customers
n = int(input())
earnings = 0

for _ in range(n):
    size, price = map(int, input().split())
    if stock[size] > 0:   # Shoe available
        earnings += price
        stock[size] -= 1  # Reduce stock

print(earnings)
