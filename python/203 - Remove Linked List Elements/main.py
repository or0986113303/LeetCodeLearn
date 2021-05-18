# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursivetoremove(self, curr, prev, target):
        if curr is None:
            return 
        
        if curr.val == target:
            prev.next = curr.next
        else :
            prev = prev.next
        curr = curr.next
        self.recursivetoremove(curr, prev, target)
    
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        
        if head is None:
            return head
        
        dummy = ListNode(0)
        prev = dummy
        prev.next = head
        
        self.recursivetoremove(head, prev, val)
        
        return dummy.next