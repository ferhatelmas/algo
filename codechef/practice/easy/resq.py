for _ in range(int(input())):
    n = int(input())

    m = n
    for a in range(1, int(n**0.5 + 1)):
        if n % a == 0:
            b = n / a
            m = min(m, abs(a - b))

    print(m)
