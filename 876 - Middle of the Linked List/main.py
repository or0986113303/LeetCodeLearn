# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rescusionofmiddlevalue(self, source, index, count):
        if not source:
            return 0
        count += 1
        result = 0
        if count == index:
            result = source.val
            return source.next
            
        return self.rescusionofmiddlevalue(source.next, index, count)
        
    def recursionoflength(self, source, count):
        if not source:
            return
        count[0] += 1
        self.recursionoflength(source.next, count)
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head :
            return head
        elif not head.next:
            return head
        length = [0]
        self.recursionoflength(head, length)
        print(length)
        middle = length[0] // 2
        result = self.rescusionofmiddlevalue(head, middle, 0)
        print(result)
        return result