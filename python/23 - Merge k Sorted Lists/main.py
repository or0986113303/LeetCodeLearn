# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def makesourcetmp(self, source, result):
        if not source:
            return
        result.append(source.val)
        self.makesourcetmp(source.next, result)
    
    def makefromsource(self, source, result):
        for part in source:
            tmp = ListNode(val=part)
            result.next = tmp
            result = result.next
        
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        sourcetmp = []
        for part in lists:
            self.makesourcetmp(part, sourcetmp)
        sourcetmp.sort()
        result = ListNode()
        self.makefromsource(sourcetmp, result)
        return result.next
        