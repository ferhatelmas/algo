a, n, k = map(int, raw_input().split())
n += 1

while a and k:
    print a % n,
    a /= n
    k -= 1

while k:
    print 0,
    k -= 1
print
