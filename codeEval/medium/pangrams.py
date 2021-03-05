import sys, string

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    s = test.lower()
    s = filter(lambda x: x not in s, string.ascii_lowercase)
    if s:
        print s
    else:
        print "NULL"
test_cases.close()
