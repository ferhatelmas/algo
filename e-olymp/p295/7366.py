s = int(input())

d, s = divmod(s, 86400)
h, s = divmod(s, 3600)
m, s = divmod(s, 60)
print(d, h, m, s)
