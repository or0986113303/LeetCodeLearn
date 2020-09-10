# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def maketolist(self, source, result):
        for index, part in enumerate(source):
            tmp = ListNode(val=part)
            result.next = tmp
            result = result.next
    def makefromsource(self, curr):
        if curr is None:
            return ''
        return str(curr.val) + self.makefromsource(curr.next)
        
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None and l2 is not None:
            return l2
        elif l1 is not None and l2 is None:
            return l1
        elif l1 is None and l2 is None:
            return
        
        val1 = int(self.makefromsource(l1))
        val2 = int(self.makefromsource(l2))
        resultval = str(val1 + val2)
        result = ListNode(0)
        operator = result
        self.maketolist(resultval, operator)
        return operator.next