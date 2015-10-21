def read_n(n):
    ls = []
    while len(ls) < n:
        line = input().rstrip()
        if line != "":
            ls.extend(line.split())
    return int(input()), ls


def my_zip(ls):
    return dict(zip(ls, range(len(ls))))


def get_cost(ls):
    d1, d2 = my_zip(ls), my_zip(sorted(ls))
    return sum(abs(d2[k] - v) for k, v in d1.items())


n, i = int(input()), 0
while n != 0:
    (n, ls), i = read_n(n), i + 1
    print("Site {}: {}".format(i, get_cost(ls)))
