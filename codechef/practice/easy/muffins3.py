import sys

print("\n".join(str(int(i) / 2 + 1) for i in sys.stdin.readlines()[1:]))
