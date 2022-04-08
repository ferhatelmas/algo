t = int(input())
while t:
    t -= 1
    n = int(input())
    m = float(n)
    print(sum(m / j for j in range(1, n + 1)))
