from sys import argv


def convert_to_title(num):
    ls = []
    while num:
        num, i = divmod(num, 26)
        if i == 0 and num > 0:
            num -= 1
            i = 26
        ls.append(chr(ord('A') - 1 + i))
    return ''.join(reversed(ls))


with open(argv[1], 'r') as test_cases:
    for test in test_cases:
        print(convert_to_title(int(test)))
