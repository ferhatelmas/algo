def s(k):
    n = 0
    while k > 0:
        n, k = 2 * (n + 1), k - 1
    return n / 2


n = int(input())
while n > 0:
    print(s(int(input())))
    n -= 1
