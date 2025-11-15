
M = int(input())
a = input()
lis = a.split()
# print(lis)
a_new = set(list(map(int,lis)))
# print(a_new)

N = int(input())
b = input()
liss = b.split()
# print(lis)s
b_new = set(list(map(int,liss)))
# print(a_new)

c = list(a_new.symmetric_difference(b_new))
c.sort()
# print(c)



for i in c:
    print(i)

