import sys
from collections import defaultdict

groups, people, my_groups = defaultdict(set), {}, {}

test_cases = open(sys.argv[1], "r")
for test in test_cases:
    name, friend, group = test.rstrip().split(":")

    for g in group.split(","):
        if g:
            groups[g].add(name)
    my_groups[name] = set(group.split(","))
    people[name] = set(friend.split(","))
test_cases.close()

res = {}
for name, friends in people.items():
    cands, l = set(), len(friends)
    for g, members in groups.items():
        if not l or (len(friends & members) >= l / 2.0):
            cands.add(g)
    suggestions = cands - my_groups[name]
    if suggestions:
        res[name] = suggestions

for name in sorted(res.keys()):
    print "{name}:{groups}".format(name=name, groups=",".join(sorted(res[name])))
