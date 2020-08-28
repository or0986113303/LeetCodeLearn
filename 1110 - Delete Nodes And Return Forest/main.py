# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def dfstraversal(self, source, target, result, isroot):
        if not source:
            return None
        
        if source.val in target:
            self.dfstraversal(source.left, target, result, True)
            self.dfstraversal(source.right, target, result, True)
            return None
        else :
            if isroot:
                result.append(source)
            source.left = self.dfstraversal(source.left, target, result, False)
            source.right = self.dfstraversal(source.right, target, result, False)
            return source
        
    def delNodes(self, root, to_delete):
        """
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        result = []
        if not root :
            return []
        self.dfstraversal(root, to_delete, result, True)
        return result