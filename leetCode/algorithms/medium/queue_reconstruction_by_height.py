import itertools
import operator


class Solution(object):
    def reconstructQueue(self, people):
        res = []
        people.sort(reverse=True)
        for k, g in itertools.groupby(people, key=operator.itemgetter(0)):
            for person in sorted(g):
                res.insert(person[1], person)
        return res
