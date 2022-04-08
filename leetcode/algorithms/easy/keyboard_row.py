class Solution(object):
    def findWords(self, words):
        rows = [set("qwertyuiop"), set("asdfghjkl"), set("zxcvbnm")]
        return [w for w in words if sum(set(w.lower()) <= row for row in rows) == 1]
