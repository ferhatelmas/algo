from operator import itemgetter


class CandidatesSelectionEasy:
    def sort(self, score, x):
        ls = sorted(((i, s[x]) for i, s in enumerate(score)), key=itemgetter(1))
        return [e for e, _ in ls]
