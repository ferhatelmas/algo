class Solution:
    def isPalindrome(self, head):
        w = []
        while head:
            w.append(head.val)
            head = head.next
        return w == w[::-1]
