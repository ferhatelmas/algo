n, k = map(int, input().split())
ls = [False] * n
for _ in range(k):
    s = input()
    if s.startswith("CLICK"):
        i = int(s.split()[1]) - 1
        ls[i] = not ls[i]
    else:
        ls = [False] * n
    print(sum(ls))
