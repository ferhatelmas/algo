s, p1, p2 = 2, 1, 2
while p2 < 4000000:
    p1, p2 = p2, p1 + p2
    if p2 % 2 == 0:
        s += p2
print(s)
