for _ in range(int(input())):
    p = int(input())
    cnt = p / 2048
    cnt += bin(p % 2048)[2:].count("1")
    print(cnt)
