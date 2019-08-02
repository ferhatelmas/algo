# TODO: make a trie
from string import lowercase
from itertools import product


class WordDictionary:
    def __init__(self):
        self.words = set()

    def addWord(self, word):
        self.words.add(word)

    def search(self, word):
        return any(
            "".join(e) in self.words
            for e in product(*([e] if e else list(lowercase) for e in word.split(".")))
        )


w = WordDictionary()
w.addWord("bad")
w.addWord("dad")
w.addWord("mad")
assert not w.search("pad")
assert w.search("bad")
assert w.search(".ad")
assert w.search("b..")
