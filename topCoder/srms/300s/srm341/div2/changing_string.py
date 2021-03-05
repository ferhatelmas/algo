class ChangingString:
    def distance(self, A, B, K):
        ns = sorted(
            map(lambda (e1, e2): abs(ord(e1) - ord(e2)), zip(A, B)), reverse=True
        )
        c = len(filter(lambda e: e > 0, ns[:K]))
        return K - c if c < K else sum(ns[K:])
