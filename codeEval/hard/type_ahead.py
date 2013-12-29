import sys

text = """
  Mary had a little lamb its fleece was white as snow;
  And everywhere that Mary went, the lamb was sure to go.
  It followed her to school one day, which was against the rule;
  It made the children laugh and play, to see a lamb at school.
  And so the teacher turned it out, but still it lingered near,
  And waited patiently about till Mary did appear.
  "Why does the lamb love Mary so?" the eager children cry; "Why, Mary loves the lamb, you know" the teacher did reply."
"""

def ngram(n, w):
    d, cnt, lw = {}, 0.0, len(w.split())
    for i in xrange(len(ls)-lw):
        gram = ' '.join(ls[i:i+lw])
        if gram == w:
            for e in ls[i+lw:i+n]:
                cnt += 1
                d[e] = d.get(e, 0) + 1

    gs = [(k, v/cnt) for k, v in d.iteritems()]
    return ';'.join(['%s,%.3f' % (k, v) for k, v in sorted(gs, key=lambda (k, v): (-v, k))])

ls = [e.strip('",.;?') for e in text.split()]

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
    n, w = test.strip().split(",")
    print ngram(int(n), w)
test_cases.close()
