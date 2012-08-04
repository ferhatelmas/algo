[x, y] = raw_input().split()
x = int(x)
y = float(y)

if x%5 == 0: 
	n = y-x-0.50
	if n >= 0:
		print "%.2f" % n
	else:
		print "%.2f" % y
else:
	print "%.2f" % y