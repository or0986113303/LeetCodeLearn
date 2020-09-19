import copy
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """
        
        if not preorder or not inorder:
            return None
        
        result = TreeNode(val=preorder[0])
        middleindex = inorder.index(preorder[0])
        leftpart = self.buildTree(preorder[1:middleindex+1], inorder[:middleindex])
        rightpart = self.buildTree(preorder[middleindex+1:], inorder[middleindex+1:])
        result.left = leftpart
        result.right = rightpart
        return result
        
        
    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        inorder = sorted(preorder)
        
        print(preorder)
        print(inorder)
        
        result = self.buildTree(preorder, inorder)
        return result
        
        