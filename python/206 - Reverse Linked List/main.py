# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursivereverse(self, curr, prev):
        if curr is None:
            return prev
        else :
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp
            return self.recursivereverse(curr, prev)
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        result = self.recursivereverse(curr, prev)
        return result
        