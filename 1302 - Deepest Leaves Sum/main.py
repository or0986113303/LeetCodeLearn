# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelordertraversal(self, source, level, result):
        if not source :
            return
        
        if len(result) - 1 >= level : 
            result[level].append(source.val)
        else :
            result.append([source.val])
        self.levelordertraversal(source.left, level + 1, result)
        self.levelordertraversal(source.right, level + 1, result)
    
    def deepestLeavesSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        
        result = [[]]
        self.levelordertraversal(root, 0, result)
        sumofresult = sum(result[len(result) - 1])
        return sumofresult
        