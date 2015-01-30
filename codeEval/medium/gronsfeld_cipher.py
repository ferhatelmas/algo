import sys

alphabet = (' !"#$%&\'()*+,-./0123456789:<=>?@'
            'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz')
l = len(alphabet)


def decrypt(k, s):
    return ''.join(
        alphabet[(alphabet.index(e) - int(i) + l) % l]
        for i, e in zip(k * ((len(s) / len(k)) + 1), s)
    )


with open(sys.argv[1], 'r') as f:
    for test in f:
        print decrypt(*test.rstrip().split(';', 1))
