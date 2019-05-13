class Solution:
    def getIntersectionNode(self, headA, headB):
        a, b, ai, bi = headA, headB, 0, 0
        while a is not None:
            a = a.next
            ai += 1
        while b is not None:
            b = b.next
            bi += 1
        c = min(ai, bi)
        print c, ai, bi
        a, b = headA, headB
        while ai > c:
            ai -= 1
            a = a.next
        while bi > c:
            bi -= 1
            b = b.next
        while a is not b:
            a = a.next
            b = b.next
        if a is b:
            return a
