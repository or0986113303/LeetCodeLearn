# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inordertraversal(self, source, target):
        if not source :
            return False
        
        left = self.inordertraversal(source.left, target)
        right = self.inordertraversal(source.right, target)
        
        if left :
            source.left = None
        if right :
            source.right = None
        
        if not source.left and not source.right and source.val == target:
            return True
        else:
            return False
    
    def removeLeafNodes(self, root, target):
        """
        :type root: TreeNode
        :type target: int
        :rtype: TreeNode
        """
        if self.inordertraversal(root, target):
            root = None
        return root
        