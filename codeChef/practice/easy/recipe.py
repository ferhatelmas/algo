import itertools

def gcd(a, b):
  if b == 0:
    return a
  else:
    return gcd(b, a%b)

def min_gcd(recipe):
  m = 1000
  for (a, b) in itertools.combinations(recipe, 2):
    m = min(gcd(a, b), m)
    if m == 1:
      break
  return m

for _ in xrange(int(raw_input())):
  recipe = map(int, raw_input().split())[1:]
  m = min_gcd(recipe)
  print " ".join(map(lambda x: str(x/m), recipe))