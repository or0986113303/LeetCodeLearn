# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteNodes(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        result = ListNode(-1)
        operator = result
        operator.next = head
        while head is not None:
            count = 1
            while count < m and head:
                head = head.next
                count += 1
            prev = head
            if head is None:
                break
            count = -1
            while count < n and head:
                head = head.next
                count += 1
            prev.next = head
        return result.next
        