# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def dfstraversal(self, source, result):
        if not source:
            return
        result.append(source.val)
        self.dfstraversal(source.next, result)
    
    def makeresult(self, source, result):
        if not source:
            return
        
        for index in range(0, len(source), 1):
            tmp = ListNode(val=source[index])
            result.next = tmp
            result = result.next
    
    def removebyindex(self, source, endthindex):
        result = source[:len(source) - endthindex] + source[len(source) - endthindex + 1 : ]
        return result
    
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if not head :
            return head
        sourcetmp = []
        result = ListNode()
        self.dfstraversal(head, sourcetmp)
        sourcetmpafteroperated = self.removebyindex(sourcetmp, n)
        self.makeresult(sourcetmpafteroperated, result)
        return result.next
        
        