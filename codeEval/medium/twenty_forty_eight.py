from sys import argv


def step(ls, reverse):
    r = []
    for e in (reversed(ls) if reverse else ls):
        if e == 0:
            continue
        if not r:
            r.append([e, False])
        else:
            if r[-1][0] == e:
                if r[-1][1]:
                    r.append([e, False])
                else:
                    r[-1] = [2 * e, True]
            else:
                r.append([e, False])
    zeros = [0] * (len(ls) - len(r))
    if reverse:
        return zeros + [a for a, _ in reversed(r)]
    return [a for a, _ in r] + zeros


def performx(ls, n, r=False, t=False):
    if t:
        ls = map(list, zip(*ls))
    for i in xrange(n):
        ls[i] = step(ls[i], r)
    if t:
        ls = zip(*ls)
    return ls


def perform(action, n, ls):
    if action == 'RIGHT':
        performx(ls, n, True)
    elif action == 'LEFT':
        performx(ls, n)
    elif action == 'UP':
        ls = performx(ls, n, t=True)
    else:
        ls = performx(ls, n, True, True)
    return '|'.join(' '.join(map(str, e)) for e in ls)


with open(argv[1], 'rb') as test_cases:
    for test in test_cases:
        action, n, board = [e.strip() for e in test.split(';')]
        board = [map(int, e.split()) for e in board.split('|')]
        print(perform(action, int(n), board))
