# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def makefromsource(self, curr, result):
        if curr is None:
            return 0
        result.append(curr.val)
        return 1 + self.makefromsource(curr.next, result)
        
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        if head is None:
            return []
        sourcetmp = []
        # make the arry and array length from linked list
        length = self.makefromsource(head, sourcetmp)
        print(length)
        result = [0] * length
        stack = []
        for index, part in enumerate(sourcetmp):
            # if find the next greater number, iterate previus numbers to check is correct or not
            while stack and sourcetmp[stack[-1]] < part:
                result[stack.pop()] = part
            # else insert the index in to stack to store the index of every elements be traversaled
            stack.append(index)
        return result
        
        
        