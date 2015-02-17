from sys import stdin


print '\n'.join(
    str(len(set(ln.split())))
    for i, ln in enumerate(stdin)
    if i and i % 2 == 0
)
