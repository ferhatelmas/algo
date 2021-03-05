from sys import argv, stdout

f = open(argv[1], "r")
map(lambda l: stdout.write(l.lower()), f)
f.close()
