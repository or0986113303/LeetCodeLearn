# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursionforlength(self, source, count):
        if not source :
            return
        count[0] += 1
        self.recursionforlength(source.next, count)
    
    def recursionofall(self, source, order):
        if not source :
            return 0
        return source.val * 2**order + self.recursionofall(source.next, order - 1)
        
    def getDecimalValue(self, head):
        """
        :type head: ListNode
        :rtype: int
        """
        if not head :
            return 0
        order = [0]
        self.recursionforlength(head, order)
        return self.recursionofall(head, order[0] - 1)
        