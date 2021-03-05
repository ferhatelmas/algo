import sys


def my_eval(ls):
    ops, args = [], []
    for e in reversed(ls):
        (args, ops)[e in "*/+"].append(e)
    return do_my_eval(ops, map(int, args))


def do_my_eval(ops, args):
    for op in ops:
        if op == "+":
            args.append(args.pop() + args.pop())
        elif op == "/":
            args.append(args.pop() / args.pop())
        else:
            args.append(args.pop() * args.pop())
    return args[0]


test_cases = open(sys.argv[1], "r")
for test in test_cases:
    print my_eval(test.strip().split())
test_cases.close()
