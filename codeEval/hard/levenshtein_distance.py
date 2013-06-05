import sys
from string import ascii_lowercase as alphabet

def generate_neighbours(ws, s):
  ls, l = set(), len(s)
  for i in xrange(l+1):
    ls.add(s[:i] + s[i+1:])
    for e in alphabet:
      ls.add(s[:i] + e + s[i:])
      if i < l and e != s[i]:
        ls.add(s[:i] + e + s[i+1:])
  return ls.intersection(ws)
    
def generate_network(ws, s):
  gen, r = generate_neighbours(ws, s), set(s)
  while len(gen) > 0:
    s = gen.pop()
    if s not in r:
      r.add(s)
      gen.update(generate_neighbours(ws, s))
  return len(r.intersection(ws))

test_cases = open(sys.argv[1], 'r')
words = set([test.strip() for test in test_cases])
test_cases.close()
print generate_network(words, "hello")
