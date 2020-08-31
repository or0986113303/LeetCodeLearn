# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorder(self, source, result, tmp):
        if source:
            tmp += str(source.val)
            if not source.left and not source.right:  # if reach a leaf
                result.append(tmp)  # update paths  
            else:
                tmp += '->'  # extend the current path
                self.preorder(source.left, result, tmp)
                self.preorder(source.right, result, tmp)

        
    def binaryTreePaths(self, root):
        """
        :type root: TreeNode
        :rtype: List[str]
        """
        result = []
        self.preorder(root, result, '')
        return result
        