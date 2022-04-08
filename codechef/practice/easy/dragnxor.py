for _ in range(int(input())):
    n, a, b = map(int, input().split())
    a1, b1 = bin(a)[2:].count("1"), bin(b)[2:].count("1")
    cnt = min(a1, n - b1) + min(n - a1, b1)
    print(int("1" * cnt + "0" * (n - cnt), 2))
