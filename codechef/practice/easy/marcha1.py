def is_balanced(d, m):
    if len(d) > 0 and d[0] == m:
        return True

    if len(d) > 1 and d[0] < m:
        return is_balanced(d[1:], m) or is_balanced(d[1:], m - d[0])


for _ in range(int(input())):
    [n, m] = [int(i) for i in input().split()]

    d = []
    for _ in range(n):
        i = int(input())
        if i <= m:
            d.append(i)
    d.sort()
    print("Yes" if is_balanced(d, m) else "No")
