from sys import stdin

for _ in range(int(stdin.readline())):
  stdin.readline()
  
  piles = [int(p) for p in stdin.readline().split(' ')]
  i = 1
  hands = 0
  for p in piles:
    hands += p/i
    i += 1

  print 'ALICE' if hands%2 == 1 else 'BOB'