for _ in range(int(input())):
    l = int(input())
    pies = sorted(map(int, input().split()))
    racks = sorted(map(int, input().split()))

    i, j = 0, 0
    while i < l and j < l:
        if pies[i] <= racks[j]:
            i += 1
        j += 1

    print(i)
