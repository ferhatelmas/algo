import sys


ls = [1, 1]
for i in range(2, 60):
    ls.append((ls[i - 1] + ls[i - 2]) % 10)


for ln in sys.stdin:
    print(ls[int(ln) % 60])
