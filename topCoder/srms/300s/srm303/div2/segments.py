class Segments:
    def intersection(self, s1, s2):
        l = max(min(s1[0::2]), min(s2[0::2]))
        r = min(max(s1[0::2]), max(s2[0::2]))
        t = max(min(s1[1::2]), min(s2[1::2]))
        b = min(max(s1[1::2]), max(s2[1::2]))

        if l > r or t > b:
            return "NO"
        if l == r and t == b:
            return "POINT"
        return "SEGMENT"
