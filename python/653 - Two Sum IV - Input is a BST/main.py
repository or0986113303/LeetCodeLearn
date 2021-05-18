# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def compareBST(self, source1, source2, target):
        if source1 is None:
            return False
        
        if self.BST(source2, target - source1.val, source1.val):
            return True
        else :
            return self.compareBST(source1.left, source2, target) or self.compareBST(source1.right, source2, target)
    
    def BST(self, source, target, subpart):
        if source is None:
            return False
        
        if source.val == target and source.val != subpart:
            return True
        elif target > source.val:
            return self.BST(source.right, target, subpart)
        else :
            return self.BST(source.left, target, subpart)
        
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        if root is None:
            return False
        elif k is None:
            return False
        
        return self.compareBST(root, root, k)