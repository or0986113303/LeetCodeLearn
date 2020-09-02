# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def makeresult(self, source):
        result = ListNode(0)
        ooperator = result
        sourcetmp = str(source)
        for index in range(len(sourcetmp) - 1, -1, -1):
            tmp = ListNode(sourcetmp[index])
            ooperator.next = tmp
            ooperator = ooperator.next
        return result.next
            
    def convertarraytostring(self, source):
        result = ''
        for parts in source:
            result += str(parts)
        return result
    
    def remakesource(self, source, result) :
        if not source:
            return
        self.remakesource(source.next, result)
        result.append(source.val)
        
    def addTwoNumbers(self, l1, l2) :
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        resulttmp1 = []
        resulttmp2 = []
        self.remakesource(l1, resulttmp1)
        self.remakesource(l2, resulttmp2)
        resultint1 = self.convertarraytostring(resulttmp1)
        resultint2 = self.convertarraytostring(resulttmp2)
        return self.makeresult(int(resultint1) + int(resultint2))
        
        