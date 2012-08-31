from sys import stdin

def parse(expr, i):
  i += 1

  if expr[i] == '(':
    op1, i = parse(expr, i)
  else:
    op1 = expr[i]
    i += 1
	
  opt = expr[i]
  i += 1

  if expr[i] == '(':
    op2, i = parse(expr, i)
  else:	
    op2 = expr[i]
    i += 1

  i += 1
return op1 + op2 + opt, i 


stdin.readline()
for expr in stdin:
  rpn, i = parse(expr, 0)
  print rpn

