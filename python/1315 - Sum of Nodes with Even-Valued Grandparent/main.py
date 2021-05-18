# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, source, parent, grandparent):
        if source is None:
            return 0
        result = 0
        if grandparent:
            result += source.val
        
        leftpart = self.dfs(source.left, source.val %2 == 0, parent)
        rightpart = self.dfs(source.right, source.val %2 == 0, parent)
        return result + leftpart + rightpart
        
    def sumEvenGrandparent(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root is None:
            return 0
        result = self.dfs(root, False, False)
        print(result)
        return result
        