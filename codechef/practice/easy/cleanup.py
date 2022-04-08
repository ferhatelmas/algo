for _ in range(int(input())):
    n, m = input().split()
    f = map(int, input().split())
    f.sort()

    fi = range(1, int(n) + 1)
    for i in f:
        fi.remove(i)

    l = len(fi)
    print(" ".join(map(str, [fi[i] for i in range(0, l, 2)])))
    print(" ".join(map(str, [fi[i] for i in range(1, l, 2)])))
