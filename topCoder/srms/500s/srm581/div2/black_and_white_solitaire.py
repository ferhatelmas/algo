class BlackAndWhiteSolitaire:
    def minimumTurns(self, cardFront):
        cnt = len(cardFront)
        for e in 'BW':
            curr = 0
            for c in cardFront:
                if c != e:
                    curr += 1
                e = 'W' if e == 'B' else 'B'
            cnt = min(cnt, curr)
        return cnt
