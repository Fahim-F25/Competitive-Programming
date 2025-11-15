n = int(input())
roll_n = set(map(int,input().split()))

b = int(input())
roll_b = set(map(int,input().split()))

c = roll_n.union(roll_b)
# print(c)
print(len(c))