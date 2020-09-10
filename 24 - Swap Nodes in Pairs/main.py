# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursionswap(self, curr, prev):       
        if curr is None or curr.next is None:
            return
        else :
            tmp = curr.next
            curr.next = tmp.next
            tmp.next = curr
            prev.next = tmp
            prev = curr
            return self.recursionswap(curr.next, prev)
        
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        result = ListNode(0)
        prev = result
        prev.next = head
        self.recursionswap(head, prev)
        print(result)
        return result.next