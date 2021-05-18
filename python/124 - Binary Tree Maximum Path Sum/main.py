# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    maxsum = float('-inf')
    def dfsmaxsum(self, source):
        if not source:
            return 0
        
        leftpart = max(self.dfsmaxsum(source.left), 0)
        rightpart = max(self.dfsmaxsum(source.right), 0)
        sumtmp = source.val + leftpart + rightpart
        self.maxsum = max(self.maxsum, sumtmp)
        
        return source.val + max(leftpart, rightpart)
        
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfsmaxsum(root)
        return self.maxsum 