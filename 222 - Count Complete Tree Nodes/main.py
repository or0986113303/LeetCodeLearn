# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self, source):
        if not source:
            return 0
        result = 1
        left = self.preorder(source.left)
        right = self.preorder(source.right)
        return result + left + right
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        result = self.preorder(root)
        print(result)
        return result
        