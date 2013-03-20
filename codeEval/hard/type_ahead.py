import sys, re
from operator import itemgetter

ls, text = [], """
  Mary had a little lamb its fleece was white as snow;
  And everywhere that Mary went, the lamb was sure to go. 
  It followed her to school one day, which was against the rule;
  It made the children laugh and play, to see a lamb at school.
  And so the teacher turned it out, but still it lingered near,
  And waited patiently about till Mary did appear.
  "Why does the lamb love Mary so?" the eager children cry;"Why, Mary loves the lamb, you know" the teacher did reply."
"""

def add_corpus(ls, s):
  ls += [e for e in map(lambda e: e.strip(), \
    re.sub('[^A-Za-z0-9 ]', '', s).split()) if e != ""]
  
def ngram(n, w):
  d, cnt = {}, 0.0
  for i in xrange(len(ls)):
    if ls[i] == w:
      gram = "".join(ls[i+1:i+n])
      cnt += 1
      if gram in d:
        d[gram] += 1
      else:
        d[gram] = 1

  xs = sorted(sorted([(k, d[k]/cnt) for k in d.keys()], \
    key=itemgetter(0)), key=itemgetter(1), reverse=True)
  return ";".join(map(lambda x: x[0] + "," + ("%.3f" % x[1]), xs))

# add data: current corpus, text to be added
add_corpus(ls, text)

test_cases = open(sys.argv[1], 'r')
for test in test_cases:
  n, w = test.strip().split(",")
  print ngram(int(n), w)
test_cases.close()