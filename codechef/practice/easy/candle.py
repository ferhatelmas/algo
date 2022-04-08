for _ in range(int(input())):
    candles = map(int, input().split())

    m1 = min(candles)
    i1 = candles.index(m1)

    if i1 == 0:
        candles.remove(m1)
        m2 = min(candles)
        i2 = candles.index(m2) + 1
        if m1 == m2:
            print(str(i2) * (m2 + 1))
        else:
            print("1" + "0" * (m1 + 1))
    else:
        print(str(i1) * (m1 + 1))
