# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def dfsmerge(self, l1, l2, result):
        if not l1 and not l2:
            return
        elif not l1 and l2:
            result.next = l2
            result = result.next
            self.dfsmerge(l1, l2.next, result)
        elif not l2 and l1:
            result.next = l1
            result = result.next
            self.dfsmerge(l1.next, l2, result)
        elif l1.val > l2.val:
            result.next = l2
            result = result.next
            self.dfsmerge(l1, l2.next, result)
        else :
            result.next = l1
            result = result.next
            self.dfsmerge(l1.next, l2, result)
    
    def makefromsource(self, source, result):
        if not source:
            return
        result.append(source.val)
        self.makefromsource(source.next, result)
    
    def makeresult(self, source, result):
        for _, part in enumerate(source):
            tmp = ListNode(val = part)
            result.next = tmp
            result = result.next
    
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        elif not l1 and not l2:
            return None
        
        l1tmp = []
        l2tmp = []
        
        self.makefromsource(l1, l1tmp)
        self.makefromsource(l2, l2tmp)
        
        sourcetmp = l1tmp + l2tmp
        sourcetmp.sort()
        result = ListNode()
        #self.makeresult(sourcetmp, result)
        self.dfsmerge(l1, l2, result)
        return result.next
        