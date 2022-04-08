"""
Correct but time limit, notatri.cpp is ok
"""
n = int(input())
while n != 0:
    p = sorted(map(int, input().split()))
    cnt = 0
    for i in range(n - 1, 1, -1):
        b, e = 0, i - 1
        while b < e:
            if p[i] > p[e] + p[b]:
                cnt += e - b
                b += 1
            else:
                e -= 1
    print(cnt)
    n = int(input())
