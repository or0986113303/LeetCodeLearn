# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def determinduplicate(self, curr, targets):
        if curr is None:
            return
        if curr.val not in targets:
            targets[curr.val] = 1
        else :
            targets[curr.val] += 1
        self.determinduplicate(curr.next, targets)
        
    def removetarget(self, curr, prev, target):
        if curr is None :
            return 

        if target[curr.val] > 1:
            prev.next = curr.next
            self.removetarget(curr.next, prev, target)
        else:
            self.removetarget(curr.next, prev.next, target)
        
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head is None:
            return head
        
        occuredhash = {}
        dummy = ListNode(0)
        operator = dummy
        operator.next = head
        
        self.determinduplicate(head, occuredhash)
        
        self.removetarget(head, operator, occuredhash)
        
        print(dummy.next)
        return dummy.next
        
        