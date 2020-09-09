# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def cleanlistbeforemiddle(self, curr, middle, index):
        if curr is None :
            return curr
        elif index == middle:
            return curr
        else : 
            return self.cleanlistbeforemiddle(curr.next, middle, index + 1)
    def determincapacity(self, curr):
        if curr is None:
            return 0
        return 1+ self.determincapacity(curr.next)
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return head
        
        capacity = self.determincapacity(head)
        middle = capacity // 2
        
        result = self.cleanlistbeforemiddle(head, middle, 0)
        return result