def is_valid(p):
    return sum(map(int, str(abs(p[0])))) + sum(map(int, str(abs(p[1])))) < 20


def walk(start):
    visit, points, cnt = set(), set(), 0
    visit.add(start)
    while len(visit) > 0:
        p = visit.pop()
        cnt += 1
        points.add(p)
        visit.update(
            filter(
                lambda pp: pp not in points and is_valid(pp),
                [
                    (p[0] - 1, p[1]),
                    (p[0], p[1] - 1),
                    (p[0], p[1] + 1),
                    (p[0] + 1, p[1]),
                ],
            )
        )
    print cnt


walk((0, 0))
