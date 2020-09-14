# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preordertraversal(self, source, target, resulttmp, occuredhash):
        if source is None:
            return resulttmp
        
        occuredhash[source.val - target] = source.val
        leftresult = self.preordertraversal(source.left, target, resulttmp, occuredhash)
        rightresult = self.preordertraversal(source.right, target, leftresult, occuredhash)
        
        return min(leftresult, rightresult)
        
    def closestValue(self, root, target):
        """
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        if root is None:
            return 0
        elif target is None:
            return 0
        occuredhash = {}
        self.preordertraversal(root, target, float('inf'), occuredhash)
        occuredhash = sorted(occuredhash.keys(), key=lambda key:abs(key), reverse=False)
        print(occuredhash)
        return int(target + occuredhash[0])
        
        