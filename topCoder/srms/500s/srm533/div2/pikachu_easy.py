class PikachuEasy:
    def check(self, word):
        def c():
            for e in ('pi', 'ka', 'chu'):
                if word.startswith(e):
                    rest = word.replace(e, '', 1)
                    return rest, True
            return word, False
        while word:
            word, ok = c()
            if not ok:
                return 'NO'
        return 'YES'
