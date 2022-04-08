[n, k] = [int(x) for x in input().split()]

nums = []
for _ in range(int(n)):
    nums.append(input())

cnt = 0
for num in nums:
    if int(num) % k == 0:
        cnt += 1
print(cnt)
