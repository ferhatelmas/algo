import sys

test_cases = open(sys.argv[1], "r")
for i, test in enumerate(test_cases):
    test = test.rstrip()
    if i == 0:
        j = test.index("_")
        print test[:j] + "|" + test[j + 1 :]
    else:
        try:
            k = test.index("C")
        except:
            k = test.index("_")
        if k < j:
            j = k
            k = "/"
        elif k == j:
            k = "|"
        else:
            j = k
            k = "\\"
        print test[:j] + k + test[j + 1 :]
test_cases.close()
