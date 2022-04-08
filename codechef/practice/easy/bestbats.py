import math

for _ in range(int(input())):
    scores, k = sorted(map(int, input().split()), reverse=True), int(input())
    mscores = scores[:k]

    n, m = mscores.count(mscores[-1]), scores.count(mscores[-1])
    print(math.factorial(m) / (math.factorial(n) * math.factorial(m - n)))
