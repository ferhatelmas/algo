input()
c = v = 0
for t in map(int, input().split()):
    n = bin(t).count('1')
    if n > c:
        c, v = n, t
    elif n == c:
        v = min(v, t)
print(v)
