# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def createfromsource(self, curr):
        if curr is None:
            return ''
        return str(curr.val) + self.createfromsource(curr.next)
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resultstr = str(int(self.createfromsource(l1)) + int(self.createfromsource(l2)))
        result = ListNode(-1)
        operator = result
        for index, part in enumerate(resultstr):
            tmp = ListNode(val = int(part))
            operator.next = tmp
            operator = operator.next
        return result.next
        