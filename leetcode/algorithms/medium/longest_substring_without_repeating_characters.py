class Solution:
    def lengthOfLongestSubstring(self, s):
        i = j = m = 0
        t, l = set(), len(s)

        while j < l:
            if s[j] not in t:
                t.add(s[j])
                j += 1
                m = max(m, len(t))
            else:
                t.remove(s[i])
                i += 1
        return m
