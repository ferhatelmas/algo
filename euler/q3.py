n = 600851475143

d = 2
while n > 1:
    while n % d == 0:
        n //= d
    d += 1

print(d - 1)
