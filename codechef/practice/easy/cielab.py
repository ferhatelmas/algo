a, b = map(int, input().split())
l = list(str(a - b))
l[0] = "1" if l[0] != "1" else "2"
print("".join(l))
