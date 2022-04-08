from sys import stdin, stdout

stdin.readline()
stdout.write("".join(sorted(stdin, key=int)))
