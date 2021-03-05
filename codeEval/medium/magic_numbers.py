from sys import argv


def is_magic(s):
    l = len(s)
    if len(set(s)) != l:
        return False
    visited = set()
    a = b = s[0]
    j = 0
    while b not in visited:
        visited.add(b)
        j = (int(b) + j) % l
        b = s[j]
    return a == b and len(visited) == l


magic = {}
for i in range(1, 10001):
    magic[i] = is_magic(str(i))


with open(argv[1], "r") as test_cases:
    for test in test_cases:
        a, b = map(int, test.split())
        r = " ".join(str(i) for i in range(a, b + 1) if magic[i])
        print(-1 if r == "" else r)
