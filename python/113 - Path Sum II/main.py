# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preordersum(self, source, target, resulttmp, result):
        if not source:
            return
        resulttmp.append(source.val)
        
        if target == source.val and not source.left and not source.right:
            result.append(list(resulttmp))
        else :
            self.preordersum(source.left, target - source.val, resulttmp, result)
            self.preordersum(source.right, target - source.val, resulttmp, result)
        resulttmp.pop()
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        if not root and sum:
            return []
        result = []
        self.preordersum(root, sum, [], result)
        print(result)
        return result