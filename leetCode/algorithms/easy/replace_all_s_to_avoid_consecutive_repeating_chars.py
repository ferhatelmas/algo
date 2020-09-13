from string import ascii_lowercase


class Solution:
    def modifyString(self, s: str) -> str:
        ls = list(s)
        for i, e in enumerate(ls):
            if e != "?":
                continue

            for f in ascii_lowercase:
                if i and f == ls[i - 1]:
                    continue
                if i < len(s) - 1 and f == ls[i + 1]:
                    continue
                ls[i] = f
                break

        return "".join(ls)
