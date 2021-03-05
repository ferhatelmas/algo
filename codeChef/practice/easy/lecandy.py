from sys import stdin


for i, ln in enumerate(stdin):
    if i == 0:
        continue
    if i % 2:
        _, c = map(int, ln.split())
    else:
        print("Yes", "No")[c < sum(map(int, ln.split()))]
