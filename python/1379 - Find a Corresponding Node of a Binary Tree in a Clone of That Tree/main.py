# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorder(self, source, target):
        if source is None:
            return
        
        if source.val == target.val:
            return source
        
        left = self.preorder(source.left, target)
        right = self.preorder(source.right, target)
        return left if left is not None else right
        
    def getTargetCopy(self, original, cloned, target):
        """
        :type original: TreeNode
        :type cloned: TreeNode
        :type target: TreeNode
        :rtype: TreeNode
        """
        if original is None or cloned is None or target is None:
            return
        
        self.preorder(cloned, target)
        return self.preorder(cloned, target)