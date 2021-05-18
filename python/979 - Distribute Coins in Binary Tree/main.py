# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    result = 0
    def dfstraversal(self, source):
        if not source:
            return 0
        
        left = self.dfstraversal(source.left)
        right = self.dfstraversal(source.right)
        
        self.result += abs(left) + abs(right)
        
        return source.val -1 + left + right
    
    def distributeCoins(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        print(self.dfstraversal(root))
        return self.result
        