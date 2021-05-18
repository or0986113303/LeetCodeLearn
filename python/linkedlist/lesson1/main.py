# -*- coding: utf-8 -*-
"""
Spyderエディタ

これは一時的なスクリプトファイルです。
"""

class ListNode:
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution:
    def insertionSortList(self, head):
        if not head or not head.next: return head
        root = ListNode(0)
        root.next = head
        while head.next:
            if head.val <= head.next.val:
                head = head.next # by pass not in condition value
            else:
                targettemp = head.next # assigned the target node
                operator = root # assigned the source list operator node
                head.next = head.next.next # move the source next node to the next one
                while operator.next and operator.next.val < targettemp.val:
                    operator = operator.next
                targettemp.next = operator.next
                operator.next = targettemp
        return root.next

def makeSourcetoLinkedlist(sourcearray):
    result = ListNode(0)
    operator = result
    for parts in sourcearray :
        tmp = ListNode(parts)
        operator.next = tmp
        operator = operator.next
    return result.next
    
def makeSourcetoArray(sourcelinkedlist, result):
    if sourcelinkedlist == None:
        return 
    result.append(sourcelinkedlist.val)
    makeSourcetoArray(sourcelinkedlist.next, result)
    

if __name__ == '__main__':
    sourcearray = [4,2,1,3]
    source = makeSourcetoLinkedlist(sourcearray)
    sourcearraytocompare = []
    makeSourcetoArray(source, sourcearraytocompare)
    result = Solution().insertionSortList(source)
    resultarraytocompare = []
    makeSourcetoArray(result, resultarraytocompare)
    print('sourcearraytocompare : ' + str(sourcearraytocompare))
    print('resultarraytocompare : ' + str(resultarraytocompare))