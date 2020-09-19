# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, source):
        if not source :
            return None
        sourceval = max(source)
        result = TreeNode(val = sourceval)
        
        left = self.buildTree(source[:source.index(sourceval)])
        right = self.buildTree(source[source.index(sourceval) + 1:])
        result.left = left
        result.right = right
        return result
    
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if nums is None:
            return 
        
        result = self.buildTree(nums)
        return result