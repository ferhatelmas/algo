def my_sum(s):
    return sum(ord(e) - ord("0") for e in s)


def digital_root(s):
    n = my_sum(s)
    while n > 9:
        n = my_sum(str(n))
    return n, int(s)


print(" ".join(sorted(input().split(), key=digital_root)))
