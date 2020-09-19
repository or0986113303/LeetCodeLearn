# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    sumtmp = 0
    def sumofall(self, source):
        if not source:
            return
        
        self.sumofall(source.right)
        self.sumtmp += source.val
        source.val = self.sumtmp
        self.sumofall(source.left)
        
        
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root:
            return
        
        self.sumofall(root)
        print(root)
        return root
        