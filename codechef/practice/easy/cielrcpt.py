for _ in range(int(raw_input())):
    p = int(raw_input())
    cnt = p / 2048
    cnt += bin(p % 2048)[2:].count("1")
    print cnt
