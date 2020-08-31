# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    L = 0
    R = 0
    def trim(self, node):
        if not node:
            return None
        elif node.val > self.R:
            return self.trim(node.left)
        elif node.val < self.L:
            return self.trim(node.right)
        else:
            node.left = self.trim(node.left)
            node.right = self.trim(node.right)
            return node
    def trimBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: TreeNode
        """
        self.L = L
        self.R = R
        return self.trim(root)
        