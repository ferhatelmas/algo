def is_valid(levels, n):
    stem = 0
    for i in range(n):
        stem += levels[i]
        if stem % 2 != 0:
            if stem == 1 and i == n - 1:
                return "Yes"
            else:
                return "No"
        stem /= 2
    return "No"


for _ in range(int(input())):
    n = int(input())
    levels = map(int, input().split())
    levels.reverse()
    print(is_valid(levels, n))
