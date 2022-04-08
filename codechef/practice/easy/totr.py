from sys import stdin


alphabet = None


def translate(s):
    ls = []
    for e in s:
        if e == "_":
            ls.append(" ")
        elif "a" <= e <= "z":
            ls.append(alphabet[e])
        elif "A" <= e <= "Z":
            ls.append(alphabet[e.lower()].upper())
        else:
            ls.append(e)
    return "".join(ls)


for i, ln in enumerate(stdin):
    if i == 0:
        alphabet = dict(zip("abcdefghijklmnopqrstuvwxyz", ln.split()[1]))
    else:
        print(translate(ln.rstrip()))
