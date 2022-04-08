t = int(raw_input())
while t:
    t -= 1
    n = int(raw_input())
    m = float(n)
    print(sum(m / j for j in range(1, n + 1)))
