a, b = map(int, raw_input().split())
l = list(str(a-b))
l[0] = '1' if l[0] != '1' else '2'
print "".join(l)