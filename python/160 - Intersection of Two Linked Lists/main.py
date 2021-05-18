# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        
        if headA is None or headB is None:
            return None
        tmpA = headA
        tmpB = headB
        while tmpA != tmpB:
            if tmpA is None:
                tmpA = headB
            else:
                tmpA = tmpA.next
            if tmpB is None:
                tmpB = headA
            else :
                tmpB = tmpB.next
        
        return tmpA