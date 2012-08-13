while(int(raw_input()) != 0):
	p = [int(x) for x in raw_input().split()]
	ip = [1 for _ in range(len(p))]
	i = 1
	for e in p:
		ip[e-1] = i
		i += 1

	print "ambiguous" if p == ip else "not ambiguous"