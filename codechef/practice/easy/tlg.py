from math import fabs

x = 0
y = 0
lv = 0
l = 0
for _ in range(int(input())):
    scores = [int(score) for score in input().split()]
    x += scores[0]
    y += scores[1]

    lead = fabs(x - y)
    if lead > lv:
        lv = lead
        l = 1 if x > y else 2

print("%d %d" % (l, lv))
