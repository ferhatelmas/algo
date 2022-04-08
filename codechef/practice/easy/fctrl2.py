fac = [1]
n = 1
for x in range(1, 101):
    n *= x
    fac.append(n)

for _ in range(int(input())):
    print(fac[int(input())])
