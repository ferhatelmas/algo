voters = {}
for _ in range(sum(map(int, input().split()))):
    v = int(input())
    if v in voters:
        voters[v] += 1
    else:
        voters[v] = 1

r = sorted([k for (k, v) in voters.iteritems() if v > 1])
print(len(r))
for i in r:
    print(i)
