# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def recursionremove(self, curr, prev, val):
        #print('prev : ' + str(prev))
        #print('curr : ' + str(curr))
        if not curr :
            return 
        if curr.val == val:
            tmp = curr.next
            prev.next = tmp
            curr = curr.next
        else:
            prev.next = curr
            prev = curr
            curr = curr.next
                
        return self.recursionremove(curr, prev, val)
    
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if not head :
            return head
        
        result = ListNode(-1)
        prev = result
        self.recursionremove(head, prev, val)
        #print(head)
        #print(result)
        return result.next