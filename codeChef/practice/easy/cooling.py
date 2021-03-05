for _ in xrange(int(raw_input())):
    l = int(raw_input())
    pies = sorted(map(int, raw_input().split()))
    racks = sorted(map(int, raw_input().split()))

    i, j = 0, 0
    while i < l and j < l:
        if pies[i] <= racks[j]:
            i += 1
        j += 1

    print i
