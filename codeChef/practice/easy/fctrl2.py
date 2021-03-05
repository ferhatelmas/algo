fac = [1]
n = 1
for x in range(1, 101):
    n *= x
    fac.append(n)

for _ in range(int(raw_input())):
    print fac[int(raw_input())]
