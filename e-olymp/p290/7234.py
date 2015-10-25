a, b = map(int, input().split())
op = input()
if op == 'freeze':
    print(a if a < b else b)
elif op == 'heat':
    print(b if a < b else a)
elif op == 'auto':
    print(b)
else:
    print(a)
