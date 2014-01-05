import sys

def predict(n):
    return bin(n)[2:].count('1')%3

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    print predict(int(test))
test_cases.close()
