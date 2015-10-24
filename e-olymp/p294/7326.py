c = m = 0
for e in input():
    if e == 'k':
        c += 1
        m = max(m, c)
    else:
        c = 0
print(m)
