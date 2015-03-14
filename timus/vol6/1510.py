from collections import Counter
from sys import stdin


print(
    Counter(
        e
        for i, e in enumerate(stdin)
        if i
    ).most_common(1)[0][0]
)
