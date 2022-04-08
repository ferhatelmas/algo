import math


def isPrime(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True


s = input()
n = int(s)

if n >= 98690:
    print("1003001")
else:
    if n % 2 == 0:
        n += 1
        s = str(n)

    while not (s == s[::-1] and isPrime(n)):
        n += 2
        s = str(n)
    print(n)
