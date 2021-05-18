# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursiveplusone(self, curr, prev):
        if curr is None:
            prev.val += 1
            return
        
        self.recursiveplusone(curr.next, prev.next)
        if prev.next.val >= 10:
            prev.next.val = prev.next.val%10
            prev.val += 1
            
    def plusOne(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return head
        
        result = ListNode(0)
        prev = result
        prev.next = head
        self.recursiveplusone(head, prev)
        print(result)
            
        return result if result.val else result.next