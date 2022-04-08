for _ in range(int(input())):
    n = int(input())
    r = map(chr, (range(97, 123) * (n / 25)))
    if n % 25 > 0:
        r += map(chr, range(97, 98 + n % 25))
    r.reverse()
    print("".join(r))
