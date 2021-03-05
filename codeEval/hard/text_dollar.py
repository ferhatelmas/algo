import sys

ones = [
    "Zero",
    "One",
    "Two",
    "Three",
    "Four",
    "Five",
    "Six",
    "Seven",
    "Eight",
    "Nine",
    "Ten",
    "Eleven",
    "Twelve",
    "Thirteen",
    "Fourteen",
    "Fifteen",
    "Sixteen",
    "Seventeen",
    "Eighteen",
    "Nineteen",
]
twos = [
    "Ten",
    "Twenty",
    "Thirty",
    "Forty",
    "Fifty",
    "Sixty",
    "Seventy",
    "Eighty",
    "Ninety",
]
threes = [
    ("Hundred", 100, 1000),
    ("Thousand", 1000, 10 ** 6),
    ("Million", 10 ** 6, 10 ** 9),
]


def do_text_dollar(n):
    if n < 20:
        return ones[n]
    if n < 100:
        return twos[n / 10 - 1] + (ones[n % 10], "")[n % 10 == 0]
    for s, l, h in threes:
        if n >= l and n < h:
            return do_text_dollar(n / l) + s + (do_text_dollar(n % l), "")[n % l == 0]
    return "Unexpected larger value"


def get_text_dollar(n):
    return do_text_dollar(n) + "Dollars"


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print get_text_dollar(int(test.strip()))
test_cases.close()
