class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteNode(self, node):
        if node is None:
            return
        while node.next is not None:
            node.val = node.next.val
            if node.next.next is None:
                node.next = None
            else:
                node = node.next
