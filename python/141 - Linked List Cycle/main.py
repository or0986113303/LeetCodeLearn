# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def iscyclelinkedlist(self, slower, faster):
        while slower is not None and faster is not None and faster.next is not None:
            faster = faster.next.next
            slower = slower.next
            if slower == faster:
                return True
        return False
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        return self.iscyclelinkedlist(head, head)
        