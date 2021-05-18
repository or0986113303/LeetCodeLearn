# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sumtmp = 0
    def greaterofall(self, source):
        if not source:
            return 
        
        self.greaterofall(source.right)
        self.sumtmp += source.val
        source.val = self.sumtmp
        self.greaterofall(source.left)
        
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        self.greaterofall(root)
        return root
        
        