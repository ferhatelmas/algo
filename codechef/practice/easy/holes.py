from sys import stdin


def find_holes(word):
    holes = 0
    one = ["A", "D", "O", "P", "Q", "R"]
    for c in word:
        if c in one:
            holes += 1
        elif c == "B":
            holes += 2

    return holes


stdin.readline()
for w in stdin:
    print(find_holes(w))
