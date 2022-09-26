from string import ascii_lowercase
from typing import List


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = {}

        def root(e):
            nonlocal parent
            return e if parent[e] == e else root(parent[e])

        for e in ascii_lowercase:
            parent[e] = e

        for eq in equations:
            if eq[1] == "=":
                a, b = root(eq[0]), root(eq[3])
                if a != b:
                    parent[b] = a
        for eq in equations:
            if eq[1] == "!":
                a, b = root(eq[0]), root(eq[3])
                if a == b:
                    return False

        return True
