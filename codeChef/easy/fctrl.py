for _ in range(int(raw_input())):
	n = int(raw_input())
	zeros = 0
	while n >= 5:
		n /= 5
		zeros += n
	print zeros