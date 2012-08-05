[n, k] = [int(x) for x in raw_input().split()]

nums = []
for _ in range(int(n)):
	nums.append(raw_input())

cnt = 0
for num in nums:	
	if int(num)%k == 0:
		cnt += 1 
print cnt