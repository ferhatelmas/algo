import sys


slang = [
    ", yeah!",
    ", this is crazy, I tell ya.",
    ", can U believe this?",
    ", eh?",
    ", aw yea.",
    ", yo.",
    "? No way!",
    ". Awesome!",
]

i, l, j = 0, len(slang), True
with open(sys.argv[1], "rb") as test_cases:
    for test in test_cases:
        ls = []
        for e in test.rstrip():
            if e in "!?.":
                if j:
                    ls.append(e)
                else:
                    ls.append(slang[i])
                    i = (i + 1) % l
                j = not j
            else:
                ls.append(e)
        print "".join(ls)
