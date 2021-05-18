# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursiondelete(self, curr, prev):
        if curr is not None :
            if prev is None:
                prev = curr
                curr = curr.next
            elif curr.val == prev.val:
                curr = curr.next
                prev.next = curr
            else :
                curr = curr.next
                prev = prev.next
            self.recursiondelete(curr, prev)
        else :
            return
        
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return 
        prev = None
        self.recursiondelete(head, prev)
        return(head)