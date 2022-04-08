for _ in range(int(input())):
    n = int(input())
    zeros = 0
    while n >= 5:
        n /= 5
        zeros += n
    print(zeros)
