# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfs(self, source, result):
            if not source:
                return float('inf'), -float('inf')
            lmin, lmax = self.dfs(source.left, result)
            rmin, rmax = self.dfs(source.right, result)
            sourcemin = min(source.val, lmin, rmin)
            sourcemax = max(source.val, lmax, rmax)
            result.append(max(abs(source.val - sourcemin), abs(source.val - sourcemax)))
            #print(result)
            return sourcemin, sourcemax
        
    def maxAncestorDiff(self, root):
        result = []
        self.dfs(root, result)
        return max(result)
        