# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def comparetest(self, source, source2, target):
        if source is None:
            return False
        if self.BTS(source2, target - source.val):
            return True
        else:
            return self.comparetest(source.left, source2, target) or self.comparetest(source.right, source2, target)
    
    def BTS(self, source, target):
        if source is None:
            return False
        if source.val == target :
            return True
        elif target > source.val :
            return self.BTS(source.right, target)
        else : 
            return self.BTS(source.left, target)
    def preorderfromsource(self, source, result):
        if source is None:
            return
        result.append(source.val)
        self.preorderfromsource(source.left, result)
        self.preorderfromsource(source.right, result)
        
    def twoSumBSTs(self, root1, root2, target):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :type target: int
        :rtype: bool
        """
        
        if root1 is None:
            return False
        elif root2 is None:
            return False
        
        sourcetmp1 = []
        sourcetmp2 = []
        self.preorderfromsource(root1, sourcetmp1)
        self.preorderfromsource(root2, sourcetmp2)
        '''
        for index, part in enumerate(sourcetmp1):
            if target - part in sourcetmp2:
                return True
        '''
        return self.comparetest(root1, root2, target)
        