# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def merge(self, leftpart, rightpart):
        if leftpart is None:
            return rightpart
        elif rightpart is None:
            return leftpart
        dummy = ListNode(0)
        operator = dummy
        
        while leftpart and rightpart:
            if leftpart.val > rightpart.val:
                tmp = ListNode(val=rightpart.val)
                operator.next = tmp
                rightpart = rightpart.next
            else :
                tmp = ListNode(val=leftpart.val)
                operator.next = tmp
                leftpart = leftpart.next
            operator = operator.next
        operator.next = leftpart if leftpart else rightpart
        return dummy.next
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # assume there need to determine the middle index of source data
        # just make two pointer to caculate it
        
        if head is None:
            return head
        elif head.next is None:
            return head
        
        faster, slower, preslow = head, head, head
        
        while faster is not None and faster.next is not None:
            faster = faster.next.next
            preslow = slower
            slower = slower.next
        preslow.next = None
        leftpart = slower
        rightpart = head
        leftsorted = self.sortList(leftpart)
        rightsorted = self.sortList(rightpart)
        return self.merge(leftsorted, rightsorted)
        
        
        