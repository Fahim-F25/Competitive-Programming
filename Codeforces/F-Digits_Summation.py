n , m = map(int, input().split())

def last_digit(l):
    return l % 10

n1 = last_digit(n)
m1 = last_digit(m)
print(n1 + m1)