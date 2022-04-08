catalans = [1]
for i in range(0, 1001):
    catalans.append((2 * (2 * i + 1) * catalans[-1]) / (i + 2))

for _ in range(int(input())):
    print(catalans[int(input()) - 1] % 10000)
