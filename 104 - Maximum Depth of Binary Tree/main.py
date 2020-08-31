# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, source):
        if not source:
            return 0
        result = 1
        leftpart = 0
        rightpart = 0
        leftpart += self.dfs(source.left)
        rightpart += self.dfs(source.right)
        result += max(leftpart, rightpart)
        return result
        
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root :
            return 0
        result = self.dfs(root)
        return result
        