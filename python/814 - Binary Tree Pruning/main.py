# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def containsOne(self, node):
            if not node: 
                return False
            left = self.containsOne(node.left)
            right = self.containsOne(node.right)
            if not left: 
                node.left = None
            if not right: 
                node.right = None
            
            if node.val == 1 or left or right:
                result = True
            else:
                result = False
            return result

    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        result = None 
        if self.containsOne(root):
            result = root
        
        return result
        