# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfsfordepth(self, source, result):
        if not source :
            return 0
        
        left = self.dfsfordepth(source.left, result)
        right = self.dfsfordepth(source.right, result)
        depth = max(left, right)
        if len(result) == depth:
            result.append([source.val])
        else :
            result[depth].append(source.val)
        
        return depth + 1
        
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        result = []
        self.dfsfordepth(root, result)
        return result
        